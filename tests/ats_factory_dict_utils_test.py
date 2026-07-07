# -*- coding: UTF-8 -*-

'''
Module
    ats_factory_dict_utils_test.py
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
    Defines class ATSFactoryDictUtilsTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of factory_dict_utils functions.
Execute
    python3 -m unittest -v ats_factory_dict_utils_test
'''

from unittest import TestCase, main
from ats_utilities.factory_dict_utils import cherry_pick_dict, has_required_keys, require_keys
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class ATSFactoryDictUtilsTestCase(TestCase):
    '''
        Defines class ATSFactoryDictUtilsTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of factory_dict_utils functions.
    '''

    def test_cherry_pick_dict_success(self) -> None:
        source = {'a': 1, 'b': 2, 'c': 3}
        keys = frozenset(['a', 'c', 'd'])
        res = cherry_pick_dict(source, keys)
        self.assertEqual(res, {'a': 1, 'c': 3})

    def test_cherry_pick_dict_empty_source(self) -> None:
        keys = frozenset(['a'])
        self.assertEqual(cherry_pick_dict(None, keys), {})
        self.assertEqual(cherry_pick_dict({}, keys), {})

    def test_cherry_pick_dict_empty_keys(self) -> None:
        source = {'a': 1}
        self.assertEqual(cherry_pick_dict(source, frozenset()), {})

    def test_has_required_keys_true(self) -> None:
        source = {'a': 1, 'b': 2}
        keys = frozenset(['a'])
        self.assertTrue(has_required_keys(source, keys))

    def test_has_required_keys_false(self) -> None:
        source = {'a': 1, 'b': 2}
        keys = frozenset(['c'])
        self.assertFalse(has_required_keys(source, keys))

    def test_require_keys_success(self) -> None:
        source = {'a': 1, 'b': 2}
        keys = frozenset(['a', 'b'])
        require_keys(source, keys)

    def test_require_keys_missing_keys(self) -> None:
        source = {'a': 1}
        keys = frozenset(['a', 'b'])
        with self.assertRaises(ATSValueError):
            require_keys(source, keys)

    def test_require_keys_invalid_source(self) -> None:
        keys = frozenset(['a'])
        with self.assertRaises(ATSTypeError):
            require_keys("not a dict", keys)

    def test_require_keys_invalid_keys(self) -> None:
        source = {'a': 1}
        with self.assertRaises(ATSTypeError):
            require_keys(source, ['a'])  # type: ignore


if __name__ == '__main__':
    main()
