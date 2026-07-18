# -*- coding: UTF-8 -*-

'''
Module
    reporter_bundle_test.py
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
    Unit tests for ReporterBundle class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.reporter_bundle import ReporterBundle
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ReporterBundleTest(unittest.TestCase):
    '''
        Defines class ReporterBundleTest with attribute(s) and method(s).
        Tests ReporterBundle dataclass logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_valid - Tests successful ReporterBundle initialization.
                | test_init_invalid_none - Tests ReporterBundle initialization with None values.
                | test_init_invalid_type - Tests ReporterBundle initialization with wrong types.
                | test_to_dict - Tests ReporterBundle to_dict method.
    '''

    def test_init_valid(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        bundle = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=mock_logger
        )
        self.assertIs(bundle.checker, mock_checker)
        self.assertIs(bundle.theme, mock_theme)
        self.assertIs(bundle.logger, mock_logger)

    def test_init_invalid_none(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        with self.assertRaises(ATSValueError):
            ReporterBundle(
                checker=None,  # type: ignore
                theme=mock_theme,
                logger=mock_logger
            )

        with self.assertRaises(ATSValueError):
            ReporterBundle(
                checker=mock_checker,
                theme=None,  # type: ignore
                logger=mock_logger
            )

        with self.assertRaises(ATSValueError):
            ReporterBundle(
                checker=mock_checker,
                theme=mock_theme,
                logger=None  # type: ignore
            )

    def test_init_invalid_type(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        with self.assertRaises(ATSTypeError):
            ReporterBundle(
                checker=object(),  # type: ignore
                theme=mock_theme,
                logger=mock_logger
            )

        with self.assertRaises(ATSTypeError):
            ReporterBundle(
                checker=mock_checker,
                theme=object(),  # type: ignore
                logger=mock_logger
            )

        with self.assertRaises(ATSTypeError):
            ReporterBundle(
                checker=mock_checker,
                theme=mock_theme,
                logger=object()  # type: ignore
            )

    def test_to_dict(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        bundle = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=mock_logger
        )
        expected = {
            "checker": mock_checker,
            "theme": mock_theme,
            "logger": mock_logger
        }
        self.assertEqual(bundle.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
