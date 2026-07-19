# -*- coding: UTF-8 -*-

'''
Module
    context_support_test.py
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
    Unit tests for ContextSupport base class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.context.context_support import ContextSupport
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyContextSupport(ContextSupport):
    def __str__(self) -> str:
        return "DummyContextSupport"


class ContextSupportTest(unittest.TestCase):
    '''
        Defines class ContextSupportTest with attribute(s) and method(s).
        Tests ContextSupport base class.
    '''

    def setUp(self) -> None:
        '''
            Set up standard mocked dependencies.
        '''
        self.mock_checker = MagicMock(spec=IChecker)
        self.mock_logger = MagicMock(spec=ILogger)
        self.mock_reporter = MagicMock(spec=IReporter)
        self.context_bundle = ContextBundle(
            checker=self.mock_checker,
            logger=self.mock_logger,
            reporter=self.mock_reporter,
            verbose=True
        )

    def test_initialization_success(self) -> None:
        '''
            Tests successful initialization and property getters.
        '''
        support = DummyContextSupport(self.context_bundle)
        self.assertIs(support.checker, self.mock_checker)
        self.assertIs(support.logger, self.mock_logger)
        self.assertIs(support.reporter, self.mock_reporter)
        self.assertTrue(support.verbose)

    def test_initialization_none_bundle(self) -> None:
        '''
            Tests initialization fails with None bundle.
        '''
        with self.assertRaises(ATSValueError):
            DummyContextSupport(None)  # type: ignore

    def test_initialization_invalid_bundle_type(self) -> None:
        '''
            Tests initialization fails with invalid bundle type.
        '''
        with self.assertRaises(ATSTypeError):
            DummyContextSupport("not a bundle")  # type: ignore


if __name__ == "__main__":
    unittest.main()
