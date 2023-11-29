# -*- coding: UTF-8 -*-

'''
Module
    json_cli.py
Copyright
    Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class JsonCLI with attribute(s) and method(s).
    Creates API for check and load information, setup argument parser.
'''

import sys
from typing import Any
from abc import abstractmethod

try:
    from ats_utilities.config_io.json import JsonBase
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class JsonCLI(JsonBase):
    '''
        Defines class JsonCLI with attribute(s) and method(s).
        Creates API for check and load information, setup argument parser.
        Command line interface configurtion based on JSON format.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initial JsonCLI constructor.
                | add_new_option - Adding new option for CL interface.
                | parse_args - Parse CL arguments.
                | process - Process and run tool operation (Abstract method).
    '''

    _verbose: bool

    def __init__(
        self, information_file: str | None, verbose: bool = False
    ) -> None:
        '''
            Initial JsonCLI constructor.

            :param information_file: Informations file path | None
            :type information_file: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        super().__init__(information_file, verbose)
        self._verbose = verbose
        verbose_message(self._verbose, ['init ATS json cli'])

    def add_new_option(self, *args: str, **kwargs: Any) -> None:
        '''
            Adding new option for CL interface.

            :param args: Arguments in string form
            :type args: <str>
            :param kwargs: arguments in Any form
            :type kwargs: <Any>
            :exceptions: None
        '''
        self.option_parser.add_operation(*args, **kwargs)

    def parse_args(self, argv: list[Any] | list[str]) -> Any | None:
        '''
            Process arguments from start.

            :param argv: List of arguments
            :type argv: <list[Any] | list[str]>
            :return: Options and arguments
            :rtype: <Any | NoneType>
            :exceptions: None
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([('list:argv', argv)])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        return self.option_parser.parse_args(argv)

    @abstractmethod
    def process(self, verbose: bool = False) -> bool:
        '''
            Process and run tool operation (Abstract method).

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (successfully finished) | False
            :rtype: <bool>
            :exception: TypeError
        '''
