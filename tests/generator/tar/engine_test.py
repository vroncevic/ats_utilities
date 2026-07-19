# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch, mock_open
from tarfile import TarFile, TarInfo
from typing import Any

# Adjust imports according to your project structure
from ats_utilities.generator.tar.engine import TarProcessor
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.generator.tar.tar_process_bundle import TarProcessBundle
from ats_utilities.generator.tar.tar_process_member_bundle import TarProcessMemberBundle
from ats_utilities.exceptions import ATSGeneratorError


class TestTarProcessor(unittest.TestCase):
    """Unit tests for the TarProcessor engine class."""

    def setUp(self) -> None:
        """Set up standard mocked dependencies for TarProcessor test instances."""
        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.mock_template_processor = MagicMock(spec=ITemplateProcessor)
        
        # Valid bundles
        self.mock_member_bundle = MagicMock(spec=TarProcessMemberBundle)
        self.mock_member_bundle.vals = {"name": "test"}
        self.mock_member_bundle.dest_full_path = "/target/path/file.txt"
        self.mock_member_bundle.member = MagicMock(spec=TarInfo)
        self.mock_member_bundle.tar = MagicMock(spec=TarFile)

        self.mock_process_bundle = MagicMock(spec=TarProcessBundle)
        self.mock_process_bundle.target_dir = "/target/dir"
        self.mock_process_bundle.archive_path = "/archive.tgz"
        self.mock_process_bundle.source_dir = "templates"
        self.mock_process_bundle.exclude_patterns = []
        self.mock_process_bundle.path_replacements = {}
        self.mock_process_bundle.vals = {"key": "value"}

    def test_initialization_success(self) -> None:
        """Test successful instantiation and property alignment."""
        processor = TarProcessor(self.mock_context_bundle, self.mock_template_processor)
        
        self.assertEqual(processor._template_processor, self.mock_template_processor)

    def test_initialization_invalid_template_processor(self) -> None:
        """Test initialization failure when template processor validation fails."""
        with self.assertRaises(Exception):
            TarProcessor(self.mock_context_bundle, None)  # type: ignore

        with self.assertRaises(Exception):
            TarProcessor(self.mock_context_bundle, MagicMock())  # type: ignore

    @patch("ats_utilities.generator.tar.engine.makedirs")
    def test_process_tar_member_directory(self, mock_makedirs: MagicMock) -> None:
        """Test that process_tar_member constructs directory layouts for directory members."""
        processor = TarProcessor(self.mock_context_bundle, self.mock_template_processor)
        self.mock_member_bundle.member.isdir.return_value = True
        self.mock_member_bundle.member.isfile.return_value = False

        processor.process_tar_member(self.mock_member_bundle)

        mock_makedirs.assert_called_once_with("/target/path/file.txt", exist_ok=True)

    @patch("ats_utilities.generator.tar.engine.write_content")
    @patch("ats_utilities.generator.tar.engine.makedirs")
    def test_process_tar_member_file(
        self, mock_makedirs: MagicMock, mock_write: MagicMock
    ) -> None:
        """Test file member extraction, placeholder substitution, and content execution."""
        processor = TarProcessor(self.mock_context_bundle, self.mock_template_processor)
        self.mock_member_bundle.member.isdir.return_value = False
        self.mock_member_bundle.member.isfile.return_value = True

        mock_f_obj = MagicMock()
        mock_f_obj.read.return_value = b"raw content"
        self.mock_member_bundle.tar.extractfile.return_value = mock_f_obj
        self.mock_template_processor.render.return_value = "rendered content"

        processor.process_tar_member(self.mock_member_bundle)

        mock_makedirs.assert_called_once_with("/target/path", exist_ok=True)
        self.mock_member_bundle.tar.extractfile.assert_called_once_with(self.mock_member_bundle.member)
        self.mock_template_processor.render.assert_called_once_with(b"raw content", {"name": "test"})
        mock_write.assert_called_once_with(
            "/target/path/file.txt",
            "rendered content",
            "tar_processor::process_tar_member(...)",
            "error writing to file /target/path/file.txt"
        )

    def test_process_tar_member_neither_dir_nor_file(self) -> None:
        """Test process_tar_member when member is neither a directory nor a file."""
        processor = TarProcessor(self.mock_context_bundle, self.mock_template_processor)
        self.mock_member_bundle.member.isdir.return_value = False
        self.mock_member_bundle.member.isfile.return_value = False

        # Should exit cleanly without calling extractfile or render
        processor.process_tar_member(self.mock_member_bundle)
        self.mock_member_bundle.tar.extractfile.assert_not_called()

    @patch("ats_utilities.generator.tar.engine.makedirs")
    def test_process_tar_member_file_object_is_none(self, mock_makedirs: MagicMock) -> None:
        """Test process_tar_member when extractfile returns None."""
        processor = TarProcessor(self.mock_context_bundle, self.mock_template_processor)
        self.mock_member_bundle.member.isdir.return_value = False
        self.mock_member_bundle.member.isfile.return_value = True
        self.mock_member_bundle.tar.extractfile.return_value = None

        # Should exit cleanly without calling render
        processor.process_tar_member(self.mock_member_bundle)
        self.mock_template_processor.render.assert_not_called()
        mock_makedirs.assert_called_once_with("/target/path", exist_ok=True)

    @patch("ats_utilities.generator.tar.engine.TarProcessMemberBundle")
    @patch("ats_utilities.generator.tar.engine.open")
    @patch("ats_utilities.generator.tar.engine.normalize_path")
    @patch("ats_utilities.generator.tar.engine.resolve_relative_path")
    @patch("ats_utilities.generator.tar.engine.is_excluded_path")
    @patch("ats_utilities.generator.tar.engine.apply_path_replacements")
    @patch("ats_utilities.generator.tar.engine.makedirs")
    def test_process_success_loop(
        self, mock_makedirs: MagicMock, mock_apply_repl: MagicMock,
        mock_is_excluded: MagicMock, mock_resolve_rel: MagicMock, mock_normalize: MagicMock,
        mock_tar_open: MagicMock, mock_member_bundle_cls: MagicMock
    ) -> None:
        """Test an absolute successful execution iteration across archive members."""
        # Arrange
        processor = TarProcessor(self.mock_context_bundle, self.mock_template_processor)
        
        mock_tar_instance = MagicMock()
        mock_member = MagicMock(spec=TarInfo)
        mock_member.name = "templates/file.txt"
        mock_tar_instance.getmembers.return_value = [mock_member]
        mock_tar_open.return_value.__enter__.return_value = mock_tar_instance

        mock_normalize.return_value = "templates/file.txt"
        mock_resolve_rel.return_value = "file.txt"
        mock_is_excluded.return_value = False
        mock_apply_repl.return_value = "substituted_file.txt"

        mock_member_bundle_instance = MagicMock()
        mock_member_bundle_cls.return_value = mock_member_bundle_instance

        with patch.object(processor, "process_tar_member") as mock_process_member:
            # Act
            processor.process(self.mock_process_bundle)

            # Assert
            mock_makedirs.assert_any_call("/target/dir", exist_ok=True)
            mock_tar_open.assert_called_once_with("/archive.tgz", "r:gz")
            mock_process_member.assert_called_once_with(mock_member_bundle_instance)

    @patch("ats_utilities.generator.tar.engine.open")
    @patch("ats_utilities.generator.tar.engine.makedirs")
    def test_process_skips_out_of_scope_or_excluded_paths(
        self, mock_makedirs: MagicMock, mock_tar_open: MagicMock
    ) -> None:
        """Test skipping over file headers when paths are excluded or resolve out-of-scope."""
        processor = TarProcessor(self.mock_context_bundle, self.mock_template_processor)
        
        mock_tar_instance = MagicMock()
        mock_member1 = MagicMock(spec=TarInfo)  # Outside of template dir scope
        mock_member1.name = "outside/path/file.txt"
        mock_member2 = MagicMock(spec=TarInfo)  # Inside but excluded
        mock_member2.name = "templates/excluded_file.txt"
        mock_tar_instance.getmembers.return_value = [mock_member1, mock_member2]
        mock_tar_open.return_value.__enter__.return_value = mock_tar_instance

        with patch("ats_utilities.generator.tar.engine.resolve_relative_path") as mock_resolve, \
             patch("ats_utilities.generator.tar.engine.is_excluded_path", return_value=True), \
             patch.object(processor, "process_tar_member") as mock_process_member:
            
            mock_resolve.side_effect = [None, "excluded_file.txt"]
            
            processor.process(self.mock_process_bundle)
            mock_process_member.assert_not_called()

    @patch("ats_utilities.generator.tar.engine.format_error_raw")
    @patch("ats_utilities.generator.tar.engine.open")
    def test_process_wraps_exceptions_safely(
        self, mock_tar_open: MagicMock, mock_format_error: MagicMock
    ) -> None:
        """Test that operational crashes convert strictly into raised ATSGeneratorError hooks."""
        processor = TarProcessor(self.mock_context_bundle, self.mock_template_processor)
        mock_tar_open.side_effect = RuntimeError("Archive corrupted")
        mock_format_error.return_value = "Formatted error content description"

        with self.assertRaises(ATSGeneratorError):
            processor.process(self.mock_process_bundle)

    def test_is_initialized_delegation(self) -> None:
        """Test initialization flag queries mirror internal render dependencies."""
        processor = TarProcessor(self.mock_context_bundle, self.mock_template_processor)
        
        self.mock_template_processor.is_initialized.return_value = True
        self.assertTrue(processor.is_initialized())

        self.mock_template_processor.is_initialized.return_value = False
        self.assertFalse(processor.is_initialized())

    @patch("ats_utilities.generator.tar.engine.to_str")
    def test_string_representation(self, mock_to_str: MagicMock) -> None:
        """Test reflection serialization mappings upon string requests."""
        processor = TarProcessor(self.mock_context_bundle, self.mock_template_processor)
        mock_to_str.return_value = "TarProcessor{template_processor=ITemplateProcessor}"

        result = str(processor)
        
        mock_to_str.assert_called_once_with(processor)
        self.assertEqual(result, "TarProcessor{template_processor=ITemplateProcessor}")


if __name__ == '__main__':
    unittest.main()
