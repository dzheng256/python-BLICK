from blick.classes import Constraint

defaultConstraints = [Constraint("[+stress][+syllabic]", 1.87),
                      Constraint("[+syllabic][+stress]", 0.673),
                      Constraint("[-tense][+syllabic]", 6.528),
                      Constraint("[+low][+syllabic]", 4.266),
                      Constraint("[-tense,+stress][+word_boundary]", 5.683),
                      Constraint("[+low][+word_boundary]", 2.956),
                      Constraint(
                          "[-stress,-tense,+high][+word_boundary]", 6.327),
                      Constraint(
                          "[-tense,+stress][+continuant,+voice][+word_boundary]", 1.634),
                      Constraint(
                          "[-rhyme,-consonantal][-rhyme,+consonantal]", 0.931),
                      Constraint("[-rhyme,-consonantal][-rhyme]", 0.462),
                      Constraint("[-rhyme,+approximant][-rhyme]", 2.291),
                      Constraint(
                          "[-rhyme,+sonorant][-rhyme,+consonantal]", 3.833),
                      Constraint(
                          "[+rhyme,-sonorant][+rhyme,+approximant]", 0.125),
                      Constraint(
                          "[+rhyme,-sonorant][+rhyme,+sonorant]", 1.536),
                      Constraint(
                          "[+rhyme,-approximant][+rhyme,+approximant]", 0.262),
                      Constraint(
                          "[+rhyme,-approximant][+rhyme,+sonorant]", 1.849),
                      Constraint(
                          "[+rhyme,+consonantal][+rhyme,-consonantal]", 0.398),
                      Constraint(
                          "[+rhyme,+consonantal][+rhyme,+approximant]", 0.594),
                      Constraint(
                          "[+rhyme,+consonantal][+rhyme,+sonorant]", 2.394),
                      Constraint("[+rhyme][+rhyme,-consonantal]", 0.692),
                      Constraint("[+rhyme][+rhyme,+approximant]", 1.688),
                      Constraint("[+rhyme][+rhyme,+sonorant]", 0.434),
                      Constraint("[-rhyme,-strident][-approximant]", 5.837),
                      Constraint("[-rhyme][+continuant]", 3.041),
                      Constraint("[-rhyme][+voice]", 1.874),
                      Constraint("[-rhyme][+strident]", 1.543),
                      Constraint(
                          "[-rhyme,+continuant,-anterior][-rhyme]", 3.665),
                      Constraint(
                          "[-rhyme][-rhyme,-anterior,+consonantal]", 1.511),
                      Constraint("[-rhyme,+continuant,+voice][-rhyme]", 3.601),
                      Constraint("[-rhyme][-sonorant,-consonantal]", 0.927),
                      Constraint(
                          "[-rhyme,+sonorant,-LABIAL][-rhyme,-back]", 2.714),
                      Constraint(
                          "[-rhyme,+sonorant][+CORONAL,-consonantal]", 4.359),
                      Constraint(
                          "[-rhyme,+sonorant][+LABIAL,-consonantal]", 3.106),
                      Constraint("[-rhyme,+LABIAL][-rhyme,+LABIAL]", 2.088),
                      Constraint(
                          "[-rhyme,+anterior,+strident][+CORONAL,-consonantal]", 1.845),
                      Constraint(
                          "[-rhyme,-consonantal][+CORONAL,-consonantal]", 2.861),
                      Constraint(
                          "[-rhyme,+CORONAL,-sonorant,-strident][+lateral]", 1.953),
                      Constraint(
                          "[-rhyme,+CORONAL,-sonorant,-strident][-rhyme,+round]", 0.961),
                      Constraint("[+rhyme][+rhyme][-syllabic]", 0.819),
                      Constraint(
                          "[-strident,-sonorant][+rhyme,-CORONAL]", 2.655),
                      Constraint("[-continuant][+rhyme,-CORONAL]", 1.356),
                      Constraint("[+voice][+rhyme,-CORONAL]", 0.527),
                      Constraint("[-sonorant][+voice,+rhyme]", 3.152),
                      Constraint("[-syllabic][+DORSAL,+sonorant]", 1.875),
                      Constraint(
                          "[+rhyme,-sonorant][+rhyme,-anterior,+consonantal]", 2.736),
                      Constraint("[+nasal][+voice,+rhyme,-CORONAL]", 2.798),
                      Constraint(
                          "[+rhyme,-sonorant][+continuant,-CORONAL]", 1.095),
                      Constraint(
                          "[+nasal][+continuant,+rhyme,-anterior]", 1.944),
                      Constraint(
                          "[+rhyme,+LABIAL,+nasal][+rhyme,-LABIAL]", 2.497),
                      Constraint(
                          "[+CORONAL,+rhyme,+nasal][+rhyme,-CORONAL]", 3.45),
                      Constraint(
                          "[+DORSAL,+rhyme,+sonorant][+rhyme,-DORSAL]", 0.268),
                      Constraint(
                          "[+CORONAL,+nasal][-continuant,+LABIAL]", 3.473),
                      Constraint(
    "[+anterior,-continuant,+rhyme][+anterior,+strident,+rhyme]", 2.851),
    Constraint("[+lateral,+rhyme][+rhyme,-CORONAL]", 1.159),
    Constraint("[+strident][+rhyme,-CORONAL]", 1.345),
    Constraint("[+word_boundary][+rhyme]", 6.728),
    Constraint("[-rhyme][+word_boundary]", 8.138),
    Constraint("[-rhyme][+rhyme]", 6.942),
    Constraint("[-voice][+voice]", 3.552),
    Constraint("[+voice][-voice]", 1.193),
    Constraint("[+voice,+rhyme][+rhyme,-voice]", 1.719),
    Constraint("[+rhyme,-voice][+voice,+rhyme]", 0.203),
    Constraint("[-rhyme,+voice][-rhyme,-voice]", 0.989),
    Constraint("[-rhyme,-voice][-rhyme,+voice]", 0.802),
    Constraint("[+CORONAL,-sonorant][+high,-LABIAL]", 4.005),
    Constraint("[+anterior,+strident,-voice][+CORONAL,-consonantal]", 2.65),
    Constraint("[+round,+stress][+round,+high]", 2.073),
    Constraint("[+anterior,-continuant][+continuant,-anterior]", 3.142),
    Constraint("[+rhyme,+LABIAL,+nasal][-LABIAL]", 2.173),
    Constraint("[+DORSAL,+rhyme,+sonorant][-DORSAL]", 3.475),
    Constraint("[-continuant,-voice][-sonorant,-consonantal]", 1.652),
    Constraint("[+anterior,-continuant][-continuant,-CORONAL]", 3.698),
    Constraint("[+continuant][+continuant,+strident]", 2.496),
    Constraint("[+continuant,-strident][+strident]", 2.011),
    Constraint("[+strident][+continuant,+strident]", 2.029),
    Constraint("[-word_boundary][-sonorant,-consonantal][-stress]", 4.492),
    Constraint("[+LABIAL][+LABIAL,-consonantal]", 2.155),
    Constraint("[-rhyme,-strident,-DORSAL,-LABIAL][+consonantal]", 3.142),
    Constraint("[+rhotic][+CORONAL,-consonantal]", 3.298),
    Constraint("[+CORONAL,-consonantal][+stress,+rhotic]", 3.238),
    Constraint("[+continuant,-strident,+CORONAL][-sonorant]", 2.672),
    Constraint("[-sonorant][+continuant,-strident,+CORONAL]", 0.882),
    Constraint("[-continuant,-anterior][-syllabic]", 4.461),
    Constraint("[-low,+tense][+DORSAL,+sonorant]", 3.104),
    Constraint("[-rhotic,-stress][+DORSAL,+sonorant]", 3.733),
    Constraint("[-rhotic,-stress][+continuant,+rhyme,-anterior]", 2.684),
    Constraint("[-stress,+rhotic][+rhyme,-CORONAL]", 0.86),
    Constraint("[-low,+tense][-syllabic][+rhyme,-CORONAL]", 2.815),
    Constraint("[-low,+tense][+rhyme,-CORONAL][-syllabic]", 3.109),
    Constraint("[+diphthong,+round][+rhyme,-CORONAL]", 2.791),
    Constraint("[-stress,+tense][+rhyme]", 3.008),
    Constraint("[-stress,+round][+rhyme]", 0.127),
    Constraint("[-diphthong,-low,+tense][+CORONAL,+rhyme,-consonantal]", 2.985),
    Constraint("[+low,-back][+CORONAL,+rhyme,-consonantal]", 4.111),
    Constraint("[-rhotic,+stress][+CORONAL,+rhyme,-consonantal]", 1.86),
    Constraint(
        "[-low,-tense,-high,-back][+CORONAL,+rhyme,-consonantal][-syllabic]", 3.034),
    Constraint("[-rhotic][+CORONAL,+rhyme,-consonantal]", 2.295),
    Constraint("[-stress][+CORONAL,+rhyme,-consonantal]", 4.709),
    Constraint("[+tense,+high,+back][+voice,+DORSAL]", 0.892),
    Constraint("[-low,+tense][+rhyme,-CORONAL,+nasal]", 0.19),
    Constraint("[-low,+tense][+voice,+rhyme,+DORSAL]", 0.536),
    Constraint("[+rhyme][+voice,+rhyme,+DORSAL]", 1.478),
    Constraint("[-rhyme][+LABIAL,-consonantal][+syllabic,-low,+round]", 0.625),
    Constraint("[-rhyme][+LABIAL,-consonantal][+syllabic,+round,+high]", 0.525),
    Constraint("[-rhyme][+high,-LABIAL][+low]", 2.718),
    Constraint("[-rhyme][+high,-LABIAL][+syllabic,-back]", 3.758),
    Constraint("[-rhyme][+high,-LABIAL][-high,+stress,-low]", 2.789),
    Constraint("[-rhyme,+round][+low,-back]", 1.2),
    Constraint(
        "[+DORSAL,-sonorant][-diphthong,-round,+tense,+stress,+high]", 1.051),
    Constraint(
        "[+voice,+DORSAL][-diphthong,-round,+tense,+stress,+high]", 1.095),
    Constraint("[+syllabic][-CORONAL,+high][-stress]", 4.384),
    Constraint("[+continuant,-anterior,+voice][+stress]", 2.013),
    Constraint("[+word_boundary][+continuant,-anterior,+voice]", 1.934),
    Constraint("[+continuant,-LABIAL,-strident,+voice][+stress]", 0.779),
    Constraint("[+rhyme,-DORSAL][+syllabic]", 3.067),
    Constraint("[+rhyme,-sonorant][+syllabic]", 2.338),
    Constraint("[+rhyme][+stress]", 1.159),
    Constraint("[+rhyme][+syllabic]", 4.009),
    Constraint("[-tense,+stress][-rhyme][+stress]", 2.135),
    Constraint("[-continuant,+LABIAL][-continuant,+LABIAL]", 2.467),
    Constraint("[+anterior,-continuant][+anterior,-continuant]", 4.17),
    Constraint("[-continuant,-anterior][-continuant,-anterior]", 0.12),
    Constraint("[+DORSAL,-sonorant][+DORSAL,-sonorant]", 3.123),
    Constraint("[+continuant,+LABIAL][+continuant,+LABIAL]", 1.506),
    Constraint("[+anterior,+strident][+anterior,+strident]", 0.984),
    Constraint("[+continuant,-anterior][+continuant,-anterior]", 0.055),
    Constraint("[+LABIAL,+nasal][+LABIAL,+nasal]", 2.901),
    Constraint("[+CORONAL,+nasal][+CORONAL,+nasal]", 3.103),
    Constraint("[+lateral][+lateral]", 3.094),
    Constraint("[+CORONAL,-consonantal][+CORONAL,-consonantal]", 2.358),
    Constraint("[-stress,-back,+tense][-stress,-back,+tense]", 2.887),
    Constraint("[+rhotic][+rhotic]", 2.994),
    Constraint("[+anterior,-continuant][-continuant,-anterior]", 2.698),
    Constraint("[+continuant,+rhyme,-strident,+CORONAL]", 2.048),
    Constraint("[-low,+tense,+stress]", 1.05),
    Constraint("[+rhyme,+high]", 1.865),
    Constraint("[+rhyme,-anterior,+consonantal]", 0.913),
    Constraint("[+voice,+rhyme]", 0.488),
    Constraint("[+rhyme,-CORONAL,-consonantal]", 5.936),
    Constraint("[-rhyme,+DORSAL,+sonorant]", 5.558),
    Constraint("[+continuant,+rhyme,-anterior,+voice]", 2.853),
    Constraint("[-rhyme,+continuant,-LABIAL,-strident,+voice]", 3.217),
    Constraint("[+round,+mainstress,-tense]", 2.73),
    Constraint("[-stress,+round,+high]", 3.191),
    Constraint("[-rhyme,+continuant,+CORONAL,-strident,-voice]", 2.076),
    Constraint("[+continuant,+rhyme,+LABIAL,-voice]", 2.055),
    Constraint("[-stress,+round,-high]", 2.706),
    Constraint("[-rhyme,-continuant,-anterior,-voice]", 1.576),
    Constraint("[+round,+mainstress,-back]", 2.083),
    Constraint("[+continuant,+rhyme,-LABIAL,-strident,+voice]", 1.595),
    Constraint("[-rhyme,+continuant,-anterior,+voice]", 2.118),
    Constraint("[+continuant,+rhyme,-anterior,-voice]", 1.358),
    Constraint("[+voice,+rhyme,-continuant,+LABIAL]", 1.294),
    Constraint("[+voice,+rhyme,+DORSAL]", 1.155),
    Constraint("[+rhyme,-continuant,+LABIAL,-voice]", 1.265),
    Constraint("[+rhyme,-continuant,-anterior,-voice]", 1.191),
    Constraint("[-rhyme,+voice,+anterior,+strident]", 0.992),
    Constraint("[-rhyme,+round]", 0.972),
    Constraint("[-rhyme,-sonorant,-consonantal]", 0.558),
    Constraint("[+DORSAL,+rhyme,+sonorant]", 0.613),
    Constraint("[-rhyme,+voice,-continuant,-anterior]", 0.787),
    Constraint("[+low,+round,+mainstress]", 1.05),
    Constraint("[+diphthong,+mainstress,+back]", 1.386),
    Constraint("[-rhyme,-back]", 0.576),
    Constraint("[-rhotic,+mainstress]", 0.933),
    Constraint("[-rhyme,+voice,+DORSAL]", 0.705),
    Constraint("[+voice,+anterior,+strident,+rhyme]", 0.839),
    Constraint("[-rhyme,+continuant,+LABIAL,+voice]", 0.498),
    Constraint("[+continuant,+rhyme,+CORONAL,-strident,-voice]", 0.454),
    Constraint("[-rhyme,+continuant,+LABIAL,-voice]", 0.371),
    Constraint("[+continuant,+rhyme,+LABIAL,+voice]", 0.595),
    Constraint("[-stress,+rhotic]", 1.132),
    Constraint("[-rhyme,+continuant,-anterior,-voice]", 0.271),
    Constraint("[+low,-round,+mainstress,+back]", 0.405),
    Constraint("[-rhyme,+voice,-continuant,+LABIAL]", 0.116),
    Constraint("[-stress,-back,+tense]", 0.901),
    Constraint("[-word_boundary][-word_boundary]", 5.776, tier="Main"),
    Constraint("[+word_boundary][+word_boundary]", 7.497, tier="Main"),
    Constraint("[+mainstress][+stress][+stress]", 2.171, tier="Stress"),
    Constraint("[-stress][-stress][-stress][-stress]", 1.402, tier="Syllable"),
    Constraint("[-stress][-stress][-stress][+word_boundary]",
               0.843, tier="Syllable"),
    Constraint("[+word_boundary][-stress][-stress]", 4.798, tier="Syllable"),
    Constraint("[+stress][+stress]", 1.902, tier="Syllable"),
    Constraint("[-word_boundary][+stress][+word_boundary]",
               1.741, tier="Syllable"),
    Constraint("[-word_boundary][+mainstress][+word_boundary]",
               0.411, tier="Syllable"),
    Constraint("[+stress,-mainstress][-stress][-stress][+word_boundary]",
               2.671, tier="Syllable"),
    Constraint("[+stress,-mainstress][-stress][+word_boundary]",
               1.284, tier="Syllable"),
    Constraint("[-word_boundary][+stress][+stress]", 1.069, tier="Syllable"),
    Constraint("[+mainstress][+stress][-stress][-word_boundary]", 1.79, tier="Syllable")]

