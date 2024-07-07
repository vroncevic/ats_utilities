# -*- coding: UTF-8 -*-

'''
Module
    success.py
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
    Defines class ATSSuccess with attribute(s) and method(s).
    Creates a success message container for the console log mechanism.
'''

import sys
from typing import Any, List, Optional

try:
    from colorama import init, Fore
    from ats_utilities.checker import ATSChecker
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


class ATSSuccess:
    '''
        Defines class ATSSuccess with attribute(s) and method(s).
        Creates a success message container for the console log mechanism.
        Mechanism for logging success messages.

        It defines:

            :attributes:
                | _message - Success message container.
            :methods:
                | __init__ - Initials ATSSuccess constructor.
                | message - Property methods for set/get operations.
                | is_not_none - Checks is message not None.
    '''

    def __init__(self) -> None:
        '''
            Initials ATSSuccess constructor.

            :exceptions: None
        '''
        self._message: Optional[str] = None

    @property
    def message(self) -> Optional[str]:
        '''
            Property method for getting message.

            :return: Formatted success message | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self._message

    @message.setter
    def message(self, message: Optional[str]) -> None:
        '''
            Property method for setting message.

            :param message: Succcess message | None
            :type message: <Optional[str]>
            :exceptions: None
        '''
        if message:
            init(autoreset=False)
            self._message = f'{Fore.GREEN}{message}{Fore.RESET}'

    def is_not_none(self) -> bool:
        '''
            Checks is message not None.

            :return: True (message is not None) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self._message is not None


def success_message(message: List[Any]) -> None:
    '''
        Shows success message.

        :param message: Message combined as list of any elements
        :type message: <List[Any]>
        :exceptions: ATSTypeError
    '''
    checker: ATSChecker = ATSChecker()
    error_msg: Optional[str] = None
    error_id: Optional[int] = None
    error_msg, error_id = checker.check_params([('list:message', message)])
    if error_id == checker.TYPE_ERROR:
        raise ATSTypeError(error_msg)
    success: ATSSuccess = ATSSuccess()
    success.message = ' '.join([str(item) for item in message])
    if success.is_not_none():
        print(f'{success.message}')
