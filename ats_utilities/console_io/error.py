# -*- coding: UTF-8 -*-

'''
Module
    error.py
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
    Defines class ATSError with attribute(s) and method(s).
    Creates error message container for console log mechanism.
'''

import sys
from typing import Any, List

try:
    from colorama import init, Fore
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
__version__ = '2.9.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSError:
    '''
        Defines class ATSError with attribute(s) and method(s).
        Creates error message container for console log mechanism.
        Mechanism for logging error messages.

        It defines:

            :attributes:
                | _message - Error message container.
            :methods:
                | __init__ - Initial ATSError constructor.
                | message - Property methods for set/get operations.
                | is_not_none - Check is message not None.
    '''

    _message: str | None

    def __init__(self) -> None:
        '''
            Initial ATSError constructor.

            :exceptions: None
        '''
        self._message = None

    @property
    def message(self) -> str | None:
        '''
            Property method for getting message.

            :return: Formatted errors message | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self._message

    @message.setter
    def message(self, message: str | None) -> None:
        '''
            Property method for setting message.

            :param message: Error message text
            :type message: <str>
            :exceptions: None
        '''
        init(autoreset=False)
        if message is not None:
            self._message = f'{Fore.RED}{message}{Fore.RESET}'

    def is_not_none(self) -> bool:
        '''
            Checking is message not None.

            :return: True (not None) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self._message is not None


def error_message(message: List[Any]) -> None:
    '''
        Show error message.

        :param message: Message combined as list of any elements
        :type message: <List[Any]>
        :exceptions: ATSTypeError | ATSBadCallError
    '''
    checker: ATSChecker = ATSChecker()
    error_msg: str | None = None
    error_id: int | None = None
    error_msg, error_id = checker.check_params([('list:message', message)])
    if error_id == checker.TYPE_ERROR:
        raise ATSTypeError(error_msg)
    if error_id == checker.VALUE_ERROR:
        raise ATSBadCallError(error_msg)
    error: ATSError = ATSError()
    error.message = ' '.join([str(item) for item in message])
    if error.is_not_none():
        print(f'{error.message}')
