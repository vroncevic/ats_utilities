# -*- coding: UTF-8 -*-

'''
Module
    pro_name.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class ProName with attribute(s) and method(s).
    Defines project name container.
'''

import sys
from typing import List

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProName:
    '''
        Defines class ProName with attribute(s) and method(s).
        Defines project name container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | _pro_name - Project name.
            :methods:
                | __init__ - Initials ProName constructor.
                | pro_name - Property methods for set/get operations.
                | is_pro_name_ok - Checks is project name ok.
    '''

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials ProName constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self._pro_name: str | None = None
        verbose_message(verbose, ['init project name'])

    @property
    def pro_name(self) -> str | None:
        '''
            Property method for getting project name.

            :return: Formatted project name | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self._pro_name

    @pro_name.setter
    def pro_name(self, pro_name: str | None) -> None:
        '''
            Property method for setting project name.

            :param pro_name: Project name | None
            :type pro_name: <str> | <NoneType>
            :exceptions: ATSTypeError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:pro_name', pro_name)
        ])
        if error_id == checker.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        self._pro_name = pro_name

    def is_pro_name_ok(self) -> bool:
        '''
            Checks is project name ok.

            :return: True (project name is ok) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return all([bool(self._pro_name), isinstance(self._pro_name, str)])
