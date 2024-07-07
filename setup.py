#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines setup for package ats_utilities.
'''

from typing import List, Optional
from os.path import abspath, dirname, join
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

THIS_DIR: str = abspath(dirname(__file__))
long_description: Optional[str] = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
LICENSE_PREFIX: str = 'License :: OSI Approved ::'
LICENSES: List[str] = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES: List[str] = [
    f'{LICENSE_PREFIX} {LICENSE}' for LICENSE in LICENSES
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES
setup(
    name='ats_utilities',
    version='3.3.2',
    description='Python App/Tool/Script Utilities',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/ats_utilities',
    license='GPL 2017 - 2024 Free software to use and distributed it.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='util, config, log, option, xml, cfg, ini, json, yml, cli, meta',
    platforms='any',
    classifiers=PYP_CLASSIFIERS,
    packages=[
        'ats_utilities',
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
        'ats_utilities.pro_config',
        'ats_utilities.splash'
    ],
    install_requires=['colorama', 'bs4', 'lxml', 'PyYAML'],
    package_data={
        'ats_utilities': [
            'py.typed'
        ]
    }
)
