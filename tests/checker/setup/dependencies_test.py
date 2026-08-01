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
    Unit tests for CheckerDependencies class.
'''

from __future__ import annotations

import unittest
from typing import get_type_hints
from unittest.mock import MagicMock

from ats_utilities.checker.setup.dependencies import CheckerDependencies
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.checker.type.itype_validator import ITypeValidator


class CheckerDependenciesTest(unittest.TestCase):
    '''
        Defines class CheckerDependenciesTest with attribute(s) and method(s).
        Tests CheckerDependencies TypeDict structure.
    '''

    def test_type_hints(self) -> None:
        hints = get_type_hints(CheckerDependencies)
        self.assertEqual(hints['format_validator'], IFormatValidator)
        self.assertEqual(hints['type_validator'], ITypeValidator)
        self.assertEqual(hints['context_provider'], IContextProvider)
        self.assertEqual(hints['check_reporter'], ICheckReporter)

    def test_instantiation(self) -> None:
        deps: CheckerDependencies = {
            'format_validator': MagicMock(spec=IFormatValidator),
            'type_validator': MagicMock(spec=ITypeValidator),
            'context_provider': MagicMock(spec=IContextProvider),
            'check_reporter': MagicMock(spec=ICheckReporter)
        }
        self.assertEqual(len(deps), 4)


if __name__ == "__main__":
    unittest.main()
