# -*- coding: UTF-8 -*-

'''
Module
    context_registry_test.py
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
    Unit tests for ContextBundleRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.registry import ContextBundleRegistry
from ats_utilities.context.dependencies import ContextBundleDependencies

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ContextRegistryTest(unittest.TestCase):
    '''
        Defines class ContextRegistryTest with attribute(s) and method(s).
        Tests ContextBundleRegistry logic.
    '''

    def test_create_bundle(self) -> None:
        mock_checker = MagicMock(spec=IChecker)
        mock_logger = MagicMock(spec=ILogger)
        mock_reporter = MagicMock(spec=IReporter)

        bundle = ContextBundleRegistry.create_bundle(
            ContextBundleDependencies(
                checker=mock_checker,
                logger=mock_logger,
                reporter=mock_reporter,
                verbose=True
            )
        )
        self.assertIsInstance(bundle, ContextBundle)
        self.assertTrue(bundle.verbose)
        self.assertIs(bundle.checker, mock_checker)
        self.assertIs(bundle.logger, mock_logger)
        self.assertIs(bundle.reporter, mock_reporter)


if __name__ == "__main__":
    unittest.main()
