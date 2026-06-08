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

from typing import List
from unittest import TestCase, main
from unittest.mock import MagicMock
from os.path import dirname
from ats_utilities.config_io.cfg import CfgBase
from ats_utilities.config_io import IRead, IWrite
from ats_utilities.checker.iats_checker import IATSChecker
from ats_utilities.option import ATSOptionParser
from ats_utilities.console_io import IATSReporter, ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBaseCfg(CfgBase):
    '''Simple Class for checking CfgBase.'''

    _CONFIG: str = '/config/ats_cli_cfg_api.cfg'
    _OPS: List[str] = ['-t', '--test', '-v']

    def __init__(self, reporter: IATSReporter = ATSReporter(), verbose: bool = False) -> None:
        '''Initial constructor.'''
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(info_file=base_info, verbose=verbose)
        self._verbose = verbose
        if self.is_tool_ok():
            reporter.success(['init ATS cfg cli'])


class CfgBaseTestCase(TestCase):
    '''
        Defines class CfgBaseTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS Cfg interfaces.
        CfgBase unit tests.

        It defines:

            :attributes:
                | ats_base_cfg - API for checking base Cfg.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseCfg not None.
                | test_tool_operational - Test is tool operational.
                | test_none_config_path - Test for None as file path.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_base_cfg: ATSBaseCfg = ATSBaseCfg()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create CfgBase'''
        self.assertIsNotNone(self.ats_base_cfg)

    def test_tool_operational(self) -> None:
        '''Test is tool operational'''
        self.assertTrue(self.ats_base_cfg.is_tool_ok())

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        with self.assertRaises(ATSTypeError):
            CfgBase(None)


class CfgBaseUnitTestCase(TestCase):
    '''
        Unit tests for CfgBase class using mocks.

        It defines:

            :attributes:
                | config_path - Path for configuration file.
                | mock_checker - Mocked IATSChecker.
                | mock_reporter - Mocked IATSReporter.
                | mock_cfg2obj - Mocked IRead interface.
                | mock_obj2cfg - Mocked IWrite interface.
            :methods:
                | setUp - Set up test environment with mocks.
                | test_init - Test initialization.
                | test_is_tool_ok_non_operational - Test non-operational status.
                | test_option_parser_access_non_operational - Test property error.
                | test_operational_cfg_base - Test operational state.
    '''

    def setUp(self) -> None:
        '''Set up test environment.'''
        self.config_path = 'ats_cli_cfg_api.cfg'
        self.mock_checker = MagicMock(spec=IATSChecker)
        self.mock_reporter = MagicMock(spec=IATSReporter)
        self.mock_cfg2obj = MagicMock(spec=IRead)
        self.mock_obj2cfg = MagicMock(spec=IWrite)

        # Setup mock behavior
        self.mock_checker.validate_parameters.return_value = ('', 0)
        self.mock_cfg2obj.read_configuration.return_value = {}

        # Use keyword arguments to ensure correct dependency injection
        self.cfg_base: CfgBase = CfgBase(
            info_file=self.config_path,
            cfg2object=self.mock_cfg2obj,
            object2cfg=self.mock_obj2cfg,
            checker=self.mock_checker,
            reporter=self.mock_reporter,
            verbose=True
        )

    def test_init(self) -> None:
        '''Test initialization of CfgBase.'''
        self.assertIsNotNone(self.cfg_base)
        self.mock_cfg2obj.read_configuration.assert_called_once()

    def test_is_tool_ok_non_operational(self) -> None:
        '''Test is_tool_ok status when CfgBase is not operational.'''
        self.assertFalse(self.cfg_base.is_tool_ok())

    def test_option_parser_access_non_operational(self) -> None:
        '''Test if option_parser access raises AttributeError when not operational.'''
        with self.assertRaises(AttributeError):
            _ = self.cfg_base.option_parser

    def test_operational_cfg_base(self) -> None:
        '''Test CfgBase when it is operational.'''
        operational_mock_cfg2obj = MagicMock(spec=IRead)
        operational_mock_obj2cfg = MagicMock(spec=IWrite)
        operational_mock_checker = MagicMock(spec=IATSChecker)
        operational_mock_reporter = MagicMock(spec=IATSReporter)
        operational_mock_options_parser = MagicMock(spec=ATSOptionParser)

        operational_mock_checker.validate_parameters.return_value = ('', 0)
        operational_mock_cfg2obj.read_configuration.return_value = {
            'ats_name': 'Test Tool',
            'ats_version': '1.0.0',
            'ats_licence': 'MIT',
            'ats_build_date': '2023-01-01'
        }

        operational_cfg_base = CfgBase(
            info_file=self.config_path,
            cfg2object=operational_mock_cfg2obj,
            object2cfg=operational_mock_obj2cfg,
            options_parser=operational_mock_options_parser,
            checker=operational_mock_checker,
            reporter=operational_mock_reporter,
            verbose=True
        )

        self.assertTrue(operational_cfg_base.is_tool_ok())
        self.assertIsNotNone(operational_cfg_base.option_parser)
        operational_mock_cfg2obj.read_configuration.assert_called_once()
        operational_mock_options_parser.add_version_operation.assert_called_once_with('1.0.0')


if __name__ == '__main__':
    main()
