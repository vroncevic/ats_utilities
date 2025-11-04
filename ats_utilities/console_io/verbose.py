# -*- coding: UTF-8 -*-

'''
Module
    verbose.py
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
    Defines class ATSVerbose with attribute(s) and method(s).
    Creates a verbose message container for the console log mechanism.
'''

import sys
from typing import Any, List, Optional

try:
    from colorama import init, Fore
    from ats_utilities.checker import ATSChecker
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as ats_error_message:  # pragma: no cover
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')  # pragma: no cover

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSVerbose:
    '''
        Defines class ATSVerbose with attribute(s) and method(s).
        Creates a verbose message container for the console log mechanism.
        Mechanism for logging verbose messages.

        It defines:

            :attributes:
                | _message - Verbose message container.
            :methods:
                | __init__ - Initials ATSVerbose constructor.
                | message - Property methods for set/get operations.
                | is_not_none - Checks is message not None.
    '''

    def __init__(self) -> None:
        '''
            Initials ATSVerbose constructor.

            :exceptions: None
        '''
        self._message: Optional[str] = None

    @property
    def message(self) -> Optional[str]:
        '''
            Property method for getting message.

            :return: Formatted verbose message | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self._message

    @message.setter
    def message(self, message: Optional[str]) -> None:
        '''
            Property method for setting message.

            :param message: Verbose message | None
            :type message: <Optional[str]>
            :exceptions: None
        '''
        if message:
            init(autoreset=False)
            self._message = f'{Fore.BLUE}{message}{Fore.RESET}'

    def is_not_none(self) -> bool:
        '''
            Checks is message not None.

            :return: True (message is not None) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self._message is not None


def verbose_message(control: bool, message: List[Any]) -> None:
    '''
        Shows verbose message.

        :param control: Enable/Disable verbose option
        :type control: <bool>
        :param message: Message combined as list of any elements
        :type message: <List[Any]>
        :exceptions: ATSTypeError
    '''
    checker: ATSChecker = ATSChecker()
    error_msg: Optional[str] = None
    error_id: Optional[int] = None
    error_msg, error_id = checker.check_params([
        ('bool:control', control), ('list:message', message)
    ])
    if error_id == checker.TYPE_ERROR:
        raise ATSTypeError(error_msg)
    if control:
        verbose: ATSVerbose = ATSVerbose()
        verbose.message = ' '.join([str(item) for item in message])
        if verbose.is_not_none():
            print(f'{verbose.message}')
