# -*- coding: UTF-8 -*-

'''
Module
    options_test.py
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
    Unit tests for ContextOptions TypedDict.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.options import ContextOptions
from ats_utilities.checker.setup.options import CheckerOptions
from ats_utilities.logger.setup.options import LoggerOptions
from ats_utilities.reporter.setup.options import ReporterOptions


class TestContextOptions(unittest.TestCase):
    """Unit tests for the ContextOptions TypedDict structure."""

    def test_context_options_dict(self) -> None:
        """Test creating and accessing ContextOptions structure."""
        mock_checker = MagicMock(spec=CheckerOptions)
        mock_logger = MagicMock(spec=LoggerOptions)
        mock_reporter = MagicMock(spec=ReporterOptions)

        options: ContextOptions = {
            "checker": mock_checker,
            "logger": mock_logger,
            "reporter": mock_reporter,
            "verbose": True
        }

        self.assertEqual(options["checker"], mock_checker)
        self.assertEqual(options["logger"], mock_logger)
        self.assertEqual(options["reporter"], mock_reporter)
        self.assertTrue(options["verbose"])


if __name__ == '__main__':
    unittest.main()
