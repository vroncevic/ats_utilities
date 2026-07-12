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
    Defines component bundle dataclass for dependency grouping and management.
    Encapsulates reporter components to minimize constructor overhead.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

from ats_utilities.factory_value import require_not_none, require_not_satisfied
from ats_utilities.factory_type import check_type
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, kw_only=True)
class LoggerComponentBundle:
    '''
        Defines component bundle dataclass for dependency grouping and management.
        Encapsulates logger components to minimize constructor overhead.

        It defines:

            :attributes:
                | logger - Logger instance (default None).
                | log_file - Log file path (default None).
            :methods:
                | __post_init__ - Post-initializes LoggerComponentBundle.
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the LoggerComponentBundle instance to a dictionary.
    '''

    logger: Any | None = None
    log_file: str | None = None

    def __post_init__(self) -> None:
        '''
            Post-initializes LoggerComponentBundle.
            Post-initialization hook for automatic component creation and
            validation of component types. It tries to create component from
            passed parameters otherwise default values are used. In case of
            type validation failure raises ATSTypeError exception.

            :exceptions:
                | ATSTypeError: Logger must be an ILogger or standard logging.Logger instance.
        '''
        if self.logger is None:
            from logging import getLogger, basicConfig, INFO

            if not getLogger().hasHandlers():
                log_config: dict[str, Any] = {
                    'format': '%(asctime)s - %(levelname)s - %(message)s',
                    'datefmt': '%m/%d/%Y %I:%M:%S %p',
                    'level': INFO
                }

                if self.log_file is not None:
                    log_config['filename'] = self.log_file

                basicConfig(**log_config)

            self.logger = getLogger()

        require_not_satisfied(
            not (hasattr(self.logger, 'info') or hasattr(self.logger, 'write_log')),
            r'logger must be an ILogger instance or a standard logging.Logger instance',
            exception_class=ATSTypeError
        )

    def validate(self) -> None:
        '''
            Validates that LoggerComponentBundle is valid (can be called after merge).
            Performs validation of logger and log_file attributes.
            Logger must be non-None and have 'info' or 'write_log' attribute.
            Log file must be non-None and an instance of str type.

            :exceptions:
                | ATSValueError: Logger must be provided.
                | ATSValueError: Log file must be provided.
                | ATSTypeError: Logger must be an ILogger or standard logging.Logger instance.
                | ATSTypeError: Log file must be a str instance.
        '''
        require_not_none(self.logger, r'logger must be provided')
        require_not_none(self.log_file, r'log_file must be provided')
        require_not_satisfied(
            not (hasattr(self.logger, 'info') or hasattr(self.logger, 'write_log')),
            r'logger must be an ILogger instance or a standard logging.Logger instance',
            exception_class=ATSTypeError
        )
        check_type(self.log_file, str, r'log_file must be a str instance')

    def merge(self, other: LoggerComponentBundle) -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <LoggerComponentBundle>
            :exceptions:
                | ATSValueError: Other LoggerComponentBundle must be provided.
                | ATSTypeError: Other must be a LoggerComponentBundle instance.
        '''
        require_not_none(other, r'other LoggerComponentBundle must be provided')
        check_type(other, LoggerComponentBundle, r'other must be a LoggerComponentBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the LoggerComponentBundle instance to a dictionary.

            :return: Dictionary representation of the LoggerComponentBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
