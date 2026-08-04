# -*- coding: UTF-8 -*-

import unittest

from ats_utilities.exceptions import ATSValueError
from ats_utilities.info.setup.expose import InfoExpose
from ats_utilities.info.setup.iexpose import IInfoExpose
from ats_utilities.info.setup.keys import InfoBundleKeys


class TestInfoExpose(unittest.TestCase):
    """Unit test suite covering the InfoExpose concrete implementation."""

    def setUp(self):
        """Prepare sample valid configuration mappings for tests."""
        self.valid_config = {
            InfoBundleKeys.ATS_NAME: "ats_utilities",
            InfoBundleKeys.ATS_VERSION: "3.4.5",
            InfoBundleKeys.ATS_BUILD_DATE: "2026-08-01",
            InfoBundleKeys.ATS_LICENCE: "GPL-3.0-or-later",
            InfoBundleKeys.ATS_REPOSITORY: "https://github.com/vroncevic/ats_utilities",
            InfoBundleKeys.ATS_ORGANIZATION: "ats",
            InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE: True,
            InfoBundleKeys.ATS_LOGO_PATH: "/path/to/logo.png",
            InfoBundleKeys.ATS_LOG_FILE: "/path/to/app.log",
            InfoBundleKeys.ATS_INFO_OK: True,
        }

    def test_protocol_conformance(self):
        """Test if InfoExpose satisfies the runtime_checkable IInfoExpose protocol interface."""
        self.assertIsInstance(InfoExpose, IInfoExpose)

    def test_get_all_properties_success(self):
        """Test successfully extracting all configuration properties."""
        self.assertEqual(InfoExpose.get_name(self.valid_config), "ats_utilities")
        self.assertEqual(InfoExpose.get_version(self.valid_config), "3.4.5")
        self.assertEqual(InfoExpose.get_build_date(self.valid_config), "2026-08-01")
        self.assertEqual(InfoExpose.get_licence(self.valid_config), "GPL-3.0-or-later")
        self.assertEqual(InfoExpose.get_repository(self.valid_config), "https://github.com/vroncevic/ats_utilities")
        self.assertEqual(InfoExpose.get_organization(self.valid_config), "ats")
        self.assertTrue(InfoExpose.get_use_github_infrastructure(self.valid_config))
        self.assertEqual(InfoExpose.get_logo_path(self.valid_config), "/path/to/logo.png")
        self.assertEqual(InfoExpose.get_log_file(self.valid_config), "/path/to/app.log")
        self.assertTrue(InfoExpose.get_info_ok(self.valid_config))

    def test_get_property_missing_key_raises_exception(self):
        """Test extracting properties from config missing required keys raises ATSValueError."""
        incomplete_config = {"ats_version": "1.0.0"}

        with self.assertRaises(ATSValueError):
            InfoExpose.get_name(incomplete_config)

        with self.assertRaises(ATSValueError):
            InfoExpose.get_build_date(incomplete_config)


if __name__ == "__main__":
    unittest.main()
