# -*- coding: UTF-8 -*-

'''
Module
    icontext_support.py
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
    Defines abstract class IContextSupport with method(s).
    Interface for context support mechanism.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IContextSupport(ABC):
    '''
        Defines abstract class IContextSupport with method(s).
        Interface for context support mechanism.

        It defines:

        :methods:
            | checker - Property for getting checker.
            | logger - Property for getting logger.
            | reporter - Property for getting reporter.
            | verbose - Property for getting verbose mode.
            | __str__ - Returns context support as string representation.
    '''

    @property
    @abstractmethod
    def checker(self) -> IChecker:
        '''
            Property method for getting checker.

            :return: Checker instance.
            :rtype: <IChecker>
            :exceptions: None.
        '''
        pass

    @property
    @abstractmethod
    def logger(self) -> ILogger:
        '''
            Property method for getting logger.

            :return: Logger instance.
            :rtype: <ILogger>
            :exceptions: None.
        '''
        pass

    @property
    @abstractmethod
    def reporter(self) -> IReporter:
        '''
            Property method for getting reporter.

            :return: Reporter instance.
            :rtype: <IReporter>
            :exceptions: None.
        '''
        pass

    @property
    @abstractmethod
    def verbose(self) -> bool:
        '''
            Property method for checking if verbose option is enabled.

            :return: <True> if enabled, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns context support as string representation.

            :return: Context support as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
