# -*- coding: UTF-8 -*-

'''
Module
    context_support.py
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
    Defines class ContextSupport with attribute(s) and method(s).
    Base implementation for context support.
'''

from __future__ import annotations

from typing import override

from ats_utilities.context.icontext_support import IContextSupport
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ContextSupport(IContextSupport):
    '''
        Defines class ContextSupport with attribute(s) and method(s).
        Base implementation for context support.

        It defines:

            :attributes:
                | _checker - Reference to checker.
                | _logger - Reference to logger.
                | _reporter - Reference to reporter.
                | _verbose - Verbose mode.
            :methods:
                | __init__ - ContextSupport constructor.
                | checker - Property for getting checker.
                | logger - Property for getting logger.
                | reporter - Property for getting reporter.
                | verbose - Property for getting verbose mode.
    '''

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes ContextSupport constructor.

            :param context_bundle: Context bundle with dependencies.
            :type context_bundle: <ContextBundle>
            :exceptions:
                | ATSValueError - Context bundle must be provided.
                | ATSTypeError - Context bundle must be a ContextBundle instance.
        '''
        not_none(
            context_bundle,
            r'context_support::init(...)',
            r'context bundle must be provided'
        )
        istype(
            context_bundle, ContextBundle,
            r'context_support::init(...)',
            r'context bundle must be a ContextBundle instance'
        )
        self._checker = context_bundle.checker
        self._logger = context_bundle.logger
        self._reporter = context_bundle.reporter
        self._verbose = context_bundle.verbose

    @property
    @override
    def checker(self) -> IChecker:
        '''
            Property method for getting checker.

            :return: Checker instance.
            :rtype: <IChecker>
            :exceptions: None.
        '''
        return self._checker

    @property
    @override
    def logger(self) -> ILogger:
        '''
            Property method for getting logger.

            :return: Logger instance.
            :rtype: <ILogger>
            :exceptions: None.
        '''
        return self._logger

    @property
    @override
    def reporter(self) -> IReporter:
        '''
            Property method for getting reporter.

            :return: Reporter instance.
            :rtype: <IReporter>
            :exceptions: None.
        '''
        return self._reporter

    @property
    @override
    def verbose(self) -> bool:
        '''
            Property method for checking if verbose option is enabled.

            :return: <True> if enabled, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._verbose
