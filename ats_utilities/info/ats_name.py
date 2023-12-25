# -*- coding: UTF-8 -*-

'''
Module
    ats_name.py
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
    Defines class ATSName with attribute(s) and method(s).
    Creates an API for the ATS name in one property object.
'''

import sys
from typing import List

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
__version__ = '3.1.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSName(ATSChecker):
    '''
        Defines class ATSName with attribute(s) and method(s).
        Creates an API for the ATS name in one property object.
        The ATS name container.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _name - The ATS name.
            :methods:
                | __init__ - Initials ATSName constructor.
                | name - Property methods for set/get operations.
                | is_name_not_none - Checks is ATS name not None.
    '''

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials ATSName constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__()
        self._verbose: bool = verbose
        self._name: str | None = None

    @property
    def name(self) -> str | None:
        '''
            Property method for getting ATS name.

            :return: The ATS name | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self._name

    @name.setter
    def name(self, name: str | None) -> None:
        '''
            Property method for setting ATS name.

            :param name: The ATS name | None
            :type name: <str> | <NoneType>
            :exceptions: ATSTypeError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([('str:name', name)])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        self._name = name
        verbose_message(self._verbose, [f'name {name}'])

    def is_name_not_none(self) -> bool:
        '''
            Checks is ATS name not None.

            :return: True (ATS name is not None) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self._name is not None
