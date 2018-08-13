'''
Created on 2012-10-02

@author: michael

Modified: 2018-08-12
@author: dzheng256
'''
import os


class BlickLoader:
    def __init__(self, grammarType='default', debug=False):
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        self.debug = debug
        if debug:
            self.init_log()

        if debug:
            self.update_log('Loading syllabification information...')
        from blick.syllabification import ONSETS, VOWELS
        self.onsets = ONSETS
        self.vowels = VOWELS

        if debug:
            self.update_log('Loading grammar...')
        if grammarType == 'HayesWhite':
            from blick.grammars import hayesWhiteConstraints as constraints
        elif grammarType == 'NoStress':
            from blick.grammars import noStressConstraints as constraints
        else:
            from blick.grammars import defaultConstraints as constraints
        self.grammar = constraints
        if debug:
            self.update_log('Loading natural classes...')
        if grammarType == 'HayesWhite':
            from blick.naturalClasses import hayesWhiteNC as nc
        elif grammarType == 'NoStress':
            from blick.naturalClasses import noStressNC as nc
        else:
            from blick.naturalClasses import defaultNC as nc
        self.segMapping = nc
        if debug:
            self.update_log('Done initializing!')

    def init_log(self):
        f = open(os.path.join(self.basedir, 'PyBlickLog.txt'), 'w')
        f.write('Begin operation\n')
        f.close()

    def update_log(self, linetowrite):
        f = open(os.path.join(self.basedir, 'PyBlickLog.txt'), 'a')
        f.write(linetowrite+'\n')
        f.close()

    def _syllabify(self, inputword):
        segs = inputword.split(' ')
        seglist = []
        cons = []
        # Convert the segment list into a list of Vowels and Consonant lists
        for s in segs:
            if s in self.vowels:
                if cons != []:
                    seglist.append(cons)
                    cons = []
                seglist.append(s)  # Vowels appended as strings
            else:
                cons.append(s)  # Consonant(s) are appended as lists
        # Deal with leftover segment at the end
        if cons != []:
            seglist.append(cons)
        # At this point,  seglist should look like:
        # [['C', 'C'], 'V', ['C'], 'V', 'V']
        # Make Consonants either onsets or codas
        returnlist = []
        VowAdded = False  # Tracks whether the first vowel is present
        for i in range(len(seglist)):
            s = seglist[i]
            # Append vowels as is
            if not isinstance(s, list):
                returnlist.append(s)
                VowAdded = True
                continue
            # If a vowel hasn't been found yet,  everything is an onset
            if not VowAdded:
                for o in s:
                    returnlist.append(o)
                continue
            if i != len(seglist)-1:
                for j in range(len(s)):
                    # Look for maximal acceptable onsets
                    if ' '.join(s[j:]) in self.onsets:
                        for c in s[:j]:  # Whatever comes before the maximal onset is a coda
                            returnlist.append(c+'Coda')
                        for o in s[j:]:
                            returnlist.append(o)
                        break
                else:
                    returnlist.extend([c+'Coda' for c in s])
            else:  # All consonants at the end are codas
                for c in s:
                    returnlist.append(c+'Coda')
        return returnlist

    def assess_word(self, inputword, includeConstraints=False):
        segs = self._syllabify(inputword)  # Syllabify segments
        segs = ['#'] + segs + ['#']
        f = []  # Convert segments into feature sets
        for s in segs:
            f.append(self.segMapping[s])
        score = 0.0
        cons = []
        # For each constraint,  evaluate the word and sum scores on each constraint
        for c in self.grammar:
            cScore = c.assess(f)
            if cScore != 0.0:
                score += cScore
                cons.append(str(c))
        if includeConstraints:
            return score, cons
        return score

    def assess_file(self, path, outpath=None, includeConstraints=False):
        if outpath is None:
            mod = os.path.split(path)
            outpath = os.path.join(mod[0], mod[1].replace('.', '-output.'))
        if self.debug:
            self.update_log(' '.join(['Assessing', os.path.abspath(path)]))
        if self.debug:
            self.update_log(
                ' '.join(['Creating output file', os.path.abspath(outpath)]))
        with open(outpath, 'w') as outf:
            with open(path, 'r') as inf:
                for line in inf:
                    line = line.strip().split('\t')
                    segs = line[0].strip()
                    outline = [segs]
                    if includeConstraints:
                        score, cons = self.assess_word(
                            segs, includeConstraints=True)
                        outline.extend([str(score), ', '.join(cons)])
                    else:
                        score = self.assess_word(segs)
                        outline.append(str(score))
                    outf.write('\t'.join(outline+line[1:]))
                    outf.write('\n')
        if self.debug:
            self.update_log(
                ' '.join(['Finished assessing', os.path.abspath(path)]))


class Constraint:
    def __init__(self, textdesc, score, tier='default'):
        self.score = score
        self.tier = tier
        if self.tier == 'Main':  # Features that determine inclusion in a tier
            self.tierFeats = set(['+mainstress'])
        elif self.tier == 'Stress':
            self.tierFeats = set(['+stress'])
        elif self.tier == 'Syllable':
            self.tierFeats = set(['+syllabic'])
        else:
            self.tierFeats = set([])
        # Convert description of constraint into feature sets
        desc = textdesc.split('][')
        self.description = []
        for i in desc:
            self.description.append(
                set(i.replace(']', '').replace('[', '').split(', ')))

    def _getTierSegs(self, segs):
        tierSegs = []
        for s in segs:
            if s >= self.tierFeats or s == set(['+word_boundary']):
                tierSegs.append(s)
        return tierSegs

    def assess(self, segs):
        if self.tier != 'default':  # Only look at segments relevant for a tier
            segs = self._getTierSegs(segs)
        wLength = len(self.description)
        if wLength > 1:  # Create all possible comparisons based on window length of constraint
            assess_list = [segs[i:i+wLength]
                          for i in range(len(segs)-(wLength-1))]
        else:
            assess_list = [segs[i:i+1] for i in range(len(segs)-1)]
        score = 0.0
        for w in assess_list:
            match = True
            # Compare all feature sets of a constraint to the corresponding feature sets of segments
            for i in range(wLength):
                # If the constraint feature sets are not subsets of the segment feature set
                # then that comparison doesn't meet constraint criteria
                if len(self.description[i] - w[i]) != 0:
                    match = False
                    break
            if match:  # For each match,  find the product of number of instances and the score
                score += self.score
        return score

    def writeDescription(self):
        output = ''
        for x in self.description:
            output += '['
            output += ', '.join(x)
            output += ']'
        return output

    def __str__(self):  # Recreate string description of constraint
        output = '*'
        output += self.writeDescription()
        output += ' ( ' + str(self.score)+')'
        if self.tier != 'default':
            output += ' (' + self.tier+' tier)'
        return output
