# -*- coding: UTF-8 -*-

'''
Module
    ats_config_loader_test.py
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
    python3 -m unittest -v tests/config_io/ats_config_loader_test.py
'''

from os.path import dirname
from unittest import TestCase, main, mock
from ats_utilities.config_io.config_loader import ConfigLoader
from ats_utilities.config_io.iconfig_loader import IConfigLoader
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.config_io.cfg.cfg_loader import CFGLoader
from ats_utilities.config_io.cfg.cfg2object import Cfg2Object
from ats_utilities.config_io.cfg.cfg_processor import CFGProcessor
from ats_utilities.config_io.ini.ini_loader import INILoader
from ats_utilities.config_io.ini.ini2object import Ini2Object
from ats_utilities.config_io.ini.ini_processor import INIProcessor
from ats_utilities.config_io.json.json_loader import JSONLoader
from ats_utilities.config_io.json.json2object import Json2Object
from ats_utilities.config_io.json.json_processor import JSONProcessor
from ats_utilities.config_io.xml.xml_loader import XMLLoader
from ats_utilities.config_io.xml.xml2object import Xml2Object
from ats_utilities.config_io.xml.xml_processor import XMLProcessor
from ats_utilities.config_io.yaml.yaml_loader import YAMLLoader
from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
from ats_utilities.config_io.yaml.yaml_processor import YAMLProcessor
from ats_utilities.config_io.config_loader_bundle import ConfigLoaderBundle
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.context_bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


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
        bundle = ConfigLoaderBundle()
        manager = ConfigLoader(bundle)
        self.assertIsNotNone(manager)
        self.assertTrue(isinstance(manager, IConfigLoader))  # type: ignore

    def test_str(self) -> None:
        '''Test string representation of ConfigLoader.'''
        bundle = ConfigLoaderBundle()
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
        self.mock_file_checker = mock.MagicMock(spec=FileCheck)
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

        self.config_file_bundle = ConfigFileBundle(
            file_checker=self.mock_file_checker,
            context=ContextBundle(
                checker=self.mock_checker,
                reporter=self.mock_reporter
            )
        )

    def test_setup_config_loader_cfg(self) -> None:
        '''Test loading .cfg file.'''
        config_file: str = '/assets/config/correct/ats_cli_cfg_api.cfg'
        current_dir: str = dirname(dirname(__file__))
        base_info: str = f'{current_dir}{config_file}'

        mock_read = mock.MagicMock(spec=Cfg2Object)
        mock_processor = mock.MagicMock(spec=CFGProcessor)
        mock_processor.to_dict.return_value = {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0',
            'ats_licence': 'MIT',
            'ats_build_date': '2023-01-01'
        }
        mock_read.read_configuration.return_value = mock_processor

        bundle = ConfigLoaderBundle(
            info_file=base_info,
            config2object=mock_read,
            config_bundle=self.config_file_bundle,
            processor=mock_processor
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsInstance(config, CFGLoader)

    def test_setup_config_loader_ini(self) -> None:
        '''Test loading .ini file.'''
        config_file: str = '/assets/config/correct/ats_cli_ini_api.ini'
        current_dir: str = dirname(dirname(__file__))
        base_info: str = f'{current_dir}{config_file}'

        mock_read = mock.MagicMock(spec=Ini2Object)
        mock_processor = mock.MagicMock(spec=INIProcessor)
        mock_processor.to_dict.return_value = {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0',
            'ats_licence': 'MIT',
            'ats_build_date': '2023-01-01'
        }
        mock_read.read_configuration.return_value = mock_processor

        bundle = ConfigLoaderBundle(
            info_file=base_info,
            config2object=mock_read,
            config_bundle=self.config_file_bundle,
            processor=mock_processor
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsInstance(config, INILoader)

    def test_setup_config_loader_json(self) -> None:
        '''Test loading .json file.'''
        config_file: str = '/assets/config/correct/ats_cli_json_api.json'
        current_dir: str = dirname(dirname(__file__))
        base_info: str = f'{current_dir}{config_file}'

        mock_read = mock.MagicMock(spec=Json2Object)
        mock_processor = mock.MagicMock(spec=JSONProcessor)
        mock_processor.to_dict.return_value = {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0',
            'ats_licence': 'MIT',
            'ats_build_date': '2023-01-01'
        }
        mock_read.read_configuration.return_value = mock_processor

        bundle = ConfigLoaderBundle(
            info_file=base_info,
            config2object=mock_read,
            config_bundle=self.config_file_bundle,
            processor=mock_processor
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsInstance(config, JSONLoader)

    def test_setup_config_loader_xml(self) -> None:
        '''Test loading .xml file.'''
        config_file: str = '/assets/config/correct/ats_cli_xml_api.xml'
        current_dir: str = dirname(dirname(__file__))
        base_info: str = f'{current_dir}{config_file}'

        mock_read = mock.MagicMock(spec=Xml2Object)
        mock_processor = mock.MagicMock(spec=XMLProcessor)
        mock_processor.to_dict.return_value = {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0',
            'ats_licence': 'MIT',
            'ats_build_date': '2023-01-01'
        }
        mock_read.read_configuration.return_value = mock_processor

        bundle = ConfigLoaderBundle(
            info_file=base_info,
            config2object=mock_read,
            config_bundle=self.config_file_bundle,
            processor=mock_processor
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsInstance(config, XMLLoader)

    def test_setup_config_loader_yaml(self) -> None:
        '''Test loading .yaml file.'''
        config_file: str = '/assets/config/correct/ats_cli_yaml_api.yaml'
        current_dir: str = dirname(dirname(__file__))
        base_info: str = f'{current_dir}{config_file}'

        mock_read = mock.MagicMock(spec=Yaml2Object)
        mock_processor = mock.MagicMock(spec=YAMLProcessor)
        mock_processor.to_dict.return_value = {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0',
            'ats_licence': 'MIT',
            'ats_build_date': '2023-01-01'
        }
        mock_read.read_configuration.return_value = mock_processor

        bundle = ConfigLoaderBundle(
            info_file=base_info,
            config2object=mock_read,
            config_bundle=self.config_file_bundle,
            processor=mock_processor
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsInstance(config, YAMLLoader)

    def test_setup_config_loader_none(self) -> None:
        '''Test loading with None.'''
        bundle = ConfigLoaderBundle(
            info_file=None,
            config2object=self.mock_read,
            config_bundle=self.config_file_bundle
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsNone(config)

    def test_setup_config_loader_unsupported(self) -> None:
        '''Test loading unsupported format.'''
        bundle = ConfigLoaderBundle(
            info_file='test.txt',
            config2object=self.mock_read,
            config_bundle=self.config_file_bundle
        )
        manager = ConfigLoader(bundle)
        config = manager.setup_config_loader()
        self.assertIsNone(config)


    def test_cfg_loader_bool_false(self) -> None:
        '''Test CFGLoader when cfg2obj is False.'''
        class FalsyCfg2Object(Cfg2Object):
            def __init__(self):
                pass
            def __bool__(self) -> bool:
                return False
            def read_configuration(self):
                return None

        mock_read = FalsyCfg2Object()
        mock_processor = mock.MagicMock(spec=CFGProcessor)
        loader = CFGLoader(
            info_file='some_file.cfg',
            config_bundle=self.config_file_bundle,
            cfg_processor=mock_processor,
            cfg2object=mock_read
        )
        self.assertIsNone(loader._configuration)

    def test_ini_loader_bool_false(self) -> None:
        '''Test INILoader when ini2obj is False.'''
        class FalsyIni2Object(Ini2Object):
            def __init__(self):
                pass
            def __bool__(self) -> bool:
                return False
            def read_configuration(self):
                return None

        mock_read = FalsyIni2Object()
        mock_processor = mock.MagicMock(spec=INIProcessor)
        loader = INILoader(
            info_file='some_file.ini',
            config_bundle=self.config_file_bundle,
            ini_processor=mock_processor,
            ini2object=mock_read
        )
        self.assertIsNone(loader._configuration)

    def test_json_loader_bool_false(self) -> None:
        '''Test JSONLoader when json2obj is False.'''
        class FalsyJson2Object(Json2Object):
            def __init__(self):
                pass
            def __bool__(self) -> bool:
                return False
            def read_configuration(self):
                return None

        mock_read = FalsyJson2Object()
        mock_processor = mock.MagicMock(spec=JSONProcessor)
        loader = JSONLoader(
            info_file='some_file.json',
            config_bundle=self.config_file_bundle,
            json_processor=mock_processor,
            json2object=mock_read
        )
        self.assertIsNone(loader._configuration)

    def test_xml_loader_bool_false(self) -> None:
        '''Test XMLLoader when xml2obj is False.'''
        class FalsyXml2Object(Xml2Object):
            def __init__(self):
                pass
            def __bool__(self) -> bool:
                return False
            def read_configuration(self):
                return None

        mock_read = FalsyXml2Object()
        mock_processor = mock.MagicMock(spec=XMLProcessor)
        loader = XMLLoader(
            info_file='some_file.xml',
            config_bundle=self.config_file_bundle,
            xml_processor=mock_processor,
            xml2object=mock_read
        )
        self.assertIsNone(loader._configuration)

    def test_yaml_loader_bool_false(self) -> None:
        '''Test YAMLLoader when yaml2obj is False.'''
        class FalsyYaml2Object(Yaml2Object):
            def __init__(self):
                pass
            def __bool__(self) -> bool:
                return False
            def read_configuration(self):
                return None

        mock_read = FalsyYaml2Object()
        mock_processor = mock.MagicMock(spec=YAMLProcessor)
        loader = YAMLLoader(
            info_file='some_file.yaml',
            config_bundle=self.config_file_bundle,
            yaml_processor=mock_processor,
            yaml2object=mock_read
        )
        self.assertIsNone(loader._configuration)


if __name__ == '__main__':
    main()
