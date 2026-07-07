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

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


@dataclass(slots=True, kw_only=True)
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
                | validate - Validates that LoggerBundle is valid (can be called after merge).
                | merge - Merges non-None values from another LoggerBundle into this one.
                | to_dict - Converts the LoggerBundle instance to a dictionary.
    '''

    name: str | None = None
    configure_logging: bool = True
    log_stdout: bool = True
    log_file: str | None = None

    def validate(self) -> None:
        '''
            Validates that LoggerBundle is valid (can be called after merge).
            Performs validation of name, configure_logging, log_stdout and log_file attributes.
            Name must be non-None.
            Configure logging must be non-None.
            Log to standard output must be non-None.
            Log file must be non-None.

            :exceptions:
                | ATSValueError: Logger name must be provided.
                | ATSValueError: Configure logging must be provided.
                | ATSValueError: Log to standard output must be provided.
                | ATSValueError: Log file must be provided.
                | ATSTypeError: Configure logging must be a boolean.
                | ATSTypeError: Log to standard output must be a boolean.
                | ATSTypeError: Log file must be a string.
                | ATSTypeError: Name must be a string.
        '''
        require_not_none(self.name, "name must be provided")
        require_not_none(self.configure_logging, "configure_logging must be provided")
        require_not_none(self.log_stdout, "log_stdout must be provided")
        require_not_none(self.log_file, "log_file must be provided")
        check_type(self.configure_logging, bool, "configure_logging must be a boolean")
        check_type(self.log_stdout, bool, "log_stdout must be a boolean")
        check_type(self.log_file, str, "log_file must be a string")
        check_type(self.name, str, "name must be a string")

    def merge(self, other: LoggerBundle) -> None:
        '''
            Merges non-None values from another LoggerBundle into this one.

            :param other: Another LoggerBundle to merge into this one.
            :type other: <LoggerBundle>
            :exceptions:
                | ATSTypeError: Other must be a LoggerBundle instance.
        '''
        check_type(other, LoggerBundle, "other must be a LoggerBundle instance")

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the LoggerBundle instance to a dictionary.

            :return: Dictionary representation of the LoggerBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return asdict(self)
