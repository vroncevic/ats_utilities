# -*- coding: UTF-8 -*-

import unittest
from types import MappingProxyType
from collections.abc import Sequence

from ats_utilities.exceptions import ATSValueError
from ats_utilities.info.setup.schema import InfoSchema
from ats_utilities.info.setup.ischema import IInfoSchema
from ats_utilities.info.setup.keys import InfoBundleKeys


class TestInfoSchema(unittest.TestCase):
    """Unit test suite covering the InfoSchema concrete implementation."""

    def test_protocol_conformance(self):
        """Test if InfoSchema satisfies the runtime_checkable IInfoSchema protocol interface."""
        self.assertIsInstance(InfoSchema, IInfoSchema)

    def test_get_config_keys(self):
        """Test retrieving all registered config keys."""
        keys = InfoSchema.get_config_keys()
        self.assertIsInstance(keys, tuple)
        self.assertEqual(len(keys), 10)
        self.assertIn(InfoBundleKeys.ATS_NAME, keys)

    def test_is_registered_config_key(self):
        """Test checking registered vs unregistered config keys."""
        self.assertTrue(InfoSchema.is_registered_config_key(InfoBundleKeys.ATS_NAME))
        self.assertFalse(InfoSchema.is_registered_config_key("invalid_key"))

    def test_get_config_keys_to_dependency_keys(self):
        """Test retrieving mapping of config keys to dependency keys."""
        mapping = InfoSchema.get_config_keys_to_dependency_keys()
        self.assertIsInstance(mapping, MappingProxyType)
        self.assertEqual(mapping[InfoBundleKeys.ATS_NAME], InfoBundleKeys.DEPENDENCY_NAME)

    def test_optional_and_required_keys(self):
        """Test identifying optional vs required keys."""
        optional_keys = InfoSchema.get_optional_config_keys()
        required_keys = InfoSchema.get_required_config_keys()

        self.assertIn(InfoBundleKeys.ATS_LOGO_PATH, optional_keys)
        self.assertIn(InfoBundleKeys.ATS_NAME, required_keys)
        self.assertTrue(InfoSchema.is_optional_config_key(InfoBundleKeys.ATS_LOGO_PATH))
        self.assertTrue(InfoSchema.is_required_config_key(InfoBundleKeys.ATS_NAME))

    def test_get_name_of_config_key_valid(self):
        """Test retrieving dependency name for a registered config key."""
        dep_name = InfoSchema.get_name_of_config_key(InfoBundleKeys.ATS_VERSION)
        self.assertEqual(dep_name, InfoBundleKeys.DEPENDENCY_VERSION)

    def test_get_name_of_config_key_invalid_raises_exception(self):
        """Test retrieving dependency name for an unregistered key raises ATSValueError."""
        with self.assertRaises(ATSValueError):
            InfoSchema.get_name_of_config_key("unregistered_key")

    def test_get_names_sequences(self):
        """Test helper sequence getters for optional, required, and all dependency names."""
        optional_names = InfoSchema.get_names_of_optional_config_keys()
        required_names = InfoSchema.get_names_of_required_config_keys()
        all_names = InfoSchema.get_all_names_config_keys()

        self.assertIsInstance(optional_names, Sequence)
        self.assertIsInstance(required_names, Sequence)
        self.assertIsInstance(all_names, Sequence)
        self.assertEqual(len(all_names), len(optional_names) + len(required_names))

    def test_get_config_key_to_type(self):
        """Test retrieving mapping of config keys to engine type classes."""
        type_mapping = InfoSchema.get_config_key_to_type()
        self.assertIsInstance(type_mapping, MappingProxyType)
        self.assertIn(InfoBundleKeys.ATS_NAME, type_mapping)


if __name__ == "__main__":
    unittest.main()
