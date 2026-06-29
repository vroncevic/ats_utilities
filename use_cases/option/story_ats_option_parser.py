# -*- coding: utf-8 -*-

'''
Module
    story_ats_option_parser.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Use cases for ATS option parser.
'''

import sys
from typing import Any
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.component_bundle import OptionComponentBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


#
# default [based on argparse]
# =============================
#
opt_parser = {
    'name': 'mytool',
    'epilog': 'mytool is simple',
    'description': 'mytool is simple cli tool',
    'version': '1.2.4'
}

OPS: list[str] = ['-n', '--name', '-v', '--verbose']
component_bundle: OptionComponentBundle = OptionComponentBundle(parameters=opt_parser)
parser: OptionManager = OptionManager(component_bundle=component_bundle)
parser.add_version_operation('1.2.4')
parser.add_operation(OPS[0], OPS[1], dest='name', help='generate project (provide name)')

args: Any = parser.parse_args(sys.argv)
if bool(getattr(args, "name")):
    print(f'option name: {getattr(args, "name")}')
