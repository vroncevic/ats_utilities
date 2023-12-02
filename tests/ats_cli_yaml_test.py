# -*- coding: UTF-8 -*-

'''
Module
    ats_cli_yaml_test.py
Copyright
    Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines classes ATSCliXXXXTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of CLI.
Execute
    python3 -m unittest -v ats_cli_yaml_test
'''

import sys
from typing import List
from unittest.mock import MagicMock
from unittest import TestCase, main
from os.path import dirname

try:
    from ats_utilities.cli.yaml_cli import YamlCLI
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSCliYamlAPI(YamlCLI):
    '''Simple Class for checking YamlCLI.'''

    _CONFIG: str = '/config/ats_cli_yaml_api.yaml'
    _OPS: List[str] = ['-t', '--test', '-v']

    def __init__(self, verbose: bool = False) -> None:
        '''Initial constructor.'''
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(base_info, verbose)
        if self.tool_operational:
            self.add_new_option(
                self._OPS[0], self._OPS[1], dest='test',
                help='flag'
            )
            self.add_new_option(
                self._OPS[2], action='store_true', default=False,
                help='activate verbose mode'
            )

    def process(self, verbose: bool = False) -> bool:
        '''Process and run operation.'''
        status: bool = False
        if self.tool_operational:
            status = True
        return status


class YamlTestCase(TestCase):
    '''
        Defines class YamlTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS CLI interfaces.
        It defines:

            :attributes:
                | ats_cli_yaml_api - API for checking Yaml CLI.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSCliYamlAPI not None.
                | test_process - Test for process.
                | test_add_new_option_called - Test is add new option called.
                | test_parse_args_called - Test is parse args called.
                | test_parse_wrong_args_called - Test parse without args.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_cli_yaml_api = ATSCliYamlAPI()
        self.mock_add_new = MagicMock()
        self.mock_pars_arg = MagicMock()
        self.ats_cli_yaml_api.option_parser.add_operation = self.mock_add_new
        self.ats_cli_yaml_api.option_parser.parse_args = self.mock_pars_arg

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create'''
        self.assertIsNotNone(self.ats_cli_yaml_api)

    def test_process(self) -> None:
        '''Test for process.'''
        self.assertTrue(self.ats_cli_yaml_api.process())

    def test_add_new_option_called(self) -> None:
        '''Test add new option for option parser'''
        self.ats_cli_yaml_api.add_new_option('arg1', 'arg2', option='value')
        self.mock_add_new.assert_called_once()

    def test_parse_args_called(self) -> None:
        '''Test parse args'''
        self.ats_cli_yaml_api.add_new_option('arg1', 'arg2', option='value')
        self.ats_cli_yaml_api.parse_args(['arg1', 'arg2'])
        self.mock_pars_arg.assert_called_once()

    def test_parse_wrong_args_called(self) -> None:
        '''Test parse without args'''
        with self.assertRaises(ATSTypeError):
            self.ats_cli_yaml_api.add_new_option(
                'arg1', 'arg2', option='value'
            )
            self.ats_cli_yaml_api.parse_args(None)  # type: ignore


if __name__ == '__main__':
    main()
