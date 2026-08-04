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
    Unit tests for GeneratorBundleFactory class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.generation.setup.bundle import GeneratorBundle
from ats_utilities.generation.setup.factory import GeneratorBundleFactory
from ats_utilities.generation.setup.options import GeneratorBundleOptions
from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generation.tar.itar_processor import ITarProcessor
from ats_utilities.generation.template.itemplate_processor import ITemplateProcessor


class GeneratorFactoryTest(unittest.TestCase):
    '''
        Defines class GeneratorFactoryTest with attribute(s) and method(s).
        Tests GeneratorBundleFactory logic.
    '''

    @patch("ats_utilities.generation.setup.factory.SchemeLoader")
    @patch("ats_utilities.generation.setup.factory.TemplateProcessor")
    @patch("ats_utilities.generation.setup.factory.TarProcessor")
    def test_create_bundle(self, mock_tar: MagicMock, mock_tpl: MagicMock, mock_scheme: MagicMock) -> None:
        mock_scheme.return_value = MagicMock(spec=ISchemeLoader)
        mock_tpl.return_value = MagicMock(spec=ITemplateProcessor)
        mock_tar.return_value = MagicMock(spec=ITarProcessor)

        mock_context = MagicMock(spec=ContextBundle)
        mock_context.checker = MagicMock(spec=IChecker)
        mock_context.logger = MagicMock(spec=ILogger)
        mock_context.reporter = MagicMock(spec=IReporter)
        mock_context.verbose = True

        options = GeneratorBundleOptions(context_bundle=mock_context)
        bundle = GeneratorBundleFactory.create_bundle(options)

        self.assertIsInstance(bundle, GeneratorBundle)
        self.assertIs(bundle.context_bundle, mock_context)


if __name__ == "__main__":
    unittest.main()
