# -*- coding: UTF-8 -*-

'''
Module
    ats_bundles_test.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines classes BundlesTestCase and ComponentBundlesTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of parameter bundles.
Execute
    python3 -m unittest -v ats_bundles_test
'''

from unittest import TestCase, main
from unittest.mock import MagicMock
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.config_io.config_loader_bundle import ConfigLoaderBundle
from ats_utilities.config_io.file_bundle import FileBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.logging.logger_bundle import LoggerBundle
from ats_utilities.logging.component_bundle import LoggingComponentBundle
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.base.component_bundle import BaseComponentBundle
from ats_utilities.checker.component_bundle import CheckerComponentBundle
from ats_utilities.checker.checker_reporter_bundle import CheckerReporterBundle
from ats_utilities.info.component_bundle import InfoComponentBundle
from ats_utilities.reporter.component_bundle import ReporterComponentBundle
from ats_utilities.splasher.component_bundle import SplashComponentBundle
from ats_utilities.splasher.splash_center_bundle import SplashCenterBundle
from ats_utilities.generator.component_bundle import GeneratorComponentBundle
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.tar_process_bundle import TarProcessBundle
from ats_utilities.generator.tar_process_member_bundle import TarProcessMemberBundle
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.option.iparser_strategy import IParserStrategy
from ats_utilities.logging.ilogger import ILogger
from ats_utilities.checker.itype_validator import ITypeValidator
from ats_utilities.checker.iformat_validator import IFormatValidator
from ats_utilities.checker.icontext_provider import IContextProvider
from ats_utilities.checker.icheck_reporter import ICheckReporter
from ats_utilities.info.iname import IName
from ats_utilities.info.iversion import IVersion
from ats_utilities.info.ilicence import ILicence
from ats_utilities.info.ibuild_date import IBuildDate
from ats_utilities.info.irepository import IRepository
from ats_utilities.info.iorganization import IOrganization
from ats_utilities.info.iuse_github import IUseGitHub
from ats_utilities.info.ilogo_path import ILogoPath
from ats_utilities.info.iinfo_ok import IInfoOk
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.splasher.isplash_property import ISplashProperty
from ats_utilities.splasher.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.iprogress_bar import IProgressBar
from ats_utilities.generator.ischeme_loader import ISchemeLoader
from ats_utilities.generator.itar_processor import ITarProcessor
from ats_utilities.generator.itemplate_processor import ITemplateProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class BundlesTestCase(TestCase):
    '''
        Defines class BundlesTestCase with attribute(s) and method(s).
        Creates test cases for checking base parameter bundles.

        It defines:

            :methods:
                | test_context_bundle - Test ContextBundle methods.
                | test_context_bundle_validation_errors - Test ContextBundle validation exceptions.
                | test_logger_bundle - Test LoggerBundle methods.
                | test_ats_file_bundle - Test FileBundle methods.
                | test_ats_config_file_bundle - Test ConfigFileBundle methods.
                | test_ats_config_loader_bundle - Test ConfigLoaderBundle methods.
                | test_checker_reporter_bundle - Test CheckerReporterBundle methods.
                | test_checker_reporter_bundle_validation_errors - Test CheckerReporterBundle validation exceptions.
                | test_splash_center_bundle - Test SplashCenterBundle methods.
                | test_splash_center_bundle_validation_errors - Test SplashCenterBundle validation exceptions.
    '''

    def test_context_bundle(self) -> None:
        '''Test ContextBundle methods.'''
        mock_checker = MagicMock(spec=IChecker)
        mock_reporter = MagicMock(spec=IReporter)

        bundle1 = ContextBundle()
        bundle2 = ContextBundle(checker=mock_checker, reporter=mock_reporter, verbose=True)

        # test merge
        bundle1.merge(bundle2)
        self.assertEqual(bundle1.checker, mock_checker)
        self.assertEqual(bundle1.reporter, mock_reporter)
        self.assertTrue(bundle1.verbose)

        # test validate
        bundle1.validate()

        # test to_dict
        d = bundle1.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['checker'], mock_checker)
        self.assertEqual(d['reporter'], mock_reporter)
        self.assertTrue(d['verbose'])

    def test_context_bundle_validation_errors(self) -> None:
        '''Test ContextBundle validation exceptions.'''
        bundle = ContextBundle()
        bundle.checker = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

        bundle = ContextBundle()
        bundle.reporter = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

    def test_logger_bundle(self) -> None:
        '''Test LoggerBundle methods.'''
        bundle1 = LoggerBundle()
        bundle2 = LoggerBundle(name='test_logger', configure_logging=False, log_stdout=False, log_file='test.log')

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.name, 'test_logger')
        self.assertFalse(bundle1.configure_logging)
        self.assertFalse(bundle1.log_stdout)
        self.assertEqual(bundle1.log_file, 'test.log')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['name'], 'test_logger')

    def test_logger_bundle_validation_errors(self) -> None:
        '''Test LoggerBundle validation exceptions.'''
        fields = {
            'name': 'test_logger',
            'configure_logging': True,
            'log_stdout': True,
            'log_file': 'test.log'
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = LoggerBundle(**kwargs)
            with self.assertRaises(ValueError):
                bundle.validate()

        bundle = LoggerBundle(name='test_logger', configure_logging='not_bool', log_file='test.log')
        with self.assertRaises(ValueError):
            bundle.validate()

        bundle = LoggerBundle(name='test_logger', log_stdout='not_bool', log_file='test.log')
        with self.assertRaises(ValueError):
            bundle.validate()

    def test_ats_file_bundle(self) -> None:
        '''Test FileBundle methods.'''
        bundle1 = FileBundle()
        bundle2 = FileBundle(file_path='a.txt', file_mode='w', file_format='txt')

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.file_path, 'a.txt')
        self.assertEqual(bundle1.file_mode, 'w')
        self.assertEqual(bundle1.file_format, 'txt')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['file_path'], 'a.txt')

    def test_ats_file_bundle_validation_errors(self) -> None:
        '''Test FileBundle validation exceptions.'''
        fields = {
            'file_path': 'a.txt',
            'file_mode': 'w',
            'file_format': 'txt'
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = FileBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()

    def test_ats_config_file_bundle(self) -> None:
        '''Test ConfigFileBundle methods.'''
        mock_context = ContextBundle()
        mock_file_checker = MagicMock()
        bundle1 = ConfigFileBundle()
        bundle2 = ConfigFileBundle(context=mock_context, file_checker=mock_file_checker)

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.context, mock_context)
        self.assertEqual(bundle1.file_checker, mock_file_checker)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['context']['verbose'], mock_context.verbose)
        self.assertIsInstance(d['context']['checker'], type(mock_context.checker))
        self.assertIsInstance(d['context']['reporter'], type(mock_context.reporter))

    def test_ats_config_file_bundle_validation_errors(self) -> None:
        '''Test ConfigFileBundle validation exceptions.'''
        mock_context = ContextBundle()
        mock_file_checker = MagicMock()
        fields = {
            'context': mock_context,
            'file_checker': mock_file_checker
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = ConfigFileBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()

    def test_ats_config_loader_bundle(self) -> None:
        '''Test ConfigLoaderBundle methods.'''
        mock_config2object = MagicMock()
        mock_config_bundle = MagicMock()
        mock_processor = MagicMock()
        bundle1 = ConfigLoaderBundle()
        bundle2 = ConfigLoaderBundle(
            info_file='config.json',
            config2object=mock_config2object,
            config_bundle=mock_config_bundle,
            processor=mock_processor
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.info_file, 'config.json')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['info_file'], 'config.json')

    def test_ats_config_loader_bundle_validation_errors(self) -> None:
        '''Test ConfigLoaderBundle validation exceptions.'''
        mock_config2object = MagicMock()
        mock_config_bundle = MagicMock()
        mock_processor = MagicMock()
        fields = {
            'info_file': 'config.json',
            'config2object': mock_config2object,
            'config_bundle': mock_config_bundle,
            'processor': mock_processor
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = ConfigLoaderBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()

    def test_checker_reporter_bundle(self) -> None:
        '''Test CheckerReporterBundle methods.'''
        bundle1 = CheckerReporterBundle()
        bundle2 = CheckerReporterBundle(context='some_context', parameters_meta=[], err_indices=[1, 2], is_fmt_err=True)

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.context, 'some_context')
        self.assertEqual(bundle1.parameters_meta, [])
        self.assertEqual(bundle1.err_indices, [1, 2])
        self.assertTrue(bundle1.is_fmt_err)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['context'], 'some_context')

    def test_checker_reporter_bundle_validation_errors(self) -> None:
        '''Test CheckerReporterBundle validation exceptions.'''
        bundle = CheckerReporterBundle(context=None, parameters_meta=[])
        with self.assertRaises(ValueError):
            bundle.validate()

        bundle = CheckerReporterBundle(context='ctx')
        bundle.parameters_meta = None
        with self.assertRaises(ValueError):
            bundle.validate()

    def test_splash_center_bundle(self) -> None:
        '''Test SplashCenterBundle methods.'''
        bundle1 = SplashCenterBundle()
        bundle2 = SplashCenterBundle(columns=80, additional_shifter=2, text='Welcome')

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.columns, 80)
        self.assertEqual(bundle1.additional_shifter, 2)
        self.assertEqual(bundle1.text, 'Welcome')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['text'], 'Welcome')

    def test_splash_center_bundle_validation_errors(self) -> None:
        '''Test SplashCenterBundle validation exceptions.'''
        # columns type error
        bundle = SplashCenterBundle(columns='not_int', additional_shifter=2, text='ok')
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        # columns value error
        bundle = SplashCenterBundle(columns=80, additional_shifter=2, text='ok')
        bundle.columns = -1
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # additional_shifter type error
        bundle = SplashCenterBundle(columns=80, additional_shifter='not_int', text='ok')
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        # additional_shifter value error
        bundle = SplashCenterBundle(columns=80, additional_shifter=2, text='ok')
        bundle.additional_shifter = -1
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # text type error
        bundle = SplashCenterBundle(columns=80, additional_shifter=2, text=123)  # type: ignore
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        # text value error (empty string)
        bundle = SplashCenterBundle(columns=80, additional_shifter=2, text='   ')
        with self.assertRaises(ATSValueError):
            bundle.validate()


