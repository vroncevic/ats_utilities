# -*- coding: UTF-8 -*-

'''
Module
    dependencies_test.py
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
    Unit tests for ContextDependencies TypedDict.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.dependencies import ContextDependencies
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter


class TestContextDependencies(unittest.TestCase):
    """Unit tests for the ContextDependencies TypedDict structure."""

    def test_context_dependencies_dict(self) -> None:
        """Test creating and accessing ContextDependencies structure."""
        mock_checker = MagicMock(spec=IChecker)
        mock_logger = MagicMock(spec=ILogger)
        mock_reporter = MagicMock(spec=IReporter)

        deps: ContextDependencies = {
            "checker": mock_checker,
            "logger": mock_logger,
            "reporter": mock_reporter,
            "verbose": True
        }

        self.assertEqual(deps["checker"], mock_checker)
        self.assertEqual(deps["logger"], mock_logger)
        self.assertEqual(deps["reporter"], mock_reporter)
        self.assertTrue(deps["verbose"])


if __name__ == '__main__':
    unittest.main()
