# -*- coding: UTF-8 -*-

'''
Module
    build_date.py
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
    Defines class ATSBuildDate with attribute(s) and method(s).
    Creates an API for the ATS build date in one property object.
'''

from typing import ClassVar, List, Optional
from ats_utilities.checker.ichecker import IATSChecker, ErrorChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.info.ibuild_date import IATSBuildDate

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBuildDate(IATSBuildDate):
    '''
        Defines class ATSBuildDate with attribute(s) and method(s).
        Creates an API for the ATS build date in one property object.
        The ATS build date container.

        It defines:

            :attributes:
                | ERRORS - Error checker mapping.
                | __checker - Error checker.
                | __reporter - ATSReporter for messaging.
                | __verbose - Enable/Disable verbose option.
                | __build_date - The ATS build date.
            :methods:
                | __init__ - Initials ATSBuildDate constructor.
                | build_date - Property methods for set/get operations.
                | is_build_date_not_none - Checks is ATS build date not None.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSBuildDate constructor.

            :param checker: Error checker | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__build_date: Optional[str] = None

    @property
    def build_date(self) -> Optional[str]:
        '''
            Property method for getting ATS build date.

            :return: The ATS build date | None
            :rtype: <Optional[str]>
            :exceptions: None
        '''
        return self.__build_date

    @build_date.setter
    def build_date(self, build_date: Optional[str]) -> None:
        '''
            Property method for setting ATS build date.

            :param build_date: The ATS build date | None
            :type build_date: <Optional[str]>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([('str:build_date', build_date)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        self.__build_date = build_date
        self.__reporter.verbose(self.__verbose, [f'build date {build_date}'])

    def is_build_date_not_none(self) -> bool:
        '''
            Checks is ATS build date not None.

            :return: True (ATS build date is not None) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return self.__build_date is not None
