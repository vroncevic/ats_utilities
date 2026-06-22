# -*- coding: UTF-8 -*-

'''
Module
    ats_config_manager_test.py
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
    Defines classes ConfigManagerTestCase and ConfigManagerUnitTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ConfigLoader.
Execute
    python3 -m unittest -v ats_config_manager_test
'''

from os.path import dirname
from unittest import TestCase, main, mock
from ats_utilities.config_io.config_loader import ConfigLoader
from ats_utilities.config_io.iconfig_loader import IConfigLoader
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.iparser_strategy import IParserStrategy
from ats_utilities.config_io.cfg.cfg_loader import CFGLoader
from ats_utilities.config_io.ini.ini_loader import INILoader
from ats_utilities.config_io.json.json_loader import JSONLoader
from ats_utilities.config_io.xml.xml_loader import XMLLoader
from ats_utilities.config_io.yaml.yaml_loader import YAMLLoader
from ats_utilities.config_io.config_loader_bundle import ATSConfigLoaderBundle
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.context_bundle import ContextBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ConfigManagerTestCase(TestCase):
    '''
        Defines class ConfigManagerTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ConfigLoader.

        It defines:
            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | test_not_none - Test is ConfigLoader not None.
                | test_str - Test string representation of ConfigLoader.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def test_not_none(self) -> None:
        '''Test for create ConfigLoader'''
        bundle = ATSConfigLoaderBundle()
        manager = ConfigLoader(bundle)
        self.assertIsNotNone(manager)
        self.assertTrue(isinstance(manager, IConfigLoader))  # type: ignore

    def test_str(self) -> None:
        '''Test string representation of ConfigLoader.'''
        bundle = ATSConfigLoaderBundle()
        manager = ConfigLoader(bundle)
        self.assertIsInstance(str(manager), str)


class ConfigManagerUnitTestCase(TestCase):
    '''
        Unit tests for ConfigLoader class using mocks.

        It defines:

            :attributes:
                | mock_read - Mocked IRead interface.
                | mock_write - Mocked IWrite interface.
                | mock_checker - Mocked IChecker.
                | mock_reporter - Mocked IReporter.
                | config_file_bundle - Context configuration file bundle.
            :methods:
                | setUp - Set up test environment with mocks.
                | test_setup_config_loader_cfg - Test loading .cfg file.
                | test_setup_config_loader_ini - Test loading .ini file.
                | test_setup_config_loader_json - Test loading .json file.
                | test_setup_config_loader_xml - Test loading .xml file.
                | test_setup_config_loader_yaml - Test loading .yaml file.
                | test_setup_config_loader_none - Test loading with None.
                | test_setup_config_loader_unsupported - Test loading unsupported format.
    '''

    def setUp(self) -> None:
        '''Set up test environment.'''
        self.mock_read = mock.MagicMock(spec=IRead)
        self.mock_write = mock.MagicMock(spec=IWrite)
        self.mock_parser = mock.MagicMock(spec=OptionManager)
        self.mock_checker = mock.MagicMock(spec=IChecker)
        self.mock_reporter = mock.MagicMock(spec=IReporter)
        self.mock_file_checker = mock.MagicMock(spec=IFileCheck)
        self.mock_strategy = mock.MagicMock(spec=IParserStrategy)

        # Configure mock_checker to always return a successful validation
        self.mock_checker.validates_parameters.return_value = ('', 0)

        # Configure mock_read to return a mock processor that provides valid ATSInfo data
        self.mock_processor = mock.MagicMock()
        self.mock_processor.to_dict.return_value = {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0',
            'ats_licence': 'MIT',
            'ats_build_date': '2023-01-01'
        }
        self.mock_read.read_configuration.return_value = self.mock_processor

        self.config_file_bundle = ATSConfigFileBundle(
            file_checker=self.mock_file_checker,
            context=ContextBundle(
                checker=self.mock_checker,
                reporter=self.mock_reporter
            )
        )

    def test_setup_config_loader_cfg(self) -> None:
        '''Test loading .cfg file.'''
        config_file: str = '/config/correct/ats_cli_cfg_api.cfg'
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{config_file}'

        bundle = ATSConfigLoaderBundle(
            info_file=base_info,
            config2object=self.mock_read,
            config_bundle=self.config_file_bundle,
            processor=self.mock_processor
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsInstance(config, CFGLoader)

    def test_setup_config_loader_ini(self) -> None:
        '''Test loading .ini file.'''
        config_file: str = '/config/correct/ats_cli_ini_api.ini'
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{config_file}'

        bundle = ATSConfigLoaderBundle(
            info_file=base_info,
            config2object=self.mock_read,
            config_bundle=self.config_file_bundle,
            processor=self.mock_processor
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsInstance(config, INILoader)

    def test_setup_config_loader_json(self) -> None:
        '''Test loading .json file.'''
        config_file: str = '/config/correct/ats_cli_json_api.json'
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{config_file}'

        bundle = ATSConfigLoaderBundle(
            info_file=base_info,
            config2object=self.mock_read,
            config_bundle=self.config_file_bundle,
            processor=self.mock_processor
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsInstance(config, JSONLoader)

    def test_setup_config_loader_xml(self) -> None:
        '''Test loading .xml file.'''
        config_file: str = '/config/correct/ats_cli_xml_api.xml'
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{config_file}'

        bundle = ATSConfigLoaderBundle(
            info_file=base_info,
            config2object=self.mock_read,
            config_bundle=self.config_file_bundle,
            processor=self.mock_processor
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsInstance(config, XMLLoader)

    def test_setup_config_loader_yaml(self) -> None:
        '''Test loading .yaml file.'''
        config_file: str = '/config/correct/ats_cli_yaml_api.yaml'
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{config_file}'

        bundle = ATSConfigLoaderBundle(
            info_file=base_info,
            config2object=self.mock_read,
            config_bundle=self.config_file_bundle,
            processor=self.mock_processor
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsInstance(config, YAMLLoader)

    def test_setup_config_loader_none(self) -> None:
        '''Test loading with None.'''
        bundle = ATSConfigLoaderBundle(
            info_file=None,
            config2object=self.mock_read,
            config_bundle=self.config_file_bundle
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsNone(config)

    def test_setup_config_loader_unsupported(self) -> None:
        '''Test loading unsupported format.'''
        bundle = ATSConfigLoaderBundle(
            info_file='test.txt',
            config2object=self.mock_read,
            config_bundle=self.config_file_bundle
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsNone(config)


if __name__ == '__main__':
    main()