class ComponentBundlesTestCase(TestCase):
    '''
        Defines class ComponentBundlesTestCase with attribute(s) and method(s).
        Creates test cases for checking component bundles.

        It defines:

            :methods:
                | test_logging_component_bundle - Test LoggingComponentBundle methods.
                | test_option_component_bundle - Test OptionComponentBundle methods.
                | test_option_component_bundle_validation_errors - Test OptionComponentBundle validation exceptions.
                | test_base_component_bundle - Test BaseComponentBundle methods.
                | test_base_component_bundle_validation_errors - Test BaseComponentBundle validation exceptions.
                | test_checker_component_bundle - Test CheckerComponentBundle methods.
                | test_info_component_bundle - Test InfoComponentBundle methods.
                | test_info_component_bundle_validation_errors - Test InfoComponentBundle validation exceptions.
                | test_reporter_component_bundle - Test ReporterComponentBundle methods.
                | test_reporter_component_bundle_validation_errors - Test ReporterComponentBundle validation exceptions.
                | test_splash_component_bundle - Test SplashComponentBundle methods.
                | test_splash_component_bundle_validation_errors - Test SplashComponentBundle validation exceptions.
    '''

    def test_logging_component_bundle(self) -> None:
        '''Test LoggingComponentBundle methods.'''
        mock_logger = MagicMock(spec=ILogger)
        mock_logger_bundle = LoggerBundle()
        mock_context = ContextBundle()
        bundle1 = LoggingComponentBundle()
        bundle2 = LoggingComponentBundle(
            logger=mock_logger,
            logger_bundle=mock_logger_bundle,
            context_bundle=mock_context
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.logger, mock_logger)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['logger'], mock_logger)

    def test_logging_component_bundle_validation_errors(self) -> None:
        '''Test LoggingComponentBundle validation exceptions.'''
        mock_logger = MagicMock(spec=ILogger)
        mock_logger_bundle = LoggerBundle()
        mock_context = ContextBundle()

        fields = {
            'logger': mock_logger,
            'logger_bundle': mock_logger_bundle,
            'context_bundle': mock_context
        }

        for field in fields:
            bundle = LoggingComponentBundle(
                logger=mock_logger,
                logger_bundle=mock_logger_bundle,
                context_bundle=mock_context
            )
            setattr(bundle, field, None)
            with self.assertRaises(ATSValueError):
                bundle.validate()

    def test_option_component_bundle(self) -> None:
        '''Test OptionComponentBundle methods.'''
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_context = ContextBundle()

        bundle1 = OptionComponentBundle()
        bundle2 = OptionComponentBundle(parameters={'a': 'b'}, strategy=mock_strategy, context_bundle=mock_context)

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.parameters, {'a': 'b'})
        self.assertEqual(bundle1.strategy, mock_strategy)
        self.assertEqual(bundle1.context_bundle, mock_context)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['parameters'], {'a': 'b'})

    def test_option_component_bundle_validation_errors(self) -> None:
        '''Test OptionComponentBundle validation exceptions.'''
        mock_strategy = MagicMock(spec=IParserStrategy)
        mock_context = ContextBundle()

        # Missing parameters
        bundle = OptionComponentBundle(parameters={'a': 'b'}, strategy=mock_strategy, context_bundle=mock_context)
        bundle.parameters = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # Missing strategy
        bundle = OptionComponentBundle(parameters={'a': 'b'}, strategy=mock_strategy, context_bundle=mock_context)
        bundle.strategy = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # Missing context_bundle
        bundle = OptionComponentBundle(parameters={'a': 'b'}, strategy=mock_strategy, context_bundle=mock_context)
        bundle.context_bundle = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

    def test_base_component_bundle(self) -> None:
        '''Test BaseComponentBundle methods.'''
        bundle1 = BaseComponentBundle()
        bundle2 = BaseComponentBundle(info_file='config_file')

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.info_file, 'config_file')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['info_file'], 'config_file')

    def test_base_component_bundle_validation_errors(self) -> None:
        '''Test BaseComponentBundle validation exceptions.'''
        bundle = BaseComponentBundle(info_file=None)
        with self.assertRaises(ValueError):
            bundle.validate()

    def test_checker_component_bundle(self) -> None:
        '''Test CheckerComponentBundle methods.'''
        mock_format_validator = MagicMock(spec=IFormatValidator)
        mock_type_validator = MagicMock(spec=ITypeValidator)
        mock_context_provider = MagicMock(spec=IContextProvider)
        mock_check_reporter = MagicMock(spec=ICheckReporter)

        bundle1 = CheckerComponentBundle()
        bundle2 = CheckerComponentBundle(
            format_validator=mock_format_validator,
            type_validator=mock_type_validator,
            context_provider=mock_context_provider,
            check_reporter=mock_check_reporter
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.format_validator, mock_format_validator)
        self.assertEqual(bundle1.type_validator, mock_type_validator)
        self.assertEqual(bundle1.context_provider, mock_context_provider)
        self.assertEqual(bundle1.check_reporter, mock_check_reporter)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['format_validator'], mock_format_validator)

    def test_checker_component_bundle_validation_errors(self) -> None:
        '''Test CheckerComponentBundle validation exceptions.'''
        mock_format_validator = MagicMock(spec=IFormatValidator)
        mock_type_validator = MagicMock(spec=ITypeValidator)
        mock_context_provider = MagicMock(spec=IContextProvider)
        mock_check_reporter = MagicMock(spec=ICheckReporter)

        fields = {
            'format_validator': mock_format_validator,
            'type_validator': mock_type_validator,
            'context_provider': mock_context_provider,
            'check_reporter': mock_check_reporter
        }

        for field in fields:
            bundle = CheckerComponentBundle(**fields)
            setattr(bundle, field, None)
            with self.assertRaises(ValueError):
                bundle.validate()

    def test_info_component_bundle(self) -> None:
        '''Test InfoComponentBundle methods.'''
        mock_name = MagicMock(spec=IName)
        mock_version = MagicMock(spec=IVersion)
        mock_licence = MagicMock(spec=ILicence)
        mock_build_date = MagicMock(spec=IBuildDate)
        mock_repository = MagicMock(spec=IRepository)
        mock_organization = MagicMock(spec=IOrganization)
        mock_use_github = MagicMock(spec=IUseGitHub)
        mock_logo_path = MagicMock(spec=ILogoPath)
        mock_info_ok = MagicMock(spec=IInfoOk)

        bundle = InfoComponentBundle(
            name=mock_name,
            version=mock_version,
            licence=mock_licence,
            build_date=mock_build_date,
            repository=mock_repository,
            organization=mock_organization,
            use_github=mock_use_github,
            logo_path=mock_logo_path,
            info_ok=mock_info_ok
        )

        bundle.validate()
        d = bundle.to_dict()
        self.assertEqual(d['name'], mock_name)

        # Test merge
        bundle1 = InfoComponentBundle()
        bundle1.merge(bundle)
        self.assertEqual(bundle1.name, mock_name)
        self.assertEqual(bundle1.version, mock_version)

    def test_info_component_bundle_validation_errors(self) -> None:
        '''Test InfoComponentBundle validation exceptions.'''
        mock_name = MagicMock(spec=IName)
        mock_version = MagicMock(spec=IVersion)
        mock_licence = MagicMock(spec=ILicence)
        mock_build_date = MagicMock(spec=IBuildDate)
        mock_repository = MagicMock(spec=IRepository)
        mock_organization = MagicMock(spec=IOrganization)
        mock_use_github = MagicMock(spec=IUseGitHub)
        mock_logo_path = MagicMock(spec=ILogoPath)
        mock_info_ok = MagicMock(spec=IInfoOk)

        fields = {
            'name': mock_name,
            'version': mock_version,
            'licence': mock_licence,
            'build_date': mock_build_date,
            'repository': mock_repository,
            'organization': mock_organization,
            'use_github': mock_use_github,
            'logo_path': mock_logo_path,
            'info_ok': mock_info_ok
        }

        # Test each required field missing raises ValueError
        for field in fields:
            bundle = InfoComponentBundle(**fields)
            setattr(bundle, field, None)
            with self.assertRaises(ValueError):
                bundle.validate()

    def test_reporter_component_bundle(self) -> None:
        '''Test ReporterComponentBundle methods.'''
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)
        bundle1 = ReporterComponentBundle()
        bundle2 = ReporterComponentBundle(checker=mock_checker, theme=mock_theme)

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.checker, mock_checker)
        self.assertEqual(bundle1.theme, mock_theme)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['checker'], mock_checker)

    def test_reporter_component_bundle_validation_errors(self) -> None:
        '''Test ReporterComponentBundle validation exceptions.'''
        mock_checker = MagicMock(spec=IChecker)
        mock_theme = MagicMock(spec=IConsoleTheme)

        # Missing checker
        bundle = ReporterComponentBundle()
        bundle.checker = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # Missing theme
        bundle = ReporterComponentBundle()
        bundle.theme = None
        with self.assertRaises(ATSValueError):
            bundle.validate()

    def test_splash_component_bundle(self) -> None:
        '''Test SplashComponentBundle methods.'''
        mock_splash_prop = MagicMock(spec=ISplashProperty)
        mock_term_prop = MagicMock(spec=ITerminalProperties)
        mock_github = MagicMock(spec=IExtInfrastructure)
        mock_ext = MagicMock(spec=IExtInfrastructure)
        mock_pb = MagicMock(spec=IProgressBar)
        mock_context = ContextBundle()

        bundle1 = SplashComponentBundle()
        bundle2 = SplashComponentBundle(
            prop={'a': 'b'},
            splash_property=mock_splash_prop,
            terminal_property=mock_term_prop,
            github=mock_github,
            ext=mock_ext,
            pb=mock_pb,
            context_bundle=mock_context
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.prop, {'a': 'b'})

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['prop'], {'a': 'b'})

    def test_splash_component_bundle_validation_errors(self) -> None:
        '''Test SplashComponentBundle validation exceptions.'''
        mock_splash_prop = MagicMock(spec=ISplashProperty)
        mock_term_prop = MagicMock(spec=ITerminalProperties)
        mock_github = MagicMock(spec=IExtInfrastructure)
        mock_ext = MagicMock(spec=IExtInfrastructure)
        mock_pb = MagicMock(spec=IProgressBar)
        mock_context = ContextBundle()

        fields = {
            'prop': {'enabled': False},
            'splash_property': mock_splash_prop,
            'terminal_property': mock_term_prop,
            'github': mock_github,
            'ext': mock_ext,
            'pb': mock_pb,
            'context_bundle': mock_context
        }

        for field in fields:
            bundle = SplashComponentBundle(**fields)
            setattr(bundle, field, None)
            with self.assertRaises(ValueError):
                bundle.validate()

    def test_generator_component_bundle(self) -> None:
        '''Test GeneratorComponentBundle methods.'''
        mock_scheme_loader = MagicMock(spec=ISchemeLoader)
        mock_tar_processor = MagicMock(spec=ITarProcessor)
        mock_template_processor = MagicMock(spec=ITemplateProcessor)
        mock_context_bundle = ContextBundle()

        bundle1 = GeneratorComponentBundle()
        bundle2 = GeneratorComponentBundle(
            scheme_loader=mock_scheme_loader,
            tar_processor=mock_tar_processor,
            template_processor=mock_template_processor,
            context_bundle=mock_context_bundle
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.scheme_loader, mock_scheme_loader)
        self.assertEqual(bundle1.tar_processor, mock_tar_processor)
        self.assertEqual(bundle1.template_processor, mock_template_processor)
        self.assertEqual(bundle1.context_bundle, mock_context_bundle)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['scheme_loader'], mock_scheme_loader)

    def test_generator_component_bundle_validation_errors(self) -> None:
        '''Test GeneratorComponentBundle validation exceptions.'''
        mock_scheme_loader = MagicMock(spec=ISchemeLoader)
        mock_tar_processor = MagicMock(spec=ITarProcessor)
        mock_template_processor = MagicMock(spec=ITemplateProcessor)
        mock_context_bundle = ContextBundle()

        fields = {
            'scheme_loader': mock_scheme_loader,
            'tar_processor': mock_tar_processor,
            'template_processor': mock_template_processor,
            'context_bundle': mock_context_bundle
        }

        for field in fields:
            bundle = GeneratorComponentBundle(
                scheme_loader=mock_scheme_loader,
                tar_processor=mock_tar_processor,
                template_processor=mock_template_processor,
                context_bundle=mock_context_bundle
            )
            setattr(bundle, field, None)
            with self.assertRaises(ATSValueError):
                bundle.validate()

    def test_generator_bundle_methods(self) -> None:
        '''Test GeneratorBundle methods.'''
        bundle1 = GeneratorBundle(
            archive_path='a.tgz',
            target_dir='tmp',
            template_key='key',
            scheme={},
            template_values={}
        )
        bundle2 = GeneratorBundle(
            archive_path='b.tgz',
            target_dir='out',
            template_key='key2',
            scheme={'a': 'b'},
            template_values={'x': 'y'}
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.archive_path, 'b.tgz')
        self.assertEqual(bundle1.target_dir, 'out')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['archive_path'], 'b.tgz')

    def test_generator_bundle_validation_errors(self) -> None:
        '''Test GeneratorBundle validation exceptions.'''
        # Missing values (None)
        fields = {
            'archive_path': 'a.tgz',
            'target_dir': 'tmp',
            'template_key': 'key',
            'scheme': {},
            'template_values': {}
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = GeneratorBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()

        # Type errors
        type_checks = {
            'archive_path': 123,
            'target_dir': 123,
            'template_key': 123,
            'scheme': 123,
            'template_values': 123
        }
        for field, invalid_val in type_checks.items():
            kwargs = fields.copy()
            kwargs[field] = invalid_val
            bundle = GeneratorBundle(**kwargs)
            with self.assertRaises(ATSTypeError):
                bundle.validate()

    def test_tar_process_bundle(self) -> None:
        '''Test TarProcessBundle methods.'''
        bundle1 = TarProcessBundle(
            archive_path='a.tgz',
            target_dir='tmp',
            source_dir='src',
            path_replacements={},
            exclude_patterns=[],
            vals={}
        )
        bundle2 = TarProcessBundle(
            archive_path='b.tgz',
            target_dir='out',
            source_dir='src2',
            path_replacements={'x': 'y'},
            exclude_patterns=['*.py'],
            vals={'k': 'v'}
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.archive_path, 'b.tgz')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['archive_path'], 'b.tgz')

    def test_tar_process_bundle_validation_errors(self) -> None:
        '''Test TarProcessBundle validation exceptions.'''
        fields = {
            'archive_path': 'a.tgz',
            'target_dir': 'tmp',
            'source_dir': 'src',
            'path_replacements': {},
            'exclude_patterns': [],
            'vals': {}
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = TarProcessBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()

    def test_tar_process_member_bundle(self) -> None:
        '''Test TarProcessMemberBundle methods.'''
        mock_tar = MagicMock()
        mock_member = MagicMock()
        bundle1 = TarProcessMemberBundle(
            tar=mock_tar,
            member=mock_member,
            dest_full_path='dest',
            vals={}
        )
        mock_tar2 = MagicMock()
        mock_member2 = MagicMock()
        bundle2 = TarProcessMemberBundle(
            tar=mock_tar2,
            member=mock_member2,
            dest_full_path='dest2',
            vals={'x': 'y'}
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.tar, mock_tar2)
        self.assertEqual(bundle1.member, mock_member2)
        self.assertEqual(bundle1.dest_full_path, 'dest2')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['dest_full_path'], 'dest2')

    def test_tar_process_member_bundle_validation_errors(self) -> None:
        '''Test TarProcessMemberBundle validation exceptions.'''
        mock_tar = MagicMock()
        mock_member = MagicMock()
        fields = {
            'tar': mock_tar,
            'member': mock_member,
            'dest_full_path': 'dest',
            'vals': {}
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = TarProcessMemberBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()


if __name__ == '__main__':
    main()
