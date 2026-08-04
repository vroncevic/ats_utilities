# -*- coding: UTF-8 -*-

'''
Module
    dep_validator_test.py
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
    Unit tests for CheckerBundleDependenciesValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.setup.dependencies import CheckerBundleDependencies
from ats_utilities.checker.setup.dep_validator import CheckerBundleDependenciesValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class CheckerDependenciesValidatorTest(unittest.TestCase):
    '''
        Defines class CheckerDependenciesValidatorTest with attribute(s) and method(s).
        Tests CheckerBundleDependenciesValidator component logic.
    '''

    def _get_valid_deps(self) -> CheckerBundleDependencies:
        return CheckerBundleDependencies(
            format_validator=MagicMock(spec=IFormatValidator),
            type_validator=MagicMock(spec=ITypeValidator),
            context_provider=MagicMock(spec=IContextProvider),
            check_reporter=MagicMock(spec=ICheckReporter)
        )

    def test_validate_valid(self) -> None:
        deps = self._get_valid_deps()
        CheckerBundleDependenciesValidator.validate(deps)

    def test_validate_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            CheckerBundleDependenciesValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            CheckerBundleDependenciesValidator.validate("not_a_dict")  # type: ignore

    def test_validate_missing_attributes(self) -> None:
        deps = self._get_valid_deps()
        del deps['format_validator']  # type: ignore
        with self.assertRaises(ATSValueError):
            CheckerBundleDependenciesValidator.validate(deps)

        deps = self._get_valid_deps()
        del deps['type_validator']  # type: ignore
        with self.assertRaises(ATSValueError):
            CheckerBundleDependenciesValidator.validate(deps)

    def test_validate_invalid_attribute_types(self) -> None:
        deps = self._get_valid_deps()
        deps['format_validator'] = "invalid"  # type: ignore
        with self.assertRaises(ATSTypeError):
            CheckerBundleDependenciesValidator.validate(deps)


if __name__ == "__main__":
    unittest.main()
