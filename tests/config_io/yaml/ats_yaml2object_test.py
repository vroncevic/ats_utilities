# -*- coding: UTF-8 -*-

'''
Module
    ats_yaml2object_test.py
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
    Defines classes Yaml2ObjectTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Yaml2Object.
Execute
    python3 -m unittest -v ats_yaml2object_test
'''

from unittest import TestCase, main, mock
from unittest.mock import MagicMock
from os.path import dirname
from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
from ats_utilities.exceptions import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class Yaml2ObjectTestCase(TestCase):
    '''
        Defines class Yaml2ObjectTestCase with attribute(s) and method(s).
        Creates test cases for checking Yaml2Object interfaces.
        Yaml2Object unit tests.

        It defines:

            :attributes:
                | yaml2obj - API for checking base Yaml2Object.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is Yaml2Object not None.
                | test_read_configuration - Test for read configuration.
                | test_none_config_path - Test for None as file path.
                | test_str - Test string representation of Yaml2Object.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.yaml2obj: Yaml2Object = Yaml2Object(
            f'{dirname(dirname(dirname(__file__)))}/assets/config/ats_cli_yaml_api.yaml'
        )

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create Yaml2Object'''
        self.assertIsNotNone(self.yaml2obj)

    def test_read_configuration(self) -> None:
        '''Test for read configuration'''
        self.assertIsNotNone(self.yaml2obj.read_configuration())

    @mock.patch('ats_utilities.config_io.yaml.yaml2object.ConfFile')
    def test_read_configuration_failure(self, mock_conf_file: MagicMock) -> None:
        '''Test read_configuration when file content is empty.'''
        mock_file = MagicMock()
        mock_file.read.return_value = ""
        mock_conf_file.return_value.__enter__.return_value = mock_file
        self.assertIsNone(self.yaml2obj.read_configuration())

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        yaml2obj = Yaml2Object(None)
        self.assertIsNone(yaml2obj.read_configuration())

    def test_str(self) -> None:
        '''Test string representation of Yaml2Object.'''
        self.assertIsInstance(str(self.yaml2obj), str)


if __name__ == '__main__':
    main()

