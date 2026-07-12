# -*- coding: UTF-8 -*-

'''
Module
    ats_base_yaml_test.py
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
    Defines classes YamlBaseTestCase with attribute(s) and method(s).
    Defines classes YamlBaseTestCase and YamlBaseUnitTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Yaml.
Execute
    python3 -m unittest -v ats_base_yaml_test
'''

from unittest import TestCase, main
from unittest.mock import MagicMock
from os.path import dirname
from ats_utilities.config_io.yaml.yaml_loader import YAMLLoader
from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
from ats_utilities.config_io.yaml.yaml_processor import YAMLProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ATSBaseYaml(YAMLLoader):
    '''Simple Class for checking YAMLLoader.'''

    _CONFIG: str = '/assets/config/correct/ats_cli_yaml_api.yaml'

    def __init__(self) -> None:
        '''Initial constructor.'''
        current_dir: str = dirname(dirname(dirname(__file__)))
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(info_file=base_info)


class YamlBaseTestCase(TestCase):
    '''
        Defines class YamlBaseTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS Yaml interfaces.
        YAMLLoader unit tests.

        It defines:

            :attributes:
                | ats_base_yaml - API for checking base Yaml.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseYaml not None.
                | test_load_configuration - Test loading configuration.
                | test_none_config_path_returns_empty_dict - Test for None as file path.
                | test_str - Test string representation of YAMLLoader.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_base_yaml: ATSBaseYaml = ATSBaseYaml()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create YAMLLoader.'''
        self.assertIsNotNone(self.ats_base_yaml)

    def test_load_configuration(self) -> None:
        '''Test loading configuration.'''
        config = self.ats_base_yaml.load_configuration()
        self.assertIsInstance(config, dict)
        self.assertEqual(config.get('ats_name'), 'ats_cli_test')
        self.assertEqual(config.get('ats_version'), '1.0.0')

    def test_none_config_path_returns_empty_dict(self) -> None:
        '''Test for None as file path.'''
        loader = YAMLLoader(None)
        self.assertEqual(loader.load_configuration(), {})

    def test_str(self) -> None:
        '''Test string representation of YAMLLoader.'''
        self.assertIsInstance(str(self.ats_base_yaml), str)


class YamlBaseUnitTestCase(TestCase):
    '''
        Unit tests for YAMLLoader class using mocks.

        It defines:

            :attributes:
                | config_path - Path for configuration file.
                | mock_yaml2obj - Mocked IRead interface.
                | mock_processor - Mocked IYAMLProcessor interface.
            :methods:
                | setUp - Set up test environment with mocks.
                | test_init - Test initialization.
                | test_load_configuration - Test load configuration.
                | test_load_configuration_empty - Test load configuration when empty.
    '''

    def setUp(self) -> None:
        '''Set up test environment.'''
        self.config_path = 'ats_cli_yaml_api.yaml'
        self.mock_yaml2obj = MagicMock(spec=Yaml2Object)
        self.mock_processor = MagicMock(spec=YAMLProcessor)

        # Setup mock behavior
        self.mock_yaml2obj.read_configuration.return_value = self.mock_processor
        self.mock_processor.to_dict.return_value = {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0'
        }

        self.yaml_loader: YAMLLoader = YAMLLoader(
            info_file=self.config_path,
            yaml2object=self.mock_yaml2obj,
            yaml_processor=self.mock_processor
        )

    def test_init(self) -> None:
        '''Test initialization of YAMLLoader.'''
        self.assertIsNotNone(self.yaml_loader)
        self.mock_yaml2obj.read_configuration.assert_called_once()

    def test_load_configuration(self) -> None:
        '''Test load configuration.'''
        config = self.yaml_loader.load_configuration()
        self.assertEqual(config, {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0'
        })
        self.mock_processor.to_dict.assert_called_once()

    def test_load_configuration_empty(self) -> None:
        '''Test load configuration when empty.'''
        # Setup loader with no configuration loaded
        mock_yaml2obj_empty = MagicMock(spec=Yaml2Object)
        mock_yaml2obj_empty.read_configuration.return_value = None
        loader = YAMLLoader(
            info_file=self.config_path,
            yaml2object=mock_yaml2obj_empty
        )
        self.assertEqual(loader.load_configuration(), {})

    def test_init_bool_false(self) -> None:
        '''Test initialization when yaml2obj is falsy in bool evaluation.'''
        class FalsyYaml2Object(Yaml2Object):
            def __init__(self):
                pass
            def __bool__(self) -> bool:
                return False
            def read_configuration(self):
                return None

        mock_yaml2obj = FalsyYaml2Object()
        mock_yaml2obj.read_configuration = MagicMock(return_value=None)
        loader = YAMLLoader(
            info_file=self.config_path,
            yaml2object=mock_yaml2obj
        )
        self.assertEqual(loader.load_configuration(), {})
        mock_yaml2obj.read_configuration.assert_not_called()


if __name__ == '__main__':
    main()

