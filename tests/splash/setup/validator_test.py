# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
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
    Unit tests for SplashBundleValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splash.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splash.progressbar.iprogress_bar import IProgressBar
from ats_utilities.splash.property.isplash_property import ISplashProperty
from ats_utilities.splash.setup.bundle import SplashBundle
from ats_utilities.splash.setup.validator import SplashBundleValidator
from ats_utilities.splash.terminal.iterminal_properties import ITerminalProperties


@patch("ats_utilities.splash.setup.validator.ContextBundleValidator.validate")
class SplashValidatorTest(unittest.TestCase):
    '''
        Defines class SplashValidatorTest with attribute(s) and method(s).
        Tests SplashBundleValidator logic.
    '''

    def _get_mocks(self) -> dict[str, object]:
        return {
            "splash_property": MagicMock(spec=ISplashProperty),
            "terminal_property": MagicMock(spec=ITerminalProperties),
            "ext": MagicMock(spec=IExtInfrastructure),
            "pb": MagicMock(spec=IProgressBar),
            "context_bundle": MagicMock(spec=ContextBundle),
        }

    @patch("ats_utilities.splash.setup.validator.check_file_exists")
    def test_validate_valid(self, mock_check: MagicMock, mock_context_val: MagicMock) -> None:
        mocks = self._get_mocks()
        # Mock splash property to simulate enabled settings with logo
        mocks["splash_property"].is_settings_enabled.return_value = True
        mocks["splash_property"].get_logo.return_value = "/path/to/logo.png"

        bundle = SplashBundle(**mocks)
        SplashBundleValidator.validate(bundle)
        mock_check.assert_called_once_with(
            "/path/to/logo.png",
            "splash_bundle_validator::validate(...)",
            "the App/Tool/Script logo file path not correct"
        )
        mock_context_val.assert_called_once_with(bundle.context_bundle)

    @patch("ats_utilities.splash.setup.validator.check_file_exists")
    def test_validate_disabled(self, mock_check: MagicMock, mock_context_val: MagicMock) -> None:
        mocks = self._get_mocks()
        mocks["splash_property"].is_settings_enabled.return_value = False

        bundle = SplashBundle(**mocks)
        SplashBundleValidator.validate(bundle)
        mock_check.assert_not_called()
        mock_context_val.assert_called_once_with(bundle.context_bundle)

    def test_validate_invalid_bundle(self, mock_context_val: MagicMock) -> None:
        with self.assertRaises(ATSValueError):
            SplashBundleValidator.validate(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            SplashBundleValidator.validate(object())  # type: ignore

    def test_validate_invalid_none(self, mock_context_val: MagicMock) -> None:
        for key in self._get_mocks().keys():
            mocks = self._get_mocks()
            mocks[key] = None  # type: ignore
            bundle = SplashBundle.__new__(SplashBundle)
            for k, v in mocks.items():
                object.__setattr__(bundle, k, v)
            with self.assertRaises(ATSValueError):
                SplashBundleValidator.validate(bundle)

    def test_validate_invalid_type(self, mock_context_val: MagicMock) -> None:
        type_mismatches = {
            "splash_property": MagicMock(spec=ContextBundle),
            "terminal_property": MagicMock(spec=IProgressBar),
            "ext": MagicMock(spec=ISplashProperty),
            "pb": MagicMock(spec=ITerminalProperties),
            "context_bundle": MagicMock(spec=IExtInfrastructure)
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                mocks = self._get_mocks()
                mocks[field] = bad_value
                bundle = SplashBundle.__new__(SplashBundle)
                for k, v in mocks.items():
                    object.__setattr__(bundle, k, v)
                with self.assertRaises(ATSTypeError):
                    SplashBundleValidator.validate(bundle)


if __name__ == "__main__":
    unittest.main()
