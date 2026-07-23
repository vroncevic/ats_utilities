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
    Unit tests for ProjectValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.generator.project.ipro_config import IProConfig
from ats_utilities.generator.project.ipro_name import IProName
from ats_utilities.generator.project.itemplate_dir import ITemplateDir
from ats_utilities.generator.project.setup.bundle import ProjectBundle
from ats_utilities.generator.project.setup.validator import ProjectValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ProjectValidatorTest(unittest.TestCase):
    '''
        Defines class ProjectValidatorTest with attribute(s) and method(s).
        Tests ProjectValidator logic.
    '''

    def setUp(self) -> None:
        self.mock_pro_name = MagicMock(spec=IProName)
        self.mock_pro_config = MagicMock(spec=IProConfig)
        self.mock_template_dir = MagicMock(spec=ITemplateDir)
        self.mock_context = MagicMock(spec=ContextBundle)

        self.valid_params = {
            "pro_name": self.mock_pro_name,
            "pro_config": self.mock_pro_config,
            "template_dir": self.mock_template_dir,
            "context_bundle": self.mock_context
        }

    def test_validate_valid(self) -> None:
        bundle = ProjectBundle(**self.valid_params)
        # Should validate successfully
        ProjectValidator.validate(bundle)

    def test_validate_invalid_bundle(self) -> None:
        with self.assertRaises(ATSValueError):
            ProjectValidator.validate(None)  # type: ignore

        with self.assertRaises(ATSTypeError):
            ProjectValidator.validate(object())  # type: ignore

    def test_validate_invalid_none(self) -> None:
        fields = ["pro_name", "pro_config", "template_dir", "context_bundle"]

        for field in fields:
            with self.subTest(field=field):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = None  # type: ignore
                bundle = ProjectBundle(**invalid_params)
                with self.assertRaises(ATSValueError):
                    ProjectValidator.validate(bundle)

    def test_validate_invalid_type(self) -> None:
        type_mismatches = {
            "pro_name": MagicMock(spec=ContextBundle),
            "pro_config": MagicMock(spec=IProName),
            "template_dir": MagicMock(spec=IProConfig),
            "context_bundle": MagicMock(spec=ITemplateDir)
        }

        for field, bad_value in type_mismatches.items():
            with self.subTest(field=field, bad_value=bad_value):
                invalid_params = self.valid_params.copy()
                invalid_params[field] = bad_value
                bundle = ProjectBundle(**invalid_params)
                with self.assertRaises(ATSTypeError):
                    ProjectValidator.validate(bundle)


if __name__ == "__main__":
    unittest.main()
