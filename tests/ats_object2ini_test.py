# -*- coding: UTF-8 -*-

'''
Module
    ats_object2ini_test.py
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
    Defines classes Object2IniTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Object2Ini.
Execute
    python3 -m unittest -v ats_object2ini_test
'''

import sys
from typing import List
from configparser import ConfigParser
from unittest import TestCase, main
from os.path import dirname

try:
    from ats_utilities.config_io.ini.ini2object import Ini2Object
    from ats_utilities.config_io.ini.object2ini import Object2Ini
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Object2IniTestCase(TestCase):
    '''
        Defines class Object2IniTestCase with attribute(s) and method(s).
        Creates test cases for checking Object2Ini interfaces.
        Object2Ini unit tests.

        It defines:

            :attributes:
                | obj2ini - API for checking base Object2Ini.
                | ini2obj - API for checking base Ini2Object.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is Object2Ini not None.
                | test_read_configuration - Test for read configuration.
                | test_none_config_path - Test for None as file path.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ini2obj: Ini2Object = Ini2Object(
            f'{dirname(__file__)}/config/ats_cli_ini_api.ini'
        )
        self.obj2ini: Object2Ini = Object2Ini(
            f'{dirname(__file__)}/config/ats_cli_ini_api.ini'
        )

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create Object2Ini'''
        self.assertIsNotNone(self.obj2ini)

    def test_write_configuration(self) -> None:
        '''Test for read configuration'''
        configuration: ConfigParser | None = self.ini2obj.read_configuration()
        self.assertTrue(self.obj2ini.write_configuration(configuration))

    def test_write_none_configuration(self) -> None:
        '''Test for read configuration'''
        with self.assertRaises(ATSTypeError):
            self.obj2ini.write_configuration(None)  # type: ignore

    def test_write_empty_configuration(self) -> None:
        '''Test for read configuration'''
        self.assertFalse(self.obj2ini.write_configuration(ConfigParser()))

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        with self.assertRaises(ATSTypeError):
            Object2Ini(None)


if __name__ == '__main__':
    main()
