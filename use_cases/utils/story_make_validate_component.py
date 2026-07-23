# -*- coding: utf-8 -*-

'''
Module
    story_make_validate_component.py
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
    Use cases for ATS context bundle.
'''

from collections.abc import Sequence

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.setup.factory import CheckerFactory
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.logger.engine import Logger
from ats_utilities.logger.setup.factory import LoggerFactory
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import Reporter
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.reporter.theme.engine import ConsoleTheme
from ats_utilities.reporter.reporter_bundle import ReporterBundle
from ats_utilities.utils.component import make_component, validate_component
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class TestComponent:
    '''
    Test component for demonstrating factory component utilities.
    '''
    def __init__(self) -> None:
        '''
        Initialize a new instance of the TestComponent class.

        :exceptions: None.
        '''
        checker_bundle = CheckerFactory.create_default_bundle()
        self.checker: IChecker = make_component(None, Checker, {'own': checker_bundle})
        self.theme: IConsoleTheme = make_component(None, ConsoleTheme, None)
        logger_bundle = LoggerFactory.create_default_bundle()
        logger_instance = make_component(None, Logger, {'own': logger_bundle})
        reporter_bundle = ReporterBundle(theme=self.theme, checker=self.checker, logger=logger_instance)
        self.reporter: IReporter = make_component(None, Reporter, {'own': reporter_bundle})

    def validate(self) -> None:
        '''
        Validate all components.

        :exceptions: None.
        '''
        validate_component(self.checker, IChecker, 'testcomponent::validate', 'checker should be of type IChecker')
        validate_component(self.theme, IConsoleTheme, 'testcomponent::validate', 'theme should be of type IConsoleTheme')
        validate_component(self.reporter, IReporter, 'testcomponent::validate', 'reporter should be of type IReporter')

    def wrong_validate(self) -> None:
        '''
        Validate components with wrong types.

        :exceptions: None.
        '''
        validate_component(self.checker, IChecker, 'testcomponent::wrong_validate', 'checker should be of type IChecker')
        validate_component(self.theme, IConsoleTheme, 'testcomponent::wrong_validate', 'theme should be of type IConsoleTheme')
        validate_component(self.reporter, int, 'testcomponent::wrong_validate', 'reporter should be of type IReporter')

    def run_message(self, message: Sequence[str]) -> None:
        """
        Run the message.

        :param message: Messages to run.
        :type message: Sequence[str]
        :exceptions: None.
        """
        self.reporter.success(message)

    def __str__(self) -> str:
        return f'TestComponent({self.checker}, {self.theme}, {self.reporter})'


try:
    test_component: TestComponent = TestComponent()
    test_component.validate()
    test_component.wrong_validate()
    test_component.run_message(['This is a test message', 'Another test message', 'Yet another test message'])

except ATSTypeError as exc:
    print(exc)