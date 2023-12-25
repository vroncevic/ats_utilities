# -*- coding: UTF-8 -*-

'''
Module
    cfg_cli.py
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
    Defines class CfgCLI with attribute(s) and method(s).
    Creates an API for checks and loads an information argument parser.
'''

import sys
from typing import Any, List, Sequence
from argparse import Namespace
from abc import abstractmethod

try:
    from ats_utilities.config_io.cfg import CfgBase
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CfgCLI(CfgBase):
    '''
        Defines class CfgCLI with attribute(s) and method(s).
        Creates an API for checks and loads an information argument parser.
        Command-line interface configuration based on CFG format.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials CfgCLI constructor.
                | add_new_option - Adds a new option for the the CL interface.
                | parse_args - Parses the CL arguments.
                | process - Processes and runs tool operations (Abstract).
    '''

    def __init__(self, info_file: str | None, verbose: bool = False) -> None:
        '''
            Initials CfgCLI constructor.

            :param info_file: Information file path | None
            :type info_file: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__(info_file, verbose)
        self._verbose: bool = verbose
        verbose_message(self._verbose, ['init ATS CFG cli'])

    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds a new option for the CL interface.

            :param args: Arguments in string form
            :type args: <str>
            :param kwargs: arguments in Any form
            :type kwargs: <Any>
            :exceptions: None
        '''
        self.option_parser.add_operation(*args, **kwargs)

    def parse_args(self, argv: Sequence[str] | None) -> Namespace:
        '''
            Parses the CL arguments.

            :param argv: Sequence of arguments | None
            :type argv: <Sequence[str]> | <NoneType>
            :return: Options and arguments
            :rtype: <Namespace>
            :exceptions: ATSTypeError
        '''
        return self.option_parser.parse_args(argv)

    @abstractmethod
    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs tool operations (Abstract).

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (successfully finished) | False
            :rtype: <bool>
            :exception: TypeError
        '''
