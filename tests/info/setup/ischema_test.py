# -*- coding: UTF-8 -*-

import unittest
from collections.abc import Sequence
from types import MappingProxyType

from ats_utilities.info.setup.ischema import IInfoSchema


class ValidSchemaImpl:
    """Mock implementation fulfilling the IInfoSchema protocol interface."""

    @classmethod
    def get_config_keys(cls) -> Sequence[str]:
        return ("ats_name",)

    @classmethod
    def is_registered_config_key(cls, name: str) -> bool:
        return name == "ats_name"

    @classmethod
    def get_config_keys_to_dependency_keys(cls) -> MappingProxyType[str, str]:
        return MappingProxyType({"ats_name": "name"})

    @classmethod
    def get_optional_config_keys(cls) -> Sequence[str]:
        return ()

    @classmethod
    def is_optional_config_key(cls, key: str) -> bool:
        return False

    @classmethod
    def is_required_config_key(cls, key: str) -> bool:
        return key == "ats_name"

    @classmethod
    def get_required_config_keys(cls) -> Sequence[str]:
        return ("ats_name",)

    @classmethod
    def get_name_of_config_key(cls, config_key: str) -> str:
        return "name"

    @classmethod
    def get_names_of_optional_config_keys(cls) -> Sequence[str]:
        return ()

    @classmethod
    def get_names_of_required_config_keys(cls) -> Sequence[str]:
        return ("name",)

    @classmethod
    def get_all_names_config_keys(cls) -> Sequence[str]:
        return ("name",)

    @classmethod
    def get_config_key_to_type(cls) -> MappingProxyType[str, type]:
        return MappingProxyType({"ats_name": str})


class InvalidSchemaImpl:
    """Mock implementation missing required protocol methods."""
    pass


class TestIInfoSchema(unittest.TestCase):
    """Unit test suite for testing runtime protocol conformance of IInfoSchema."""

    def test_iinfo_schema_conformance_positive(self):
        """Test that a valid class satisfies the IInfoSchema protocol."""
        self.assertIsInstance(ValidSchemaImpl, IInfoSchema)

    def test_iinfo_schema_conformance_negative(self):
        """Test that an incomplete class fails the IInfoSchema protocol check."""
        self.assertFalse(isinstance(InvalidSchemaImpl, IInfoSchema))


if __name__ == "__main__":
    unittest.main()
