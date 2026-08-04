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
    Unit tests for CheckerBundleRegistry class.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.setup.bundle import CheckerBundle
from ats_utilities.checker.setup.registry import CheckerBundleRegistry
from ats_utilities.checker.setup.dependencies import CheckerBundleDependencies
from ats_utilities.checker.context.engine import ContextProvider
from ats_utilities.checker.format.engine import FormatValidator
from ats_utilities.checker.reporter.engine import CheckReporter
from ats_utilities.checker.type.engine import TypeValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class RegistryTest(unittest.TestCase):
    '''
        Defines class RegistryTest with attribute(s) and method(s).
        Tests CheckerBundleRegistry logic.
    '''

    def test_create_bundle_with_args(self) -> None:
        format_validator = FormatValidator()
        type_validator = TypeValidator()
        context_provider = ContextProvider()
        check_reporter = CheckReporter()

        bundle = CheckerBundleRegistry.create_bundle(
            dependencies=CheckerBundleDependencies(
                format_validator=format_validator,
                type_validator=type_validator,
                context_provider=context_provider,
                check_reporter=check_reporter
            )
        )
        self.assertIsInstance(bundle, CheckerBundle)
        self.assertIs(bundle.format_validator, format_validator)
        self.assertIs(bundle.type_validator, type_validator)
        self.assertIs(bundle.context_provider, context_provider)
        self.assertIs(bundle.check_reporter, check_reporter)

    def test_create_bundle_invalid(self) -> None:
        with self.assertRaises(ATSValueError):
            CheckerBundleRegistry.create_bundle(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            CheckerBundleRegistry.create_bundle("invalid")  # type: ignore


if __name__ == "__main__":
    unittest.main()
