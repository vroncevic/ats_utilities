# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch

# Adjust imports according to your project structure
from ats_utilities.config_io.processor.cfg_processor import CFGProcessor


class TestCFGProcessor(unittest.TestCase):
    """Unit tests for the CFGProcessor class."""

    def setUp(self) -> None:
        """Set up dynamic schemas and test definitions."""
        self.sample_scheme = {
            "hostname": "",
            "port": "",
            "verbose": ""
        }
        self.valid_raw_content = "hostname = localhost\nport = 8080\nverbose = True\n"

    def test_initialization_without_scheme(self) -> None:
        """Test instantiation with no validation scheme provided."""
        processor = CFGProcessor()
        self.assertEqual(processor._data, {})
        self.assertIsNone(processor._scheme)

    def test_initialization_with_scheme(self) -> None:
        """Test instantiation with an explicit validation scheme."""
        processor = CFGProcessor(scheme=self.sample_scheme)
        self.assertEqual(processor._data, {})
        self.assertEqual(processor._scheme, self.sample_scheme)

    def test_deserialize_with_valid_string_content(self) -> None:
        """Test deserialization with valid key-value pairs formatted as a string."""
        processor = CFGProcessor(scheme=self.sample_scheme)
        success = processor.deserialize(self.valid_raw_content)

        self.assertTrue(success)
        expected_data = {"hostname": "localhost", "port": "8080", "verbose": "True"}
        self.assertEqual(processor.to_dict(), expected_data)

    def test_deserialize_with_list_of_lines(self) -> None:
        """Test deserialization when content is provided as an iterable sequence of lines."""
        processor = CFGProcessor(scheme=self.sample_scheme)
        lines = ["hostname=127.0.0.1", "port=9000", "verbose=False"]
        
        success = processor.deserialize(lines)
        
        self.assertTrue(success)
        self.assertEqual(processor.to_dict()["hostname"], "127.0.0.1")
        self.assertEqual(processor.to_dict()["port"], "9000")

    def test_deserialize_skips_empty_lines_and_whitespace(self) -> None:
        """Test that lines containing only whitespace or invalid characters are ignored."""
        processor = CFGProcessor()
        content_with_spaces = "\n   \nkey_one = value_one\n\n"
        
        processor.deserialize(content_with_spaces)
        self.assertEqual(processor.to_dict(), {"key_one": "value_one"})

    def test_deserialize_fails_validation_scheme(self) -> None:
        """Test that deserialization reports failure if mandatory schema fields are missing."""
        processor = CFGProcessor(scheme=self.sample_scheme)
        incomplete_content = "hostname = localhost\nverbose = False\n"
        
        success = processor.deserialize(incomplete_content)
        self.assertFalse(success)
        # Data is still parsed organically even if validation fails
        self.assertIn("hostname", processor.to_dict())
        self.assertNotIn("port", processor.to_dict())

    def test_serialize_formats_correctly(self) -> None:
        """Test that serialize exports inner definitions back into clear key-value lines."""
        processor = CFGProcessor()
        processor._data = {"domain": "example.com", "secure": "yes"}
        
        output = processor.serialize()
        # Order is preserved from internal dictionary sequence
        self.assertEqual(output, "domain = example.com\nsecure = yes\n")

    def test_update_data_success(self) -> None:
        """Test updating data fields conforming perfectly with validation rules."""
        processor = CFGProcessor(scheme=self.sample_scheme)
        processor.deserialize(self.valid_raw_content)

        updates = {"port": "443", "verbose": "False"}
        success = processor.update_data(updates)

        self.assertTrue(success)
        self.assertEqual(processor.to_dict()["port"], "443")
        self.assertEqual(processor.to_dict()["verbose"], "False")

    def test_update_data_rollback_on_failed_validation(self) -> None:
        """Test that an update rolls back completely if it violates validation requirements."""
        # Custom scheme needing a strict parameter
        strict_scheme = {"required_key": ""}
        processor = CFGProcessor(scheme=strict_scheme)
        processor._data = {"required_key": "original_val"}

        # Perform update that drops or fails criteria via mock patch
        with patch.object(processor, 'validate_by_scheme', return_value=False):
            success = processor.update_data({"required_key": "changed_val", "extra": "data"})
            
            self.assertFalse(success)
            # Ensure rollback reverted state to what it was initially
            self.assertEqual(processor.to_dict(), {"required_key": "original_val"})

    def test_validate_by_scheme_without_scheme(self) -> None:
        """Test that validation evaluates to True by default when no scheme exists."""
        processor = CFGProcessor(scheme=None)
        processor._data = {"arbitrary_field": "value"}
        self.assertTrue(processor.validate_by_scheme())

    def test_validate_by_scheme_missing_keys(self) -> None:
        """Test validation tracking when explicit scheme mandates are missing."""
        processor = CFGProcessor(scheme=self.sample_scheme)
        processor._data = {"hostname": "localhost"}  # missing port and verbose
        self.assertFalse(processor.validate_by_scheme())

    @patch("ats_utilities.config_io.processor.cfg_processor.to_str")
    def test_string_representation(self, mock_to_str: MagicMock) -> None:
        """Test that __str__ delegates representation parsing properly to reflection utilities."""
        processor = CFGProcessor()
        mock_to_str.return_value = "CFGProcessor{data={}}"

        result = str(processor)
        mock_to_str.assert_called_once_with(processor)
        self.assertEqual(result, "CFGProcessor{data={}}")


if __name__ == '__main__':
    unittest.main()