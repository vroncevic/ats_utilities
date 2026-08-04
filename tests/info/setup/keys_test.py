# -*- coding: UTF-8 -*-

import unittest
from types import MappingProxyType
from collections.abc import Mapping

from ats_utilities.info.setup.keys import InfoBundleKeys
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
    """Unit tests covering all constants and class methods of InfoBundleKeys."""

    def test_dependency_key_constants(self):
        """Test that dependency key string constants match expected values."""
        self.assertEqual(InfoBundleKeys.DEPENDENCY_NAME, 'name')
        self.assertEqual(InfoBundleKeys.DEPENDENCY_VERSION, 'version')
        self.assertEqual(InfoBundleKeys.DEPENDENCY_BUILD_DATE, 'build_date')
        self.assertEqual(InfoBundleKeys.DEPENDENCY_LICENCE, 'licence')
        self.assertEqual(InfoBundleKeys.DEPENDENCY_REPOSITORY, 'repository')
        self.assertEqual(InfoBundleKeys.DEPENDENCY_ORGANIZATION, 'organization')
        self.assertEqual(InfoBundleKeys.DEPENDENCY_USE_GITHUB_INFRASTRUCTURE, 'use_github')
        self.assertEqual(InfoBundleKeys.DEPENDENCY_LOGO_PATH, 'logo')
        self.assertEqual(InfoBundleKeys.DEPENDENCY_LOG_FILE, 'log_file')
        self.assertEqual(InfoBundleKeys.DEPENDENCY_INFO_OK, 'info_ok')
        self.assertEqual(InfoBundleKeys.DEPENDENCY_CONTEXT_BUNDLE, 'context_bundle')

    def test_option_key_constants(self):
        """Test that option key string constants match expected values."""
        self.assertEqual(InfoBundleKeys.OPTION_INFO, 'info')
        self.assertEqual(InfoBundleKeys.OPTION_CONTEXT_BUNDLE, 'context_bundle')

    def test_information_key_constants(self):
        """Test that information key string constants match expected values."""
        self.assertEqual(InfoBundleKeys.ATS_NAME, 'ats_name')
        self.assertEqual(InfoBundleKeys.ATS_VERSION, 'ats_version')
        self.assertEqual(InfoBundleKeys.ATS_BUILD_DATE, 'ats_build_date')
        self.assertEqual(InfoBundleKeys.ATS_LICENCE, 'ats_licence')
        self.assertEqual(InfoBundleKeys.ATS_REPOSITORY, 'ats_repository')
        self.assertEqual(InfoBundleKeys.ATS_ORGANIZATION, 'ats_organization')
        self.assertEqual(InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE, 'ats_use_github_infrastructure')
        self.assertEqual(InfoBundleKeys.ATS_LOGO_PATH, 'ats_logo_path')
        self.assertEqual(InfoBundleKeys.ATS_LOG_FILE, 'ats_log_file')
        self.assertEqual(InfoBundleKeys.ATS_INFO_OK, 'ats_info_ok')

    def test_get_dependency_to_type(self):
        """Test get_dependency_to_type returns immutable MappingProxyType with valid types."""
        result = InfoBundleKeys.get_dependency_to_type()

        self.assertIsInstance(result, MappingProxyType)
        self.assertEqual(len(result), 11)

        expected_mapping = {
            InfoBundleKeys.DEPENDENCY_NAME: IName,
            InfoBundleKeys.DEPENDENCY_VERSION: IVersion,
            InfoBundleKeys.DEPENDENCY_BUILD_DATE: IBuildDate,
            InfoBundleKeys.DEPENDENCY_LICENCE: ILicence,
            InfoBundleKeys.DEPENDENCY_REPOSITORY: IRepository,
            InfoBundleKeys.DEPENDENCY_ORGANIZATION: IOrganization,
            InfoBundleKeys.DEPENDENCY_USE_GITHUB_INFRASTRUCTURE: IUseGitHub,
            InfoBundleKeys.DEPENDENCY_LOGO_PATH: ILogo,
            InfoBundleKeys.DEPENDENCY_LOG_FILE: ILogFile,
            InfoBundleKeys.DEPENDENCY_INFO_OK: IInfoOk,
            InfoBundleKeys.DEPENDENCY_CONTEXT_BUNDLE: ContextBundle,
        }

        for key, expected_type in expected_mapping.items():
            self.assertIn(key, result)
            self.assertEqual(result[key], expected_type)

    def test_get_option_to_type(self):
        """Test get_option_to_type returns immutable MappingProxyType with valid types."""
        result = InfoBundleKeys.get_option_to_type()

        self.assertIsInstance(result, MappingProxyType)
        self.assertEqual(len(result), 2)

        self.assertEqual(result[InfoBundleKeys.OPTION_INFO], Mapping[str, object])
        self.assertEqual(result[InfoBundleKeys.OPTION_CONTEXT_BUNDLE], ContextBundle)

    def test_mapping_immutability(self):
        """Test that returned proxy mappings cannot be modified."""
        dep_mapping = InfoBundleKeys.get_dependency_to_type()
        opt_mapping = InfoBundleKeys.get_option_to_type()

        with self.assertRaises(TypeError):
            dep_mapping['new_key'] = str  # type: ignore

        with self.assertRaises(TypeError):
            opt_mapping['new_key'] = str  # type: ignore


if __name__ == '__main__':
    unittest.main()
