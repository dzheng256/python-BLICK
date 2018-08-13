from setuptools import setup

setup(
    name='python-BLICK',
    version='0.2.12',
    author='Michael McAuliffe, Bruce Hayes',
    author_email='michael.e.mcauliffe@gmail.com',
    packages=['blick', 'blick.test'],
    scripts=['bin/BlickAFile.py'],
    url='http://pypi.python.org/pypi/python-BLICK/',
    license='LICENSE.txt',
    description='Python implementation of BLICK (a phonotactic probability calculator for English)',
    install_requires=[],
)
