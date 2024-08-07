# -*- coding: UTF-8 -*-

'''
Module
    ats_cli_test.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines classes CLITestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of CLI.
Execute
    python3 -m unittest -v ats_cli_cfg_test
'''

import sys
from typing import List
from unittest.mock import MagicMock
from unittest import TestCase, main
from os.path import dirname

try:
    from ats_utilities.cli import ATSCli
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSCliCfgAPI(ATSCli):
    '''Simple Class for checking CfgCLI.'''

    _CONFIG: str = '/config/ats_cli_cfg_api.cfg'
    _OPS: List[str] = ['-t', '--test', '-v']

    def __init__(self, verbose: bool = False) -> None:
        '''Initial constructor.'''
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(base_info, verbose)
        if self.is_operational():
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
        return self.is_operational()


class CLITestCase(TestCase):
    '''
        Defines class CLITestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS CLI interfaces.
        CfgCLI unit tests.

        It defines:

            :attributes:
                | ats_cli_cfg_api - API for checking Cfg CLI.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSCliCfgAPI not None.
                | test_process - Test for process.
                | test_add_new_option_called - Test is add new option called.
                | test_parse_args_called - Test is parse args called.
                | test_parse_wrong_args_called - Test parse without args.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_cli_api: ATSCliCfgAPI = ATSCliCfgAPI()
        self.mock_add_new = MagicMock()
        self.mock_pars_arg = MagicMock()
        self.ats_cli_api.add_new_option = self.mock_add_new
        self.ats_cli_api.parse_args = self.mock_pars_arg

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create'''
        self.assertIsNotNone(self.ats_cli_api)

    def test_process(self) -> None:
        '''Test for process.'''
        self.assertTrue(self.ats_cli_api.process())

    def test_add_new_option_called(self) -> None:
        '''Test add new option for option parser'''
        self.ats_cli_api.add_new_option('arg1', 'arg2', option='value')
        self.mock_add_new.assert_called_once()

    def test_parse_args_called(self) -> None:
        '''Test parse args'''
        self.ats_cli_api.add_new_option('arg1', 'arg2', option='value')
        self.ats_cli_api.parse_args(['arg1', 'arg2'])
        self.mock_pars_arg.assert_called_once()

    def test_parse_wrong_args_called(self) -> None:
        '''Test parse without args'''
        self.ats_cli_api.add_new_option('arg1', 'arg2', option='value')
        self.assertIsNotNone(self.ats_cli_api.parse_args(None))


if __name__ == '__main__':
    main()
