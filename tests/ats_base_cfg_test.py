# -*- coding: UTF-8 -*-

'''
Module
    ats_base_cfg_test.py
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
    Defines classes CfgBaseTestCase and CfgBaseUnitTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Cfg.
Execute
    python3 -m unittest -v ats_base_cfg_test
'''

from unittest import TestCase, main
from unittest.mock import MagicMock
from os.path import dirname
from ats_utilities.config_io.cfg.cfg_loader import CFGLoader
from ats_utilities.config_io.cfg.cfg2object import Cfg2Object
from ats_utilities.config_io.cfg.cfg_processor import CFGProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBaseCfg(CFGLoader):
    '''Simple Class for checking CFGLoader.'''

    _CONFIG: str = '/config/correct/ats_cli_cfg_api.cfg'

    def __init__(self) -> None:
        '''Initial constructor.'''
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(info_file=base_info)


class CfgBaseTestCase(TestCase):
    '''
        Defines class CfgBaseTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS Cfg interfaces.
        CFGLoader unit tests.

        It defines:

            :attributes:
                | ats_base_cfg - API for checking base Cfg.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseCfg not None.
                | test_load_configuration - Test loading configuration.
                | test_none_config_path_returns_empty_dict - Test for None as file path.
                | test_str - Test string representation of CFGLoader.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_base_cfg: ATSBaseCfg = ATSBaseCfg()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create CFGLoader.'''
        self.assertIsNotNone(self.ats_base_cfg)

    def test_load_configuration(self) -> None:
        '''Test loading configuration.'''
        config = self.ats_base_cfg.load_configuration()
        self.assertIsInstance(config, dict)
        self.assertEqual(config.get('ats_name'), 'ats_cli_test')
        self.assertEqual(config.get('ats_version'), '1.0.0')

    def test_none_config_path_returns_empty_dict(self) -> None:
        '''Test for None as file path.'''
        loader = CFGLoader(None)
        self.assertEqual(loader.load_configuration(), {})

    def test_str(self) -> None:
        '''Test string representation of CFGLoader.'''
        self.assertIsInstance(str(self.ats_base_cfg), str)


class CfgBaseUnitTestCase(TestCase):
    '''
        Unit tests for CFGLoader class using mocks.

        It defines:

            :attributes:
                | config_path - Path for configuration file.
                | mock_cfg2obj - Mocked IRead interface.
                | mock_processor - Mocked ICFGProcessor interface.
            :methods:
                | setUp - Set up test environment with mocks.
                | test_init - Test initialization.
                | test_load_configuration - Test load configuration.
                | test_load_configuration_empty - Test load configuration when empty.
    '''

    def setUp(self) -> None:
        '''Set up test environment.'''
        self.config_path = 'ats_cli_cfg_api.cfg'
        self.mock_cfg2obj = MagicMock(spec=Cfg2Object)
        self.mock_processor = MagicMock(spec=CFGProcessor)

        # Setup mock behavior
        self.mock_cfg2obj.read_configuration.return_value = self.mock_processor
        self.mock_processor.to_dict.return_value = {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0'
        }

        self.cfg_loader: CFGLoader = CFGLoader(
            info_file=self.config_path,
            cfg2object=self.mock_cfg2obj,
            cfg_processor=self.mock_processor
        )

    def test_init(self) -> None:
        '''Test initialization of CFGLoader.'''
        self.assertIsNotNone(self.cfg_loader)
        self.mock_cfg2obj.read_configuration.assert_called_once()

    def test_load_configuration(self) -> None:
        '''Test load configuration.'''
        config = self.cfg_loader.load_configuration()
        self.assertEqual(config, {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0'
        })
        self.mock_processor.to_dict.assert_called_once()

    def test_load_configuration_empty(self) -> None:
        '''Test load configuration when empty.'''
        # Setup loader with no configuration loaded
        mock_cfg2obj_empty = MagicMock(spec=Cfg2Object)
        mock_cfg2obj_empty.read_configuration.return_value = None
        loader = CFGLoader(
            info_file=self.config_path,
            cfg2object=mock_cfg2obj_empty
        )
        self.assertEqual(loader.load_configuration(), {})



if __name__ == '__main__':
    main()
