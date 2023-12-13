# -*- coding: UTF-8 -*-

'''
Module
    yaml_cli.py
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
    Defines class YamlCLI with attribute(s) and method(s).
    Creates an API for checks and loads an information argument parser.
'''

import sys
from typing import Any, List
from abc import abstractmethod

try:
    from ats_utilities.config_io.yaml import YamlBase
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class YamlCLI(YamlBase):
    '''
        Defines class YamlCLI with attribute(s) and method(s).
        Creates an API for checks and loads an information argument parser.
        Command-line interface configuration based on YAML format.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials YamlCLI constructor.
                | add_new_option - Adds a new option for the CL interface.
                | parse_args - Parses the CL arguments.
                | process - Processes and runs tool operations (Abstract).
    '''

    def __init__(self, info_file: str | None, verbose: bool = False) -> None:
        '''
            Initial YamlCLI constructor.

            :param info_file: Information file path | None
            :type info_file: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__(info_file, verbose)
        self._verbose: bool = verbose
        verbose_message(self._verbose, ['init ATS YAML cli'])

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

    def parse_args(self, argv: List[Any] | List[str]) -> Any | None:
        '''
            Parses the CL arguments.

            :param argv: List of arguments
            :type argv: <List[Any] | List[str]>
            :return: Options and arguments
            :rtype: <Any | NoneType>
            :exceptions: ATSTypeError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([('list:argv', argv)])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
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
