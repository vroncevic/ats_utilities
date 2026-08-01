# -*- coding: UTF-8 -*-

import unittest
from collections.abc import Mapping

from ats_utilities.info.setup.iexpose import IInfoExpose


class ValidExposeImpl:
    """Mock implementation fulfilling the IInfoExpose protocol interface."""

    @classmethod
    def get_name(cls, config: Mapping[str, str]) -> str:
        return config["ats_name"]

    @classmethod
    def get_version(cls, config: Mapping[str, str]) -> str:
        return config["ats_version"]

    @classmethod
    def get_build_date(cls, config: Mapping[str, str]) -> str:
        return config["ats_build_date"]

    @classmethod
    def get_licence(cls, config: Mapping[str, str]) -> str:
        return config["ats_licence"]

    @classmethod
    def get_repository(cls, config: Mapping[str, str]) -> str:
        return config["ats_repository"]

    @classmethod
    def get_organization(cls, config: Mapping[str, str]) -> str:
        return config["ats_organization"]

    @classmethod
    def get_use_github_infrastructure(cls, config: Mapping[str, str]) -> bool:
        return True

    @classmethod
    def get_logo_path(cls, config: Mapping[str, str]) -> str:
        return config["ats_logo_path"]

    @classmethod
    def get_log_file(cls, config: Mapping[str, str]) -> str:
        return config["ats_log_file"]

    @classmethod
    def get_info_ok(cls, config: Mapping[str, str]) -> bool:
        return True


class InvalidExposeImpl:
    """Mock implementation missing required protocol methods."""
    pass


class TestIInfoExpose(unittest.TestCase):
    """Unit test suite for testing runtime protocol conformance of IInfoExpose."""

    def test_iinfo_expose_conformance_positive(self):
        """Test that a valid class satisfies the IInfoExpose protocol."""
        self.assertIsInstance(ValidExposeImpl, IInfoExpose)

    def test_iinfo_expose_conformance_negative(self):
        """Test that an incomplete class fails the IInfoExpose protocol check."""
        self.assertFalse(isinstance(InvalidExposeImpl, IInfoExpose))


if __name__ == "__main__":
    unittest.main()
