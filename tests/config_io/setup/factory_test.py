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
    Unit tests for ConfigIOFactory class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.config_io.setup.bundle import ConfigIOBundle
from ats_utilities.config_io.setup.factory import ConfigIOFactory
from ats_utilities.config_io.setup.options import ConfigIOOptions


class ConfigIOFactoryTest(unittest.TestCase):
    '''
        Defines class ConfigIOFactoryTest with attribute(s) and method(s).
        Tests ConfigIOFactory logic.
    '''

    @patch("ats_utilities.config_io.setup.factory.ConfigProcessorFactory")
    def test_create_bundle(self, mock_factory: MagicMock) -> None:
        mock_processor = MagicMock(spec=IConfigProcessor)
        mock_factory.create_from_file_path.return_value = mock_processor

        mock_context = MagicMock(spec=ContextBundle)
        mock_context.checker = MagicMock(spec=IChecker)
        mock_context.logger = MagicMock(spec=ILogger)
        mock_context.reporter = MagicMock(spec=IReporter)
        mock_context.verbose = True

        options = ConfigIOOptions(
            file_path="/tmp/config.json",
            scheme={"key": "val"},
            context_bundle=mock_context
        )
        bundle = ConfigIOFactory.create_bundle(options)

        self.assertIsInstance(bundle, ConfigIOBundle)
        self.assertEqual(bundle.file_path, "/tmp/config.json")
        self.assertIs(bundle.processor, mock_processor)
        self.assertIs(bundle.context_bundle, mock_context)


if __name__ == "__main__":
    unittest.main()
