# -*- coding: UTF-8 -*-

'''
Module
    ats_checker_test.py
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
    Defines class ATSCheckerTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATS param checker.
Execute
    python3 -m unittest -v ats_checker_test
'''

import sys
from typing import Any, Dict, Tuple, List, Set, Optional
from collections import OrderedDict
from unittest import TestCase, main

try:
    from ats_utilities.checker import ATSChecker
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.2.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSCheckerTestCase(TestCase):
    '''
        Defines class ATSCheckerTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS param checker.
        ATSChecker unit tests.

        It defines:

            :attributes:
                | checker - API for checking parameters.
                | error_msg - error message from ATSChecker.
                | error_id - error status from ATSChecker.
            :methods:
                | setUp - call before every test case.
                | tearDown - call after every test case.
                | test_str_parameter - Test for string param checking.
                | test_int_parameter - Test for int param checking.
                | test_float_parameter - Test for float param checking.
                | test_complex_parameter - Test for complex param checking.
                | test_bool_parameter - Test for bool param checking.
                | test_bytearray_parameter - Test for bytearray param checking.
                | test_bytes_parameter - Test for bytes param checking.
                | test_dict_parameter - Test for dict param checking.
                | test_frozenset_parameter - Test for frozenset param checking.
                | test_list_parameter - Test for list param checking.
                | test_set_parameter - Test for set param checking.
                | test_tuple_parameter - Test for tuple param checking.
                | test_object_parameter - Test for object param checking.
                | test_type_error - Test for type param checking.
                | test_value_error - Test for value param checking.
    '''

    def setUp(self) -> None:
        '''Call before every test case.'''
        self.checker: ATSChecker = ATSChecker()
        self.error_msg: Optional[str] = None
        self.error_id: Optional[int] = -1

    def tearDown(self) -> None:
        '''Call after every test case.'''
        self.error_msg = None
        self.error_id = -1

    def test_checker_not_none(self) -> None:
        '''Test for checker not None.'''
        self.assertIsNotNone(self.checker)

    def test_none_collect_parameter(self) -> None:
        '''Test for None param collecting.'''
        self.assertFalse(self.checker.collect_params(None))  # type: ignore

    def test_none_check_type_parameter(self) -> None:
        '''Test for None param checking type.'''
        self.assertFalse(self.checker.check_types(None))  # type: ignore

    def test_none_check_priority_error(self) -> None:
        '''Test for None param checking type.'''
        self.checker.check_types(None)  # type: ignore
        self.assertEqual(
            self.checker.priority_error(), self.checker.FORMAT_ERROR
        )

    def test_str_parameter(self) -> None:
        '''Test for string param checking.'''
        simple_var: str = '8'
        self.error_msg, self.error_id = self.checker.check_params([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_int_parameter(self) -> None:
        '''Test for int param checking.'''
        simple_var: int = 2342425252
        self.error_msg, self.error_id = self.checker.check_params([
            ('int:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_float_parameter(self) -> None:
        '''Test for float param checking.'''
        simple_var: float = 34.4546464
        self.error_msg, self.error_id = self.checker.check_params([
            ('float:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_complex_parameter(self) -> None:
        '''Test for complex param checking.'''
        simple_var: complex = 3 + 6j
        self.error_msg, self.error_id = self.checker.check_params([
            ('complex:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_bool_parameter(self) -> None:
        '''Test for bool param checking.'''
        simple_var: bool = True
        self.error_msg, self.error_id = self.checker.check_params([
            ('bool:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_bytearray_parameter(self) -> None:
        '''Test for bytearray param checking.'''
        simple_var: bytearray = bytearray(b'hello')
        self.error_msg, self.error_id = self.checker.check_params([
            ('bytearray:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_bytes_parameter(self) -> None:
        '''Test for bytes param checking.'''
        simple_var: bytes = bytes(b'hello')
        self.error_msg, self.error_id = self.checker.check_params([
            ('bytes:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_dict_parameter(self) -> None:
        '''Test for dict param checking.'''
        simple_var: Dict[Any, Any] = {'a': 1, 'b': 2, 3: "test"}
        self.error_msg, self.error_id = self.checker.check_params([
            ('dict:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_frozenset_parameter(self) -> None:
        '''Test for frozenset param checking.'''
        simple_var: frozenset[int] = frozenset([123, 12, 34, 3443, 3434])
        self.error_msg, self.error_id = self.checker.check_params([
            ('frozenset:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_list_parameter(self) -> None:
        '''Test for list param checking.'''
        simple_var: List[Any] = ['8', 34, 43.343533, {'a', 'bs'}]
        self.error_msg, self.error_id = self.checker.check_params([
            ('list:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_set_parameter(self) -> None:
        '''Call test for set param checking.'''
        simple_var: Set[str] = {'apple', 'banana', 'cherry'}
        self.error_msg, self.error_id = self.checker.check_params([
            ('set:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_tuple_parameter(self) -> None:
        '''Test for tuple param checking.'''
        simple_var: Tuple[Any, ...] = ('quick test', 8, 32.4, [-99, 8, 3.4])
        self.error_msg, self.error_id = self.checker.check_params([
            ('tuple:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_object_parameter(self) -> None:
        '''Test for object param checking.'''
        simple_var: object = object()
        self.error_msg, self.error_id = self.checker.check_params([
            ('object:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 0)

    def test_type_error(self) -> None:
        '''Test for type param checking.'''
        simple_var: Tuple[Any, ...] = ('quick test', 8, 32.4, [-99, 8, 3.4])
        self.error_msg, self.error_id = self.checker.check_params([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 1)

    def test_value_error(self) -> None:
        '''Test for value param checking.'''
        simple_var = None
        self.error_msg, self.error_id = self.checker.check_params([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, 1)

    def test_collect_params(self) -> None:
        '''Test for collect parameters.'''
        self.assertFalse(self.checker.collect_params(OrderedDict([])))

    def test_check_type_params(self) -> None:
        '''Test for check type parameters.'''
        self.assertFalse(self.checker.check_types(OrderedDict([])))

    def test_check_type_params_missing_description(self) -> None:
        '''Test for check value parameters.'''
        simple_config: int = 0
        complex_config: str = 'test'
        self.assertFalse(
            self.checker.check_types(
                OrderedDict(
                    [
                        ('', simple_config), ('', complex_config)
                    ]
                )
            )
        )

    def test_non_base_type_check(self) -> None:
        '''Test for check non base type'''

        class Test:
            '''Simple type'''

            def __init__(self) -> None:
                '''Initial Test Constructor'''
                self.var: int = 0

        test = Test()
        self.assertTrue(self.checker.check_types(OrderedDict([
            ('Test:test', test)
        ])))

    def test_check_value_params_base_none(self) -> None:
        '''Test for check value parameters.'''
        simple_config: Optional[int] = None
        self.assertFalse(
            self.checker.check_types(OrderedDict([('', simple_config)]))
        )


if __name__ == '__main__':
    main()
