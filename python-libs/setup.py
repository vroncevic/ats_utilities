#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(
    name='ats_utilities',
    version='1.0',
    description='Python ATS Utilities',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/py_util/',
    license='GPL 2017 Free software to use and distributed it.',
    long_description='Configuration ats_utilities for python App/Tool/Script.',
    keywords='util, config, log, option, xml, cfg, ini, json, yaml',
    platforms='POSIX',
    packages=[
        'ats_utilities',
        'ats_utilities.config',
        'ats_utilities.config.cfg',
        'ats_utilities.config.ini',
        'ats_utilities.config.json',
        'ats_utilities.config.xml',
        'ats_utilities.config.yaml',
        'ats_utilities.logging',
        'ats_utilities.option',
        'ats_utilities.error'
    ]
)
