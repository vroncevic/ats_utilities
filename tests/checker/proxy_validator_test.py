# -*- coding: UTF-8 -*-

'''
Module
    proxy_validator_test.py
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
    Unit tests for mcheck and fcheck decorators in proxy_validator.py.
'''

from __future__ import annotations

import unittest
from typing import Any
from unittest.mock import MagicMock

from ats_utilities.checker.setup.factory import CheckerFactory
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.ichecker import ErrorChecker
from ats_utilities.checker.proxy_validator import mcheck, fcheck
from ats_utilities.exceptions import ATSAttributeError, ATSRuntimeError, ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyClass:
    def __init__(self, use_checker: bool = True) -> None:
        if use_checker:
            self._checker = Checker(CheckerFactory.create_default_bundle())

    @mcheck([('str:name', None), ('int:value', None)])
    def my_method(self, name: str, value: int) -> str:
        return f"{name}-{value}"

    @mcheck([('str:name', None), ('int:nonexistent_param', None)])
    def method_unbound(self, name: str) -> str:
        return name


@mcheck([('str:name', None)])
def invalid_vcheck_free(name: str) -> str:
    return name


@mcheck([])
def invalid_vcheck_free_no_args() -> str:
    return "no_args"


@fcheck([('str:name', None), ('int:value', None)])
def my_helper(name: str, value: int) -> str:
    return f"{name}-{value}"


@fcheck([('str | None:name', None)])
def my_optional_helper(name: str | None = None) -> str | None:
    return name


@fcheck([('str:name', None), ('int:nonexistent_param', None)])
def helper_unbound(name: str) -> str:
    return name


class ProxyValidatorTest(unittest.TestCase):
    '''
        Defines class ProxyValidatorTest with attribute(s) and method(s).
        Tests mcheck and fcheck decorators logic.

        It defines:

            :attributes: None.
            :methods:
                | test_vcheck_valid - Tests successful mcheck usage.
                | test_vcheck_invalid_type - Tests mcheck raising ATSTypeError.
                | test_vcheck_invalid_format - Tests mcheck raising ATSValueError.
                | test_vcheck_non_class_method - Tests mcheck on free function.
                | test_vcheck_missing_checker - Tests mcheck on class without _checker.
                | test_vcheck_unbound_param - Tests mcheck with parameter not in function signature.
                | test_vcheck_required_param_none - Tests mcheck with required parameter set to None.
                | test_vcheck_mocked_format_error - Tests mcheck format error path via mocking.
                | test_fcheck_valid - Tests successful fcheck usage.
                | test_fcheck_invalid_type - Tests fcheck raising ATSTypeError.
                | test_fcheck_invalid_format - Tests fcheck raising ATSValueError.
                | test_fcheck_optional - Tests fcheck with optional parameter.
                | test_fcheck_unbound_param - Tests fcheck with parameter not in function signature.
                | test_fcheck_required_param_none - Tests fcheck with required parameter set to None.
                | test_fcheck_mocked_format_error - Tests fcheck format error path via mocking.
    '''

    def test_vcheck_valid(self) -> None:
        obj = DummyClass()
        self.assertEqual(obj.my_method("test", 123), "test-123")

    def test_vcheck_invalid_type(self) -> None:
        obj = DummyClass()
        with self.assertRaises(ATSTypeError):
            obj.my_method(123, 123)  # type: ignore

        with self.assertRaises(ATSTypeError):
            obj.my_method("test", "not_int")  # type: ignore

    def test_vcheck_invalid_format(self) -> None:
        class BadSpecClass:
            def __init__(self) -> None:
                self._checker = Checker(CheckerFactory.create_default_bundle())

            @mcheck([('invalid_format', None)])
            def bad_method(self, name: str) -> str:
                return name

        obj = BadSpecClass()
        with self.assertRaises(ATSValueError):
            obj.bad_method("test")

    def test_vcheck_non_class_method(self) -> None:
        with self.assertRaises(ATSRuntimeError):
            invalid_vcheck_free("test")

        with self.assertRaises(ATSRuntimeError):
            invalid_vcheck_free_no_args()

    def test_vcheck_missing_checker(self) -> None:
        obj = DummyClass(use_checker=False)
        with self.assertRaises(ATSRuntimeError):
            obj.my_method("test", 123)

    def test_vcheck_unbound_param(self) -> None:
        obj = DummyClass()
        # nonexistent_param spec will be skipped as it's not in actual_params_dict
        self.assertEqual(obj.method_unbound("test"), "test")

    def test_vcheck_required_param_none(self) -> None:
        obj = DummyClass()
        with self.assertRaises(ATSTypeError):
            obj.my_method("test", None)  # type: ignore

    def test_vcheck_mocked_format_error(self) -> None:
        obj = DummyClass()
        # Mock validates_parameters to return FORMAT_ERROR
        obj._checker.validates_parameters = MagicMock(
            return_value=("Mock format error", ErrorChecker.FORMAT_ERROR)
        )
        with self.assertRaises(ATSValueError):
            obj.my_method("test", 123)

    def test_fcheck_valid(self) -> None:
        self.assertEqual(my_helper("test", 123), "test-123")

    def test_fcheck_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            my_helper(123, 123)  # type: ignore

        with self.assertRaises(ATSTypeError):
            my_helper("test", "not_int")  # type: ignore

    def test_fcheck_invalid_format(self) -> None:
        @fcheck([('invalid_format', None)])
        def bad_helper(name: str) -> str:
            return name

        with self.assertRaises(ATSValueError):
            bad_helper("test")

    def test_fcheck_optional(self) -> None:
        self.assertIsNone(my_optional_helper(None))
        self.assertEqual(my_optional_helper("test"), "test")
        with self.assertRaises(ATSTypeError):
            my_optional_helper(123)  # type: ignore

    def test_fcheck_unbound_param(self) -> None:
        self.assertEqual(helper_unbound("test"), "test")

    def test_fcheck_required_param_none(self) -> None:
        with self.assertRaises(ATSTypeError):
            my_helper("test", None)  # type: ignore

    def test_fcheck_mocked_format_error(self) -> None:
        checker = None
        for cell in (my_helper.__closure__ or []):
            if isinstance(cell.cell_contents, Checker):
                checker = cell.cell_contents
                break

        if checker is None:
            self.fail("Could not find Checker in my_helper closure")

        original_validates = checker.validates_parameters
        checker.validates_parameters = MagicMock(
            return_value=("Mock format error", ErrorChecker.FORMAT_ERROR)
        )
        try:
            with self.assertRaises(ATSValueError):
                my_helper("test", 123)
        finally:
            checker.validates_parameters = original_validates


if __name__ == "__main__":
    unittest.main()
