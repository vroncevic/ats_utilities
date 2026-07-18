# -*- coding: UTF-8 -*-

'''
Module
    checker_reporter_registry_test.py
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
    Unit tests for CheckerReporterRegistry class.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.reporter.checker_reporter_bundle import CheckerReporterBundle
from ats_utilities.checker.reporter.checker_reporter_registry import CheckerReporterRegistry

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class CheckerReporterRegistryTest(unittest.TestCase):
    '''
        Defines class CheckerReporterRegistryTest with attribute(s) and method(s).
        Tests CheckerReporterRegistry static factory logic.

        It defines:

            :attributes: None.
            :methods:
                | test_create_checker_reporter_bundle - Tests CheckerReporterBundle creation.
    '''

    def test_create_checker_reporter_bundle(self) -> None:
        bundle = CheckerReporterRegistry.create_checker_reporter_bundle(
            context="my_context",
            parameters_meta=[("p", "t", "v")],
            err_indices=[0],
            is_fmt_err=False
        )
        self.assertIsInstance(bundle, CheckerReporterBundle)
        self.assertEqual(bundle.context, "my_context")
        self.assertEqual(bundle.parameters_meta, [("p", "t", "v")])
        self.assertEqual(bundle.err_indices, [0])
        self.assertFalse(bundle.is_fmt_err)


if __name__ == "__main__":
    unittest.main()
