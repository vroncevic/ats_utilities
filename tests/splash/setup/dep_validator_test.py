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
    Unit tests for SplashDependenciesValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splash.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splash.progressbar.iprogress_bar import IProgressBar
from ats_utilities.splash.property.isplash_property import ISplashProperty
from ats_utilities.splash.setup.dep_validator import SplashDependenciesValidator
from ats_utilities.splash.setup.dependencies import SplashDependencies
from ats_utilities.splash.terminal.iterminal_properties import ITerminalProperties


@patch("ats_utilities.splash.setup.dep_validator.ContextValidator.validate")
class SplashDependenciesValidatorTest(unittest.TestCase):
    '''
        Defines class SplashDependenciesValidatorTest with attribute(s) and method(s).
        Tests SplashDependenciesValidator.
    '''

    def _get_valid_deps(self) -> SplashDependencies:
        return {
            "splash_property": MagicMock(spec=ISplashProperty),
            "terminal_property": MagicMock(spec=ITerminalProperties),
            "ext": MagicMock(spec=IExtInfrastructure),
            "pb": MagicMock(spec=IProgressBar),
            "context_bundle": MagicMock(spec=ContextBundle),
        }

    def test_validate_valid(self, mock_context_val: MagicMock) -> None:
        deps = self._get_valid_deps()
        SplashDependenciesValidator.validate(deps)
        mock_context_val.assert_called_once_with(deps["context_bundle"])

    def test_validate_invalid_none(self, mock_context_val: MagicMock) -> None:
        with self.assertRaises(ATSValueError):
            SplashDependenciesValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self, mock_context_val: MagicMock) -> None:
        with self.assertRaises(ATSTypeError):
            SplashDependenciesValidator.validate(object())  # type: ignore

    def test_validate_missing_keys(self, mock_context_val: MagicMock) -> None:
        for key in self._get_valid_deps().keys():
            with self.subTest(missing_key=key):
                deps = self._get_valid_deps()
                del deps[key]  # type: ignore
                with self.assertRaises(ATSValueError):
                    SplashDependenciesValidator.validate(deps)

    def test_validate_bad_types(self, mock_context_val: MagicMock) -> None:
        type_mismatches = {
            "splash_property": object(),
            "terminal_property": MagicMock(spec=IProgressBar),
            "ext": MagicMock(spec=ISplashProperty),
            "pb": MagicMock(spec=ITerminalProperties),
            "context_bundle": MagicMock(spec=IExtInfrastructure)
        }
        for key, bad_value in type_mismatches.items():
            with self.subTest(key=key, bad_value=bad_value):
                deps = self._get_valid_deps()
                deps[key] = bad_value  # type: ignore
                with self.assertRaises(ATSTypeError):
                    SplashDependenciesValidator.validate(deps)


if __name__ == "__main__":
    unittest.main()
