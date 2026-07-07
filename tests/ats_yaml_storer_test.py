# -*- coding: UTF-8 -*-

'''
Module
    ats_yaml_storer_test.py
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
    Defines class YAMLStorerTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of YAMLStorer.
Execute
    python3 -m unittest -v ats_yaml_storer_test
'''

from unittest import TestCase, main, mock
from unittest.mock import MagicMock
from ats_utilities.config_io.yaml.yaml_storer import YAMLStorer
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.yaml.iyaml_processor import IYAMLProcessor
from ats_utilities.config_io.yaml.object2yaml import Object2Yaml
from ats_utilities.config_io.yaml.yaml_processor import YAMLProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class YAMLStorerTestCase(TestCase):
    '''
        Defines class YAMLStorerTestCase with attribute(s) and method(s).
        Creates test cases for checking YAMLStorer interfaces.
        YAMLStorer unit tests.

        It defines:

            :methods:
                | test_not_none - Test is YAMLStorer not None.
                | test_store_configuration_success - Test storing configuration successfully.
                | test_store_configuration_decode_fail - Test storing configuration when decode fails.
                | test_str - Test string representation of YAMLStorer.
    '''

    def test_not_none(self) -> None:
        '''Test is YAMLStorer not None.'''
        storer = YAMLStorer(info_file='dummy.yaml')
        self.assertIsNotNone(storer)

    def test_store_configuration_success(self) -> None:
        '''Test storing configuration successfully.'''
        mock_obj2yaml = MagicMock(spec=Object2Yaml)
        mock_processor = MagicMock(spec=YAMLProcessor)
        
        mock_processor.decode.return_value = True
        mock_obj2yaml.write_configuration.return_value = True
        
        storer = YAMLStorer(
            info_file='dummy.yaml',
            object2yaml=mock_obj2yaml,
            yaml_processor=mock_processor
        )
        
        config = {'key': 'value'}
        result = storer.store_configuration(config)
        self.assertTrue(result)
        mock_processor.decode.assert_called_once()
        mock_obj2yaml.write_configuration.assert_called_once_with(mock_processor)

    def test_store_configuration_decode_fail(self) -> None:
        '''Test storing configuration when decode fails.'''
        mock_obj2yaml = MagicMock(spec=Object2Yaml)
        mock_processor = MagicMock(spec=YAMLProcessor)
        
        mock_processor.decode.return_value = False
        
        storer = YAMLStorer(
            info_file='dummy.yaml',
            object2yaml=mock_obj2yaml,
            yaml_processor=mock_processor
        )
        
        config = {'key': 'value'}
        result = storer.store_configuration(config)
        self.assertFalse(result)
        mock_processor.decode.assert_called_once()
        mock_obj2yaml.write_configuration.assert_not_called()

    def test_str(self) -> None:
        '''Test string representation of YAMLStorer.'''
        storer = YAMLStorer(info_file='dummy.yaml')
        self.assertIsInstance(str(storer), str)

    @mock.patch('ats_utilities.config_io.yaml.yaml_storer.dump')
    def test_store_configuration_serialize_fail(self, mock_dump) -> None:
        '''Test storing configuration when YAML serialization fails.'''
        mock_dump.side_effect = TypeError('Cannot dump to YAML')
        mock_obj2yaml = MagicMock(spec=Object2Yaml)
        mock_processor = MagicMock(spec=YAMLProcessor)
        storer = YAMLStorer(
            info_file='dummy.yaml',
            object2yaml=mock_obj2yaml,
            yaml_processor=mock_processor
        )
        config = {'key': 'value'}
        result = storer.store_configuration(config)
        self.assertFalse(result)


if __name__ == '__main__':
    main()

