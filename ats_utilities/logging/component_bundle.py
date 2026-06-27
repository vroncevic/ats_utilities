# -*- coding: UTF-8 -*-

'''
Module
    component_bundle.py
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
    Defines component bundle data classe for dependency group simplification.
    Encapsulates logging components to minimize constructor overhead.
'''

from typing import Any
from dataclasses import dataclass
from ats_utilities.logging.ilogger import ILogger
from ats_utilities.logging.logger_bundle import LoggerBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class LoggingComponentBundle:
    '''
        Defines component bundle data classe for dependency group simplification.
        Encapsulates logging components to minimize constructor overhead.

        It defines:

            :attributes:
                | logger - Logger instance (default None).
                | logger_bundle - Bundle with logger parameters (default None).
                | context_bundle - Bundle with context (default None).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    logger: ILogger | None = None
    logger_bundle: LoggerBundle | None = None
    context_bundle: ContextBundle | None = None

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ATSValueError - Logger must be provided.
                | ATSValueError - Logger bundle must be provided.
                | ATSValueError - Context bundle must be provided.
        '''
        if self.logger is None:
            raise ATSValueError('logger must be provided.')

        if self.logger_bundle is None:
            raise ATSValueError('logger bundle must be provided.')

        if self.context_bundle is None:
            raise ATSValueError('context bundle must be provided.')

    def merge(self, other: 'LoggingComponentBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <LoggingComponentBundle>
            :exceptions: None.
        '''
        for field_name in self.__dataclass_fields__:
            other_value = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the bundle attributes to a dictionary.

            :return: Dictionary representation of the bundle attributes.
            :rtype: <dict>
            :exceptions: None.
        '''
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_')
        }

