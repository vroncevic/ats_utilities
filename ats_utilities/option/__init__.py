# -*- coding: utf-8 -*-

'''
Module
    __init__.py
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
    Defines class ATSOptionParser with attribute(s) and method(s).
    Creates an option parser and an argument processor.
'''

import sys
from typing import Any, List, Tuple, Optional, Sequence, TypeAlias
from argparse import ArgumentParser, Namespace

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

KnownArgs: TypeAlias = Tuple[Namespace, List[str]]
OptArgs: TypeAlias = Optional[Sequence[str]]


class ATSOptionParser(ATSChecker):
    '''
        Defines class ATSOptionParser with attribute(s) and method(s).
        Creates an option parser and an argument processor.
        Mechanism for application, tool, or script option parser.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _opt_parser - Options parser.
            :methods:
                | __init__ - Initials ATSOptionParser constructor.
                | add_operation - Adds an option to the ATS parser.
                | parse_input_args - Processes arguments from the start.
                | parse_args - Processes arguments from the start.
    '''

    def __init__(
        self,
        version: Optional[str],
        epilog: Optional[str],
        description: Optional[str],
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSOptionParser constructor.

            :param version: ATS version and build date | None
            :type version: <Optional[str]>
            :param epilog: ATS long description | None
            :type epilog: <Optional[str]>
            :param description: ATS author and license | None
            :type description: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        super().__init__()
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('str:version', version),
            ('str:epilog', epilog),
            ('str:description', description)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        self._verbose: bool = verbose
        self._opt_parser: ArgumentParser = ArgumentParser(
            version, epilog, description=description
        )
        verbose_message(
            self._verbose, [f'{version}, {epilog}, {description}']
        )

    def add_operation(self, *args: str, **kwargs: Any) -> None:
        '''
            Adds an option to the ATS parser.

            :param args: List of flags for the ATS
            :type args: <str>
            :param kwargs: Arguments in shape of dictionary
            :type kwargs: <Any>
            :exceptions: None
        '''
        self._opt_parser.add_argument(*args, **kwargs)

    def parse_input_args(
        self, arguments: OptArgs, verbose: bool = False
    ) -> Namespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None
            :type arguments: <OptArgs>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Namespace object
            :rtype: <Namespace>
            :exceptions: None
        '''
        args: Namespace = self._opt_parser.parse_args(arguments)
        verbose_message(self._verbose or verbose, [f'arguments {arguments}'])
        return args

    def parse_args(
            self, arguments: OptArgs, verbose: bool = False
    ) -> Namespace:
        '''
            Processes arguments from the start.

            :param arguments: Sequence of arguments | None
            :type arguments: <OptArgs>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Namespace object
            :rtype: <Namespace>
            :exceptions: None
        '''
        args: KnownArgs = self._opt_parser.parse_known_args(arguments)
        verbose_message(self._verbose or verbose, [f'arguments {arguments}'])
        return args[0]
