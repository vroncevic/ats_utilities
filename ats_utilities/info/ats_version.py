# -*- coding: UTF-8 -*-

'''
Module
    ats_version.py
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
    Defines class ATSVersion with attribute(s) and method(s).
    Creates an API for the ATS version in one property object.
'''

import sys
from typing import List, Optional

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


class ATSVersion(ATSChecker):
    '''
        Defines class ATSVersion with attribute(s) and method(s).
        Creates an API for the ATS version in one property object.
        The ATS version container.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _version - The ATS version.
            :methods:
                | __init__ - Initials ATSVersion constructor.
                | version - Property methods for set/get operations.
                | is_version_not_none - Checks is ATS version not None.
    '''

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials ATSVersion constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__()
        self._verbose: bool = verbose
        self._version: Optional[str] = None

    @property
    def version(self) -> Optional[str]:
        '''
            Property method for getting ATS version.

            :return: The ATS version | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self._version

    @version.setter
    def version(self, version: Optional[str]) -> None:
        '''
            Property method for setting ATS version.

            :param version: The ATS version | None
            :type version: <Optional[str]>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([('str:version', version)])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        self._version = version
        verbose_message(self._verbose, [f'version {version}'])

    def is_version_not_none(self) -> bool:
        '''
            Checks is ATS version not None.

            :return: True (ATS version is not None) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self._version is not None
