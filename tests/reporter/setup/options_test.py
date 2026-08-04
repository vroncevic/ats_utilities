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
    Unit tests for ReporterBundleOptions TypedDict.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.setup.options import CheckerBundleOptions
from ats_utilities.logger.setup.options import LoggerBundleOptions
from ats_utilities.reporter.setup.options import ReporterBundleOptions


class OptionsTest(unittest.TestCase):
    '''
        Defines class OptionsTest with attribute(s) and method(s).
        Tests ReporterBundleOptions structure.
    '''

    def test_options_structure(self) -> None:
        checker_opts: CheckerBundleOptions = {}
        logger_opts: LoggerBundleOptions = {
            "log_level": 20
        }
        theme_opts = {
            "success": "green"
        }

        opts: ReporterBundleOptions = {
            "checker": checker_opts,
            "theme": theme_opts,
            "logger": logger_opts
        }
        self.assertEqual(opts["checker"], checker_opts)
        self.assertEqual(opts["theme"], theme_opts)
        self.assertEqual(opts["logger"], logger_opts)


if __name__ == "__main__":
    unittest.main()
