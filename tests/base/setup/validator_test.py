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
    Unit tests for BaseBundleValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.validator import BaseBundleValidator
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.context.bundle import ContextBundle


@patch("ats_utilities.base.setup.validator.ContextBundleValidator")
class BaseValidatorTest(unittest.TestCase):
    '''
        Defines class BaseValidatorTest with attribute(s) and method(s).
        Tests BaseBundleValidator logic.
    '''

    def setUp(self) -> None:
        self.mock_info_manager = MagicMock(spec=IInfoManager)
        self.mock_option_manager = MagicMock(spec=IOptionManager)
        self.mock_splash_manager = MagicMock(spec=ISplashManager)
        self.mock_generation_manager = MagicMock(spec=IGeneratorManager)
        self.mock_context_bundle = MagicMock(spec=ContextBundle)

        self.valid_params = {
            "context_bundle": self.mock_context_bundle,
            "info_manager": self.mock_info_manager,
            "option_manager": self.mock_option_manager,
            "splash_manager": self.mock_splash_manager,
            "generation_manager": self.mock_generation_manager
        }

    def test_validate_valid(self, mock_ctx_val: MagicMock) -> None:
        bundle = BaseBundle(**self.valid_params)
        mock_ctx_val.validate.side_effect = None
        # Should validate successfully
        BaseBundleValidator.validate(bundle)

    def test_validate_valid_gen_manager_none(self, mock_ctx_val: MagicMock) -> None:
        params = self.valid_params.copy()
        params["generation_manager"] = None
        bundle = BaseBundle(**params)
        mock_ctx_val.validate.side_effect = None
        # Should validate successfully
        BaseBundleValidator.validate(bundle)

    def test_validate_invalid_bundle(self, mock_ctx_val: MagicMock) -> None:
        with self.assertRaises(ATSValueError):
            BaseBundleValidator.validate(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            BaseBundleValidator.validate(object())  # type: ignore

    def test_validate_invalid_none(self, mock_ctx_val: MagicMock) -> None:
        fields = [
            "context_bundle", "info_manager", "option_manager", "splash_manager"
        ]

        for field in fields:
            with self.subTest(field=field):
                mocks = self.valid_params.copy()
                mocks[field] = None  # type: ignore
                bundle = BaseBundle.__new__(BaseBundle)
                for k, v in mocks.items():
                    object.__setattr__(bundle, k, v)
                
                if field == "context_bundle":
                    mock_ctx_val.validate.side_effect = ATSValueError("the bundle must be provided")
                else:
                    mock_ctx_val.validate.side_effect = None
                    
                with self.assertRaises(ATSValueError):
                    BaseBundleValidator.validate(bundle)

    def test_validate_invalid_type(self, mock_ctx_val: MagicMock) -> None:
        type_mismatches = {
            "context_bundle": MagicMock(spec=IInfoManager),
            "info_manager": MagicMock(spec=ContextBundle),
            "option_manager": MagicMock(spec=ISplashManager),
            "splash_manager": MagicMock(spec=IOptionManager),
            "generation_manager": MagicMock(spec=ContextBundle)
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                mocks = self.valid_params.copy()
                mocks[field] = bad_value
                bundle = BaseBundle.__new__(BaseBundle)
                for k, v in mocks.items():
                    object.__setattr__(bundle, k, v)
                
                if field == "context_bundle":
                    mock_ctx_val.validate.side_effect = ATSTypeError("invalid bundle type")
                else:
                    mock_ctx_val.validate.side_effect = None
                    
                with self.assertRaises(ATSTypeError):
                    BaseBundleValidator.validate(bundle)


if __name__ == "__main__":
    unittest.main()
