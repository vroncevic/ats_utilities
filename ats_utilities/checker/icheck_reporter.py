# -*- coding: UTF-8 -*-

'''
Module
    icheck_reporter.py
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
    Defines abstract class IATSCheckReporter with attribute(s) and method(s).
    Creates an interface for formating message report in context of checker.
'''

from abc import ABC, abstractmethod
from typing import List, Optional
from ats_utilities.checker.checker_reporter_bundle import ATSCheckerReporterBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IATSCheckReporter(ABC):
    '''
        Defines abstract class IATSCheckReporter with attribute(s) and method(s).
        Creates an interface for formating message report in context of checker.

        It defines:

            :attributes: None
            :methods:
                | build_message_format - Builds the final message report for checker.
                | __str__ - Returns a human-readable string representation of the reporter.
    '''
    @abstractmethod
    def build_message_format(self, report_bundle: Optional[ATSCheckerReporterBundle] = None) -> str:
        '''
            Builds the final message report for checker.

            :param report_bundle: Bundle with parameters | None
            :type report_bundle: <Optional[ATSCheckerReporterBundle]>
            :return: Formatted message report
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method build_message_format() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns a human-readable string representation of the reporter.

            :return: String representation
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
