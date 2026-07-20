# -*- coding: UTF-8 -*-

'''
Module
    logger_registry_test.py
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
    Unit tests for LoggerRegistry class.
'''

from __future__ import annotations

import logging
import unittest
from unittest.mock import patch, MagicMock

from ats_utilities.logger.logger_bundle import LoggerBundle
from ats_utilities.logger.logger_registry import LoggerRegistry
from ats_utilities.logger.logger_params import LoggerParams

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class LoggerRegistryTest(unittest.TestCase):
    '''
        Defines class LoggerRegistryTest with attribute(s) and method(s).
        Tests LoggerRegistry static factory logic.

        It defines:

            :attributes: None.
            :methods:
                | test_create_default_logger_bundle - Tests default LoggerBundle creation.
    '''

    def test_create_default_logger_bundle(self) -> None:
        bundle = LoggerRegistry.create_default_logger_bundle(
            log_file="test_registry.log",
            log_level=logging.WARNING
        )
        self.assertIsInstance(bundle, LoggerBundle)
        self.assertEqual(bundle.log_file, "test_registry.log")
        self.assertEqual(bundle.log_level, logging.WARNING)
        self.assertIsInstance(bundle.logger, logging.Logger)

    def test_create_default_logger_bundle_without_parameters(self) -> None:
        bundle = LoggerRegistry.create_default_logger_bundle()
        self.assertIsInstance(bundle, LoggerBundle)
        self.assertEqual(bundle.log_file, "")
        self.assertEqual(bundle.log_level, logging.INFO)

    def test_create_bundle(self) -> None:
        bundle = LoggerRegistry.create_bundle(
            LoggerParams(
                log_file="test_registry.log",
                log_level=logging.WARNING
            )
        )
        self.assertIsInstance(bundle, LoggerBundle)
        self.assertEqual(bundle.log_file, "test_registry.log")
        self.assertEqual(bundle.log_level, logging.WARNING)
        self.assertIsInstance(bundle.logger, logging.Logger)

    @patch("ats_utilities.logger.logger_registry.getLogger")
    def test_create_default_logger_bundle_configures_stream(self, mock_get_logger) -> None:
        mock_logger = MagicMock()
        mock_logger.hasHandlers.return_value = False
        mock_get_logger.return_value = mock_logger

        with patch("ats_utilities.logger.logger_registry.basicConfig") as mock_basic_config:
            bundle = LoggerRegistry.create_default_logger_bundle(log_file=None)
            mock_basic_config.assert_called_once()
            args, kwargs = mock_basic_config.call_args
            self.assertIn('stream', kwargs)
            self.assertNotIn('filename', kwargs)

    @patch("ats_utilities.logger.logger_registry.getLogger")
    def test_create_default_logger_bundle_configures_filename(self, mock_get_logger) -> None:
        mock_logger = MagicMock()
        mock_logger.hasHandlers.return_value = False
        mock_get_logger.return_value = mock_logger

        with patch("ats_utilities.logger.logger_registry.basicConfig") as mock_basic_config:
            bundle = LoggerRegistry.create_default_logger_bundle(log_file="test_file.log")
            mock_basic_config.assert_called_once()
            args, kwargs = mock_basic_config.call_args
            self.assertIn('filename', kwargs)
            self.assertNotIn('stream', kwargs)


if __name__ == "__main__":
    unittest.main()
