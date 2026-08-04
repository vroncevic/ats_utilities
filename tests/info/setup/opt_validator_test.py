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
    Unit tests for InfoBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.info.setup.opt_validator import InfoBundleOptionsValidator
from ats_utilities.info.setup.options import InfoBundleOptions
from ats_utilities.info.setup.keys import InfoBundleKeys
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSValueError, ATSTypeError


class TestInfoOptionsValidator(unittest.TestCase):
    """Unit tests for the InfoBundleOptionsValidator class."""

    def setUp(self) -> None:
        """Set up valid option parameters for validation."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.valid_info = {
            InfoBundleKeys.ATS_NAME: "ats_utilities",
            InfoBundleKeys.ATS_VERSION: "3.4.5",
            InfoBundleKeys.ATS_BUILD_DATE: "2026-08-01",
            InfoBundleKeys.ATS_LICENCE: "GPL-3.0",
            InfoBundleKeys.ATS_INFO_OK: "OK"
        }

        self.valid_options = InfoBundleOptions(
            info=self.valid_info,
            context_bundle=self.mock_context_bundle
        )

    def test_successful_validation(self) -> None:
        """Test successful validation with all options present and valid."""
        try:
            InfoBundleOptionsValidator.validate(self.valid_options)
        except (ATSValueError, ATSTypeError) as e:
            self.fail(f"validate raised unexpected error: {e}")

    def test_missing_options_raises_value_error(self) -> None:
        """Test that validation fails with ATSValueError when options dict is None."""
        with self.assertRaises(ATSValueError):
            InfoBundleOptionsValidator.validate(None)  # type: ignore

    def test_invalid_type_raises_type_error(self) -> None:
        """Test that validation fails with ATSTypeError when options have incorrect types."""
        # Test invalid type for info
        invalid_opts = self.valid_options.copy()
        invalid_opts['info'] = "not_a_mapping"  # type: ignore
        with self.assertRaises(ATSTypeError):
            InfoBundleOptionsValidator.validate(invalid_opts)

        # Test invalid type for context_bundle
        invalid_opts2 = self.valid_options.copy()
        invalid_opts2['context_bundle'] = "not_a_context_bundle"  # type: ignore
        with self.assertRaises(ATSTypeError):
            InfoBundleOptionsValidator.validate(invalid_opts2)

    def test_info_structure_missing_required_keys_raises_value_error(self) -> None:
        """Test that validation fails when info dictionary is missing required keys."""
        bad_info = self.valid_info.copy()
        del bad_info[InfoBundleKeys.ATS_NAME]

        invalid_opts = InfoBundleOptions(
            info=bad_info,
            context_bundle=self.mock_context_bundle
        )
        with self.assertRaises(ATSValueError):
            InfoBundleOptionsValidator.validate(invalid_opts)

    def test_info_structure_contains_invalid_keys_raises_value_error(self) -> None:
        """Test that validation fails when info dictionary contains invalid keys."""
        bad_info = self.valid_info.copy()
        bad_info["invalid_key"] = "some_value"

        invalid_opts = InfoBundleOptions(
            info=bad_info,
            context_bundle=self.mock_context_bundle
        )
        with self.assertRaises(ATSValueError):
            InfoBundleOptionsValidator.validate(invalid_opts)


if __name__ == '__main__':
    unittest.main()
