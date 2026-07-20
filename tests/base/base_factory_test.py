# -*- coding: UTF-8 -*-

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.base.base_factory import BaseFactory
from ats_utilities.base.base_bundle import BaseBundle
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.config_io.loader.engine import Loader
from ats_utilities.info.engine import InfoManager
from ats_utilities.option.engine import OptionManager
from ats_utilities.splasher.engine import Splasher
from ats_utilities.generator.engine import Generator


class TestBaseFactory(unittest.TestCase):
    """Unit tests for the BaseFactory class."""

    def setUp(self) -> None:
        """Set up standard dependencies and mock components for factory testing."""
        self.info_file = "/opt/ats/config/info.json"
        
        # Setup Logger mock that satisfies optional method interfaces
        self.mock_logger = MagicMock()
        self.mock_logger.set_log_file = MagicMock()
        self.mock_logger.stop_buffering = MagicMock()

        self.mock_context_bundle = MagicMock(spec=ContextBundle)
        self.mock_context_bundle.logger = self.mock_logger

        self.config_data = {
            "ats_log_path": "/var/log/ats.log",
            "project_name": "ats_utilities"
        }

    def test_validation_missing_or_none_fields(self) -> None:
        """Test that passing None for required parameters triggers validation errors."""
        with self.assertRaises(Exception):
            BaseFactory.create_default_base_bundle(
                info_file=None,  # type: ignore
                context_bundle=self.mock_context_bundle
            )

        with self.assertRaises(Exception):
            BaseFactory.create_default_base_bundle(
                info_file=self.info_file,
                context_bundle=None,  # type: ignore
            )

    def test_validation_type_mismatches(self) -> None:
        """Test that incorrect types passed into parameters fail validation constraints."""
        with self.assertRaises(Exception):
            BaseFactory.create_default_base_bundle(
                info_file=12345,  # type: ignore
                context_bundle=self.mock_context_bundle
            )

        with self.assertRaises(Exception):
            BaseFactory.create_default_base_bundle(
                info_file=self.info_file,
                context_bundle=MagicMock()  # type: ignore
            )

        with self.assertRaises(Exception):
            BaseFactory.create_default_base_bundle(
                info_file=self.info_file,
                context_bundle=self.mock_context_bundle,
                use_generator="True"  # type: ignore
            )

    @patch("ats_utilities.base.base_factory.BaseBundle")
    @patch("ats_utilities.base.base_factory.Generator")
    @patch("ats_utilities.base.base_factory.GeneratorFactory")
    @patch("ats_utilities.base.base_factory.OptionManager")
    @patch("ats_utilities.base.base_factory.OptionFactory")
    @patch("ats_utilities.base.base_factory.Splasher")
    @patch("ats_utilities.base.base_factory.SplashFactory")
    @patch("ats_utilities.base.base_factory.InfoManager")
    @patch("ats_utilities.base.base_factory.InfoFactory")
    @patch("ats_utilities.base.base_factory.get_first_available")
    @patch("ats_utilities.base.base_factory.Loader")
    @patch("ats_utilities.base.base_factory.ConfigIORegistry")
    def test_create_default_base_bundle_orchestration_without_generator(
        self, mock_cfg_reg: MagicMock, mock_loader_cls: MagicMock,
        mock_get_first: MagicMock, mock_info_reg: MagicMock,
        mock_info_cls: MagicMock, mock_splash_reg: MagicMock,
        mock_splash_cls: MagicMock, mock_opt_reg: MagicMock,
        mock_opt_cls: MagicMock, mock_gen_reg: MagicMock,
        mock_gen_cls: MagicMock, mock_bundle_cls: MagicMock
    ) -> None:
        """Test complete orchestration of external pipelines when use_generator is False."""
        # Arrange Mocks and Instances
        mock_config_bundle = MagicMock()
        mock_cfg_reg.create_config_io_bundle_by_file_path_and_scheme.return_value = mock_config_bundle
        
        mock_loader_inst = MagicMock(spec=Loader)
        mock_loader_inst.load_configuration.return_value = self.config_data
        mock_loader_cls.return_value = mock_loader_inst

        mock_get_first.return_value = "/var/log/ats.log"

        mock_info_bundle = MagicMock()
        mock_info_reg.create_info_bundle_from_dict.return_value = mock_info_bundle
        
        mock_info_inst = MagicMock(spec=InfoManager)
        mock_info_inst.logo = "assets/logo.png"
        mock_info_inst.get_info.return_value = {"meta": "data"}
        mock_info_cls.return_value = mock_info_inst

        mock_splash_bundle = MagicMock()
        mock_splash_reg.create_splash_bundle_from_dict.return_value = mock_splash_bundle
        mock_splash_inst = MagicMock(spec=Splasher)
        mock_splash_cls.return_value = mock_splash_inst

        mock_opt_bundle = MagicMock()
        mock_opt_reg.create_option_bundle_from_dict.return_value = mock_opt_bundle
        mock_opt_inst = MagicMock(spec=OptionManager)
        mock_opt_cls.return_value = mock_opt_inst

        mock_bundle_inst = MagicMock(spec=BaseBundle)
        mock_bundle_cls.return_value = mock_bundle_inst

        # Act
        result = BaseFactory.create_default_base_bundle(
            info_file=self.info_file,
            context_bundle=self.mock_context_bundle,
            use_generator=False
        )

        # Assert Registry Chain Actions
        mock_cfg_reg.create_config_io_bundle_by_file_path_and_scheme.assert_called_once_with(
            file_path=self.info_file, scheme={}, context_bundle=self.mock_context_bundle
        )
        mock_loader_cls.assert_called_once_with(component_bundle=mock_config_bundle)
        mock_loader_inst.load_configuration.assert_called_once()
        mock_get_first.assert_called_once_with(self.config_data, ('ats_log_path', 'ats_log_file'))
        
        # Verify Context Modifications
        self.mock_logger.set_log_file.assert_called_once_with("/var/log/ats.log")
        
        mock_info_reg.create_info_bundle_from_dict.assert_called_once_with(
            info=self.config_data, context_bundle=self.mock_context_bundle
        )
        mock_info_cls.assert_called_once_with(component_bundle=mock_info_bundle)
        
        # Verify Path normalizations for asset directory context shifts
        self.assertEqual(mock_info_inst.logo, "/opt/ats/config/assets/logo.png")

        mock_splash_reg.create_splash_bundle_from_dict.assert_called_once_with(
            prop={"meta": "data"}, context_bundle=self.mock_context_bundle
        )
        mock_splash_cls.assert_called_once_with(component_bundle=mock_splash_bundle)

        mock_opt_reg.create_option_bundle_from_dict.assert_called_once_with(
            parameters={"meta": "data"}, context_bundle=self.mock_context_bundle
        )
        mock_opt_cls.assert_called_once_with(component_bundle=mock_opt_bundle)

        # Generator boundary configurations
        mock_gen_reg.create_default_generator_bundle.assert_not_called()
        mock_gen_cls.assert_not_called()
        self.mock_logger.stop_buffering.assert_called_once()

        mock_bundle_cls.assert_called_once_with(
            info_file=self.info_file,
            config_loader=mock_loader_inst,
            info_manager=mock_info_inst,
            options_parser=mock_opt_inst,
            splasher=mock_splash_inst,
            generator=None,
            use_generator=False,
            context_bundle=self.mock_context_bundle
        )
        self.assertEqual(result, mock_bundle_inst)

    @patch("ats_utilities.base.base_factory.BaseBundle")
    @patch("ats_utilities.base.base_factory.Generator")
    @patch("ats_utilities.base.base_factory.GeneratorFactory")
    @patch("ats_utilities.base.base_factory.OptionManager")
    @patch("ats_utilities.base.base_factory.OptionFactory")
    @patch("ats_utilities.base.base_factory.Splasher")
    @patch("ats_utilities.base.base_factory.SplashFactory")
    @patch("ats_utilities.base.base_factory.InfoManager")
    @patch("ats_utilities.base.base_factory.InfoFactory")
    @patch("ats_utilities.base.base_factory.get_first_available")
    @patch("ats_utilities.base.base_factory.Loader")
    @patch("ats_utilities.base.base_factory.ConfigIORegistry")
    def test_create_default_base_bundle_with_generator_activated(
        self, mock_cfg_reg: MagicMock, mock_loader_cls: MagicMock,
        mock_get_first: MagicMock, mock_info_reg: MagicMock,
        mock_info_cls: MagicMock, mock_splash_reg: MagicMock,
        mock_splash_cls: MagicMock, mock_opt_reg: MagicMock,
        mock_opt_cls: MagicMock, mock_gen_reg: MagicMock,
        mock_gen_cls: MagicMock, mock_bundle_cls: MagicMock
    ) -> None:
        """Test orchestration instantiation pathways when use_generator evaluates to True."""
        # Setup Minimal context maps to bypass prior pipeline validations
        mock_loader_inst = MagicMock(spec=Loader)
        mock_loader_inst.load_configuration.return_value = self.config_data
        mock_loader_cls.return_value = mock_loader_inst

        mock_info_inst = MagicMock(spec=InfoManager)
        mock_info_inst.logo = "assets/logo.png"
        mock_info_cls.return_value = mock_info_inst

        mock_gen_bundle = MagicMock()
        mock_gen_reg.create_default_generator_bundle.return_value = mock_gen_bundle
        mock_gen_inst = MagicMock(spec=Generator)
        mock_gen_cls.return_value = mock_gen_inst

        # Act
        BaseFactory.create_default_base_bundle(
            info_file=self.info_file,
            context_bundle=self.mock_context_bundle,
            use_generator=True
        )

        # Assert Generator bindings are called cleanly
        mock_gen_reg.create_default_generator_bundle.assert_called_once_with(
            context_bundle=self.mock_context_bundle
        )
        mock_gen_cls.assert_called_once_with(component_bundle=mock_gen_bundle)

        mock_bundle_cls.assert_called_once_with(
            info_file=self.info_file,
            config_loader=mock_loader_inst,
            info_manager=mock_info_inst,
            options_parser=mock_opt_cls.return_value,
            splasher=mock_splash_cls.return_value,
            generator=mock_gen_inst,
            use_generator=True,
            context_bundle=self.mock_context_bundle
        )

    @patch("ats_utilities.base.base_factory.Loader")
    @patch("ats_utilities.base.base_factory.ConfigIORegistry")
    @patch("ats_utilities.base.base_factory.InfoFactory")
    @patch("ats_utilities.base.base_factory.InfoManager")
    @patch("ats_utilities.base.base_factory.SplashFactory")
    @patch("ats_utilities.base.base_factory.Splasher")
    @patch("ats_utilities.base.base_factory.OptionFactory")
    @patch("ats_utilities.base.base_factory.OptionManager")
    @patch("ats_utilities.base.base_factory.BaseBundle")
    def test_create_default_base_bundle_logger_without_optional_methods(
        self, mock_bundle_cls: MagicMock, mock_opt_cls: MagicMock,
        mock_opt_reg: MagicMock, mock_splash_cls: MagicMock,
        mock_splash_reg: MagicMock, mock_info_cls: MagicMock,
        mock_info_reg: MagicMock, mock_cfg_reg: MagicMock,
        mock_loader_cls: MagicMock
    ) -> None:
        """Test BaseFactory orchestration when logger lacks set_log_file or stop_buffering."""
        mock_loader_inst = MagicMock(spec=Loader)
        mock_loader_inst.load_configuration.return_value = {}
        mock_loader_cls.return_value = mock_loader_inst
        
        minimal_logger = object() 
        context_bundle = MagicMock(spec=ContextBundle)
        context_bundle.logger = minimal_logger

        mock_info_inst = MagicMock(spec=InfoManager)
        mock_info_inst.logo = "logo.png"
        mock_info_cls.return_value = mock_info_inst
        
        BaseFactory.create_default_base_bundle(
            info_file=self.info_file,
            context_bundle=context_bundle,
            use_generator=False
        )


if __name__ == '__main__':
    unittest.main()
