# -*- coding: UTF-8 -*-

'''
Module
    ats_base_ini_test.py
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
    Defines classes IniBaseTestCase and IniBaseUnitTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Ini.
Execute
    python3 -m unittest -v ats_base_ini_test
'''

from unittest import TestCase, main
from unittest.mock import MagicMock
from os.path import dirname
from ats_utilities.config_io.ini.ini_loader import INILoader
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.ini.iini_processor import IINIProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBaseIni(INILoader):
    '''Simple Class for checking INILoader.'''

    _CONFIG: str = '/config/correct/ats_cli_ini_api.ini'

    def __init__(self) -> None:
        '''Initial constructor.'''
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(info_file=base_info)


class IniBaseTestCase(TestCase):
    '''
        Defines class IniBaseTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS Ini interfaces.
        INILoader unit tests.

        It defines:

            :attributes:
                | ats_base_ini - API for checking base Ini.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseIni not None.
                | test_load_configuration - Test loading configuration.
                | test_none_config_path_returns_empty_dict - Test for None as file path.
                | test_str - Test string representation of INILoader.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_base_ini: ATSBaseIni = ATSBaseIni()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create INILoader.'''
        self.assertIsNotNone(self.ats_base_ini)

    def test_load_configuration(self) -> None:
        '''Test loading configuration.'''
        config = self.ats_base_ini.load_configuration()
        self.assertIsInstance(config, dict)
        self.assertEqual(config.get('ats_name'), 'ats_cli_test')
        self.assertEqual(config.get('ats_version'), '1.0.0')

    def test_none_config_path_returns_empty_dict(self) -> None:
        '''Test for None as file path.'''
        loader = INILoader(None)
        self.assertEqual(loader.load_configuration(), {})

    def test_str(self) -> None:
        '''Test string representation of INILoader.'''
        self.assertIsInstance(str(self.ats_base_ini), str)


class IniBaseUnitTestCase(TestCase):
    '''
        Unit tests for INILoader class using mocks.

        It defines:

            :attributes:
                | config_path - Path for configuration file.
                | mock_ini2obj - Mocked IRead interface.
                | mock_processor - Mocked IINIProcessor interface.
            :methods:
                | setUp - Set up test environment with mocks.
                | test_init - Test initialization.
                | test_load_configuration - Test load configuration.
                | test_load_configuration_empty - Test load configuration when empty.
    '''

    def setUp(self) -> None:
        '''Set up test environment.'''
        self.config_path = 'ats_cli_ini_api.ini'
        self.mock_ini2obj = MagicMock(spec=IRead)
        self.mock_processor = MagicMock(spec=IINIProcessor)

        # Setup mock behavior
        self.mock_ini2obj.read_configuration.return_value = self.mock_processor
        self.mock_processor.to_dict.return_value = {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0'
        }

        self.ini_loader: INILoader = INILoader(
            info_file=self.config_path,
            ini2object=self.mock_ini2obj,
            ini_processor=self.mock_processor
        )

    def test_init(self) -> None:
        '''Test initialization of INILoader.'''
        self.assertIsNotNone(self.ini_loader)
        self.mock_ini2obj.read_configuration.assert_called_once()

    def test_load_configuration(self) -> None:
        '''Test load configuration.'''
        config = self.ini_loader.load_configuration()
        self.assertEqual(config, {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0'
        })
        self.mock_processor.to_dict.assert_called_once()

    def test_load_configuration_empty(self) -> None:
        '''Test load configuration when empty.'''
        # Setup loader with no configuration loaded
        mock_ini2obj_empty = MagicMock(spec=IRead)
        mock_ini2obj_empty.read_configuration.return_value = None
        loader = INILoader(
            info_file=self.config_path,
            ini2object=mock_ini2obj_empty
        )
        self.assertEqual(loader.load_configuration(), {})


if __name__ == '__main__':
    main()
