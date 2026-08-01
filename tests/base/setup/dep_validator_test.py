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
    Unit tests for BaseDependenciesValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.base.setup.dep_validator import BaseDependenciesValidator
from ats_utilities.base.setup.dependencies import BaseDependencies
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSValueError, ATSTypeError


@patch("ats_utilities.base.setup.dep_validator.ContextValidator")
class TestBaseDependenciesValidator(unittest.TestCase):
    """Unit tests for the BaseDependenciesValidator class."""

    def setUp(self) -> None:
        """Set up valid mock objects and parameters for dependencies validation."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.mock_info_manager = MagicMock(spec=IInfoManager)
        self.mock_option_manager = MagicMock(spec=IOptionManager)
        self.mock_splash_manager = MagicMock(spec=ISplashManager)
        self.mock_generation_manager = MagicMock(spec=IGeneratorManager)

        self.valid_dependencies = BaseDependencies(
            context_bundle=self.mock_context_bundle,
            info_manager=self.mock_info_manager,
            option_manager=self.mock_option_manager,
            splash_manager=self.mock_splash_manager,
            generation_manager=self.mock_generation_manager
        )

    def test_successful_validation(self, mock_ctx_val: MagicMock) -> None:
        """Test successful validation with all dependencies present and valid."""
        mock_ctx_val.validate.side_effect = None
        try:
            BaseDependenciesValidator.validate(self.valid_dependencies)
        except (ATSValueError, ATSTypeError) as e:
            self.fail(f"validate raised unexpected error: {e}")

    def test_successful_validation_with_optional_generation_manager_none(self, mock_ctx_val: MagicMock) -> None:
        """Test successful validation when optional generation_manager is None."""
        self.valid_dependencies['generation_manager'] = None
        mock_ctx_val.validate.side_effect = None
        try:
            BaseDependenciesValidator.validate(self.valid_dependencies)
        except (ATSValueError, ATSTypeError) as e:
            self.fail(f"validate raised unexpected error with None generation_manager: {e}")

    def test_missing_dependencies_raises_value_error(self, mock_ctx_val: MagicMock) -> None:
        """Test that validation fails with ATSValueError when dependencies dict is None or missing keys."""
        mock_ctx_val.validate.side_effect = None
        with self.assertRaises(ATSValueError):
            BaseDependenciesValidator.validate(None)  # type: ignore

        # Test missing context_bundle
        invalid_deps = self.valid_dependencies.copy()
        del invalid_deps['context_bundle']
        mock_ctx_val.validate.side_effect = ATSValueError("the bundle must be provided")
        with self.assertRaises(ATSValueError):
            BaseDependenciesValidator.validate(invalid_deps)

    def test_invalid_type_raises_type_error(self, mock_ctx_val: MagicMock) -> None:
        """Test that validation fails with ATSTypeError when attributes have incorrect types."""
        # Test invalid type for context_bundle
        invalid_deps = self.valid_dependencies.copy()
        invalid_deps['context_bundle'] = "not_a_context_bundle"  # type: ignore
        mock_ctx_val.validate.side_effect = ATSTypeError("invalid bundle type")
        with self.assertRaises(ATSTypeError):
            BaseDependenciesValidator.validate(invalid_deps)

        # Test invalid type for generation_manager (not None and not IGeneratorManager)
        invalid_deps2 = self.valid_dependencies.copy()
        invalid_deps2['generation_manager'] = "not_a_generator_manager"  # type: ignore
        mock_ctx_val.validate.side_effect = None
        with self.assertRaises(ATSTypeError):
            BaseDependenciesValidator.validate(invalid_deps2)


if __name__ == '__main__':
    unittest.main()
