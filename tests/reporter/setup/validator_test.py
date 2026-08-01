# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
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
    Unit tests for ReporterValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.setup.bundle import ReporterBundle
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.setup.validator import ReporterValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ValidatorTest(unittest.TestCase):
    '''
        Defines class ValidatorTest with attribute(s) and method(s).
        Tests ReporterValidator logic.
    '''

    def test_validation_valid(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        bundle = ReporterBundle(
            checker=mock_checker,
            theme=mock_theme,
            logger=mock_logger
        )
        ReporterValidator.validate(bundle)

    def test_validation_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            ReporterValidator.validate(None)  # type: ignore

        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        with self.assertRaises(ATSValueError):
            bundle = ReporterBundle(
                checker=None,  # type: ignore
                theme=mock_theme,
                logger=mock_logger
            )
            ReporterValidator.validate(bundle)

        with self.assertRaises(ATSValueError):
            bundle = ReporterBundle(
                checker=mock_checker,
                theme=None,  # type: ignore
                logger=mock_logger
            )
            ReporterValidator.validate(bundle)

        with self.assertRaises(ATSValueError):
            bundle = ReporterBundle(
                checker=mock_checker,
                theme=mock_theme,
                logger=None  # type: ignore
            )
            ReporterValidator.validate(bundle)

    def test_validation_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            ReporterValidator.validate("invalid")  # type: ignore

        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        mock_logger = MagicMock(spec=ILogger)

        with self.assertRaises(ATSTypeError):
            bundle = ReporterBundle(
                checker="not_a_checker",  # type: ignore
                theme=mock_theme,
                logger=mock_logger
            )
            ReporterValidator.validate(bundle)

        with self.assertRaises(ATSTypeError):
            bundle = ReporterBundle(
                checker=mock_checker,
                theme="not_a_theme",  # type: ignore
                logger=mock_logger
            )
            ReporterValidator.validate(bundle)

        with self.assertRaises(ATSTypeError):
            bundle = ReporterBundle(
                checker=mock_checker,
                theme=mock_theme,
                logger="not_a_logger"  # type: ignore
            )
            ReporterValidator.validate(bundle)


if __name__ == "__main__":
    unittest.main()
