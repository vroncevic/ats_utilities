# -*- coding: UTF-8 -*-

'''
Module
    ats_checker_test.py
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
    Defines class ATSCheckerTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATS param checker.
Execute
    python3 -m unittest -v ats_checker_test
'''

from typing import Any, Dict, Tuple, List, Set, Optional
from unittest import TestCase, main, mock
from ats_utilities.checker.engine import ATSChecker
from ats_utilities.checker.ichecker import ErrorChecker, IChecker, ParametersSpecs
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import ATSReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBaseChecker(ATSChecker):
    '''Simple Class for checking ATSChecker.'''

    def __init__(self, reporter: IReporter = ATSReporter(), verbose: bool = False) -> None:
        '''Initial constructor.'''
        super().__init__()
        self._verbose = verbose
        if self.is_tool_ok():
            reporter.success(['init ATS checker'])

    def is_tool_ok(self) -> bool:
        '''
            Check is checker operational.

            :return: Is checker operational
            :rtype: <bool>
        '''
        return True


class ATSCheckerTestCase(TestCase):
    '''
        Defines class ATSCheckerTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS param checker.
        ATSChecker unit tests.

        It defines:
            :attributes:
                | ats_base_checker - API for checking base parameters.
                | error_msg - Error message from ATSChecker.
                | error_id - Error status from ATSChecker.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseChecker not None.
                | test_tool_operational - Test is tool operational.
    '''

    def setUp(self) -> None:
        '''Call before every test case.'''
        self.ats_base_checker: ATSBaseChecker = ATSBaseChecker()
        self.error_msg: str = ''
        self.error_id: int = -1

    def tearDown(self) -> None:
        '''Call after every test case.'''
        self.error_msg = ''
        self.error_id = -1

    def test_not_none(self) -> None:
        '''Test for checker not None.'''
        self.assertIsNotNone(self.ats_base_checker)

    def test_tool_operational(self) -> None:
        '''Test is tool operational'''
        self.assertTrue(self.ats_base_checker.is_tool_ok())

    def test_check_params_none_input(self) -> None:
        '''Test handling of None input for parameters.'''
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters(None)
        self.assertEqual(self.error_id, ErrorChecker.FORMAT_ERROR)
        self.assertIn('format wrong', self.error_msg.lower())

    def test_format_error_detection(self) -> None:
        '''Test detection of invalid format strings.'''
        # ATSFormatValidator expects "type:name"
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('invalid_format', 'some_value')
        ])
        self.assertEqual(self.error_id, ErrorChecker.FORMAT_ERROR)
        self.assertIn('format wrong', self.error_msg.lower())

    def test_str_parameter(self) -> None:
        '''Test for string param checking.'''
        simple_var: str = '8'
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_int_parameter(self) -> None:
        '''Test for int param checking.'''
        simple_var: int = 2342425252
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('int:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_float_parameter(self) -> None:
        '''Test for float param checking.'''
        simple_var: float = 34.4546464
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('float:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_complex_parameter(self) -> None:
        '''Test for complex param checking.'''
        simple_var: complex = 3 + 6j
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('complex:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_bool_parameter(self) -> None:
        '''Test for bool param checking.'''
        simple_var: bool = True
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('bool:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_bytearray_parameter(self) -> None:
        '''Test for bytearray param checking.'''
        simple_var: bytearray = bytearray(b'hello')
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('bytearray:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_bytes_parameter(self) -> None:
        '''Test for bytes param checking.'''
        simple_var: bytes = bytes(b'hello')
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('bytes:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_dict_parameter(self) -> None:
        '''Test for dict param checking.'''
        simple_var: Dict[Any, Any] = {'a': 1, 'b': 2, 3: "test"}
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('dict:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_frozenset_parameter(self) -> None:
        '''Test for frozenset param checking.'''
        simple_var: frozenset[int] = frozenset([123, 12, 34, 3443, 3434])
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('frozenset:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_list_parameter(self) -> None:
        '''Test for list param checking.'''
        simple_var: List[Any] = ['8', 34, 43.343533, {'a', 'bs'}]
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('list:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_set_parameter(self) -> None:
        '''Call test for set param checking.'''
        simple_var: Set[str] = {'apple', 'banana', 'cherry'}
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('set:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_tuple_parameter(self) -> None:
        '''Test for tuple param checking.'''
        simple_var: Tuple[Any, ...] = ('quick test', 8, 32.4, [-99, 8, 3.4])
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('tuple:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_object_parameter(self) -> None:
        '''Test for object param checking.'''
        simple_var: object = object()
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('object:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_type_error(self) -> None:
        '''Test for type param checking.'''
        simple_var: Tuple[Any, ...] = ('quick test', 8, 32.4, [-99, 8, 3.4])
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.TYPE_ERROR)

    def test_value_error(self) -> None:
        '''Test for None as a value when string is expected.'''
        simple_var = None
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('str:simple_var', simple_var)
        ])
        self.assertEqual(self.error_id, ErrorChecker.TYPE_ERROR)

    def test_non_base_type_check(self) -> None:
        '''Test for checking custom object types.'''
        class Test:
            '''Custom test object used for non-base type parameter checking.'''

            def __init__(self) -> None:
                self.var: int = 0

            def get_var(self) -> int:
                '''Get the value of var.'''
                return self.var

            def set_var(self, var: int) -> None:
                '''Set the value of var.'''
                self.var = var

        test = Test()
        # Using default TypeValidator which checks type(inst).__name__
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('Test:test', test)
        ])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_multiple_parameters_success(self) -> None:
        '''Test validation of multiple parameters.'''
        params: Optional[ParametersSpecs] = [('str:p1', 'v1'), ('int:p2', 2), ('float:p3', 3.0)]
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters(params)
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_multiple_parameters_failure(self) -> None:
        '''Test validation of multiple parameters where one fails.'''
        params: Optional[ParametersSpecs] = [('str:p1', 'v1'), ('int:p2', 'not_an_int')]
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters(params)
        self.assertEqual(self.error_id, ErrorChecker.TYPE_ERROR)

    def test_empty_parameters_list(self) -> None:
        '''Test validation with an empty list of parameters.'''
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([])
        self.assertEqual(self.error_id, ErrorChecker.NO_ERROR)

    def test_validate_parameters_wrong_type_format(self) -> None:
        '''Test detection of invalid type in format string.'''
        self.error_msg, self.error_id = self.ats_base_checker.validate_parameters([
            ('unknown_type:var', 'value')
        ])
        self.assertEqual(self.error_id, ErrorChecker.TYPE_ERROR)


class ATSCheckerUnitTestCase(TestCase):
    '''
        Unit tests for IChecker interface using mocks.

        It defines:
            :methods:
                | setUp - Set up test environment with mocks.
                | test_mock_validate_parameters - Test mock interaction.
    '''

    def setUp(self) -> None:
        '''Set up test environment.'''
        self.mock_checker = mock.MagicMock(spec=IChecker)

    def test_mock_validate_parameters(self) -> None:
        '''Test mock interaction for validate_parameters.'''
        self.mock_checker.validate_parameters.return_value = ('', 0)
        result = self.mock_checker.validate_parameters([('str:test', 'value')])
        self.assertEqual(result, ('', 0))
        self.mock_checker.validate_parameters.assert_called_once()


if __name__ == '__main__':
    main()
