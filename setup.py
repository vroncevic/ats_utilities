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

from distutils.core import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

setup(
    name='ats_utilities',
    version='1.0.1',
    description='Python App/Tool/Script Utilities',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/py_util/',
    license='GPL 2018 Free software to use and distributed it.',
    long_description='Configuration ats_utilities for python App/Tool/Script.',
    keywords='util, config, log, option, xml, cfg, ini, json, yaml',
    platforms='POSIX',
    packages=[
        'ats_utilities',
        'ats_utilities.abstract',
        'ats_utilities.config',
        'ats_utilities.config.cfg',
        'ats_utilities.config.ini',
        'ats_utilities.config.json',
        'ats_utilities.config.xml',
        'ats_utilities.config.yaml',
        'ats_utilities.console_io',
        'ats_utilities.exceptions',
        'ats_utilities.logging',
        'ats_utilities.option',
        'ats_utilities.register',
    ], requires=['colorama', 'bs4', 'yaml', 'configparser', 'pathlib', 'wheel']
)
