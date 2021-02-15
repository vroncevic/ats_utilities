#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
 Module
     setup.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
     ats_utilities is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     ats_utilities is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define setup for ats_utilities package.
"""

from os.path import abspath, dirname, join
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='ats_utilities',
    version='1.2.2',
    description='Python App/Tool/Script Utilities',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/ats_utilities/',
    license='GPL 2018 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='util, config, log, option, xml, cfg, ini, json, yaml',
    platforms='POSIX',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'
    ],
    packages=[
        'ats_utilities',
        'ats_utilities.abstract',
        'ats_utilities.checker',
        'ats_utilities.cli',
        'ats_utilities.config_io',
        'ats_utilities.config_io.cfg',
        'ats_utilities.config_io.ini',
        'ats_utilities.config_io.json',
        'ats_utilities.config_io.xml',
        'ats_utilities.config_io.yaml',
        'ats_utilities.console_io',
        'ats_utilities.exceptions',
        'ats_utilities.info',
        'ats_utilities.logging',
        'ats_utilities.option',
        'ats_utilities.register',
    ],
    install_requires=['colorama', 'bs4', 'PyYAML', 'configparser', 'pathlib']
)
