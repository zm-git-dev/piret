#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="pypiret",
    version='0.1.0',
    description="RNAseq pipeline",
    author="Migun Shakya",
    author_email="migun@lanl.gov",
    url="https://github.com/mshakya/piret",
    install_requires=open("requirements.txt").read().splitlines(),
    packages=find_packages(),
    scripts=['bin/piret'],
    license="Apache License 2.0",
    platforms="Posix; MacOS X",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Bioinformatics",
    ],
)
