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
    Unit tests for ContextBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from ats_utilities.context.opt_validator import ContextBundleOptionsValidator
from ats_utilities.context.options import ContextBundleOptions
from ats_utilities.exceptions import ATSValueError, ATSTypeError


class TestContextOptionsValidator(unittest.TestCase):
    """Unit tests for the ContextBundleOptionsValidator class."""

    def setUp(self) -> None:
        """Set up valid option parameters for validation."""
        self.valid_options = ContextBundleOptions(
            checker={},
            logger={},
            reporter={},
            verbose=True
        )

    def test_successful_validation(self) -> None:
        """Test successful validation with all options present and valid."""
        try:
            ContextBundleOptionsValidator.validate(self.valid_options)
        except (ATSValueError, ATSTypeError) as e:
            self.fail(f"validate raised unexpected error: {e}")

    def test_successful_validation_with_missing_optional_keys(self) -> None:
        """Test successful validation when some options keys are omitted."""
        partial_opts = ContextBundleOptions(
            verbose=False
        )
        try:
            ContextBundleOptionsValidator.validate(partial_opts)
        except (ATSValueError, ATSTypeError) as e:
            self.fail(f"validate raised unexpected error with partial options: {e}")

    def test_missing_options_raises_value_error(self) -> None:
        """Test that validation fails with ATSValueError when options dict is None."""
        with self.assertRaises(ATSValueError):
            ContextBundleOptionsValidator.validate(None)  # type: ignore

    def test_invalid_type_raises_type_error(self) -> None:
        """Test that validation fails with ATSTypeError when options have incorrect types."""
        # Test invalid type for checker
        invalid_opts = self.valid_options.copy()
        invalid_opts['checker'] = "not_a_dict"  # type: ignore
        with self.assertRaises(ATSTypeError):
            ContextBundleOptionsValidator.validate(invalid_opts)

        # Test invalid type for verbose
        invalid_opts2 = self.valid_options.copy()
        invalid_opts2['verbose'] = "not_a_bool"  # type: ignore
        with self.assertRaises(ATSTypeError):
            ContextBundleOptionsValidator.validate(invalid_opts2)


if __name__ == '__main__':
    unittest.main()
