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

from typing import List, Optional
from ats_utilities.factory import inject, format_instance_to_string
from ats_utilities.info.ibuild_date import IATSBuildDate
from ats_utilities.checker.ichecker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.console_io.proxy_reporter import vreporter

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
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __build_date - The ATS build date (default None).
            :methods:
                | __init__ - Initials ATSBuildDate constructor.
                | build_date - Property methods for set/get operations.
                | is_build_date_not_none - Checks is ATS build date not None.
                | __str__ - Returns the string representation of ATS build date.
    '''

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSBuildDate constructor.

            :param checker: Parameters checker (default set ATSChecker) | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: Reporter for messaging (default set ATSReporter) | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :exceptions: None
        '''
        # No dependency injection then use default ones.
        inject(
            self,
            ('checker', checker, ATSChecker, None),
            ('reporter', reporter, ATSReporter, ['checker']),
            ('verbose', verbose, False, None)
        )
        self.__build_date: Optional[str] = None

    @property
    @vreporter('get build_date {build_date}')
    def build_date(self) -> Optional[str]:
        '''
            Property method for getting ATS build date.

            :return: The ATS build date in string format | None
            :rtype: <Optional[str]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__build_date

    @build_date.setter
    @validator([('Optional[str]:build_date', None)])
    @vreporter('set build_date {build_date}')
    def build_date(self, build_date: Optional[str]) -> None:
        '''
            Property method for setting ATS build date.

            :param build_date: The ATS build date in string format | None
            :type build_date: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__build_date = build_date

    @vreporter('check build_date {build_date}')
    def is_build_date_not_none(self) -> bool:
        '''
            Checks is ATS build date not None.

            :return: True (ATS build date is not None) | False (ATS build date is None).
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__build_date is not None

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS build date.

            :return: The ATS build date string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
