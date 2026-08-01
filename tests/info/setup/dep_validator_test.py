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
    Unit tests for InfoDependenciesValidator class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.info.setup.dep_validator import InfoDependenciesValidator
from ats_utilities.info.setup.dependencies import InfoDependencies
from ats_utilities.info.name.iname import IName
from ats_utilities.info.version.iversion import IVersion
from ats_utilities.info.licence.ilicence import ILicence
from ats_utilities.info.build_date.ibuild_date import IBuildDate
from ats_utilities.info.info_ok.iinfo_ok import IInfoOk
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSValueError, ATSTypeError


class TestInfoDependenciesValidator(unittest.TestCase):
    """Unit tests for the InfoDependenciesValidator class."""

    def setUp(self) -> None:
        """Set up valid mock objects and parameters for dependencies validation."""
        self.mock_name = MagicMock(spec=IName)
        self.mock_version = MagicMock(spec=IVersion)
        self.mock_licence = MagicMock(spec=ILicence)
        self.mock_build_date = MagicMock(spec=IBuildDate)
        self.mock_info_ok = MagicMock(spec=IInfoOk)
        self.mock_context_bundle = MagicMock(spec=ContextBundle)

        self.valid_dependencies = InfoDependencies(
            name=self.mock_name,
            version=self.mock_version,
            licence=self.mock_licence,
            build_date=self.mock_build_date,
            info_ok=self.mock_info_ok,
            context_bundle=self.mock_context_bundle
        )

    def test_successful_validation(self) -> None:
        """Test successful validation with all dependencies present and valid."""
        try:
            InfoDependenciesValidator.validate(self.valid_dependencies)
        except (ATSValueError, ATSTypeError) as e:
            self.fail(f"validate raised unexpected error: {e}")

    def test_missing_dependencies_raises_value_error(self) -> None:
        """Test that validation fails with ATSValueError when dependencies dict is None or missing keys."""
        with self.assertRaises(ATSValueError):
            InfoDependenciesValidator.validate(None)  # type: ignore

        # Test missing name
        invalid_deps = self.valid_dependencies.copy()
        del invalid_deps['name']
        with self.assertRaises(ATSValueError):
            InfoDependenciesValidator.validate(invalid_deps)

    def test_invalid_type_raises_type_error(self) -> None:
        """Test that validation fails with ATSTypeError when attributes have incorrect types."""
        # Test invalid type for name
        invalid_deps = self.valid_dependencies.copy()
        invalid_deps['name'] = "not_a_name"  # type: ignore
        with self.assertRaises(ATSTypeError):
            InfoDependenciesValidator.validate(invalid_deps)


if __name__ == '__main__':
    unittest.main()
