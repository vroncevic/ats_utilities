# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from collections.abc import Mapping

# Adjust imports according to your project structure
from ats_utilities.config_io.processor.factory_processor import ConfigProcessorFactory
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.config_io.processor.cfg_processor import CFGProcessor
from ats_utilities.config_io.processor.ini_processor import INIProcessor
from ats_utilities.config_io.processor.json_processor import JSONProcessor
from ats_utilities.config_io.processor.xml_processor import XMLProcessor
from ats_utilities.config_io.processor.yaml_processor import YAMLProcessor


class TestConfigProcessorFactory(unittest.TestCase):
    """Unit tests for the ConfigProcessorFactory class."""

    def setUp(self) -> None:
        """Set up standard mocked dependencies for processor resolution."""
        self.mock_scheme = MagicMock(spec=Mapping)
        self.mock_processor = MagicMock(spec=IConfigProcessor)

    def test_get_processor_class_supported_extensions(self) -> None:
        """Test that get_processor_class returns correct processor classes for extensions."""
        extensions_map = {
            ".cfg": CFGProcessor,
            "cfg": CFGProcessor,
            ".ini": INIProcessor,
            "INI": INIProcessor,  # Case insensitivity check
            ".json": JSONProcessor,
            ".xml": XMLProcessor,
            ".yml": YAMLProcessor,
            ".yaml": YAMLProcessor,
        }

        for ext, expected_class in extensions_map.items():
            with self.subTest(ext=ext):
                result = ConfigProcessorFactory.get_processor_class(ext)
                self.assertIs(result, expected_class)

    def test_get_processor_class_unsupported_extension_raises(self) -> None:
        """Test that an unsupported extension raises a validation error."""
        with self.assertRaises(Exception):  # Catches validation exceptions from not_satisfied
            ConfigProcessorFactory.get_processor_class(".invalid_ext")

    def test_create_from_extension_with_injected_processor(self) -> None:
        """Test that create_from_extension immediately returns an injected processor."""
        with patch("ats_utilities.config_io.processor.factory_processor.validate_component") as mock_validate:
            result = ConfigProcessorFactory.create_from_extension(
                processor=self.mock_processor
            )
            mock_validate.assert_called_once_with(
                instance=self.mock_processor,
                expected_class=IConfigProcessor,
                exc_context=r'config_processor_factory::create_from_extension(...)',
                exc_message='provided processor must implement IConfigProcessor'
            )
            self.assertEqual(result, self.mock_processor)

    @patch("ats_utilities.config_io.processor.factory_processor.validate_component")
    @patch("ats_utilities.config_io.processor.factory_processor.make_component")
    def test_create_from_extension_builds_new_component(
        self, mock_make: MagicMock, mock_validate: MagicMock
    ) -> None:
        """Test create_from_extension builds a fresh component when processor is None."""
        # Arrange
        mock_resolved_instance = MagicMock(spec=JSONProcessor)
        mock_make.return_value = mock_resolved_instance
        self.mock_scheme.__len__.return_value = 1

        # Act
        result = ConfigProcessorFactory.create_from_extension(
            extension=".json",
            scheme=self.mock_scheme,
            processor=None
        )

        # Assert
        mock_make.assert_called_once_with(
            passed_obj=None,
            default_class=JSONProcessor,
            factory_args={'scheme': self.mock_scheme}
        )
        mock_validate.assert_called_once_with(
            instance=mock_resolved_instance,
            expected_class=IConfigProcessor,
            exc_context=r'config_processor_factory::create_from_extension(...)',
            exc_message='processor for extension .json must implement IConfigProcessor'
        )
        self.assertEqual(result, mock_resolved_instance)

    def test_create_from_file_path_with_injected_processor(self) -> None:
        """Test create_from_file_path immediately proxies if a processor is supplied."""
        with patch.object(ConfigProcessorFactory, "create_from_extension") as mock_create_ext:
            ConfigProcessorFactory.create_from_file_path(processor=self.mock_processor)
            mock_create_ext.assert_called_once_with(processor=self.mock_processor)

    @patch("ats_utilities.config_io.processor.factory_processor.check_file_exists")
    @patch.object(ConfigProcessorFactory, "create_from_extension")
    def test_create_from_file_path_resolves_suffix(
        self, mock_create_ext: MagicMock, mock_check_exists: MagicMock
    ) -> None:
        """Test create_from_file_path checks file existence and extracts file suffix extension."""
        # Arrange
        file_path = "/path/to/config.yaml"

        # Act
        ConfigProcessorFactory.create_from_file_path(
            file_path=file_path,
            scheme=self.mock_scheme,
            processor=None
        )

        # Assert
        mock_check_exists.assert_called_once_with(
            file_path,
            r'config_processor_factory::create_from_file_path(...)',
            f"file at {file_path} does not exist"
        )
        mock_create_ext.assert_called_once_with(
            extension=".yaml",
            scheme=self.mock_scheme,
            processor=None
        )


if __name__ == "__main__":
    unittest.main()
