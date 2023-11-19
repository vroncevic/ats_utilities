# -*- coding: UTF-8 -*-

'''
Module
    verbose.py
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
    Defines class ATSVerbose with attribute(s) and method(s).
    Creates verbose message container for console log mechanism.
'''

import sys
from typing import Tuple

try:
    from colorama import init, Fore
    from ats_utilities import auto_str, VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@auto_str
class ATSVerbose(metaclass=VerboseRoot):
    '''
        Defines class ATSVerbose with attribute(s) and method(s).
        Creates verbose message container for console log mechanism.
        Mechanism for logging verbose messages.

        It defines:

            :attributes:
                | _message - Verbose message container.
            :methods:
                | __init__ - Initial ATSVerbose constructor.
                | message - Property methods for set/get operations.
                | is_not_none - Check is message not None.
    '''

    _message: str | None

    def __init__(self) -> None:
        '''
            Initial ATSVerbose constructor.

            :exceptions: None
        '''
        self._message = None

    @property
    def message(self) -> str | None:
        '''
            Property method for getting message.

            :return: Formatted verbose message
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        '''
            Property method for setting message.

            :param message: Verbose message
            :type message: <str>
            :exceptions: None
        '''
        init(autoreset=False)
        self._message = f'{Fore.BLUE}{message}{Fore.RESET}'

    def is_not_none(self) -> bool:
        '''
            Checking is message not None.

            :return: True (not None) | False (it is None)
            :rtype: <bool>
            :exceptions: None
        '''
        return bool(self._message)


def verbose_message(
    verbose_path: str, control: bool, *message: Tuple[str, ...]
) -> None:
    '''
        Show verbose message.

        :param verbose_path: Verbose prefix message.
        :type verbose_path: <str>
        :param control: Enable/Disable verbose option.
        :type control: <bool>
        :param message: Message parts
        :type message: <Tuple[str, ...]>
        :exceptions: ATSTypeError | ATSBadCallError
    '''
    if control:
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:verbose_path', verbose_path), ('tuple:message', message)
        ])
        if error_id == ATSChecker.type_error:
            raise ATSTypeError(error_msg)
        if error_id == ATSChecker.value_error:
            raise ATSBadCallError(error_msg)
        verbose: ATSVerbose = ATSVerbose()
        verbose.message = ' '.join(tuple([str(item) for item in message]))
        print(f'[{verbose_path.lower()}] {verbose.message}')
