# -*- coding: utf-8 -*-

'''
Module
    story_require_attribute.py
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
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import Reporter
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.reporter.theme.engine import ConsoleTheme
from ats_utilities.reporter.component_bundle import ReporterComponentBundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import has_attrs
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class TestComponent:
    '''
    Test component for demonstrating factory component utilities.
    '''
    def __init__(self) -> None:
        '''
        Initialize a new instance of the TestComponent class.

        :exceptions: None.
        '''
        self._checker: IChecker = make_component(None, Checker, None)
        self._theme: IConsoleTheme = make_component(None, ConsoleTheme, None)
        self._reporter: IReporter = make_component(None, Reporter, {'component_bundle': ReporterComponentBundle(theme=self._theme, checker=self._checker)})
        validate_component(self._checker, IChecker, 'checker should be of type IChecker')
        validate_component(self._theme, IConsoleTheme, 'theme should be of type IConsoleTheme')
        validate_component(self._reporter, IReporter, 'reporter should be of type IReporter')

    def none_reporter(self) -> None:
        '''
        Validate components with wrong types.

        :exceptions: None.
        '''
        self._reporter = None

    @has_attrs('_reporter')
    def run_message(self, message: Sequence[str]) -> None:
        """
        Run the message.

        :param message: Messages to run.
        :type message: <Sequence[str]>
        :exceptions: None.
        """
        self._reporter.success(message)

    def __str__(self) -> str:
        return f'TestComponent({self._checker}, {self._theme}, {self._reporter})'


try:
    test_component: TestComponent = TestComponent()
    test_component.none_reporter()
    test_component.run_message(['This is a test message', 'Another test message', 'Yet another test message'])

except (ATSTypeError, ATSValueError) as exc:
    print(exc)