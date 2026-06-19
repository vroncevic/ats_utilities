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
    Creates test cases for checking functionalities of ATSConfigLoader.
Execute
    python3 -m unittest -v ats_config_manager_test
'''

from typing import List
from os.path import dirname
from unittest import TestCase, main, mock
from ats_utilities.config_io.config_loader import ATSConfigLoader
from ats_utilities.config_io.iconfig_loader import IConfigLoader
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.option.engine import ATSOptionManager
from ats_utilities.option.iparser_strategy import IArgParserStrategy
from ats_utilities.config_io.cfg.cfg_loader import CFGLoader
from ats_utilities.config_io.ini.inibase import IniBase
from ats_utilities.config_io.json.jsonbase import JsonBase
from ats_utilities.config_io.xml.xmlbase import XmlBase
from ats_utilities.config_io.yaml.yamlbase import YamlBase

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ConfigManagerTestCase(TestCase):
    '''
        Defines class ConfigManagerTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATSConfigLoader.

        It defines:

            :attributes:
                | manager - API for checking ATSConfigLoader.
            :methods:
                | setUp - Call before test case.
                | test_not_none - Test is ATSConfigLoader not None.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.manager: ATSConfigLoader = ATSConfigLoader()

    def test_not_none(self) -> None:
        '''Test for create ATSConfigLoader'''
        self.assertIsNotNone(self.manager)
        self.assertTrue(isinstance(self.manager, IConfigLoader))  # type: ignore


class ConfigManagerUnitTestCase(TestCase):
    '''
        Unit tests for ATSConfigLoader class using mocks.

        It defines:

            :attributes:
                | mock_read - Mocked IRead interface.
                | mock_write - Mocked IWrite interface.
                | mock_checker - Mocked IChecker.
                | mock_reporter - Mocked IReporter.
                | manager - ATSConfigLoader instance with mocks.
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
        self.mock_parser = mock.MagicMock(spec=ATSOptionManager)
        self.mock_checker = mock.MagicMock(spec=IChecker)
        self.mock_reporter = mock.MagicMock(spec=IReporter)
        self.mock_file_checker = mock.MagicMock(spec=IFileCheck)
        self.mock_strategy = mock.MagicMock(spec=IArgParserStrategy)

        # Configure mock_checker to always return a successful validation
        self.mock_checker.validate_parameters.return_value = ('', 0)

        # Configure mock_read to return a mock processor that provides valid ATSInfo data
        mock_processor = mock.MagicMock()
        mock_processor.to_dict.return_value = {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0',
            'ats_licence': 'MIT',
            'ats_build_date': '2023-01-01'
        }
        # For Ini and Xml, they might call get_ats_info() which then returns a dict
        mock_ats_info_getter = mock.MagicMock()
        mock_ats_info_getter.get.side_effect = lambda key: mock_processor.to_dict.return_value.get(key)
        mock_processor.get_ats_info.return_value = mock_ats_info_getter
        self.mock_read.read_configuration.return_value = mock_processor

        self.manager = ATSConfigLoader(
            config2object=self.mock_read,
            object2config=self.mock_write,
            options_parser=self.mock_parser,
            checker=self.mock_checker,
            reporter=self.mock_reporter,
            file_checker=self.mock_file_checker,
            strategy=self.mock_strategy
        )

    def test_setup_config_loader_cfg(self) -> None:
        '''Test loading .cfg file.'''
        config_file: str = '/config/correct/ats_cli_cfg_api.cfg'
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{config_file}'
        config = self.manager.setup_config_loader(base_info, True)
        self.assertIsInstance(config, CFGLoader)

    def test_setup_config_loader_ini(self) -> None:
        '''Test loading .ini file.'''
        config_file: str = '/config/correct/ats_cli_ini_api.ini'
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{config_file}'
        config = self.manager.setup_config_loader(base_info)
        self.assertIsInstance(config, IniBase)

    def test_setup_config_loader_json(self) -> None:
        '''Test loading .json file.'''
        config_file: str = '/config/correct/ats_cli_json_api.json'
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{config_file}'
        config = self.manager.setup_config_loader(base_info)
        self.assertIsInstance(config, JsonBase)

    def test_setup_config_loader_xml(self) -> None:
        '''Test loading .xml file.'''
        config_file: str = '/config/correct/ats_cli_xml_api.xml'
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{config_file}'
        config = self.manager.setup_config_loader(base_info)
        self.assertIsInstance(config, XmlBase)

    def test_setup_config_loader_yaml(self) -> None:
        '''Test loading .yaml file.'''
        config_file: str = '/config/correct/ats_cli_yaml_api.yaml'
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{config_file}'
        config = self.manager.setup_config_loader(base_info)
        self.assertIsInstance(config, YamlBase)

    def test_setup_config_loader_none(self) -> None:
        '''Test loading with None.'''
        config = self.manager.setup_config_loader(None)
        self.assertIsNone(config)

    def test_setup_config_loader_unsupported(self) -> None:
        '''Test loading unsupported format.'''
        config = self.manager.setup_config_loader('test.txt')
        self.assertIsNone(config)


if __name__ == '__main__':
    main()
