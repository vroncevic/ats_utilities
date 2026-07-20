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
        Tests LoggerRegistry logic.
    '''

    def test_create_bundle(self) -> None:
        mock_logger = logging.getLogger("test_logger")
        bundle = LoggerRegistry.create_bundle(
            LoggerParams(
                log_file="test_registry.log",
                log_level=logging.WARNING,
                logger=mock_logger
            )
        )
        self.assertIsInstance(bundle, LoggerBundle)
        self.assertEqual(bundle.log_file, "test_registry.log")
        self.assertEqual(bundle.log_level, logging.WARNING)
        self.assertIs(bundle.logger, mock_logger)


if __name__ == "__main__":
    unittest.main()
