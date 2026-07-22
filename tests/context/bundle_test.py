# -*- coding: UTF-8 -*-

'''
Module
    context_bundle_test.py
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
    Unit tests for ContextBundle class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.context.bundle import ContextBundle
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


class ContextBundleTest(unittest.TestCase):
    '''
        Defines class ContextBundleTest with attribute(s) and method(s).
        Tests ContextBundle dataclass logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_valid - Tests successful creation of ContextBundle.
                | test_init_invalid_none - Tests creation of ContextBundle with missing attributes.
                | test_init_invalid_type - Tests creation of ContextBundle with wrong attribute types.
                | test_to_dict - Tests converting ContextBundle to a dictionary.
    '''

    def test_init_valid(self) -> None:
        '''
            Tests successful creation of ContextBundle.

            :exceptions: None.
        '''
        mock_checker = MagicMock(spec=IChecker)
        mock_logger = MagicMock(spec=ILogger)
        mock_reporter = MagicMock(spec=IReporter)

        try:
            bundle = ContextBundle(
                checker=mock_checker,
                logger=mock_logger,
                reporter=mock_reporter,
                verbose=True
            )
            self.assertIs(bundle.checker, mock_checker)
            self.assertIs(bundle.logger, mock_logger)
            self.assertIs(bundle.reporter, mock_reporter)
            self.assertTrue(bundle.verbose)
        except (ATSValueError, ATSTypeError):
            self.fail("Failed to instantiate ContextBundle with valid arguments.")

    def test_init_invalid_none(self) -> None:
        '''
            Tests creation of ContextBundle with missing attributes.

            :exceptions: None.
        '''
        mock_checker = MagicMock(spec=IChecker)
        mock_logger = MagicMock(spec=ILogger)
        mock_reporter = MagicMock(spec=IReporter)

        with self.assertRaises(ATSValueError):
            ContextBundle(checker=None, logger=mock_logger, reporter=mock_reporter, verbose=True)  # type: ignore

        with self.assertRaises(ATSValueError):
            ContextBundle(checker=mock_checker, logger=None, reporter=mock_reporter, verbose=True)  # type: ignore

        with self.assertRaises(ATSValueError):
            ContextBundle(checker=mock_checker, logger=mock_logger, reporter=None, verbose=True)  # type: ignore

        with self.assertRaises(ATSValueError):
            ContextBundle(checker=mock_checker, logger=mock_logger, reporter=mock_reporter, verbose=None)  # type: ignore

    def test_init_invalid_type(self) -> None:
        '''
            Tests creation of ContextBundle with wrong attribute types.

            :exceptions: None.
        '''
        mock_checker = MagicMock(spec=IChecker)
        mock_logger = MagicMock(spec=ILogger)
        mock_reporter = MagicMock(spec=IReporter)

        with self.assertRaises(ATSTypeError):
            ContextBundle(checker="not a checker", logger=mock_logger, reporter=mock_reporter, verbose=True)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ContextBundle(checker=mock_checker, logger=123, reporter=mock_reporter, verbose=True)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ContextBundle(checker=mock_checker, logger=mock_logger, reporter=[], verbose=True)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ContextBundle(checker=mock_checker, logger=mock_logger, reporter=mock_reporter, verbose="not a bool")  # type: ignore

    def test_to_dict(self) -> None:
        '''
            Tests converting ContextBundle to a dictionary.

            :exceptions: None.
        '''
        mock_checker = MagicMock(spec=IChecker)
        mock_logger = MagicMock(spec=ILogger)
        mock_reporter = MagicMock(spec=IReporter)

        bundle = ContextBundle(
            checker=mock_checker,
            logger=mock_logger,
            reporter=mock_reporter,
            verbose=False
        )

        expected = {
            "checker": mock_checker,
            "logger": mock_logger,
            "reporter": mock_reporter,
            "verbose": False
        }
        self.assertEqual(bundle.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
