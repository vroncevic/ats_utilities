# -*- coding: UTF-8 -*-

'''
Module
    ats_info_ok.py
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
    Defines class ATSInfoOk with attribute(s) and method(s).
    Creates an API for the ATS info status in one property object.
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


class ATSInfoOk(ATSChecker):
    '''
        Defines class ATSInfoOk with attribute(s) and method(s).
        Creates an API for the ATS info status in one property object.
        The ATS info status container.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _ats_info_ok - The ATS information status.
            :methods:
                | __init__ - Initials ATSInfoOk constructor.
                | ats_info_ok - Property methods for set/get operations.
    '''

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials ATSInfoOk constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__()
        self._verbose: bool = verbose
        self._ats_info_ok: bool = False

    @property
    def ats_info_ok(self) -> bool:
        '''
            Property method for getting ATS information status.

            :return: The ATS information status
            :rtype: <bool>
            :exceptions: None
        '''
        return self._ats_info_ok

    @ats_info_ok.setter
    def ats_info_ok(self, ats_info_ok: bool) -> None:
        '''
            Property method for setting ATS information status.

            :param ats_info_ok: The ATS information status
            :type ats_info_ok: <bool>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('bool:ats_info_ok', ats_info_ok)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        self._ats_info_ok = ats_info_ok
        verbose_message(self._verbose, [f'info {ats_info_ok}'])
