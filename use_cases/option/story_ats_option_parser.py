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
from ats_utilities.context.factory import ContextBundleFactory
from ats_utilities.option.setup.factory import OptionBundleFactory
from ats_utilities.option.engine import OptionManager

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


#
# default [based on argparse]
# =============================
#
opt_parser: dict[str, object] = {
    'ats_name': 'mytool',
    'ats_version': '1.2.4',
    'ats_licence': 'mytool is simple',
    'ats_build_date': '2026-07-30',
    'ats_info_ok': True
}
OPS: list[str] = ['-n', '--name', '-v', '--verbose']
own = OptionBundleFactory.create_bundle({
    'parameters': opt_parser,
    'context_bundle': ContextBundleFactory.create_bundle()
})
parser: OptionManager = OptionManager(own=own)
parser.add_version_operation('1.2.4')
parser.add_operation(OPS[0], OPS[1], dest='name', help='generate project (provide name)')

args: object = parser.parse_args(sys.argv)

if bool(getattr(args, "name")):
    print(f'option name: {getattr(args, "name")}')
