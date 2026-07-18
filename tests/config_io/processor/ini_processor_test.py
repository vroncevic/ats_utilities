# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from io import StringIO
from configparser import ConfigParser, Error as ConfigParserError

# Adjust imports according to your project structure
from ats_utilities.config_io.processor.ini_processor import INIProcessor


class TestINIProcessor(unittest.TestCase):
    """Unit tests for the INIProcessor class."""

    def setUp(self) -> None:
        """Set up standard schemas and test definitions."""
        self.sample_scheme = {
            "ats_name": "ats_info",
            "ats_version": "ats_info",
            "hostname": "connection"
        }
        self.valid_ini_content = (
            "[ats_info]\n"
            "ats_name = test_app\n"
            "ats_version = 1.0.0\n"
            "[connection]\n"
            "hostname = localhost\n"
        )

    def test_initialization_without_scheme(self) -> None:
        """Test instantiation with no validation scheme provided."""
        processor = INIProcessor()
        self.assertIsInstance(processor._config, ConfigParser)
        self.assertIsNone(processor._scheme)

    def test_initialization_with_scheme(self) -> None:
        """Test instantiation with an explicit validation scheme."""
        processor = INIProcessor(scheme=self.sample_scheme)
        self.assertIsInstance(processor._config, ConfigParser)
        self.assertEqual(processor._scheme, self.sample_scheme)

    def test_deserialize_with_valid_string_content(self) -> None:
        """Test deserialization with a valid INI string payload matching the scheme."""
        processor = INIProcessor(scheme=self.sample_scheme)
        success = processor.deserialize(self.valid_ini_content)

        self.assertTrue(success)
        self.assertEqual(processor._config.get("ats_info", "ats_name"), "test_app")
        self.assertEqual(processor._config.get("connection", "hostname"), "localhost")

    def test_deserialize_with_file_stream(self) -> None:
        """Test deserialization using a file-like text stream (StringIO)."""
        processor = INIProcessor(scheme=self.sample_scheme)
        stream = StringIO(self.valid_ini_content)
        
        success = processor.deserialize(stream)
        self.assertTrue(success)
        self.assertEqual(processor._config.get("ats_info", "ats_version"), "1.0.0")

    def test_deserialize_catches_parsing_errors(self) -> None:
        """Test that deserialization returns False on bad content formats."""
        processor = INIProcessor()
        bad_content = "not_a_section_error = true\n"  # Missing initial section header
        
        success = processor.deserialize(bad_content)
        self.assertFalse(success)

    def test_deserialize_fails_validation_scheme(self) -> None:
        """Test that deserialization reports failure if mandatory scheme sections/options are missing."""
        processor = INIProcessor(scheme=self.sample_scheme)
        incomplete_ini = "[ats_info]\nats_name = test_app\n"  # Missing 'ats_version' and '[connection]'
        
        success = processor.deserialize(incomplete_ini)
        self.assertFalse(success)

    def test_serialize_formats_correctly(self) -> None:
        """Test that serialize exports inner config structure into structured text strings."""
        processor = INIProcessor()
        processor._config.add_section("database")
        processor._config.set("database", "user", "admin")
        
        output = processor.serialize()
        self.assertIn("[database]", output)
        self.assertIn("user = admin", output)

    @patch("configparser.ConfigParser.write")
    def test_serialize_handles_exceptions_safely(self, mock_write: MagicMock) -> None:
        """Test that serialize swallows operational exceptions safely and returns an empty string."""
        processor = INIProcessor()
        mock_write.side_effect = ConfigParserError("Simulated writer block error")
        
        output = processor.serialize()
        self.assertEqual(output, "")

    def test_update_data_with_no_scheme(self) -> None:
        """Test updating data returns False immediately if there is no scheme present."""
        processor = INIProcessor(scheme=None)
        success = processor.update_data({"key": "value"})
        self.assertFalse(success)

    def test_update_data_success_with_scheme(self) -> None:
        """Test updating fields dynamically mapping values under scheduled scheme rules."""
        processor = INIProcessor(scheme=self.sample_scheme)
        processor.deserialize(self.valid_ini_content)

        updates = {"ats_version": "2.0.0", "hostname": "127.0.0.1"}
        success = processor.update_data(updates)

        self.assertTrue(success)
        self.assertEqual(processor._config.get("ats_info", "ats_version"), "2.0.0")
        self.assertEqual(processor._config.get("connection", "hostname"), "127.0.0.1")

    def test_update_data_rollback_on_failed_validation(self) -> None:
        """Test that updates roll back if the resulting structure breaks scheme requirements."""
        processor = INIProcessor(scheme=self.sample_scheme)
        processor.deserialize(self.valid_ini_content)

        # Force validation to fail to check transaction isolation integrity
        with patch.object(processor, 'validate_by_scheme', return_value=False):
            success = processor.update_data({"ats_version": "9.9.9"})
            
            self.assertFalse(success)
            # Verify the value was rolled back to its initial state
            self.assertEqual(processor._config.get("ats_info", "ats_version"), "1.0.0")

    def test_to_dict_empty_config(self) -> None:
        """Test that to_dict returns an empty dictionary when no sections are populated."""
        processor = INIProcessor()
        self.assertEqual(processor.to_dict(), {})

    def test_to_dict_with_scheme(self) -> None:
        """Test dictionary extraction filtered specifically via provided scheme structures."""
        processor = INIProcessor(scheme=self.sample_scheme)
        processor.deserialize(self.valid_ini_content)

        result_dict = processor.to_dict()
        expected = {
            "ats_name": "test_app",
            "ats_version": "1.0.0",
            "hostname": "localhost"
        }
        self.assertEqual(result_dict, expected)

    def test_to_dict_without_scheme(self) -> None:
        """Test dictionary mapping falls back onto exporting the first section if no scheme exists."""
        processor = INIProcessor(scheme=None)
        processor.deserialize("[first_sec]\nkey1 = val1\nkey2 = val2\n[second_sec]\nkey3 = val3")

        result_dict = processor.to_dict()
        # Should cleanly collect items from 'first_sec' only
        self.assertEqual(result_dict, {"key1": "val1", "key2": "val2"})

    def test_validate_by_scheme_without_scheme(self) -> None:
        """Test that validation returns True by default when scheme is None."""
        processor = INIProcessor(scheme=None)
        self.assertTrue(processor.validate_by_scheme())

    def test_validate_by_scheme_missing_options(self) -> None:
        """Test validation tracking when a matching section exists but missing target option keys."""
        processor = INIProcessor(scheme={"missing_key": "ats_info"})
        processor.deserialize("[ats_info]\nats_name = test_app")
        
        self.assertFalse(processor.validate_by_scheme())

    @patch("ats_utilities.config_io.processor.ini_processor.to_str")
    def test_string_representation(self, mock_to_str: MagicMock) -> None:
        """Test that __str__ structural serialization targets generic class converters."""
        processor = INIProcessor()
        mock_to_str.return_value = "INIProcessor{sections=[]}"

        result = str(processor)
        mock_to_str.assert_called_once_with(processor)
        self.assertEqual(result, "INIProcessor{sections=[]}")


if __name__ == '__main__':
    unittest.main()