# -*- coding: UTF-8 -*-

'''
Module
    logger_bundle_test.py
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
    Unit tests for LoggerBundle class.
'''

from __future__ import annotations

import logging
import unittest
from unittest.mock import MagicMock

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.logger_bundle import LoggerBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class LoggerBundleTest(unittest.TestCase):
    '''
        Defines class LoggerBundleTest with attribute(s) and method(s).
        Tests LoggerBundle dataclass logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_valid - Tests successful LoggerBundle initialization.
                | test_init_invalid_none - Tests LoggerBundle initialization with None values.
                | test_init_invalid_type - Tests LoggerBundle initialization with wrong types.
                | test_to_dict - Tests LoggerBundle to_dict method.
    '''

    def test_init_valid(self) -> None:
        mock_logger = MagicMock()
        mock_logger.info = MagicMock()

        bundle = LoggerBundle(
            logger=mock_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        self.assertIs(bundle.logger, mock_logger)
        self.assertEqual(bundle.log_file, "test.log")
        self.assertEqual(bundle.log_level, logging.INFO)

    def test_init_invalid_none(self) -> None:
        mock_logger = MagicMock()
        mock_logger.info = MagicMock()

        with self.assertRaises(ATSValueError):
            LoggerBundle(
                logger=None,  # type: ignore
                log_file="test.log",
                log_level=logging.INFO
            )

        with self.assertRaises(ATSValueError):
            LoggerBundle(
                logger=mock_logger,
                log_file=None,  # type: ignore
                log_level=logging.INFO
            )

        with self.assertRaises(ATSValueError):
            LoggerBundle(
                logger=mock_logger,
                log_file="test.log",
                log_level=None  # type: ignore
            )

    def test_init_invalid_type(self) -> None:
        mock_logger = MagicMock()
        mock_logger.info = MagicMock()

        with self.assertRaises(ATSValueError):
            LoggerBundle(
                logger=object(),  # Has neither info nor write_log
                log_file="test.log",
                log_level=logging.INFO
            )

        with self.assertRaises(ATSTypeError):
            LoggerBundle(
                logger=mock_logger,
                log_file=123,  # type: ignore
                log_level=logging.INFO
            )

        with self.assertRaises(ATSTypeError):
            LoggerBundle(
                logger=mock_logger,
                log_file="test.log",
                log_level="invalid"  # type: ignore
            )

    def test_to_dict(self) -> None:
        mock_logger = MagicMock()
        mock_logger.info = MagicMock()

        bundle = LoggerBundle(
            logger=mock_logger,
            log_file="test.log",
            log_level=logging.INFO
        )
        expected = {
            "logger": mock_logger,
            "log_file": "test.log",
            "log_level": logging.INFO
        }
        self.assertEqual(bundle.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
