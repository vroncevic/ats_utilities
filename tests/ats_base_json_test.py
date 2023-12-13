# -*- coding: UTF-8 -*-

'''
Module
    ats_base_json_test.py
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
    Defines classes JsonBaseTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Json.
Execute
    python3 -m unittest -v ats_base_json_test
'''

import sys
from typing import List
from unittest import TestCase, main
from os.path import dirname

try:
    from ats_utilities.config_io.json import JsonBase
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSBaseJson(JsonBase):
    '''Simple Class for checking JsonBase.'''

    _CONFIG: str = '/config/ats_cli_json_api.json'
    _OPS: List[str] = ['-t', '--test', '-v']

    def __init__(self, verbose: bool = False) -> None:
        '''Initial constructor.'''
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(base_info, verbose)
        self._verbose = verbose
        if self.tool_operational:
            verbose_message(self._verbose, ['init ATS json cli'])


class JsonBaseTestCase(TestCase):
    '''
        Defines class JsonBaseTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS Json interfaces.
        JsonBase unit tests.

        It defines:

            :attributes:
                | ats_base_json - API for checking base Json.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseJson not None.
                | test_tool_operational - Test is tool operational.
                | test_none_config_path - Test for None as file path.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_base_json: ATSBaseJson = ATSBaseJson()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create JsonBase'''
        self.assertIsNotNone(self.ats_base_json)

    def test_tool_operational(self) -> None:
        '''Test is tool operational'''
        self.assertTrue(self.ats_base_json.is_tool_ok())

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        with self.assertRaises(ATSTypeError):
            JsonBase(None)


if __name__ == '__main__':
    main()
