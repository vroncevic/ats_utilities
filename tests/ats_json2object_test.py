# -*- coding: UTF-8 -*-

'''
Module
    ats_json2object_test.py
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
    Defines classes Json2ObjectTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Json2Object.
Execute
    python3 -m unittest -v ats_json2object_test
'''

import sys
from typing import List
from unittest import TestCase, main
from os.path import dirname

try:
    from ats_utilities.config_io.json.json2object import Json2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
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


class Json2ObjectTestCase(TestCase):
    '''
        Defines class Json2ObjectTestCase with attribute(s) and method(s).
        Creates test cases for checking Json2Object interfaces.
        Json2Object unit tests.

        It defines:

            :attributes:
                | json2obj - API for checking base Json2Object.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is Json2Object not None.
                | test_read_configuration - Test for read configuration.
                | test_none_config_path - Test for None as file path.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.json2obj: Json2Object = Json2Object(
            f'{dirname(__file__)}/config/ats_cli_json_api.json'
        )

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create Json2Object'''
        self.assertIsNotNone(self.json2obj)

    def test_read_configuration(self) -> None:
        '''Test for read configuration'''
        self.assertIsNotNone(self.json2obj.read_configuration())

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        with self.assertRaises(ATSTypeError):
            Json2Object(None)


if __name__ == '__main__':
    main()
