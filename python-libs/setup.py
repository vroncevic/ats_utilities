#!/usr/bin/env python

from distutils.core import setup

setup(
    name='utilities',
    version='1.0',
    description='Python utilities',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/py_util/',
    license='GPL 2017 Free software to use and distributed it.',
    long_description='Configuration utilities for python app/tool/script.',
    keywords='utilities, config, logging, option, xml, cfg, ini, json, yaml',
    platforms='POSIX',
    packages=[
        'utilities',
        'utilities.config',
        'utilities.config.cfg',
        'utilities.config.ini',
        'utilities.config.json',
        'utilities.config.xml',
        'utilities.config.yaml',
        'utilities.logging',
        'utilities.option',
        'utilities.error'
    ]
)
