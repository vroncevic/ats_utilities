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
    Unit tests for ContextBundle class and ContextBundleValidator.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextBundleValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ContextBundleTest(unittest.TestCase):
    '''
        Defines class ContextBundleTest with attribute(s) and method(s).
        Tests ContextBundle dataclass and ContextBundleValidator logic.
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
            ContextBundleValidator.validate(bundle)
        except (ATSValueError, ATSTypeError):
            self.fail("Failed to instantiate ContextBundle with valid arguments.")

    def test_init_invalid_none(self) -> None:
        '''
            Tests validation of ContextBundle with missing attributes.

            :exceptions: None.
        '''
        mock_checker = MagicMock(spec=IChecker)
        mock_logger = MagicMock(spec=ILogger)
        mock_reporter = MagicMock(spec=IReporter)

        with self.assertRaises(ATSValueError):
            bundle = ContextBundle(checker=None, logger=mock_logger, reporter=mock_reporter, verbose=True)  # type: ignore
            ContextBundleValidator.validate(bundle)

        with self.assertRaises(ATSValueError):
            bundle = ContextBundle(checker=mock_checker, logger=None, reporter=mock_reporter, verbose=True)  # type: ignore
            ContextBundleValidator.validate(bundle)

        with self.assertRaises(ATSValueError):
            bundle = ContextBundle(checker=mock_checker, logger=mock_logger, reporter=None, verbose=True)  # type: ignore
            ContextBundleValidator.validate(bundle)

        with self.assertRaises(ATSValueError):
            bundle = ContextBundle(checker=mock_checker, logger=mock_logger, reporter=mock_reporter, verbose=None)  # type: ignore
            ContextBundleValidator.validate(bundle)

    def test_init_invalid_type(self) -> None:
        '''
            Tests validation of ContextBundle with wrong attribute types.

            :exceptions: None.
        '''
        mock_checker = MagicMock(spec=IChecker)
        mock_logger = MagicMock(spec=ILogger)
        mock_reporter = MagicMock(spec=IReporter)

        with self.assertRaises(ATSTypeError):
            bundle = ContextBundle(checker="not a checker", logger=mock_logger, reporter=mock_reporter, verbose=True)  # type: ignore
            ContextBundleValidator.validate(bundle)

        with self.assertRaises(ATSTypeError):
            bundle = ContextBundle(checker=mock_checker, logger=123, reporter=mock_reporter, verbose=True)  # type: ignore
            ContextBundleValidator.validate(bundle)

        with self.assertRaises(ATSTypeError):
            bundle = ContextBundle(checker=mock_checker, logger=mock_logger, reporter=[], verbose=True)  # type: ignore
            ContextBundleValidator.validate(bundle)

        with self.assertRaises(ATSTypeError):
            bundle = ContextBundle(checker=mock_checker, logger=mock_logger, reporter=mock_reporter, verbose="not a bool")  # type: ignore
            ContextBundleValidator.validate(bundle)

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
