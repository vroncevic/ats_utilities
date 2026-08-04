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
    Unit tests for OptionBundleFactory class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.setup.factory import OptionBundleFactory
from ats_utilities.option.setup.options import OptionBundleOptions
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter


class OptionFactoryTest(unittest.TestCase):
    '''
        Defines class OptionFactoryTest with attribute(s) and method(s).
        Tests OptionBundleFactory static factory logic.
    '''

    def test_create_bundle(self) -> None:
        parameters = {
            "ats_name": "mytool",
            "ats_version": "1.0.0",
            "ats_licence": "GPLv3",
            "ats_build_date": "2026-08-01"
        }
        mock_context = MagicMock(spec=ContextBundle)
        mock_context.checker = MagicMock(spec=IChecker)
        mock_context.logger = MagicMock(spec=ILogger)
        mock_context.reporter = MagicMock(spec=IReporter)
        mock_context.verbose = True

        opts: OptionBundleOptions = {
            "parameters": parameters,
            "context_bundle": mock_context
        }

        bundle = OptionBundleFactory.create_bundle(opts)
        self.assertIsInstance(bundle, OptionBundle)
        self.assertIs(bundle.context_bundle, mock_context)
        self.assertIsNotNone(bundle.strategy)


if __name__ == "__main__":
    unittest.main()
