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
    Defines abstract class ICheckReporter with method(s).
    Creates an interface for formating message report in context of checker.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

from ats_utilities.checker.reporter.data import CheckReporterData

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ICheckReporter(ABC):
    '''
        Defines abstract class ICheckReporter with method(s).
        Creates an interface for formating message report in context of checker.

        It defines:

            :methods:
                | build_message_format - Builds the final message report.
                | __str__ - Returns the check reporter as string representation.
    '''
    @abstractmethod
    def build_message_format(self, data: CheckReporterData) -> str:
        '''
            Builds the final message report.

            :param data: Data to be formatted.
            :type data: CheckReporterData
            :return: Formatted message report.
            :rtype: str
            :exceptions:
                | ATSValueError: Data must be provided.
                | ATSTypeError: Data must be a CheckReporterData instance.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the check reporter as string representation.

            :return: The check reporter as string representation.
            :rtype: str
            :exceptions: None.
        '''
        pass
