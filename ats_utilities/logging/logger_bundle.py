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
    Defines parameter bundle data classes for dependency group simplification.
    Encapsulates core utilities to minimize constructor overhead.
'''

from dataclasses import dataclass
from typing import Any

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class LoggerBundle:
    '''
        Encapsulates the core system tracking, verification, and infrastructure components.
        Simplifies dependency passing for checker, reporter and verbosity settings.

        It defines:

            :attributes:
                | name - Logger name in string format (default None).
                | configure_logging - Flag for configuring logging (default True).
                | log_stdout - Flag for enabling logging to standard output (default True).
                | log_file - Logger file path in string format (default None). 
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    name: str | None = None
    configure_logging: bool = True
    log_stdout: bool = True
    log_file: str | None = None

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ValueError - Logger name must be provided.
                | ValueError - Configure logging must be provided.
                | ValueError - Log to standard output must be provided.
                | ValueError - Log file must be provided.
        '''
        if not self.name or not isinstance(self.name, str):
            raise ValueError('logger name must be provided.')

        if not isinstance(self.configure_logging, bool):
            raise ValueError('configure_logging must be a boolean.')

        if not isinstance(self.log_stdout, bool):
            raise ValueError('log_stdout must be a boolean.')

        if not self.log_file or not isinstance(self.log_file, str):
            raise ValueError('log_file must be a string.')

    def merge(self, other: 'LoggerBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <LoggerBundle>
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
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_')
        }

