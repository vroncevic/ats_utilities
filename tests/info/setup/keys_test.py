# -*- coding: UTF-8 -*-

import unittest
from types import MappingProxyType
from collections.abc import Mapping

from ats_utilities.info.setup.keys import InfoKeys
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


class TestInfoKeys(unittest.TestCase):
    """Unit tests covering all constants and class methods of InfoKeys."""

    def test_dependency_key_constants(self):
        """Test that dependency key string constants match expected values."""
        self.assertEqual(InfoKeys.DEPENDENCY_NAME, 'name')
        self.assertEqual(InfoKeys.DEPENDENCY_VERSION, 'version')
        self.assertEqual(InfoKeys.DEPENDENCY_BUILD_DATE, 'build_date')
        self.assertEqual(InfoKeys.DEPENDENCY_LICENCE, 'licence')
        self.assertEqual(InfoKeys.DEPENDENCY_REPOSITORY, 'repository')
        self.assertEqual(InfoKeys.DEPENDENCY_ORGANIZATION, 'organization')
        self.assertEqual(InfoKeys.DEPENDENCY_USE_GITHUB_INFRASTRUCTURE, 'use_github')
        self.assertEqual(InfoKeys.DEPENDENCY_LOGO_PATH, 'logo')
        self.assertEqual(InfoKeys.DEPENDENCY_LOG_FILE, 'log_file')
        self.assertEqual(InfoKeys.DEPENDENCY_INFO_OK, 'info_ok')
        self.assertEqual(InfoKeys.DEPENDENCY_CONTEXT_BUNDLE, 'context_bundle')

    def test_option_key_constants(self):
        """Test that option key string constants match expected values."""
        self.assertEqual(InfoKeys.OPTION_INFO, 'info')
        self.assertEqual(InfoKeys.OPTION_CONTEXT_BUNDLE, 'context_bundle')

    def test_information_key_constants(self):
        """Test that information key string constants match expected values."""
        self.assertEqual(InfoKeys.ATS_NAME, 'ats_name')
        self.assertEqual(InfoKeys.ATS_VERSION, 'ats_version')
        self.assertEqual(InfoKeys.ATS_BUILD_DATE, 'ats_build_date')
        self.assertEqual(InfoKeys.ATS_LICENCE, 'ats_licence')
        self.assertEqual(InfoKeys.ATS_REPOSITORY, 'ats_repository')
        self.assertEqual(InfoKeys.ATS_ORGANIZATION, 'ats_organization')
        self.assertEqual(InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE, 'ats_use_github_infrastructure')
        self.assertEqual(InfoKeys.ATS_LOGO_PATH, 'ats_logo_path')
        self.assertEqual(InfoKeys.ATS_LOG_FILE, 'ats_log_file')
        self.assertEqual(InfoKeys.ATS_INFO_OK, 'ats_info_ok')

    def test_get_dependency_to_type(self):
        """Test get_dependency_to_type returns immutable MappingProxyType with valid types."""
        result = InfoKeys.get_dependency_to_type()

        self.assertIsInstance(result, MappingProxyType)
        self.assertEqual(len(result), 11)

        expected_mapping = {
            InfoKeys.DEPENDENCY_NAME: IName,
            InfoKeys.DEPENDENCY_VERSION: IVersion,
            InfoKeys.DEPENDENCY_BUILD_DATE: IBuildDate,
            InfoKeys.DEPENDENCY_LICENCE: ILicence,
            InfoKeys.DEPENDENCY_REPOSITORY: IRepository,
            InfoKeys.DEPENDENCY_ORGANIZATION: IOrganization,
            InfoKeys.DEPENDENCY_USE_GITHUB_INFRASTRUCTURE: IUseGitHub,
            InfoKeys.DEPENDENCY_LOGO_PATH: ILogo,
            InfoKeys.DEPENDENCY_LOG_FILE: ILogFile,
            InfoKeys.DEPENDENCY_INFO_OK: IInfoOk,
            InfoKeys.DEPENDENCY_CONTEXT_BUNDLE: ContextBundle,
        }

        for key, expected_type in expected_mapping.items():
            self.assertIn(key, result)
            self.assertEqual(result[key], expected_type)

    def test_get_option_to_type(self):
        """Test get_option_to_type returns immutable MappingProxyType with valid types."""
        result = InfoKeys.get_option_to_type()

        self.assertIsInstance(result, MappingProxyType)
        self.assertEqual(len(result), 2)

        self.assertEqual(result[InfoKeys.OPTION_INFO], Mapping[str, object])
        self.assertEqual(result[InfoKeys.OPTION_CONTEXT_BUNDLE], ContextBundle)

    def test_mapping_immutability(self):
        """Test that returned proxy mappings cannot be modified."""
        dep_mapping = InfoKeys.get_dependency_to_type()
        opt_mapping = InfoKeys.get_option_to_type()

        with self.assertRaises(TypeError):
            dep_mapping['new_key'] = str  # type: ignore

        with self.assertRaises(TypeError):
            opt_mapping['new_key'] = str  # type: ignore


if __name__ == '__main__':
    unittest.main()
