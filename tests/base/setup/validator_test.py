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
    Unit tests for BaseValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock
from typing import Any

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.validator import BaseValidator
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.info.iinfo_manager import IInfoManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.context.bundle import ContextBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class BaseValidatorTest(unittest.TestCase):
    '''
        Defines class BaseValidatorTest with attribute(s) and method(s).
        Tests BaseValidator logic.
    '''

    def setUp(self) -> None:
        self.mock_config_loader = MagicMock(spec=ILoader)
        self.mock_info_manager = MagicMock(spec=IInfoManager)
        self.mock_options_parser = MagicMock(spec=IOptionManager)
        self.mock_splasher = MagicMock(spec=ISplasher)
        self.mock_generator = MagicMock(spec=IGenerator)
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        
        self.valid_params = {
            "info_file": "/path/to/info.cfg",
            "config_loader": self.mock_config_loader,
            "info_manager": self.mock_info_manager,
            "options_parser": self.mock_options_parser,
            "splasher": self.mock_splasher,
            "generator": self.mock_generator,
            "use_generator": True,
            "context_bundle": self.mock_context_bundle
        }

    def test_validate_valid(self) -> None:
        bundle = BaseBundle(**self.valid_params)
        # Should validate successfully
        BaseValidator.validate(bundle)

    def test_validate_invalid_bundle(self) -> None:
        with self.assertRaises(ATSValueError):
            BaseValidator.validate(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            BaseValidator.validate(object())  # type: ignore

    def test_validate_invalid_none(self) -> None:
        fields = [
            "info_file", "config_loader", "info_manager", 
            "options_parser", "splasher", "use_generator", "context_bundle"
        ]

        for field in fields:
            with self.subTest(field=field):
                mocks = self.valid_params.copy()
                mocks[field] = None  # type: ignore
                bundle = BaseBundle.__new__(BaseBundle)
                for k, v in mocks.items():
                    object.__setattr__(bundle, k, v)
                with self.assertRaises(ATSValueError):
                    BaseValidator.validate(bundle)

    def test_validate_invalid_type(self) -> None:
        type_mismatches = {
            "info_file": 12345,
            "config_loader": MagicMock(spec=IInfoManager),
            "info_manager": MagicMock(spec=ILoader),
            "options_parser": MagicMock(spec=ISplasher),
            "splasher": MagicMock(spec=IOptionManager),
            "use_generator": "True",
            "generator": MagicMock(spec=ContextBundle),
            "context_bundle": MagicMock(spec=IGenerator)
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                mocks = self.valid_params.copy()
                mocks[field] = bad_value
                bundle = BaseBundle.__new__(BaseBundle)
                for k, v in mocks.items():
                    object.__setattr__(bundle, k, v)
                with self.assertRaises(ATSTypeError):
                    BaseValidator.validate(bundle)


if __name__ == "__main__":
    unittest.main()