hayesWhiteConstraints = [Constraint("[+syllabic][+syllabic]", 1.125),
                         Constraint("[-tense][+syllabic]", 4.881),
                         Constraint("[-tense,+stress][+word_boundary]", 3.54),
                         Constraint("[-voice][+voice]", 3.138),
                         Constraint("[+voice][-voice]", 2.185),
                         Constraint(
                             "[+rhyme,-sonorant][+rhyme,+sonorant]", 4.538),
                         Constraint(
                             "[+rhyme,+consonantal][+rhyme,-consonantal]", 3.015),
                         Constraint(
                             "[-rhyme,-continuant][-rhyme,+continuant]", 4.669),
                         Constraint(
                             "[-rhyme,+sonorant][-rhyme,-sonorant]", 1.941),
                         Constraint(
                             "[-rhyme,-consonantal][-rhyme,+consonantal]", 4.273),
                         Constraint(
                             "[+CORONAL,+rhyme][+rhyme,+LABIAL]", 0.963),
                         Constraint(
                             "[+CORONAL,+rhyme][+DORSAL,+rhyme]", 0.742),
                         Constraint("[+rhyme,+LABIAL][+DORSAL,+rhyme]", 2.676),
                         Constraint("[+DORSAL,+rhyme][+rhyme,+LABIAL]", 3.032),
                         Constraint("[-rhyme,+DORSAL][-rhyme,+DORSAL]", 0.431),
                         Constraint("[-rhyme,+LABIAL][-rhyme,+LABIAL]", 4.068),
                         Constraint("[+tense][+rhyme][-syllabic]", 0.851),
                         Constraint("[+rhyme][+rhyme][-syllabic]", 1.007),
                         Constraint(
                             "[-rhyme,-continuant][-rhyme,-continuant]", 4.33),
                         Constraint(
                             "[+voice,+rhyme,-continuant][+voice,+rhyme,-continuant]", 0.535),
                         Constraint(
                             "[+rhyme,-continuant,-voice][+voice,+rhyme,-continuant]", 0.25),
                         Constraint(
                             "[+voice,+rhyme,-continuant][+rhyme,-continuant,-voice]", 0.886),
                         Constraint(
                             "[-rhyme,+continuant][-rhyme,+continuant]", 4.051),
                         Constraint(
                             "[+continuant,+rhyme][+continuant,+rhyme]", 1.792),
                         Constraint(
                             "[-rhyme,-continuant][-rhyme,+nasal]", 4.21),
                         Constraint(
                             "[+continuant,+rhyme][+rhyme,+nasal]", 0.632),
                         Constraint(
                             "[+CORONAL,+nasal][+rhyme,+LABIAL]", 2.769),
                         Constraint(
                             "[+CORONAL,+nasal][+DORSAL,+rhyme]", 2.582),
                         Constraint(
                             "[+LABIAL,+nasal][+CORONAL,+rhyme]", 3.408),
                         Constraint("[+LABIAL,+nasal][+DORSAL,+rhyme]", 1.047),
                         Constraint(
                             "[+DORSAL,+sonorant][+rhyme,+LABIAL]", 1.143),
                         Constraint(
                             "[+DORSAL,+sonorant][+CORONAL,+rhyme]", 3.134),
                         Constraint(
    "[-rhyme,+anterior,-sonorant][-rhyme,-anterior,+consonantal]", 3.172),
    Constraint(
        "[-rhyme,-anterior,+consonantal][-rhyme,+anterior,-sonorant]", 0.02),
    Constraint(
        "[+anterior,+rhyme,-sonorant][+rhyme,-anterior,+consonantal]", 2.226),
    Constraint(
        "[+rhyme,-anterior,+consonantal][+anterior,+rhyme,-sonorant]", 0.289),
    Constraint("[+rhyme,+high]", 4.648),
    Constraint("[+rhyme][+stress]", 2.407),
    Constraint("[+word_boundary][+DORSAL,+sonorant]", 1.008),
    Constraint("[-rhyme,+DORSAL,+sonorant]", 5.418),
    Constraint("[+rhyme,-sonorant,-consonantal]", 4.675),
    Constraint("[+word_boundary][+rhyme]", 6.407),
    Constraint("[-rhyme][+word_boundary]", 7.642),
    Constraint("[-rhyme][+rhyme]", 6.167),
    Constraint("[+rhyme][+syllabic]", 4.558),
    Constraint("[-rhyme][+voice]", 2.145),
    Constraint("[+stress,+back][+stress]", 1.518),
    Constraint("[+mainstress][+stress]", 2.049),
    Constraint("[-tense][-back]", 3.533),
    Constraint("[-diphthong,-low,+stress,+back][+round,+high]", 0.493),
    Constraint("[+continuant][+continuant,+strident]", 3.812),
    Constraint("[-anterior,+consonantal][-sonorant]", 4.112),
    Constraint("[-tense,+stress][-low]", 2.83),
    Constraint("[-tense,-back][+word_boundary]", 5.108),
    Constraint("[-rhyme,+sonorant][+consonantal]", 1.676),
    Constraint("[-rhyme,+sonorant][+CORONAL]", 3.552),
    Constraint("[-back][+diphthong]", 4.024),
    Constraint("[-rhyme,+voice][+nasal]", 1.448),
    Constraint("[-rhyme,+sonorant][+LABIAL]", 1.823),
    Constraint(
        "[-high,+tense,+stress,-low][-syllabic,+sonorant,-consonantal]", 3.901),
    Constraint("[-sonorant][+voice,+rhyme]", 2.042),
    Constraint("[+word_boundary][-diphthong,+round,+high]", 5.223),
    Constraint("[+low][+syllabic]", 4.023),
    Constraint("[-rhyme,+LABIAL][-sonorant]", 4.072),
    Constraint("[-anterior,+consonantal][-syllabic,+high]", 3.283),
    Constraint("[-rhyme,+voice,+CORONAL][+consonantal]", 1.353),
    Constraint("[-rhyme,-anterior][+consonantal]", 3.476),
    Constraint("[+diphthong][+continuant,-anterior]", 3.576),
    Constraint("[+round,-high][-low,+round]", 1.721),
    Constraint("[-rhyme,+continuant,+voice][+CORONAL]", 3.75),
    Constraint("[-strident][-sonorant]", 4.038),
    Constraint("[+diphthong,+round][+LABIAL]", 4.525),
    Constraint("[-rhyme,+CORONAL,+sonorant][-syllabic]", 3.2),
    Constraint("[-rhyme,+CORONAL,-continuant][+consonantal]", 3.443),
    Constraint("[-rhyme,+continuant,+CORONAL,+voice][-syllabic]", 2.879),
    Constraint("[-low,+tense][+DORSAL,+sonorant]", 4.855),
    Constraint("[+consonantal][+voice,-strident]", 1.876),
    Constraint("[-rhyme,+CORONAL][-syllabic,-back]", 3.516),
    Constraint("[+round,+high][-sonorant,-consonantal]", 3.783),
    Constraint("[-tense,+stress][-sonorant,-consonantal]", 4.036),
    Constraint("[-strident][-stress,+round]", 3.649),
    Constraint("[+diphthong,+round][+voice,+DORSAL]", 3.596),
    Constraint("[+diphthong,+round][-rhyme,-strident]", 3.284),
    Constraint("[+round,-back][-anterior]", 4.012),
    Constraint("[+round,-tense][-rhyme,+LABIAL,-sonorant]", 2.675),
    Constraint("[+continuant,-anterior,+voice][+round,+stress]", 3.143),
    Constraint("[+word_boundary][-diphthong,+stress][-low]", 3.573),
    Constraint("[-back][-stress,-back,+tense]", 3.277),
    Constraint("[+rhyme,-continuant,-voice][+sonorant,-consonantal]", 1.51),
    Constraint("[-stress,+tense][+voice,-strident]", 2.042),
    Constraint("[-high,+stress][+continuant][+stress,+back]", 3.105),
    Constraint("[+stress][+stress][+word_boundary]", 2.042),
    Constraint("[+mainstress][-word_boundary][+stress]", 3.096),
    Constraint("[-stress,+tense][+continuant,-anterior,+voice]", 3.151),
    Constraint("[+word_boundary][+stress][+high]", 3.584),
    Constraint("[+stress,+back][+CORONAL,+consonantal][+round,+stress]", 3.21),
    Constraint("[-rhyme,-strident][+consonantal]", 3.843),
    Constraint("[+syllabic,+round][+tense,+high][-word_boundary]", 3.858),
    Constraint("[+LABIAL,-voice][-stress,+round,+high]", 3.687),
    Constraint("[+syllabic,+round][+stress][+word_boundary]", 3.247),
    Constraint("[+round,+stress][-low,+stress][-word_boundary]", 1.584),
    Constraint("[+syllabic][+back][-low,+round]", 3.34),
    Constraint("[+stress][+round,+high][+consonantal]", 1.954),
    Constraint("[-low,+round][+LABIAL][-sonorant]", 2.603),
    Constraint("[-low,+stress][-anterior][-anterior]", 3.661),
    Constraint("[-low,-high,+back][-anterior][+CORONAL,+consonantal]", 3.403),
    Constraint("[+CORONAL,+rhyme,-sonorant][+anterior][+round]", 3.398),
    Constraint("[-low,+tense][-continuant][+voice]", 3.161),
    Constraint("[-tense,+stress][+voice,+CORONAL][+tense,+stress]", 3.885),
    Constraint(
        "[-diphthong,-low,+tense,+stress][+rhyme,-sonorant][+LABIAL]", 3.337),
    Constraint("[+round,-tense][+continuant,+rhyme,+voice]", 2.873),
    Constraint("[+tense][-anterior,+consonantal][-syllabic]", 3.303),
    Constraint("[-low,+round,-high][-syllabic,+sonorant,-consonantal]", 3.265),
    Constraint("[-high,+tense,+stress][+continuant][+round,+high]", 3.138),
    Constraint("[-high,+stress][-word_boundary][+diphthong]", 3.336),
    Constraint("[+continuant,+voice][-word_boundary][-strident]", 3.496),
    Constraint("[-low,-back][+LABIAL,-sonorant][+LABIAL]", 3.716),
    Constraint("[-low][-continuant][+DORSAL]", 3.795),
    Constraint("[-syllabic,+high][-syllabic]", 3.3),
    Constraint(
        "[-low,+tense,+back][+rhyme,+LABIAL][-rhyme,+consonantal]", 3.496),
    Constraint("[+stress][-rhyme,+CORONAL][-syllabic,+high]", 3.6),
    Constraint("[+anterior,-continuant,+rhyme][-anterior]", 3.497),
    Constraint(
        "[-sonorant][-stress,+tense][+rhyme,-anterior,+consonantal]", 3.888),
    Constraint(
        "[+continuant,-anterior][-low,+tense][-rhyme,+CORONAL,-sonorant]", 3.454),
    Constraint("[+stress][-anterior,+consonantal][+stress,+back]", 3.656),
    Constraint("[+continuant][-low,+tense,+back][-rhyme,-consonantal]", 3.587),
    Constraint("[-stress,+tense][-word_boundary][-stress,+round]", 4.149),
    Constraint("[+tense][-word_boundary][-sonorant,-consonantal]", 3.444),
    Constraint(
        "[+word_boundary][-low,+tense,-high][-syllabic,-consonantal]", 3.615),
    Constraint("[+consonantal][+round,-tense][+LABIAL]", 3.721),
    Constraint("[+sonorant,+LABIAL][-stress,+round,+high]", 3.592),
    Constraint("[-back][-high,+stress,+back][+voice,+rhyme]", 3.331),
    Constraint(
        "[+word_boundary][-stress,+tense,+back][+CORONAL,-voice]", 3.881),
    Constraint("[-low,+back][+continuant][+nasal]", 3.63),
    Constraint("[+continuant,-anterior,+voice][+stress][-sonorant]", 3.71),
    Constraint("[+voice,-strident][-word_boundary][-rhyme,-sonorant]", 2.241),
    Constraint("[+word_boundary][+diphthong,+round][+voice]", 3.514),
    Constraint("[-stress,+round][+rhyme,+LABIAL,-sonorant]", 3.792),
    Constraint("[+voice,-strident]", 2.662),
    Constraint("[+continuant,+rhyme,-anterior,+voice]", 3.304),
    Constraint(
        "[+continuant,-anterior,+voice][-word_boundary][-rhyme,-sonorant]", 3.265),
    Constraint("[+strident][-stress,-back,+tense][-rhyme]", 3.893),
    Constraint("[-diphthong,+stress][+stress]", 2.844),
    Constraint("[+rhyme][+back]", 1.991),
    Constraint("[+rhyme,-sonorant][-low]", 2.404),
    Constraint("[+stress,+back][+word_boundary]", 2.703),
    Constraint("[+voice][+rhyme]", 1.76),
    Constraint("[+mainstress][-round,+stress]", 0.0),
    Constraint("[+mainstress][+mainstress]", 1.744),
    Constraint("[+stress,+back][+round]", 1.715),
    Constraint("[+syllabic,+round][+syllabic,+round]", 2.915),
    Constraint("[+syllabic,-back][+tense,+high]", 2.953),
    Constraint("[+round,+stress][+stress,-back]", 0.891),
    Constraint("[+rhyme,-voice][-consonantal]", 2.49),
    Constraint("[-diphthong,-low,+stress][+round,+high]", 2.137),
    Constraint("[+voice,+CORONAL][+voice,+CORONAL]", 2.231),
    Constraint("[+CORONAL,-voice][+continuant,+rhyme]", 1.931),
    Constraint("[-voice][+continuant,+voice]", 1.576),
    Constraint("[+round,+stress][+stress]", 2.246),
    Constraint("[+LABIAL][+voice,+rhyme]", 2.665)]

