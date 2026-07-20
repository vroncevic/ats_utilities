# -*- coding: UTF-8 -*-

'''
Module
    checker_registry_test.py
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
    Unit tests for CheckerRegistry class.
'''

from __future__ import annotations

import unittest

from ats_utilities.checker.checker_bundle import CheckerBundle
from ats_utilities.checker.checker_registry import CheckerRegistry
from ats_utilities.checker.context.context_provider import ContextProvider
from ats_utilities.checker.format.format_validator import FormatValidator
from ats_utilities.checker.reporter.check_reporter import CheckReporter
from ats_utilities.checker.type.type_validator import TypeValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class CheckerRegistryTest(unittest.TestCase):
    '''
        Defines class CheckerRegistryTest with attribute(s) and method(s).
        Tests CheckerRegistry static factory logic.

        It defines:

            :attributes: None.
            :methods:
                | test_create_default_checker_bundle - Tests default CheckerBundle creation.
    '''

    def test_create_default_checker_bundle(self) -> None:
        bundle = CheckerRegistry.create_default_checker_bundle()
        self.assertIsInstance(bundle, CheckerBundle)
        self.assertIsInstance(bundle.format_validator, FormatValidator)
        self.assertIsInstance(bundle.type_validator, TypeValidator)
        self.assertIsInstance(bundle.context_provider, ContextProvider)
        self.assertIsInstance(bundle.check_reporter, CheckReporter)

    def test_create_bundle(self) -> None:
        bundle = CheckerRegistry.create_bundle()
        self.assertIsInstance(bundle, CheckerBundle)
        self.assertIsInstance(bundle.format_validator, FormatValidator)
        self.assertIsInstance(bundle.type_validator, TypeValidator)
        self.assertIsInstance(bundle.context_provider, ContextProvider)
        self.assertIsInstance(bundle.check_reporter, CheckReporter)

    def test_create_bundle_with_args(self) -> None:
        format_validator = FormatValidator()
        type_validator = TypeValidator()
        context_provider = ContextProvider()
        check_reporter = CheckReporter()

        bundle = CheckerRegistry.create_bundle(
            format_validator=format_validator,
            type_validator=type_validator,
            context_provider=context_provider,
            check_reporter=check_reporter
        )
        self.assertIsInstance(bundle, CheckerBundle)
        self.assertIs(bundle.format_validator, format_validator)
        self.assertIs(bundle.type_validator, type_validator)
        self.assertIs(bundle.context_provider, context_provider)
        self.assertIs(bundle.check_reporter, check_reporter)


if __name__ == "__main__":
    unittest.main()
