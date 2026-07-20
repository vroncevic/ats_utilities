# -*- coding: UTF-8 -*-

'''
Module
    logger_bundle.py
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
    Encapsulates logger runtime components for simplification of LoggerBundle creation.
'''

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ats_utilities.validation.check_value import not_none, not_satisfied
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
class LoggerBundle:
    '''
        Encapsulates logger runtime components for simplification of LoggerBundle creation.

        It defines:

            :attributes:
                | logger - Logger instance.
                | log_file - Log file path.
                | log_level - Log level.
            :methods:
                | __post_init__ - Post-initialization hook to validate logger bundle.
                | validate - Validates logger bundle.
                | to_dict - Converts logger bundle instance to dictionary.
    '''

    logger: Any
    log_file: str
    log_level: int

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate logger bundle.

            :exceptions:
                | ATSValueError: Logger must be provided.
                | ATSValueError: Log file must be provided.
                | ATSValueError: Log level must be provided.
                | ATSTypeError: Logger must be an ILogger or standard logging.Logger instance.
                | ATSTypeError: Log file must be a str instance.
                | ATSTypeError: Log level must be an int instance.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates logger bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Logger must be provided.
                | ATSValueError: Log file must be provided.
                | ATSValueError: Log level must be provided.
                | ATSTypeError: Logger must be an ILogger or standard logging.Logger instance.
                | ATSTypeError: Log file must be a str instance.
                | ATSTypeError: Log level must be an int instance.
        '''
        context: str = r'logger_bundle::validate(...)'
        not_none(self.logger, context, r'logger must be provided')
        not_none(self.log_file, context, r'log file must be provided')
        not_none(self.log_level, context, r'log level must be provided')
        istype(self.log_file, str, context, r'log file must be a str instance')
        istype(self.log_level, int, context, r'log level must be an int instance')
        not_satisfied(
            not (hasattr(self.logger, 'info') or hasattr(self.logger, 'write_log')), context,
            r'logger must be an ILogger instance or a standard logging.Logger instance'
        )

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts logger bundle instance to dictionary.

            :return: Dictionary representation of the logger bundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
