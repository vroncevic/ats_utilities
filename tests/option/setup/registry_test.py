# -*- coding: UTF-8 -*-

'''
Module
    registry_test.py
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
    Unit tests for OptionBundleRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.setup.registry import OptionBundleRegistry
from ats_utilities.option.setup.dependencies import OptionBundleDependencies
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter


class OptionRegistryTest(unittest.TestCase):
    '''
        Defines class OptionRegistryTest with attribute(s) and method(s).
        Tests OptionBundleRegistry logic.
    '''

    def test_create_bundle(self) -> None:
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_context = MagicMock(spec=ContextBundle)
        mock_context.checker = MagicMock(spec=IChecker)
        mock_context.logger = MagicMock(spec=ILogger)
        mock_context.reporter = MagicMock(spec=IReporter)
        mock_context.verbose = True

        deps = OptionBundleDependencies(
            strategy=mock_strategy,
            context_bundle=mock_context
        )

        bundle = OptionBundleRegistry.create_bundle(deps)
        self.assertIsInstance(bundle, OptionBundle)
        self.assertIs(bundle.strategy, mock_strategy)
        self.assertIs(bundle.context_bundle, mock_context)


if __name__ == "__main__":
    unittest.main()
