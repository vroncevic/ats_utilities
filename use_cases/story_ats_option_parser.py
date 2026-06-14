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
from typing import List, Any
import types
import fire
from ats_utilities.option.ats_option_parser import ATSOptionParser
from ats_utilities.option.option_namespace import OptionNamespace, OptArgs
from ats_utilities.option.iparser_strategy import IATSArgParseStrategy
from ats_utilities.option.ats_option_parser import ATSOptionParser

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

#
# 3rd party option parser [Fire]
# ==============================
#
class MyAppFireStrategy(IATSArgParseStrategy):
    '''
        ...
    '''
    def __init__(self):
        self._target = types.SimpleNamespace()

    def setup(self, parameters: dict) -> None:
        pass

    def add_argument(self, *args: str, **kwargs: Any) -> None:
        if args:
            name = args[-1].lstrip('-').replace('-', '_')
            setattr(self._target, name, kwargs.get('default'))

    def add_version(self, version: str) -> None:
        if version:
            setattr(self._target, 'version', lambda: print(version))

    def parse(self, arguments: OptArgs, known_only: bool = False) -> OptionNamespace:
        args_list = list(arguments) if arguments is not None else sys.argv[1:]

        # Ako korisnik traži pomoć, prosledi Fire-u ceo objekat da generiše Usage dokumentaciju
        if not args_list or '--help' in args_list or '-h' in args_list:
            fire.Fire(self._target, command=args_list)
            sys.exit(0)

        def binder(**kwargs):
            for k, v in kwargs.items():
                setattr(self._target, k, v)

        if args_list and any(arg in args_list for arg in ['version', '--version', '-V']):
            fire.Fire(self._target, command=['version'])
            sys.exit(0)
        else:
            fire.Fire(binder, command=args_list)

        res = types.SimpleNamespace()
        res.__dict__.update({k: v for k, v in self._target.__dict__.items() if not callable(v)})
        return res

fire_strategy = MyAppFireStrategy()
opt_parser = {
    'name': 'mytool'
}
OPS: List[str] = ['-n', '--name', '-v', '--verbose']
parser2 = ATSOptionParser(parameters=opt_parser, strategy=fire_strategy)
parser2.add_version_operation('1.2.5')
parser2.add_operation(OPS[0], OPS[1], dest='name', help='generate project (provide name)')
parser2.add_operation('--db-name', default='test_db')
args = parser2.parse_args(sys.argv[1:])
print("Parsirani argumenti:")
for key, value in vars(args).items():
    print(f"  {key}: {value}")


#
# default [without main frame]
# =============================
#
opt_parser = {
    'name': 'mytool',
    'epilog': 'mytool is simple',
    'description': 'mytool is simple cli tool',
    'version': '1.2.4'
}

OPS: List[str] = ['-n', '--name', '-v', '--verbose']
parser: ATSOptionParser = ATSOptionParser(opt_parser)
parser.add_version_operation('1.2.4')
parser.add_operation(OPS[0], OPS[1], dest='name', help='generate project (provide name)')

args: Any = parser.parse_args(sys.argv)
if bool(getattr(args, "name")):
    print(f'option name: {getattr(args, "name")}')

#
# default option parser [argparse]
# =================================
#
# with main frame
# ===============
#
def main():
    '''
        ...
    '''
    opt_parser = {
        'name': 'mytool',
        'epilog': 'mytool is simple',
        'description': 'mytool is simple cli tool',
        'version': '1.2.4'
    }

    OPS: List[str] = ['-n', '--name', '-v', '--verbose']
    parser: ATSOptionParser = ATSOptionParser(opt_parser)
    parser.add_version_operation('1.2.4')
    parser.add_operation(OPS[0], OPS[1], dest='name', help='generate project (provide name)')

    args: Any = parser.parse_args(sys.argv)

    if bool(getattr(args, "name")):
        print(f'option name: {getattr(args, "name")}')

if __name__ == '__main__':
    main()
