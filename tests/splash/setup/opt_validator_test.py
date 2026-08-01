# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
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
    Unit tests for SplashOptionsValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.splash.setup.opt_validator import SplashOptionsValidator
from ats_utilities.splash.setup.options import SplashOptions


@patch("ats_utilities.splash.setup.opt_validator.ContextValidator.validate")
class SplashOptionsValidatorTest(unittest.TestCase):
    '''
        Defines class SplashOptionsValidatorTest with attribute(s) and method(s).
        Tests SplashOptionsValidator.
    '''

    def _get_valid_opts(self) -> SplashOptions:
        return {
            "prop": {"enabled": True},
            "context_bundle": MagicMock(spec=ContextBundle),
        }

    def test_validate_valid(self, mock_context_val: MagicMock) -> None:
        opts = self._get_valid_opts()
        SplashOptionsValidator.validate(opts)
        mock_context_val.assert_called_once_with(opts["context_bundle"])

    def test_validate_invalid_none(self, mock_context_val: MagicMock) -> None:
        with self.assertRaises(ATSValueError):
            SplashOptionsValidator.validate(None)  # type: ignore

    def test_validate_invalid_type(self, mock_context_val: MagicMock) -> None:
        with self.assertRaises(ATSTypeError):
            SplashOptionsValidator.validate(object())  # type: ignore

    def test_validate_bad_types(self, mock_context_val: MagicMock) -> None:
        type_mismatches = {
            "prop": object(),
            "context_bundle": object()
        }
        for key, bad_value in type_mismatches.items():
            with self.subTest(key=key, bad_value=bad_value):
                opts = self._get_valid_opts()
                opts[key] = bad_value  # type: ignore
                with self.assertRaises(ATSTypeError):
                    SplashOptionsValidator.validate(opts)


if __name__ == "__main__":
    unittest.main()
