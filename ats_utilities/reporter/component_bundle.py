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

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import Checker
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.reporter.theme.engine import ConsoleTheme
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.logger.engine import Logger
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, kw_only=True)
class ReporterComponentBundle:
    '''
        Defines component bundle dataclass for dependency grouping and management.
        Encapsulates reporter components to minimize constructor overhead.

        It defines:

            :attributes:
                | checker - Parameters checker API (default None).
                | theme - Theme for styling messages (default None).
                | logger - Logger API (default None).
            :methods:
                | __post_init__ - Post-initializes ReporterComponentBundle.
                | validate - Validates that ReporterComponentBundle is valid (can be called after merge).
                | merge - Merges non-None values from another ReporterComponentBundle into this one.
                | to_dict - Converts the ReporterComponentBundle instance to a dictionary.
    '''

    checker: IChecker | None = None
    theme: IConsoleTheme | None = None
    logger: ILogger | None = None

    def __post_init__(self) -> None:
        '''
            Post-initializes ReporterComponentBundle.
            Post-initialization hook for automatic component creation and
            validation of component types. It tries to create component from
            passed parameters otherwise default values are used. In case of
            type validation failure raises ATSTypeError exception.

            :exceptions:
                | ATSTypeError: Component type validation failed (checker | theme | logger).
        '''
        self.checker: IChecker = make_component(self.checker, Checker, None)
        validate_component(self.checker, IChecker, r'checker must be an IChecker instance')
        self.theme: IConsoleTheme = make_component(self.theme, ConsoleTheme, None)
        validate_component(self.theme, IConsoleTheme, r'theme must be an IConsoleTheme instance')
        self.logger: ILogger = make_component(self.logger, Logger, None)
        validate_component(self.logger, ILogger, r'logger must be an ILogger instance')

    def validate(self) -> None:
        '''
            Validates that ReporterComponentBundle is valid (can be called after merge).
            Performs validation of checker, theme and logger attributes.
            Checker must be non-None and an instance of IChecker interface.
            Theme must be non-None and an instance of IConsoleTheme interface.
            Logger must be non-None and an instance of ILogger interface.

            :exceptions:
                | ATSValueError: Checker must be provided.
                | ATSValueError: Theme must be provided.
                | ATSValueError: Logger must be provided.
                | ATSTypeError: Checker must be an instance of IChecker interface.
                | ATSTypeError: Theme must be an instance of IConsoleTheme interface.
                | ATSTypeError: Logger must be an instance of ILogger interface.
        '''
        require_not_none(self.checker, r'checker must be provided')
        require_not_none(self.theme, r'theme must be provided')
        require_not_none(self.logger, r'logger must be provided')
        check_type(self.checker, IChecker, r'checker must be an IChecker instance')
        check_type(self.theme, IConsoleTheme, r'theme must be an IConsoleTheme instance')
        check_type(self.logger, ILogger, r'logger must be an ILogger instance')

    def merge(self, other: ReporterComponentBundle) -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <ReporterComponentBundle>
            :exceptions:
                | ATSValueError: Other ReporterComponentBundle must be provided.
                | ATSTypeError: Other must be a ReporterComponentBundle instance.
        '''
        require_not_none(other, r'other ReporterComponentBundle must be provided')
        check_type(other, ReporterComponentBundle, r'other must be a ReporterComponentBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the ReporterComponentBundle instance to a dictionary.

            :return: Dictionary representation of the ReporterComponentBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
