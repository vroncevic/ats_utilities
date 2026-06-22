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
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.config_loader_bundle import ATSConfigLoaderBundle
from ats_utilities.config_io.file_bundle import ATSFileBundle
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
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.iconfig_loader import IConfigLoader, IConfigProcessor
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.logging.ilogger_manager import ILoggerManager
from ats_utilities.splasher.isplasher import ISplasher

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class BundlesTestCase(TestCase):
    '''
        Defines class BundlesTestCase with attribute(s) and method(s).
        Creates test cases for checking base parameter bundles.

        It defines:

            :attributes: None
            :methods:
                | test_context_bundle - Test ContextBundle methods.
                | test_context_bundle_validation_errors - Test ContextBundle validation exceptions.
                | test_logger_bundle - Test LoggerBundle methods.
                | test_ats_file_bundle - Test ATSFileBundle methods.
                | test_ats_config_file_bundle - Test ATSConfigFileBundle methods.
                | test_ats_config_loader_bundle - Test ATSConfigLoaderBundle methods.
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
        mock_checker = MagicMock(spec=IChecker)
        mock_reporter = MagicMock(spec=IReporter)

        bundle = ContextBundle(checker=None, reporter=mock_reporter)
        with self.assertRaises(ATSValueError):
            bundle.validate()

        bundle = ContextBundle(checker=mock_checker, reporter=None)
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

    def test_ats_file_bundle(self) -> None:
        '''Test ATSFileBundle methods.'''
        bundle1 = ATSFileBundle()
        bundle2 = ATSFileBundle(file_path='a.txt', file_mode='w', file_format='txt')

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.file_path, 'a.txt')
        self.assertEqual(bundle1.file_mode, 'w')
        self.assertEqual(bundle1.file_format, 'txt')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['file_path'], 'a.txt')

    def test_ats_config_file_bundle(self) -> None:
        '''Test ATSConfigFileBundle methods.'''
        mock_context = ContextBundle()
        bundle1 = ATSConfigFileBundle()
        bundle2 = ATSConfigFileBundle(context=mock_context)

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.context, mock_context)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['context'], mock_context)

    def test_ats_config_loader_bundle(self) -> None:
        '''Test ATSConfigLoaderBundle methods.'''
        bundle1 = ATSConfigLoaderBundle()
        bundle2 = ATSConfigLoaderBundle(info_file='config.json')

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.info_file, 'config.json')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['info_file'], 'config.json')

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

        bundle = CheckerReporterBundle(context='ctx', parameters_meta=None)
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
        bundle = SplashCenterBundle(columns=-1, additional_shifter=2, text='ok')
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # additional_shifter type error
        bundle = SplashCenterBundle(columns=80, additional_shifter='not_int', text='ok')
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        # additional_shifter value error
        bundle = SplashCenterBundle(columns=80, additional_shifter=-1, text='ok')
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

            :attributes: None
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
        bundle1 = LoggingComponentBundle()
        bundle2 = LoggingComponentBundle(logger=mock_logger)

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.logger, mock_logger)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['logger'], mock_logger)

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
        bundle = OptionComponentBundle(parameters=None, strategy=mock_strategy, context_bundle=mock_context)
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # Missing strategy
        bundle = OptionComponentBundle(parameters={'a': 'b'}, strategy=None, context_bundle=mock_context)
        with self.assertRaises(ATSValueError):
            bundle.validate()

        # Missing context_bundle
        bundle = OptionComponentBundle(parameters={'a': 'b'}, strategy=mock_strategy, context_bundle=None)
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
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = InfoComponentBundle(**kwargs)
            with self.assertRaises(ValueError):
                bundle.validate()

    def test_reporter_component_bundle(self) -> None:
        '''Test ReporterComponentBundle methods.'''
        mock_checker = MagicMock(spec=IChecker)
        bundle1 = ReporterComponentBundle()
        bundle2 = ReporterComponentBundle(checker=mock_checker)

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.checker, mock_checker)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['checker'], mock_checker)

    def test_reporter_component_bundle_validation_errors(self) -> None:
        '''Test ReporterComponentBundle validation exceptions.'''
        bundle = ReporterComponentBundle(checker=None)
        with self.assertRaises(ATSValueError):
            bundle.validate()

    def test_splash_component_bundle(self) -> None:
        '''Test SplashComponentBundle methods.'''
        bundle1 = SplashComponentBundle()
        bundle2 = SplashComponentBundle(prop={'a': 'b'})

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.prop, {'a': 'b'})

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['prop'], {'a': 'b'})

    def test_splash_component_bundle_validation_errors(self) -> None:
        '''Test SplashComponentBundle validation exceptions.'''
        bundle = SplashComponentBundle(prop=None)
        with self.assertRaises(ValueError):
            bundle.validate()


if __name__ == '__main__':
    main()
