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
    Unit tests for CheckerFactory class.
'''

from __future__ import annotations

import unittest
from collections.abc import Set

from ats_utilities.checker.setup.bundle import CheckerBundle
from ats_utilities.checker.setup.factory import CheckerFactory
from ats_utilities.checker.setup.options import CheckerOptions
from ats_utilities.checker.context.engine import ContextProvider
from ats_utilities.checker.format.engine import FormatValidator
from ats_utilities.checker.reporter.engine import CheckReporter
from ats_utilities.checker.type.engine import TypeValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class FactoryTest(unittest.TestCase):
    '''
        Defines class FactoryTest with attribute(s) and method(s).
        Tests CheckerFactory static factory logic.
    '''

    def test_create_default_bundle(self) -> None:
        bundle = CheckerFactory.create_bundle()
        self.assertIsInstance(bundle, CheckerBundle)
        self.assertIsInstance(bundle.format_validator, FormatValidator)
        self.assertIsInstance(bundle.type_validator, TypeValidator)
        self.assertIsInstance(bundle.context_provider, ContextProvider)
        self.assertIsInstance(bundle.check_reporter, CheckReporter)

    def test_create_bundle_with_options(self) -> None:
        options = CheckerOptions(
            separator="-",
            abstract_types={"MySet": Set},
            stack_index_caller=4,
            messages_provider={"some": "msg"}
        )
        bundle = CheckerFactory.create_bundle(options)
        self.assertIsInstance(bundle, CheckerBundle)
        self.assertEqual(bundle.format_validator._separator, "-")
        self.assertIn("MySet", bundle.type_validator._abstract_types)
        self.assertEqual(bundle.context_provider._stack_index_caller, 4)
        self.assertEqual(bundle.check_reporter._message_provider, {"some": "msg"})

    def test_create_bundle_invalid_options(self) -> None:
        with self.assertRaises(ATSTypeError):
            CheckerFactory.create_bundle("invalid")  # type: ignore

        with self.assertRaises(ATSTypeError):
            CheckerFactory.create_bundle(CheckerOptions(separator=123))  # type: ignore


if __name__ == "__main__":
    unittest.main()
