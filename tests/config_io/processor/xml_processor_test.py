# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from collections.abc import Mapping
import xml.etree.ElementTree as ET

# Adjust imports according to your project structure
from ats_utilities.config_io.processor.xml_processor import XMLProcessor


class TestXMLProcessor(unittest.TestCase):
    """Unit tests for the XMLProcessor class."""

    def setUp(self) -> None:
        """Set up standard schemas and test definitions."""
        self.sample_scheme = {
            "__root__": "ats_utility",
            "ats_name": "ats_info",
            "hostname": "connection",
            "verbose": ""
        }
        self.valid_xml_content = (
            "<ats_utility>"
            "<ats_info><ats_name>test_app</ats_name></ats_info>"
            "<connection><hostname>localhost</hostname></connection>"
            "<verbose>True</verbose>"
            "</ats_utility>"
        )

    def test_initialization_without_scheme(self) -> None:
        """Test instantiation with no validation scheme provided defaults root tag name."""
        processor = XMLProcessor()
        self.assertIsNone(processor._root)
        self.assertIsNone(processor._scheme)
        self.assertEqual(processor._root_tag, 'configuration')

    def test_initialization_with_scheme(self) -> None:
        """Test instantiation resolves custom root tag name specified via scheme parameters."""
        processor = XMLProcessor(scheme=self.sample_scheme)
        self.assertIsNone(processor._root)
        self.assertEqual(processor._scheme, self.sample_scheme)
        self.assertEqual(processor._root_tag, 'ats_utility')

    def test_deserialize_with_valid_xml_string(self) -> None:
        """Test deserialization with a valid XML string matching the configured layout scheme."""
        processor = XMLProcessor(scheme=self.sample_scheme)
        success = processor.deserialize(self.valid_xml_content)

        self.assertTrue(success)
        self.assertIsNotNone(processor._root)
        self.assertEqual(processor._root.tag, 'ats_utility')

    def test_deserialize_invalid_xml_format(self) -> None:
        """Test that deserialization catches ET.ParseError and returns False."""
        processor = XMLProcessor()
        invalid_xml = "<ats_utility><verbose>True</verbose>"  # Missing closing root element tag
        
        success = processor.deserialize(invalid_xml)
        self.assertFalse(success)

    def test_deserialize_fails_validation_scheme(self) -> None:
        """Test that deserialization returns False if targeted structural nodes are missing."""
        processor = XMLProcessor(scheme=self.sample_scheme)
        incomplete_xml = "<ats_utility><verbose>False</verbose></ats_utility>"  # Missing 'ats_info' and 'connection'
        
        success = processor.deserialize(incomplete_xml)
        self.assertFalse(success)

    def test_serialize_formats_correctly(self) -> None:
        """Test that serialize exports internal element elements back to an XML string."""
        processor = XMLProcessor()
        processor._root = ET.Element("configuration")
        child = ET.SubElement(processor._root, "item")
        child.text = "value"
        
        output = processor.serialize()
        self.assertEqual(output, "<configuration><item>value</item></configuration>")

    def test_serialize_empty_root_returns_empty_string(self) -> None:
        """Test that serialization returns an empty string when no root element structure exists."""
        processor = XMLProcessor()
        self.assertEqual(processor.serialize(), '')

    def test_update_data_creates_new_root_if_none(self) -> None:
        """Test updating data automatically scaffolds a root element if none exists."""
        processor = XMLProcessor(scheme=self.sample_scheme)
        self.assertIsNone(processor._root)

        updates = {
            "ats_name": "my_xml_app",
            "hostname": "localhost",
            "verbose": "False"
        }
        success = processor.update_data(updates)

        self.assertTrue(success)
        self.assertIsNotNone(processor._root)
        self.assertEqual(processor._root.tag, "ats_utility")
        self.assertEqual(processor.to_dict()["verbose"], "False")

    def test_update_data_appends_or_modifies_nodes_correctly(self) -> None:
        """Test update modifications alter element texts or add missing nested sub-elements."""
        processor = XMLProcessor(scheme=self.sample_scheme)
        processor.deserialize(self.valid_xml_content)

        # Modify an existing key, and implicitly build up sub-elements through parent tags
        updates = {"verbose": "False", "ats_name": "new_app"}
        success = processor.update_data(updates)

        self.assertTrue(success)
        result = processor.to_dict()
        self.assertEqual(result["verbose"], "False")
        self.assertEqual(result["ats_name"], "new_app")

    def test_update_data_rollback_on_failed_validation(self) -> None:
        """Test that element structures roll back completely if resulting state breaks the scheme."""
        processor = XMLProcessor(scheme=self.sample_scheme)
        processor.deserialize(self.valid_xml_content)

        with patch.object(processor, 'validate_by_scheme', return_value=False):
            success = processor.update_data({"verbose": "ModifiedValue"})
            
            self.assertFalse(success)
            # Reverted structure must reflect initial parsing state perfectly
            self.assertEqual(processor.to_dict()["verbose"], "True")

    def test_to_dict_empty_processor(self) -> None:
        """Test to_dict returns an empty dictionary when no XML payload is parsed."""
        processor = XMLProcessor()
        self.assertEqual(processor.to_dict(), {})

    def test_to_dict_with_scheme(self) -> None:
        """Test dictionary extraction filtered strictly via specified scheme requirements."""
        processor = XMLProcessor(scheme=self.sample_scheme)
        processor.deserialize(self.valid_xml_content)

        result = processor.to_dict()
        expected = {
            "ats_name": "test_app",
            "hostname": "localhost",
            "verbose": "True"
        }
        self.assertEqual(result, expected)

    def test_to_dict_without_scheme(self) -> None:
        """Test dictionary extraction falls back to direct flat children tags if no scheme exists."""
        processor = XMLProcessor(scheme=None)
        raw_xml = "<configuration><key1>val1</key1><key2>val2</key2></configuration>"
        processor.deserialize(raw_xml)

        result = processor.to_dict()
        self.assertEqual(result, {"key1": "val1", "key2": "val2"})

    def test_validate_by_scheme_without_root(self) -> None:
        """Test that validation fails immediately if there is no root element available."""
        processor = XMLProcessor(scheme=self.sample_scheme)
        self.assertFalse(processor.validate_by_scheme())

    def test_validate_by_scheme_without_scheme_returns_true(self) -> None:
        """Test that validation returns True by default when scheme is None."""
        processor = XMLProcessor(scheme=None)
        processor._root = ET.Element("configuration")
        self.assertTrue(processor.validate_by_scheme())

    @patch("ats_utilities.config_io.processor.xml_processor.to_str")
    def test_string_representation(self, mock_to_str: MagicMock) -> None:
        """Test that __str__ delegates representation formatting properly to reflection utilities."""
        processor = XMLProcessor()
        mock_to_str.return_value = "XMLProcessor{root=None}"

        result = str(processor)
        mock_to_str.assert_called_once_with(processor)
        self.assertEqual(result, "XMLProcessor{root=None}")


if __name__ == '__main__':
    unittest.main()
