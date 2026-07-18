# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from collections.abc import Mapping
import yaml

# Adjust imports according to your project structure
from ats_utilities.config_io.processor.yaml_processor import YAMLProcessor


class TestYAMLProcessor(unittest.TestCase):
    """Unit tests for the YAMLProcessor class."""

    def setUp(self) -> None:
        """Set up standard schemas and test definitions."""
        self.sample_scheme = {
            "hostname": "",
            "port": "",
            "verbose": ""
        }
        self.valid_yaml_content = "hostname: localhost\nport: '8080'\nverbose: 'True'\n"

    def test_initialization_without_scheme(self) -> None:
        """Test instantiation with no validation scheme provided."""
        processor = YAMLProcessor()
        self.assertEqual(processor._data, {})
        self.assertIsNone(processor._scheme)

    def test_initialization_with_scheme(self) -> None:
        """Test instantiation with an explicit validation scheme."""
        processor = YAMLProcessor(scheme=self.sample_scheme)
        self.assertEqual(processor._data, {})
        self.assertEqual(processor._scheme, self.sample_scheme)

    def test_deserialize_with_valid_yaml_string(self) -> None:
        """Test deserialization with a valid YAML string that matches the scheme."""
        processor = YAMLProcessor(scheme=self.sample_scheme)
        success = processor.deserialize(self.valid_yaml_content)

        self.assertTrue(success)
        expected_data = {"hostname": "localhost", "port": "8080", "verbose": "True"}
        self.assertEqual(processor.to_dict(), expected_data)

    def test_deserialize_invalid_yaml_format(self) -> None:
        """Test that deserialization catches parsing errors and returns False."""
        processor = YAMLProcessor()
        # Invalid YAML structure with tab indentation or unmatched tokens
        invalid_yaml = "hostname: localhost\n\tport: 8080\n:" 
        
        success = processor.deserialize(invalid_yaml)
        self.assertFalse(success)

    def test_deserialize_fails_validation_scheme(self) -> None:
        """Test that deserialization returns False if mandatory scheme fields are missing."""
        processor = YAMLProcessor(scheme=self.sample_scheme)
        incomplete_yaml = "hostname: localhost\nverbose: 'False'\n"  # Missing 'port'
        
        success = processor.deserialize(incomplete_yaml)
        self.assertFalse(success)

    def test_serialize_formats_correctly(self) -> None:
        """Test that serialize exports inner data to a block-style YAML string."""
        processor = YAMLProcessor()
        processor._data = {"app": "auth", "debug": "false"}
        
        output = processor.serialize()
        # Verify it transforms into valid YAML and defaults to block style formatting
        self.assertIn("app: auth", output)
        self.assertIn("debug: 'false'", output)

    def test_update_data_success(self) -> None:
        """Test updating data fields that conform to the validation rules."""
        processor = YAMLProcessor(scheme=self.sample_scheme)
        processor.deserialize(self.valid_yaml_content)

        updates = {"port": "9000", "verbose": "False"}
        success = processor.update_data(updates)

        self.assertTrue(success)
        self.assertEqual(processor.to_dict()["port"], "9000")
        self.assertEqual(processor.to_dict()["verbose"], "False")

    def test_update_data_rollback_on_failed_validation(self) -> None:
        """Test that an update rolls back completely if it violates validation requirements."""
        processor = YAMLProcessor(scheme=self.sample_scheme)
        processor.deserialize(self.valid_yaml_content)

        # Patch validate_by_scheme to simulate an invalid payload configuration response
        with patch.object(processor, 'validate_by_scheme', return_value=False):
            success = processor.update_data({"hostname": "new-host", "extra_key": "invalid"})
            
            self.assertFalse(success)
            # Check that the rollback restored original values intact
            self.assertEqual(processor.to_dict()["hostname"], "localhost")
            self.assertNotIn("extra_key", processor.to_dict())

    def test_validate_by_scheme_without_scheme(self) -> None:
        """Test that validation evaluates to True by default when no scheme exists."""
        processor = YAMLProcessor(scheme=None)
        processor._data = {"any_random_key": "any_value"}
        self.assertTrue(processor.validate_by_scheme())

    def test_validate_by_scheme_missing_keys(self) -> None:
        """Test validation tracking when explicit scheme requirements are not met."""
        processor = YAMLProcessor(scheme=self.sample_scheme)
        processor._data = {"hostname": "127.0.0.1"}  # missing port and verbose
        self.assertFalse(processor.validate_by_scheme())

    @patch("ats_utilities.config_io.processor.yaml_processor.to_str")
    def test_string_representation(self, mock_to_str: MagicMock) -> None:
        """Test that __str__ delegates representation parsing properly to reflection utilities."""
        processor = YAMLProcessor()
        mock_to_str.return_value = "YAMLProcessor{data={}}"

        result = str(processor)
        mock_to_str.assert_called_once_with(processor)
        self.assertEqual(result, "YAMLProcessor{data={}}")


if __name__ == '__main__':
    unittest.main()
