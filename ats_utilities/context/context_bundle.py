# -*- coding: UTF-8 -*-

'''
Module
    context_bundle.py
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
    Encapsulates core runtime components for simplification of ContextBundle creation.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

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


@dataclass(slots=True, frozen=True, kw_only=True)
class ContextBundle:
    '''
        Encapsulates core runtime components for simplification of ContextBundle creation.
        Enables passing dependencies to other objects.

        It defines:

            :attributes:
                | checker - Checker for parameters.
                | logger - Logger for logging.
                | reporter - Reporter for providing all types of messages.
                | verbose - Flag for enabling verbose output.
            :methods:
                | __post_init__ - Post-initialization hook to validate context bundle.
                | validate - Validates context bundle.
                | to_dict - Converts context bundle to dictionary.
    '''

    checker: IChecker
    logger: ILogger
    reporter: IReporter
    verbose: bool

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate context bundle.

            :exceptions:
                | ATSValueError: Checker must be provided.
                | ATSValueError: Logger must be provided.
                | ATSValueError: Reporter must be provided.
                | ATSTypeError: Checker must be an instance of IChecker interface.
                | ATSTypeError: Logger must be an instance of ILogger interface.
                | ATSTypeError: Reporter must be an instance of IReporter interface.
                | ATSTypeError: Verbose must be a boolean.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates context bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Checker must be provided.
                | ATSValueError: Logger must be provided.
                | ATSValueError: Reporter must be provided.
                | ATSValueError: Verbose must be provided.
                | ATSTypeError: Checker must be an instance of IChecker interface.
                | ATSTypeError: Logger must be an instance of ILogger interface.
                | ATSTypeError: Reporter must be an instance of IReporter interface.
                | ATSTypeError: Verbose must be a boolean.
        '''
        context: str = r'context_bundle::validate(...)'
        not_none(self.checker, context, r'checker must be provided.')
        not_none(self.logger, context, r'logger must be provided.')
        not_none(self.reporter, context, r'reporter must be provided.')
        not_none(self.verbose, context, r'verbose must be provided.')
        istype(self.checker, IChecker, context, r'checker must be an instance of IChecker interface.')
        istype(self.logger, ILogger, context, r'logger must be an instance of ILogger interface.')
        istype(self.reporter, IReporter, context, r'reporter must be an instance of IReporter interface.')
        istype(self.verbose, bool, context, r'verbose must be a boolean.')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts context bundle to dictionary.

            :return: Dictionary representation of context bundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
