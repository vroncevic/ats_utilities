# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Unit tests for Reporter class.
'''

from __future__ import annotations

import logging
import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.setup.types import CheckerErrorType
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.engine import Reporter
from ats_utilities.reporter.setup.bundle import ReporterBundle
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests Reporter logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init - Tests Reporter initialization.
                | test_init_invalid - Tests Reporter initialization with invalid inputs.
                | test_report_methods - Tests verbose, success, warning, and error methods.
                | test_set_level - Tests set_level with different logger interfaces.
                | test_is_initialized - Tests is_initialized method.
                | test_str - Tests __str__ method.
    '''

    def test_init(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        bundle = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=mock_logger
        )
        reporter = Reporter(bundle)
        self.assertTrue(reporter.is_initialized())
        self.assertIs(reporter._checker, mock_checker)
        self.assertIs(reporter._theme, mock_theme)
        self.assertIs(reporter._logger, mock_logger)

    def test_init_invalid(self) -> None:
        with self.assertRaises(ATSValueError):
            Reporter(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            Reporter("invalid")  # type: ignore

    def test_report_methods(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_format_validator = MagicMock()
        mock_format_validator.get_separator.return_value = ":"
        mock_format_validator.split.side_effect = lambda s: s.split(":")
        mock_checker.get_format_validator.return_value = mock_format_validator
        mock_checker.ERRORS = CheckerErrorType
        mock_checker.validates_parameters.return_value = (None, CheckerErrorType.NO_ERROR)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        mock_theme.get_color.side_effect = lambda key: f"[{key}]"

        bundle = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=mock_logger
        )
        reporter = Reporter(bundle)

        # Test verbose enabled
        reporter.verbose(True, ["verbose", "msg"])
        mock_logger.write_log.assert_called_with(logging.DEBUG, "[verbose]verbose msg[reset]")

        # Test verbose disabled
        mock_logger.write_log.reset_mock()
        reporter.verbose(False, ["verbose", "msg"])
        mock_logger.write_log.assert_not_called()

        # Test success
        reporter.success(["success", "msg"])
        mock_logger.write_log.assert_called_with(logging.INFO, "[success]success msg[reset]")

        # Test warning
        reporter.warning(["warning", "msg"])
        mock_logger.write_log.assert_called_with(logging.WARNING, "[warning]warning msg[reset]")

        # Test error
        reporter.error(["error", "msg"])
        mock_logger.write_log.assert_called_with(logging.ERROR, "[error]error msg[reset]")

        # Test empty message (should not log)
        mock_logger.write_log.reset_mock()
        reporter._report([], "[red]", logging.DEBUG)
        mock_logger.write_log.assert_not_called()

    def test_set_level(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_format_validator = MagicMock()
        mock_format_validator.get_separator.return_value = ":"
        mock_format_validator.split.side_effect = lambda s: s.split(":")
        mock_checker.get_format_validator.return_value = mock_format_validator
        mock_checker.ERRORS = CheckerErrorType
        mock_checker.validates_parameters.return_value = (None, CheckerErrorType.NO_ERROR)
        mock_theme = MagicMock(spec=IConsoleTheme)

        # Case 1: logger has set_level method
        mock_logger_1 = MagicMock(spec=ILogger)
        mock_logger_1.set_level = MagicMock()
        if hasattr(mock_logger_1, "setLevel"):
            del mock_logger_1.setLevel

        bundle_1 = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=mock_logger_1
        )
        reporter_1 = Reporter(bundle_1)
        reporter_1.set_level(logging.DEBUG)
        mock_logger_1.set_level.assert_called_once_with(logging.DEBUG)

        # Case 2: logger has setLevel method
        mock_logger_2 = MagicMock(spec=ILogger)
        mock_logger_2.setLevel = MagicMock()
        if hasattr(mock_logger_2, "set_level"):
            del mock_logger_2.set_level

        bundle_2 = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=mock_logger_2
        )
        reporter_2 = Reporter(bundle_2)
        reporter_2.set_level(logging.INFO)
        mock_logger_2.setLevel.assert_called_once_with(logging.INFO)

        # Case 3: logger has neither set_level nor setLevel
        mock_logger_3 = MagicMock(spec=ILogger)
        if hasattr(mock_logger_3, "set_level"):
            del mock_logger_3.set_level
        if hasattr(mock_logger_3, "setLevel"):
            del mock_logger_3.setLevel

        bundle_3 = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=mock_logger_3
        )
        reporter_3 = Reporter(bundle_3)
        reporter_3.set_level(logging.DEBUG)

    def test_is_initialized(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)
        bundle = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=mock_logger
        )
        reporter = Reporter(bundle)
        self.assertTrue(reporter.is_initialized())

    def test_str(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)
        bundle = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=mock_logger
        )
        reporter = Reporter(bundle)
        self.assertIn("Reporter", str(reporter))

    def test_get_bundle(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)
        bundle = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=mock_logger
        )
        reporter = Reporter(bundle)
        self.assertEqual(reporter.get_bundle().checker, mock_checker)
        self.assertEqual(reporter.get_bundle().theme, mock_theme)
        self.assertEqual(reporter.get_bundle().logger, mock_logger)

    def test_update_bundle(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)
        bundle = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=mock_logger
        )
        reporter = Reporter(bundle)
        
        # Valid update
        new_logger = MagicMock(spec=ILogger)
        new_bundle = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=new_logger
        )
        self.assertTrue(reporter.update_bundle(new_bundle))
        self.assertEqual(reporter.get_bundle().logger, new_logger)

        # Invalid update
        self.assertFalse(reporter.update_bundle("invalid" * 10))  # type: ignore


if __name__ == "__main__":
    unittest.main()
