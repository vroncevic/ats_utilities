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
    Unit tests for LoggerValidator class.
'''

from __future__ import annotations

import logging
import unittest
from unittest.mock import MagicMock

from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.setup.validator import LoggerValidator
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
        Tests LoggerValidator logic.
    '''

    def test_validation_valid(self) -> None:
        mock_logger = MagicMock()
        mock_logger.info = MagicMock()

        bundle = LoggerBundle(
            logger=mock_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        # Should not raise any exceptions
        LoggerValidator.validate(bundle)

    def test_validation_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            LoggerValidator.validate(None)  # type: ignore

        mock_logger = MagicMock()
        mock_logger.info = MagicMock()

        with self.assertRaises(ATSValueError):
            bundle = LoggerBundle(
                logger=None,  # type: ignore
                log_file="test.log",
                log_level=logging.INFO
            )
            LoggerValidator.validate(bundle)

        with self.assertRaises(ATSValueError):
            bundle = LoggerBundle(
                logger=mock_logger,
                log_file=None,  # type: ignore
                log_level=logging.INFO
            )
            LoggerValidator.validate(bundle)

        with self.assertRaises(ATSValueError):
            bundle = LoggerBundle(
                logger=mock_logger,
                log_file="test.log",
                log_level=None  # type: ignore
            )
            LoggerValidator.validate(bundle)

    def test_validation_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            LoggerValidator.validate("invalid")  # type: ignore

        mock_logger = MagicMock()
        mock_logger.info = MagicMock()

        with self.assertRaises(ATSTypeError):
            bundle = LoggerBundle(
                logger=mock_logger,
                log_file=123,  # type: ignore
                log_level=logging.INFO
            )
            LoggerValidator.validate(bundle)

        with self.assertRaises(ATSTypeError):
            bundle = LoggerBundle(
                logger=mock_logger,
                log_file="test.log",
                log_level="invalid"  # type: ignore
            )
            LoggerValidator.validate(bundle)

    def test_validation_logger_spec(self) -> None:
        with self.assertRaises(ATSValueError):
            bundle = LoggerBundle(
                logger=object(),  # Has neither info nor write_log
                log_file="test.log",
                log_level=logging.INFO
            )
            LoggerValidator.validate(bundle)


if __name__ == "__main__":
    unittest.main()
