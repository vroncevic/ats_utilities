# -*- coding: UTF-8 -*-

'''
Module
    ats_factory_utils_test.py
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
    Defines class ATSFactoryUtilsTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of factory_utils functions.
Execute
    python3 -m unittest -v ats_factory_utils_test
'''

from unittest import TestCase, main
from ats_utilities.factory_utils import cherry_pick_dict, has_required_keys, require_keys, check_file_exists
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSFactoryUtilsTestCase(TestCase):
    '''
        Defines class ATSFactoryUtilsTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of factory_utils functions.
        Factory utils functions unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_cherry_pick_dict_success - Test cherry_pick_dict with valid inputs.
                | test_cherry_pick_dict_empty_source - Test cherry_pick_dict with empty/None source.
                | test_cherry_pick_dict_empty_keys - Test cherry_pick_dict with empty/None keys.
                | test_has_required_keys_true - Test has_required_keys returning True.
                | test_has_required_keys_false - Test has_required_keys returning False.
                | test_require_keys_success - Test require_keys validation success.
                | test_require_keys_missing_keys - Test require_keys raising ATSValueError.
                | test_require_keys_invalid_source - Test require_keys raising ATSTypeError for source.
                | test_require_keys_invalid_keys - Test require_keys raising ATSTypeError for keys.
                | test_check_file_exists_success - Test check_file_exists with existing file.
                | test_check_file_exists_failure - Test check_file_exists with non-existing file.
                | test_check_file_exists_invalid_type - Test check_file_exists with invalid type parameter.
    '''

    def test_cherry_pick_dict_success(self) -> None:
        '''
            Test cherry_pick_dict with valid inputs.

            :exceptions: None.
        '''
        source = {'a': 1, 'b': 2, 'c': 3}
        keys = frozenset(['a', 'c', 'd'])
        res = cherry_pick_dict(source, keys)
        self.assertEqual(res, {'a': 1, 'c': 3})

    def test_cherry_pick_dict_empty_source(self) -> None:
        '''
            Test cherry_pick_dict with empty/None source.

            :exceptions: None.
        '''
        keys = frozenset(['a'])
        self.assertEqual(cherry_pick_dict(None, keys), {})
        self.assertEqual(cherry_pick_dict({}, keys), {})

    def test_cherry_pick_dict_empty_keys(self) -> None:
        '''
            Test cherry_pick_dict with empty/None keys.

            :exceptions: None.
        '''
        source = {'a': 1}
        self.assertEqual(cherry_pick_dict(source, frozenset()), {})

    def test_has_required_keys_true(self) -> None:
        '''
            Test has_required_keys returning True.

            :exceptions: None.
        '''
        source = {'a': 1, 'b': 2}
        keys = frozenset(['a'])
        self.assertTrue(has_required_keys(source, keys))

    def test_has_required_keys_false(self) -> None:
        '''
            Test has_required_keys returning False.

            :exceptions: None.
        '''
        source = {'a': 1, 'b': 2}
        keys = frozenset(['c'])
        self.assertFalse(has_required_keys(source, keys))

    def test_require_keys_success(self) -> None:
        '''
            Test require_keys validation success.

            :exceptions: None.
        '''
        source = {'a': 1, 'b': 2}
        keys = frozenset(['a', 'b'])
        require_keys(source, keys)

    def test_require_keys_missing_keys(self) -> None:
        '''
            Test require_keys raising ATSValueError.

            :exceptions: None.
        '''
        source = {'a': 1}
        keys = frozenset(['a', 'b'])
        with self.assertRaises(ATSValueError):
            require_keys(source, keys)

    def test_require_keys_invalid_source(self) -> None:
        '''
            Test require_keys raising ATSTypeError for source.

            :exceptions: None.
        '''
        keys = frozenset(['a'])
        with self.assertRaises(ATSTypeError):
            require_keys("not a dict", keys)

    def test_require_keys_invalid_keys(self) -> None:
        '''
            Test require_keys raising ATSTypeError for keys.

            :exceptions: None.
        '''
        source = {'a': 1}
        with self.assertRaises(ATSTypeError):
            require_keys(source, ['a'])  # type: ignore

    def test_check_file_exists_success(self) -> None:
        '''
            Test check_file_exists with existing file.

            :exceptions: None.
        '''
        check_file_exists(__file__)

    def test_check_file_exists_failure(self) -> None:
        '''
            Test check_file_exists with non-existing file.

            :exceptions: None.
        '''
        with self.assertRaises(ATSValueError):
            check_file_exists("non_existing_file_path_12345.txt")

    def test_check_file_exists_invalid_type(self) -> None:
        '''
            Test check_file_exists with invalid type parameter.

            :exceptions: None.
        '''
        with self.assertRaises(ATSTypeError):
            check_file_exists(123)  # type: ignore


if __name__ == '__main__':
    main()
