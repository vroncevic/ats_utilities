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
    Defines parameter bundle dataclass for component dependency management.
    Encapsulates core runtime components for simplifcation.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.component_bundle import CheckerComponentBundle
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.logger.engine import Logger
from ats_utilities.logger.component_bundle import LoggerComponentBundle
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import Reporter
from ats_utilities.reporter.theme.engine import ConsoleTheme
from ats_utilities.reporter.component_bundle import ReporterComponentBundle
from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, kw_only=True)
class ContextBundle:
    '''
        Encapsulates core runtime components for simplifcation.
        Enables passing dependencies to other components.

        It defines:

            :attributes:
                | checker - Checker for parameters (default None).
                | logger - Logger for logging (default None).
                | reporter - Reporter for providing all types of messages (default None).
                | verbose - Flag for enabling verbose output (default False).
            :methods:
                | __post_init__ - Post-initialization hook to set up default components if not provided.
                | validate - Validates that ContextBundle is valid (can be called after merge).
                | merge - Merges non-None values from another ContextBundle into this one.
                | to_dict - Converts the ContextBundle instance to a dictionary.
    '''

    checker: IChecker | None = None
    logger: ILogger | None = None
    reporter: IReporter | None = None
    verbose: bool = False

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to set up core components if not provided.
            Initializes Checker, Logger and Reporter if None.

            :exceptions: None.
        '''
        if self.checker is None:
            self.checker = Checker(component_bundle=CheckerComponentBundle())

        if self.logger is None:
            self.logger = Logger(component_bundle=LoggerComponentBundle())

        if self.reporter is None:
            self.reporter = Reporter(
                component_bundle=ReporterComponentBundle(
                    checker=self.checker, theme=ConsoleTheme(), logger=self.logger
                )
            )

    def validate(self) -> None:
        '''
            Validates that ContextBundle is valid (can be called after merge).
            Performs validation of checker, logger, reporter and verbose attributes.
            Checker must be non-None and an instance of IChecker interface.
            Logger must be non-None and an instance of ILogger interface.
            Reporter must be non-None and an instance of IReporter interface.
            Verbose must be boolean.

            :exceptions:
                | ATSValueError: Checker must be provided.
                | ATSValueError: Logger must be provided.
                | ATSValueError: Reporter must be provided.
                | ATSTypeError: Checker must be an instance of IChecker interface.
                | ATSTypeError: Logger must be an instance of ILogger interface.
                | ATSTypeError: Reporter must be an instance of IReporter interface.
                | ATSTypeError: Verbose must be a boolean.
        '''
        require_not_none(self.checker, r'checker must be provided')
        require_not_none(self.logger, r'logger must be provided')
        require_not_none(self.reporter, r'reporter must be provided')
        check_type(self.checker, IChecker, r'checker must be an instance of IChecker interface')
        check_type(self.logger, ILogger, r'logger must be an instance of ILogger interface')
        check_type(self.reporter, IReporter, r'reporter must be an instance of IReporter interface')
        check_type(self.verbose, bool, r'verbose must be a boolean')

    def merge(self, other: ContextBundle) -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <ContextBundle>
            :exceptions:
                | ATSValueError: Other must be provided.
                | ATSTypeError: Other must be a ContextBundle instance.
        '''
        require_not_none(other, r'other must be provided')
        check_type(other, ContextBundle, r'other must be a ContextBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the ContextBundle instance to a dictionary.

            :return: Dictionary representation of the ContextBundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
