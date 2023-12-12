# -*- coding: UTF-8 -*-

'''
Module
    ats_object2yaml_test.py
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
    Defines classes Object2YamlTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Object2Yaml.
Execute
    python3 -m unittest -v ats_object2yaml_test
'''

import sys
from typing import List
from unittest import TestCase, main
from os.path import dirname

try:
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.config_io.yaml.object2yaml import Object2Yaml
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Object2YamlTestCase(TestCase):
    '''
        Defines class Object2YamlTestCase with attribute(s) and method(s).
        Creates test cases for checking Object2Yaml interfaces.
        Object2Yaml unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is Object2Yaml not None.
                | test_write_configuration - Test for write configuration.
                | test_write_none_configuration - Write none configuration.
                | test_write_empty_configuration - Write empty configuration.
                | test_none_config_path - Test for None as file path.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create Object2Yaml'''
        obj2yaml: Object2Yaml = Object2Yaml(
            f'{dirname(__file__)}/config/ats_cli_yaml_api.yaml'
        )
        self.assertIsNotNone(obj2yaml)

    def test_write_configuration(self) -> None:
        '''Test for write configuration'''
        obj2yaml: Object2Yaml = Object2Yaml(
            f'{dirname(__file__)}/config/ats_cli_yaml_api.yaml'
        )
        yaml2obj: Yaml2Object = Yaml2Object(
            f'{dirname(__file__)}/config/ats_cli_yaml_api.yaml'
        )
        self.assertTrue(obj2yaml.write_configuration(
            yaml2obj.read_configuration()
        ))

    def test_write_none_configuration(self) -> None:
        '''Test for write none configuration'''
        obj2yaml: Object2Yaml = Object2Yaml(
            f'{dirname(__file__)}/config/ats_cli_yaml_api_none.yaml'
        )
        with self.assertRaises(ATSTypeError):
            obj2yaml.write_configuration(None)  # type: ignore

    def test_write_empty_configuration(self) -> None:
        '''Test for write empty configuration'''
        obj2yaml: Object2Yaml = Object2Yaml(
            f'{dirname(__file__)}/config/ats_cli_yaml_api_empty.yaml'
        )
        self.assertFalse(obj2yaml.write_configuration({}))

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        with self.assertRaises(ATSTypeError):
            Object2Yaml(None)


if __name__ == '__main__':
    main()
