# -*- coding: UTF-8 -*-

'''
Module
    info_ok.py
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
    Defines class ATSInfoOk with attribute(s) and method(s).
    Creates an API for the ATS info status in one property object.
'''

from typing import ClassVar, List, Optional
from ats_utilities.checker import IATSChecker, ATSChecker, ErrorChecker
from ats_utilities.console_io import IATSReporter, ATSReporter
from ats_utilities.exceptions import ATSTypeError
from .iinfo_ok import IATSInfoOk

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSInfoOk(IATSInfoOk):
    '''
        Defines class ATSInfoOk with attribute(s) and method(s).
        Creates an API for the ATS info status in one property object.
        The ATS info status container.

        It defines:

            :attributes:
                | ERRORS - Error checker mapping.
                | __checker - Error checker.
                | __reporter - ATSReporter for messaging.
                | __verbose - Enable/Disable verbose option.
                | __ats_info_ok - The ATS information status.
            :methods:
                | __init__ - Initials ATSInfoOk constructor.
                | ats_info_ok - Property methods for set/get operations.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSInfoOk constructor.

            :param checker: Error checker | None
            :type checker: <Optional[ATSChecker]>
            :param reporter: ATSReporter for messaging | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__ats_info_ok: bool = False

    @property
    def ats_info_ok(self) -> bool:
        '''
            Property method for getting ATS information status.

            :return: The ATS information status
            :rtype: <bool>
            :exceptions: None
        '''
        return self.__ats_info_ok

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
        error_msg, error_id = self.__checker.validate_parameters([('bool:ats_info_ok', ats_info_ok)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        self.__ats_info_ok = ats_info_ok
        self.__reporter.verbose(self.__verbose, [f'info {ats_info_ok}'])
