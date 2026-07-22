# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Unit tests for Checker class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.checker.setup.bundle import CheckerBundle
from ats_utilities.checker.setup.factory import CheckerFactory
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.ichecker import ErrorChecker
from ats_utilities.exceptions import ATSTypeError, ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests Checker component logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init_valid - Tests successful Checker initialization.
                | test_init_invalid_none - Tests Checker initialization with None bundle.
                | test_init_invalid_type - Tests Checker initialization with wrong type.
                | test_validates_parameters_valid - Tests validates_parameters with valid parameters.
                | test_validates_parameters_none - Tests validates_parameters with None parameters list.
                | test_validates_parameters_format_error - Tests validates_parameters with format error.
                | test_validates_parameters_type_error - Tests validates_parameters with type error.
                | test_is_initialized - Tests is_initialized method.
                | test_str - Tests __str__ representation.
    '''

    def test_init_valid(self) -> None:
        bundle = CheckerFactory.create_default_bundle()
        checker = Checker(bundle)
        self.assertTrue(checker.is_initialized())

    def test_init_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            Checker(None)  # type: ignore

    def test_init_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            Checker("invalid")  # type: ignore

    def test_validates_parameters_valid(self) -> None:
        bundle = CheckerFactory.create_default_bundle()
        checker = Checker(bundle)
        msg, err_id = checker.validates_parameters([("str:param1", "test"), ("int:param2", 123)])
        self.assertEqual(err_id, ErrorChecker.NO_ERROR)
        self.assertIn("param1", msg)

    def test_validates_parameters_none(self) -> None:
        bundle = CheckerFactory.create_default_bundle()
        checker = Checker(bundle)
        msg, err_id = checker.validates_parameters(None)  # type: ignore
        self.assertEqual(err_id, ErrorChecker.FORMAT_ERROR)
        self.assertIn("format wrong", msg)

    def test_validates_parameters_format_error(self) -> None:
        bundle = CheckerFactory.create_default_bundle()
        checker = Checker(bundle)
        msg, err_id = checker.validates_parameters([("invalid_format", "test")])
        self.assertEqual(err_id, ErrorChecker.FORMAT_ERROR)
        self.assertIn("format wrong", msg)

    def test_validates_parameters_type_error(self) -> None:
        bundle = CheckerFactory.create_default_bundle()
        checker = Checker(bundle)
        msg, err_id = checker.validates_parameters([("int:param", "not_an_int")])
        self.assertEqual(err_id, ErrorChecker.TYPE_ERROR)
        self.assertIn("wrong type", msg)

    def test_validates_parameters_multiple_type_errors(self) -> None:
        bundle = CheckerFactory.create_default_bundle()
        checker = Checker(bundle)
        msg, err_id = checker.validates_parameters([
            ("int:param1", "not_an_int"),
            ("str:param2", 123)
        ])
        self.assertEqual(err_id, ErrorChecker.TYPE_ERROR)
        self.assertIn("wrong type", msg)

    def test_is_initialized(self) -> None:
        bundle = CheckerFactory.create_default_bundle()
        checker = Checker(bundle)
        self.assertTrue(checker.is_initialized())

    def test_str(self) -> None:
        bundle = CheckerFactory.create_default_bundle()
        checker = Checker(bundle)
        self.assertIn("Checker", str(checker))


if __name__ == "__main__":
    unittest.main()
