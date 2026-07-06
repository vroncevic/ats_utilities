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

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.logging.logger.ilogger import ILogger
from ats_utilities.logging.logger.logger import StandardLogger
from ats_utilities.logging.logger.logger_bundle import LoggerBundle
from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

@dataclass(slots=True, kw_only=True)
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
                | __post_init__ - Post-initialization hook for automatic component creation.
                | validate - Validates that LoggingComponentBundle is valid (can be called after merge).
                | merge - Merges non-None values from another LoggingComponentBundle into this one.
                | to_dict - Converts the LoggingComponentBundle instance to a dictionary.
    '''

    logger: ILogger | None = None
    logger_bundle: LoggerBundle | None = None
    context_bundle: ContextBundle | None = None

    def __post_init__(self) -> None:
        '''
            Post-initialization hook for automatic component creation.

            :exceptions:
                | ATSTypeError: Logger must be an instance of ILogger interface.
        '''
        if self.context_bundle is None:
            self.context_bundle = ContextBundle()

        if self.logger_bundle is None:
            self.logger_bundle = LoggerBundle()

        self.logger = make_component(
            self.logger, StandardLogger,
            {
                'logger_bundle': self.logger_bundle,
                'context_bundle': self.context_bundle
            }
        )
        validate_component(self.logger, ILogger, 'logger must be an ILogger instance')

    def validate(self) -> None:
        '''
            Validates that LoggingComponentBundle is valid (can be called after merge).
            Performs validation of logger, logger_bundle and context_bundle attributes.
            Logger must be non-None and an instance of ILogger interface.
            Logger bundle must be non-None.
            Context bundle must be non-None.

            :exceptions:
                | ATSValueError: Logger must be provided.
                | ATSValueError: Logger bundle must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Logger must be an instance of ILogger interface.
                | ATSTypeError: Logger bundle must be an instance of LoggerBundle.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        require_not_none(self.logger, 'logger must be provided')
        require_not_none(self.logger_bundle, 'logger bundle must be provided')
        require_not_none(self.context_bundle, 'context bundle must be provided')
        check_type(self.logger, ILogger, 'logger must be an instance of ILogger interface')
        check_type(self.logger_bundle, LoggerBundle, 'logger bundle must be an instance of LoggerBundle')
        check_type(self.context_bundle, ContextBundle, 'context bundle must be an instance of ContextBundle')

    def merge(self, other: LoggingComponentBundle) -> None:
        '''
            Merges non-None values from another LoggingComponentBundle into this one.

            :param other: Another LoggingComponentBundle to merge into this one.
            :type other: <LoggingComponentBundle>
            :exceptions:
                | ATSTypeError: Other must be a LoggingComponentBundle instance.
        '''
        check_type(other, LoggingComponentBundle, 'other must be a LoggingComponentBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the LoggingComponentBundle instance to a dictionary.

            :return: Dictionary representation of the LoggingComponentBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return asdict(self)