noStressConstraints = [Constraint("[+stress][+syllabic]", 1.252),
                       Constraint("[+syllabic][+stress]", 1.379),
                       Constraint("[-tense][+syllabic]", 6.48),
                       Constraint("[+low][+syllabic]", 5.047),
                       Constraint("[-tense,+stress][+word_boundary]", 7.007),
                       Constraint("[+low][+word_boundary]", 4.457),
                       Constraint(
                           "[-stress,-tense,+high][+word_boundary]", 5.724),
                       Constraint(
                           "[-tense,+stress][+continuant,+voice][+word_boundary]", 2.585),
                       Constraint(
                           "[-rhyme,-consonantal][-rhyme,+consonantal]", 0.976),
                       Constraint("[-rhyme,-consonantal][-rhyme]", 0.0),
                       Constraint("[-rhyme,+approximant][-rhyme]", 2.276),
                       Constraint(
                           "[-rhyme,+sonorant][-rhyme,+consonantal]", 3.69),
                       Constraint(
                           "[+rhyme,-sonorant][+rhyme,+approximant]", 0.125),
                       Constraint(
                           "[+rhyme,-sonorant][+rhyme,+sonorant]", 1.531),
                       Constraint(
                           "[+rhyme,-approximant][+rhyme,+approximant]", 0.261),
                       Constraint(
                           "[+rhyme,-approximant][+rhyme,+sonorant]", 1.823),
                       Constraint(
                           "[+rhyme,+consonantal][+rhyme,-consonantal]", 0.391),
                       Constraint(
                           "[+rhyme,+consonantal][+rhyme,+approximant]", 0.584),
                       Constraint(
                           "[+rhyme,+consonantal][+rhyme,+sonorant]", 2.114),
                       Constraint("[+rhyme][+rhyme,-consonantal]", 0.651),
                       Constraint("[+rhyme][+rhyme,+approximant]", 1.703),
                       Constraint("[+rhyme][+rhyme,+sonorant]", 0.517),
                       Constraint("[-rhyme,-strident][-approximant]", 5.7),
                       Constraint("[-rhyme][+continuant]", 2.936),
                       Constraint("[-rhyme][+voice]", 1.842),
                       Constraint("[-rhyme][+strident]", 1.5),
                       Constraint(
                           "[-rhyme,+continuant,-anterior][-rhyme]", 3.541),
                       Constraint(
                           "[-rhyme][-rhyme,-anterior,+consonantal]", 1.468),
                       Constraint(
                           "[-rhyme,+continuant,+voice][-rhyme]", 3.498),
                       Constraint("[-rhyme][-sonorant,-consonantal]", 0.912),
                       Constraint(
                           "[-rhyme,+sonorant,-LABIAL][-rhyme,-back]", 2.371),
                       Constraint(
                           "[-rhyme,+sonorant][+CORONAL,-consonantal]", 4.203),
                       Constraint(
                           "[-rhyme,+sonorant][+LABIAL,-consonantal]", 2.929),
                       Constraint("[-rhyme,+LABIAL][-rhyme,+LABIAL]", 1.964),
                       Constraint(
                           "[-rhyme,+anterior,+strident][+CORONAL,-consonantal]", 1.743),
                       Constraint(
                           "[-rhyme,-consonantal][+CORONAL,-consonantal]", 2.88),
                       Constraint(
                           "[-rhyme,+CORONAL,-sonorant,-strident][+lateral]", 1.873),
                       Constraint(
                           "[-rhyme,+CORONAL,-sonorant,-strident][-rhyme,+round]", 0.705),
                       Constraint("[+rhyme][+rhyme][-syllabic]", 0.586),
                       Constraint(
                           "[-strident,-sonorant][+rhyme,-CORONAL]", 2.478),
                       Constraint("[-continuant][+rhyme,-CORONAL]", 1.298),
                       Constraint("[+voice][+rhyme,-CORONAL]", 0.619),
                       Constraint("[-sonorant][+voice,+rhyme]", 2.962),
                       Constraint("[-syllabic][+DORSAL,+sonorant]", 1.756),
                       Constraint(
                           "[+rhyme,-sonorant][+rhyme,-anterior,+consonantal]", 2.47),
                       Constraint("[+nasal][+voice,+rhyme,-CORONAL]", 2.588),
                       Constraint(
                           "[+rhyme,-sonorant][+continuant,-CORONAL]", 1.262),
                       Constraint(
                           "[+nasal][+continuant,+rhyme,-anterior]", 1.675),
                       Constraint(
                           "[+rhyme,+LABIAL,+nasal][+rhyme,-LABIAL]", 2.238),
                       Constraint(
                           "[+CORONAL,+rhyme,+nasal][+rhyme,-CORONAL]", 3.341),
                       Constraint(
                           "[+DORSAL,+rhyme,+sonorant][+rhyme,-DORSAL]", 0.039),
                       Constraint(
                           "[+CORONAL,+nasal][-continuant,+LABIAL]", 3.52),
                       Constraint(
    "[+anterior,-continuant,+rhyme][+anterior,+strident,+rhyme]", 2.616),
    Constraint("[+lateral,+rhyme][+rhyme,-CORONAL]", 1.005),
    Constraint("[+strident][+rhyme,-CORONAL]", 1.152),
    Constraint("[+word_boundary][+rhyme]", 6.213),
    Constraint("[-rhyme][+word_boundary]", 8.12),
    Constraint("[-rhyme][+rhyme]", 6.553),
    Constraint("[-voice][+voice]", 3.647),
    Constraint("[+voice][-voice]", 1.256),
    Constraint("[+voice,+rhyme][+rhyme,-voice]", 1.493),
    Constraint("[+rhyme,-voice][+voice,+rhyme]", 0.178),
    Constraint("[-rhyme,+voice][-rhyme,-voice]", 0.946),
    Constraint("[-rhyme,-voice][-rhyme,+voice]", 0.711),
    Constraint("[+CORONAL,-sonorant][+high,-LABIAL]", 3.827),
    Constraint("[+anterior,+strident,-voice][+CORONAL,-consonantal]", 2.662),
    Constraint("[+round,+stress][+round,+high]", 3.21),
    Constraint("[+anterior,-continuant][+continuant,-anterior]", 3.188),
    Constraint("[+rhyme,+LABIAL,+nasal][-LABIAL]", 2.197),
    Constraint("[+DORSAL,+rhyme,+sonorant][-DORSAL]", 3.337),
    Constraint("[-continuant,-voice][-sonorant,-consonantal]", 1.998),
    Constraint("[+anterior,-continuant][-continuant,-CORONAL]", 3.691),
    Constraint("[+continuant][+continuant,+strident]", 2.463),
    Constraint("[+continuant,-strident][+strident]", 2.166),
    Constraint("[+strident][+continuant,+strident]", 2.03),
    Constraint("[-word_boundary][-sonorant,-consonantal][-stress]", 3.745),
    Constraint("[+LABIAL][+LABIAL,-consonantal]", 2.146),
    Constraint("[-rhyme,-strident,-DORSAL,-LABIAL][+consonantal]", 3.09),
    Constraint("[+rhotic][+CORONAL,-consonantal]", 3.33),
    Constraint("[+CORONAL,-consonantal][+stress,+rhotic]", 3.2),
    Constraint("[+continuant,-strident,+CORONAL][-sonorant]", 2.605),
    Constraint("[-sonorant][+continuant,-strident,+CORONAL]", 0.818),
    Constraint("[-continuant,-anterior][-syllabic]", 4.354),
    Constraint("[-low,+tense][+DORSAL,+sonorant]", 2.874),
    Constraint("[-rhotic,-stress][+DORSAL,+sonorant]", 2.799),
    Constraint("[-rhotic,-stress][+continuant,+rhyme,-anterior]", 2.028),
    Constraint("[-stress,+rhotic][+rhyme,-CORONAL]", 0.791),
    Constraint("[-low,+tense][-syllabic][+rhyme,-CORONAL]", 2.392),
    Constraint("[-low,+tense][+rhyme,-CORONAL][-syllabic]", 2.437),
    Constraint("[+diphthong,+round][+rhyme,-CORONAL]", 3.252),
    Constraint("[-stress,+tense][+rhyme]", 2.712),
    Constraint("[-stress,+round][+rhyme]", 0.1),
    Constraint("[-diphthong,-low,+tense][+CORONAL,+rhyme,-consonantal]", 2.508),
    Constraint("[+low,-back][+CORONAL,+rhyme,-consonantal]", 4.327),
    Constraint("[-rhotic,+stress][+CORONAL,+rhyme,-consonantal]", 2.266),
    Constraint(
        "[-low,-tense,-high,-back][+CORONAL,+rhyme,-consonantal][-syllabic]", 3.065),
    Constraint("[-rhotic][+CORONAL,+rhyme,-consonantal]", 2.561),
    Constraint("[-stress][+CORONAL,+rhyme,-consonantal]", 4.098),
    Constraint("[+tense,+high,+back][+voice,+DORSAL]", 0.854),
    Constraint("[-low,+tense][+rhyme,-CORONAL,+nasal]", 0.0),
    Constraint("[-low,+tense][+voice,+rhyme,+DORSAL]", 0.271),
    Constraint("[+rhyme][+voice,+rhyme,+DORSAL]", 1.431),
    Constraint("[-rhyme][+LABIAL,-consonantal][+syllabic,-low,+round]", 0.555),
    Constraint("[-rhyme][+LABIAL,-consonantal][+syllabic,+round,+high]", 0.977),
    Constraint("[-rhyme][+high,-LABIAL][+low]", 3.089),
    Constraint("[-rhyme][+high,-LABIAL][+syllabic,-back]", 3.443),
    Constraint("[-rhyme][+high,-LABIAL][-high,+stress,-low]", 2.816),
    Constraint("[-rhyme,+round][+low,-back]", 1.15),
    Constraint(
        "[+DORSAL,-sonorant][-diphthong,-round,+tense,+stress,+high]", 1.022),
    Constraint(
        "[+voice,+DORSAL][-diphthong,-round,+tense,+stress,+high]", 1.134),
    Constraint("[+syllabic][-CORONAL,+high][-stress]", 3.803),
    Constraint("[+continuant,-anterior,+voice][+stress]", 3.018),
    Constraint("[+word_boundary][+continuant,-anterior,+voice]", 2.322),
    Constraint("[+continuant,-LABIAL,-strident,+voice][+stress]", 1.446),
    Constraint("[+rhyme][+syllabic]", 3.434),
    Constraint("[+rhyme,-DORSAL][+syllabic]", 3.118),
    Constraint("[+rhyme,-sonorant][+syllabic]", 2.376),
    Constraint("[+rhyme][+stress]", 2.253),
    Constraint("[-tense,+stress][-rhyme][+stress]", 4.428),
    Constraint("[-continuant,+LABIAL][-continuant,+LABIAL]", 2.492),
    Constraint("[+anterior,-continuant][+anterior,-continuant]", 4.072),
    Constraint("[-continuant,-anterior][-continuant,-anterior]", 0.13),
    Constraint("[+DORSAL,-sonorant][+DORSAL,-sonorant]", 3.22),
    Constraint("[+continuant,+LABIAL][+continuant,+LABIAL]", 1.557),
    Constraint("[+anterior,+strident][+anterior,+strident]", 0.94),
    Constraint("[+continuant,-anterior][+continuant,-anterior]", 0.054),
    Constraint("[+LABIAL,+nasal][+LABIAL,+nasal]", 2.912),
    Constraint("[+CORONAL,+nasal][+CORONAL,+nasal]", 3.143),
    Constraint("[+lateral][+lateral]", 3.133),
    Constraint("[+CORONAL,-consonantal][+CORONAL,-consonantal]", 2.543),
    Constraint("[-stress,-back,+tense][-stress,-back,+tense]", 3.408),
    Constraint("[+rhotic][+rhotic]", 3.243),
    Constraint("[+anterior,-continuant][-continuant,-anterior]", 2.728),
    Constraint("[+continuant,+rhyme,-strident,+CORONAL]", 1.995),
    Constraint("[-low,+tense,+stress]", 1.868),
    Constraint("[+rhyme,+high]", 1.782),
    Constraint("[+rhyme,-anterior,+consonantal]", 0.936),
    Constraint("[+voice,+rhyme]", 0.589),
    Constraint("[+rhyme,+LABIAL]", 0.167),
    Constraint("[+rhyme,-CORONAL,-consonantal]", 6.047),
    Constraint("[-rhyme,+DORSAL,+sonorant]", 5.516),
    Constraint("[+continuant,+rhyme,-anterior,+voice]", 2.745),
    Constraint("[-rhyme,+continuant,-LABIAL,-strident,+voice]", 2.777),
    Constraint("[+round,+mainstress,-tense]", 2.176),
    Constraint("[-stress,+round,+high]", 2.723),
    Constraint("[-rhyme,+continuant,+CORONAL,-strident,-voice]", 2.018),
    Constraint("[+continuant,+rhyme,+LABIAL,-voice]", 2.024),
    Constraint("[-stress,+round,-high]", 2.241),
    Constraint("[-rhyme,-continuant,-anterior,-voice]", 1.525),
    Constraint("[+round,+mainstress,-back]", 1.495),
    Constraint("[+continuant,+rhyme,-LABIAL,-strident,+voice]", 1.406),
    Constraint("[-rhyme,+continuant,-anterior,+voice]", 1.546),
    Constraint("[+continuant,+rhyme,-anterior,-voice]", 1.54),
    Constraint("[+voice,+rhyme,-continuant,+LABIAL]", 1.198),
    Constraint("[+voice,+rhyme,+DORSAL]", 1.253),
    Constraint("[+rhyme,-continuant,+LABIAL,-voice]", 1.223),
    Constraint("[+rhyme,-continuant,-anterior,-voice]", 1.289),
    Constraint("[-rhyme,+voice,+anterior,+strident]", 0.93),
    Constraint("[-rhyme,+round]", 1.005),
    Constraint("[-rhyme,-sonorant,-consonantal]", 0.82),
    Constraint("[+DORSAL,+rhyme,+sonorant]", 1.017),
    Constraint("[-rhyme,+voice,-continuant,-anterior]", 0.727),
    Constraint("[+low,+round,+mainstress]", 0.983),
    Constraint("[+diphthong,+mainstress,+back]", 0.796),
    Constraint("[-rhyme,-back]", 0.677),
    Constraint("[-rhotic,+mainstress]", 0.356),
    Constraint("[-rhyme,+voice,+DORSAL]", 0.627),
    Constraint("[+voice,+anterior,+strident,+rhyme]", 0.626),
    Constraint("[-rhyme,+continuant,+LABIAL,+voice]", 0.436),
    Constraint("[+continuant,+rhyme,+CORONAL,-strident,-voice]", 0.589),
    Constraint("[-rhyme,+continuant,+LABIAL,-voice]", 0.291),
    Constraint("[+continuant,+rhyme,+LABIAL,+voice]", 0.26),
    Constraint("[-stress,+rhotic]", 0.638),
    Constraint("[-rhyme,+continuant,-anterior,-voice]", 0.216),
    Constraint("[+low,-round,+mainstress,+back]", 0.346),
    Constraint("[-rhyme,+voice,-continuant,+LABIAL]", 0.041),
    Constraint("[-stress,-back,+tense]", 0.406)]
