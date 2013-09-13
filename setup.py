#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='rdt',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Make rdesktop behave more cleverly",
    long_description="Run rdesktop after removing ~/.rdesktop and calibrating the geometry from a window manager frame.",
    scripts=['rdt'],
    data_files=[('share/man/man1', ['rdt.1'])],
)
