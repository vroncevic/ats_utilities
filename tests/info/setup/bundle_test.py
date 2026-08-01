# -*- coding: UTF-8 -*-

'''
Module
    bundle_test.py
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
    Unit tests for InfoBundle class.
'''

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from unittest.mock import MagicMock

from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.name.iname import IName
from ats_utilities.info.version.iversion import IVersion
from ats_utilities.info.licence.ilicence import ILicence
from ats_utilities.info.build_date.ibuild_date import IBuildDate
from ats_utilities.info.repository.irepository import IRepository
from ats_utilities.info.organization.iorganization import IOrganization
from ats_utilities.info.use_github.iuse_github import IUseGitHub
from ats_utilities.info.logo.ilogo import ILogo
from ats_utilities.info.log_file.ilog_file import ILogFile
from ats_utilities.info.info_ok.iinfo_ok import IInfoOk
from ats_utilities.context.bundle import ContextBundle


class TestInfoBundle(unittest.TestCase):
    """Unit tests for the InfoBundle dataclass."""

    def setUp(self) -> None:
        """Set up valid mock objects and parameters for bundle instantiation."""
        self.mock_name = MagicMock(spec=IName)
        self.mock_version = MagicMock(spec=IVersion)
        self.mock_licence = MagicMock(spec=ILicence)
        self.mock_build_date = MagicMock(spec=IBuildDate)
        self.mock_repository = MagicMock(spec=IRepository)
        self.mock_organization = MagicMock(spec=IOrganization)
        self.mock_use_github = MagicMock(spec=IUseGitHub)
        self.mock_logo = MagicMock(spec=ILogo)
        self.mock_log_file = MagicMock(spec=ILogFile)
        self.mock_info_ok = MagicMock(spec=IInfoOk)
        self.mock_context_bundle = MagicMock(spec=ContextBundle)

        self.valid_params = {
            "name": self.mock_name,
            "version": self.mock_version,
            "licence": self.mock_licence,
            "build_date": self.mock_build_date,
            "repository": self.mock_repository,
            "organization": self.mock_organization,
            "use_github": self.mock_use_github,
            "logo": self.mock_logo,
            "log_file": self.mock_log_file,
            "info_ok": self.mock_info_ok,
            "context_bundle": self.mock_context_bundle
        }

    def test_successful_initialization(self) -> None:
        """Test successful initialization when all parameters match types and constraints."""
        bundle = InfoBundle(**self.valid_params)

        self.assertEqual(bundle.name, self.mock_name)
        self.assertEqual(bundle.version, self.mock_version)
        self.assertEqual(bundle.licence, self.mock_licence)
        self.assertEqual(bundle.build_date, self.mock_build_date)
        self.assertEqual(bundle.repository, self.mock_repository)
        self.assertEqual(bundle.organization, self.mock_organization)
        self.assertEqual(bundle.use_github, self.mock_use_github)
        self.assertEqual(bundle.logo, self.mock_logo)
        self.assertEqual(bundle.log_file, self.mock_log_file)
        self.assertEqual(bundle.info_ok, self.mock_info_ok)
        self.assertEqual(bundle.context_bundle, self.mock_context_bundle)

    def test_immutability_frozen_slots(self) -> None:
        """Test that altering an attribute post-initialization throws a FrozenInstanceError."""
        bundle = InfoBundle(**self.valid_params)

        with self.assertRaises(FrozenInstanceError):
            bundle.name = MagicMock(spec=IName)  # type: ignore

    def test_keyword_only_initialization(self) -> None:
        """Test that positional arguments are barred under kw_only configuration rules."""
        with self.assertRaises(TypeError):
            InfoBundle(
                self.mock_name,
                self.mock_version,
                self.mock_licence,
                self.mock_build_date,
                self.mock_repository,
                self.mock_organization,
                self.mock_use_github,
                self.mock_logo,
                self.mock_log_file,
                self.mock_info_ok,
                self.mock_context_bundle
            )

    def test_to_dict(self) -> None:
        """Test that to_dict compiles the structural field components exactly into a dictionary."""
        bundle = InfoBundle(**self.valid_params)
        exported_dict = bundle.to_dict()

        self.assertIsInstance(exported_dict, dict)
        self.assertEqual(exported_dict, self.valid_params)
        self.assertEqual(set(exported_dict.keys()), set(bundle.__dataclass_fields__.keys()))


if __name__ == '__main__':
    unittest.main()
