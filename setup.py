from setuptools import setup, find_packages
from os.path import join, dirname

import os

setup(
    name='grammaranalyzer',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'nltk',
        'click',
        'nose'
    ],
    entry_points={
        'console_scripts':
            ['grammaranalyzer = grammaranalyzer.cli:main']
    },
    test_suite='nose.collector',
    tests_require=[
        'nose',
    ],
)
