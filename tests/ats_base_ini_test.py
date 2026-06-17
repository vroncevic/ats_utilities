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

from typing import List
from unittest import TestCase, main
from unittest.mock import MagicMock
from os.path import dirname
from ats_utilities.config_io.ini.inibase import IniBase
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.option.ats_option_parser import ATSOptionParser
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBaseIni(IniBase):
    '''Simple Class for checking IniBase.'''

    _CONFIG: str = '/config/correct/ats_cli_ini_api.ini'
    _OPS: List[str] = ['-t', '--test', '-v']

    def __init__(self, reporter: IReporter = ATSReporter(), verbose: bool = False) -> None:
        '''Initial constructor.'''
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(info_file=base_info, verbose=verbose)
        self._verbose = verbose
        if self.is_tool_ok():
            reporter.success(['init ATS ini cli'])


class IniBaseTestCase(TestCase):
    '''
        Defines class IniBaseTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS Ini interfaces.
        IniBase unit tests.

        It defines:

            :attributes:
                | ats_base_ini - API for checking base Ini.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseIni not None.
                | test_tool_operational - Test is tool operational.
                | test_none_config_path - Test for None as file path.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_base_ini: ATSBaseIni = ATSBaseIni()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create IniBase'''
        self.assertIsNotNone(self.ats_base_ini)

    def test_tool_operational(self) -> None:
        '''Test is tool operational'''
        self.assertTrue(self.ats_base_ini.is_tool_ok())

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        with self.assertRaises(ATSTypeError):
            IniBase(None)


class IniBaseUnitTestCase(TestCase):
    '''
        Unit tests for IniBase class using mocks.

        It defines:

            :attributes:
                | config_path - Path for configuration file.
                | mock_checker - Mocked IChecker.
                | mock_reporter - Mocked IReporter.
                | mock_ini2obj - Mocked IRead interface.
                | mock_obj2ini - Mocked IWrite interface.
            :methods:
                | setUp - Set up test environment with mocks.
                | test_init - Test initialization.
                | test_is_tool_ok_non_operational - Test non-operational status.
                | test_option_parser_access_non_operational - Test property error.
                | test_operational_ini_base - Test operational state.
    '''

    def setUp(self) -> None:
        '''Set up test environment.'''
        self.config_path = 'ats_cli_ini_api.ini'
        self.mock_checker = MagicMock(spec=IChecker)
        self.mock_reporter = MagicMock(spec=IReporter)
        self.mock_ini2obj = MagicMock(spec=IRead)
        self.mock_obj2ini = MagicMock(spec=IWrite)

        # Setup mock behavior
        self.mock_checker.validate_parameters.return_value = ('', 0)
        self.mock_ini2obj.read_configuration.return_value = {}

        # Use keyword arguments to ensure correct dependency injection
        self.ini_base: IniBase = IniBase(
            info_file=self.config_path,
            ini2obj=self.mock_ini2obj,
            obj2ini=self.mock_obj2ini,
            checker=self.mock_checker,
            reporter=self.mock_reporter,
            verbose=True
        )

    def test_init(self) -> None:
        '''Test initialization of IniBase.'''
        self.assertIsNotNone(self.ini_base)
        self.mock_ini2obj.read_configuration.assert_called_once()

    def test_is_tool_ok_non_operational(self) -> None:
        '''Test is_tool_ok status when IniBase is not operational.'''
        self.assertFalse(self.ini_base.is_tool_ok())

    def test_option_parser_access_non_operational(self) -> None:
        '''Test if option_parser access returns None when not operational.'''
        self.assertIsNone(self.ini_base.option_parser)

    def test_operational_ini_base(self) -> None:
        '''Test IniBase when it is operational.'''
        operational_mock_ini2obj = MagicMock(spec=IRead)
        operational_mock_obj2ini = MagicMock(spec=IWrite)
        operational_mock_checker = MagicMock(spec=IChecker)
        operational_mock_reporter = MagicMock(spec=IReporter)
        operational_mock_options_parser = MagicMock(spec=ATSOptionParser)

        operational_mock_checker.validate_parameters.return_value = ('', 0)

        # Mock the INI processor that read_configuration is expected to return
        mock_ini_processor = MagicMock()
        mock_ats_info = MagicMock()

        def mock_get(key: str):
            return {
                'ats_name': 'Test Tool',
                'ats_version': '1.0.0',
                'ats_licence': 'MIT',
                'ats_build_date': '2023-01-01'
            }.get(key)

        mock_ats_info.get.side_effect = mock_get
        mock_ini_processor.get_ats_info.return_value = mock_ats_info
        operational_mock_ini2obj.read_configuration.return_value = mock_ini_processor

        operational_ini_base = IniBase(
            info_file=self.config_path,
            ini2obj=operational_mock_ini2obj,
            obj2ini=operational_mock_obj2ini,
            options_parser=operational_mock_options_parser,
            checker=operational_mock_checker,
            reporter=operational_mock_reporter,
            verbose=True
        )

        self.assertTrue(operational_ini_base.is_tool_ok())
        self.assertIsNotNone(operational_ini_base.option_parser)
        operational_mock_ini2obj.read_configuration.assert_called_once()
        operational_mock_options_parser.add_version_operation.assert_called_once_with('1.0.0')


if __name__ == '__main__':
    main()
