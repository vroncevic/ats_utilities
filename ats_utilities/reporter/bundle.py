# -*- coding: UTF-8 -*-

'''
Module
    reporter_bundle.py
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
    Encapsulates reporter runtime components for simplification of ReporterBundle creation.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.logger.ilogger import ILogger
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
class ReporterBundle:
    '''
        Encapsulates reporter runtime components for simplification of ReporterBundle creation.

        It defines:

            :attributes:
                | checker - Checker for parameters validation.
                | theme - Theme for console output styling.
                | logger - Logger for messages logging.
            :methods:
                | __post_init__ - Post-initializes ReporterBundle.
                | validate - Validates reporter bundle.
                | to_dict - Converts reporter bundle instance to a dictionary.
    '''

    checker: IChecker
    theme: IConsoleTheme
    logger: ILogger

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate reporter bundle.

            :exceptions:
                | ATSValueError: Checker must be provided.
                | ATSValueError: Theme must be provided.
                | ATSValueError: Logger must be provided.
                | ATSTypeError: Checker must be an instance of IChecker interface.
                | ATSTypeError: Theme must be an instance of IConsoleTheme interface.
                | ATSTypeError: Logger must be an instance of ILogger interface.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates reporter bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Checker must be provided.
                | ATSValueError: Theme must be provided.
                | ATSValueError: Logger must be provided.
                | ATSTypeError: Checker must be an instance of IChecker interface.
                | ATSTypeError: Theme must be an instance of IConsoleTheme interface.
                | ATSTypeError: Logger must be an instance of ILogger interface.
        '''
        context: str = r'reporter_bundle::validate(...)'
        not_none(self.checker, context, r'checker must be provided')
        not_none(self.theme, context, r'theme must be provided')
        not_none(self.logger, context, r'logger must be provided')
        istype(self.checker, IChecker, context, r'checker must be an IChecker instance')
        istype(self.theme, IConsoleTheme, context, r'theme must be an IConsoleTheme instance')
        istype(self.logger, ILogger, context, r'logger must be an ILogger instance')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts reporter bundle instance to a dictionary.

            :return: Dictionary representation of the reporter bundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
