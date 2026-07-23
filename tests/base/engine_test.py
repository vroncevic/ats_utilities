# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch
from typing import Any, override

# Adjust imports according to your project structure
from ats_utilities.base.engine import Base
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.info.iinfo_manager import IInfoManager
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.generator.igenerator import IGenerator


class ConcreteBase(Base):
    """A concrete implementation of the abstract Base class for testing purposes."""
    
    @override
    def process(self, verbose: bool = False) -> bool:
        return True


class TestBaseEngine(unittest.TestCase):
    """Unit tests for the Base orchestrator engine class."""

    def setUp(self) -> None:
        """Set up standard context and component bundle mocks."""
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_loader = MagicMock(spec=ILoader)
        
        # Core sub-managers
        self.mock_info_manager = MagicMock(spec=IInfoManager)
        self.mock_splasher = MagicMock(spec=ISplasher)
        self.mock_options_parser = MagicMock(spec=IOptionManager)
        self.mock_generator = MagicMock(spec=IGenerator)

        # By default, configure components to report they are initialized
        self.mock_info_manager.is_initialized.return_value = True
        self.mock_splasher.is_initialized.return_value = True
        self.mock_options_parser.is_initialized.return_value = True
        self.mock_generator.is_initialized.return_value = True

        # Build mock configuration BaseBundle
        self.mock_bundle = MagicMock(spec=BaseBundle)
        self.mock_bundle.context_bundle = self.mock_context
        self.mock_bundle.config_loader = self.mock_loader
        self.mock_bundle.info_manager = self.mock_info_manager
        self.mock_bundle.splasher = self.mock_splasher
        self.mock_bundle.options_parser = self.mock_options_parser
        self.mock_bundle.generator = self.mock_generator
        self.mock_bundle.use_generator = False

    def test_initialization_success_without_generator(self) -> None:
        """Test successful initialization and readiness flags when the generator is disabled."""
        self.mock_bundle.use_generator = False
        
        base_instance = ConcreteBase(self.mock_bundle)

        self.assertEqual(base_instance.get_context(), self.mock_context)
        self.assertTrue(base_instance.is_initialized())
        
        # Verify generator was not checked or bound
        self.assertFalse(hasattr(base_instance, "_generator"))

    def test_initialization_success_with_generator(self) -> None:
        """Test successful initialization and readiness verification when the generator is enabled."""
        self.mock_bundle.use_generator = True
        
        base_instance = ConcreteBase(self.mock_bundle)

        self.assertEqual(base_instance._generator, self.mock_generator)
        self.mock_generator.is_initialized.assert_called_once()
        self.assertTrue(base_instance.is_initialized())

    def test_initialization_fails_when_component_uninitialized(self) -> None:
        """Test that if any sub-component is uninitialized, the engine reports uninitialized."""
        self.mock_info_manager.is_initialized.return_value = False
        
        base_instance = ConcreteBase(self.mock_bundle)
        self.assertFalse(base_instance.is_initialized())

    def test_initialization_invalid_bundle(self) -> None:
        """Test validation check faults when passing an invalid configuration bundle type."""
        with self.assertRaises(Exception):
            ConcreteBase(None)  # type: ignore

        with self.assertRaises(Exception):
            ConcreteBase(MagicMock())  # type: ignore

    def test_add_new_option_delegation(self) -> None:
        """Test that add_new_option properly forwards operational options to the option parser."""
        base_instance = ConcreteBase(self.mock_bundle)
        
        base_instance.add_new_option("-v", "--version", action="store_true")
        self.mock_options_parser.add_operation.assert_called_once_with(
            "-v", "--version", action="store_true"
        )

    def test_add_new_option_skipped_when_uninitialized(self) -> None:
        """Test that option registration is skipped if the engine is uninitialized."""
        self.mock_info_manager.is_initialized.return_value = False
        base_instance = ConcreteBase(self.mock_bundle)
        
        base_instance.add_new_option("-f", "--force")
        self.mock_options_parser.add_operation.assert_not_called()

    def test_parse_args_delegation(self) -> None:
        """Test that parse_args delegates argument parsing to the inner option manager."""
        base_instance = ConcreteBase(self.mock_bundle)
        mock_namespace = MagicMock(spec=OptionNamespace)
        self.mock_options_parser.parse_args.return_value = mock_namespace

        argv = ["--verbose", "run"]
        result = base_instance.parse_args(argv)

        self.mock_options_parser.parse_args.assert_called_once_with(argv)
        self.assertEqual(result, mock_namespace)

    def test_parse_args_returns_none_when_uninitialized(self) -> None:
        """Test that argument parsing instantly returns None if the engine is uninitialized."""
        self.mock_info_manager.is_initialized.return_value = False
        base_instance = ConcreteBase(self.mock_bundle)

        result = base_instance.parse_args(["--help"])
        self.assertIsNone(result)
        self.mock_options_parser.parse_args.assert_not_called()

    @patch("ats_utilities.base.engine.to_str")
    def test_string_representation(self, mock_to_str: MagicMock) -> None:
        """Test reflection serialization mappings upon string requests."""
        base_instance = ConcreteBase(self.mock_bundle)
        mock_to_str.return_value = "Base{_is_initialized=True}"

        result = str(base_instance)

        mock_to_str.assert_called_once_with(base_instance)
        self.assertEqual(result, "Base{_is_initialized=True}")


if __name__ == '__main__':
    unittest.main()
