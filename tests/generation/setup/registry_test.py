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
    Unit tests for GeneratorBundleRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.generation.setup.registry import GeneratorBundleRegistry
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.generation.setup.bundle import GeneratorBundle
from ats_utilities.generation.setup.dependencies import GeneratorBundleDependencies
from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generation.tar.itar_processor import ITarProcessor


class TestGeneratorRegistry(unittest.TestCase):
    """Unit tests for the GeneratorBundleRegistry class."""

    def setUp(self) -> None:
        """Set up standard context bundle dependency mock."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.mock_context_bundle.checker = MagicMock(spec=IChecker)
        self.mock_context_bundle.logger = MagicMock(spec=ILogger)
        self.mock_context_bundle.reporter = MagicMock(spec=IReporter)
        self.mock_context_bundle.verbose = True

    def test_create_bundle(self) -> None:
        """Test create_bundle on GeneratorBundleRegistry."""
        scheme_load = MagicMock(spec=ISchemeLoader)
        tar_proc = MagicMock(spec=ITarProcessor)

        result = GeneratorBundleRegistry.create_bundle(
            GeneratorBundleDependencies(
                context_bundle=self.mock_context_bundle,
                scheme_loader=scheme_load,
                tar_processor=tar_proc
            )
        )
        self.assertIsInstance(result, GeneratorBundle)
        self.assertEqual(result.context_bundle, self.mock_context_bundle)
        self.assertEqual(result.scheme_loader, scheme_load)
        self.assertEqual(result.tar_processor, tar_proc)


if __name__ == '__main__':
    unittest.main()
