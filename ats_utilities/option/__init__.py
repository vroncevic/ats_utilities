# -*- coding: utf-8 -*-

'''
Module
    __init__.py
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
    Defines class ATSOptionParser with attribute(s) and method(s).
    Creates option parser and argument processor.
'''

import sys
from typing import Any, Sequence
from argparse import ArgumentParser, Namespace

try:
    from ats_utilities.checker import ATSChecker
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


class ATSOptionParser(ATSChecker):
    '''
        Defines class ATSOptionParser with attribute(s) and method(s).
        Creates option parser and argument processor.
        Mechanism for argument parser.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _opt_parser - Options parser.
            :methods:
                | __init__ - Initial ATSOptionParser constructor.
                | add_operation - Add option to ATS.
                | parse_args - Process arguments from start.
    '''

    _verbose: bool
    _opt_parser: ArgumentParser

    def __init__(
        self,
        version: str | None,
        epilog: str | None,
        description: str | None,
        verbose: bool = False
    ) -> None:
        '''
            Initial ATSOptionParser constructor.

            :param version: ATS version and build date | None
            :type version: <str> | <NoneType>
            :param epilog: ATS long description | None
            :type epilog: <str> | <NoneType>
            :param description: ATS author and license | None
            :type description: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        super().__init__()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('str:version', version), ('str:epilog', epilog),
            ('str:description', description)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        self._verbose = verbose
        self._opt_parser = ArgumentParser(version, epilog, description)
        verbose_message(
            self._verbose,
            [f'{str(version)}, {str(epilog)}, {str(description)}']
        )

    def add_operation(self, *args: str, **kwargs: Any) -> None:
        '''
            Add option to ATS parser.

            :param args: List of flags
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary
            :type kwargs: <Any>
            :exceptions: None
        '''
        self._opt_parser.add_argument(*args, **kwargs)

    def parse_args(
        self, arguments: Sequence[str], verbose: bool = False
    ) -> Namespace:
        '''
            Process arguments from start.

            :param arguments: Sequence of arguments
            :type arguments: <Sequence[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Namespace object
            :rtype: <Namespace>
            :exceptions: None
        '''
        args: Namespace = self._opt_parser.parse_args(arguments)
        verbose_message(self._verbose or verbose, [f'arguments {arguments}'])
        return args
