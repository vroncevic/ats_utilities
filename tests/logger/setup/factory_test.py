# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
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
    Unit tests for LoggerFactory class.
'''

from __future__ import annotations

import logging
import unittest
from unittest.mock import patch, MagicMock

from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.setup.factory import LoggerFactory

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class FactoryTest(unittest.TestCase):
    '''
        Defines class FactoryTest with attribute(s) and method(s).
        Tests LoggerFactory static factory logic.
    '''

    def test_create_default_bundle(self) -> None:
        bundle = LoggerFactory.create_default_bundle({
            "log_file": "test_factory.log",
            "log_level": logging.WARNING
        })
        self.assertIsInstance(bundle, LoggerBundle)
        self.assertEqual(bundle.log_file, "test_factory.log")
        self.assertEqual(bundle.log_level, logging.WARNING)
        self.assertIsInstance(bundle.logger, logging.Logger)

    def test_create_default_bundle_without_parameters(self) -> None:
        bundle = LoggerFactory.create_default_bundle()
        self.assertIsInstance(bundle, LoggerBundle)
        self.assertEqual(bundle.log_file, "")
        self.assertEqual(bundle.log_level, logging.INFO)

    @patch("ats_utilities.logger.setup.factory.getLogger")
    def test_create_default_bundle_configures_stream(self, mock_get_logger) -> None:
        mock_logger = MagicMock()
        mock_logger.hasHandlers.return_value = False
        mock_get_logger.return_value = mock_logger

        with patch("ats_utilities.logger.setup.factory.basicConfig") as mock_basic_config:
            bundle = LoggerFactory.create_default_bundle({"log_file": None})
            mock_basic_config.assert_called_once()
            args, kwargs = mock_basic_config.call_args
            self.assertIn('stream', kwargs)
            self.assertNotIn('filename', kwargs)

    @patch("ats_utilities.logger.setup.factory.getLogger")
    def test_create_default_bundle_configures_filename(self, mock_get_logger) -> None:
        mock_logger = MagicMock()
        mock_logger.hasHandlers.return_value = False
        mock_get_logger.return_value = mock_logger

        with patch("ats_utilities.logger.setup.factory.basicConfig") as mock_basic_config:
            bundle = LoggerFactory.create_default_bundle({"log_file": "test_file.log"})
            mock_basic_config.assert_called_once()
            args, kwargs = mock_basic_config.call_args
            self.assertIn('filename', kwargs)
            self.assertNotIn('stream', kwargs)


if __name__ == "__main__":
    unittest.main()
