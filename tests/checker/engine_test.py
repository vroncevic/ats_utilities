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
from ats_utilities.checker.setup.factory import CheckerBundleFactory
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.setup.types import CheckerErrorType
from ats_utilities.exceptions import ATSTypeError, ATSValueError


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests Checker component logic.
    '''

    def test_init_valid(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        self.assertTrue(checker.is_initialized())

    def test_init_invalid_none(self) -> None:
        with self.assertRaises(ATSValueError):
            Checker(None)  # type: ignore

    def test_init_invalid_type(self) -> None:
        with self.assertRaises(ATSTypeError):
            Checker("invalid")  # type: ignore

    def test_validates_parameters_valid(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        msg, err_id = checker.validates_parameters([("str:param1", "test"), ("int:param2", 123)])
        self.assertEqual(err_id, CheckerErrorType.NO_ERROR)
        self.assertIn("param1", msg)

    def test_validates_parameters_none(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        msg, err_id = checker.validates_parameters(None)  # type: ignore
        self.assertEqual(err_id, CheckerErrorType.FORMAT_ERROR)
        self.assertIn("format wrong", msg)

    def test_validates_parameters_format_error(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        msg, err_id = checker.validates_parameters([("invalid_format", "test")])
        self.assertEqual(err_id, CheckerErrorType.FORMAT_ERROR)
        self.assertIn("format wrong", msg)

    def test_validates_parameters_type_error(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        msg, err_id = checker.validates_parameters([("int:param", "not_an_int")])
        self.assertEqual(err_id, CheckerErrorType.TYPE_ERROR)
        self.assertIn("wrong type", msg)

    def test_validates_parameters_multiple_type_errors(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        msg, err_id = checker.validates_parameters([
            ("int:param1", "not_an_int"),
            ("str:param2", 123)
        ])
        self.assertEqual(err_id, CheckerErrorType.TYPE_ERROR)
        self.assertIn("wrong type", msg)

    def test_is_initialized(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        self.assertTrue(checker.is_initialized())

    def test_str(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        self.assertIn("Checker", str(checker))

    def test_get_bundle(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        retrieved = checker.get_bundle()
        self.assertIsInstance(retrieved, CheckerBundle)

    def test_update_bundle(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        
        # Valid update
        new_bundle = CheckerBundleFactory.create_bundle()
        self.assertTrue(checker.update_bundle(new_bundle))
        
        # Invalid update
        self.assertFalse(checker.update_bundle("invalid" * 10))  # type: ignore

    def test_getters(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        self.assertIs(checker.get_format_validator(), bundle.format_validator)
        self.assertIs(checker.get_type_validator(), bundle.type_validator)
        self.assertIs(checker.get_context_provider(), bundle.context_provider)
        self.assertIs(checker.get_check_reporter(), bundle.check_reporter)

    def test_validates_parameters_reporter_exception(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        # Mock build_message to raise ATSValueError
        checker._check_reporter.build_message = MagicMock(side_effect=ATSValueError("mock"))
        
        # When parameters is None (covers L205)
        msg, err_id = checker.validates_parameters(None)  # type: ignore
        self.assertEqual(err_id, CheckerErrorType.FORMAT_ERROR)
        
        # When normal call fails (covers L252)
        msg, err_id = checker.validates_parameters([("str:param1", "test")])
        self.assertEqual(err_id, CheckerErrorType.NO_ERROR)

    def test_validates_parameters_format_validation_check_failure(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        # "a:b:c" is invalid format (len(split) == 3 != 2)
        msg, err_id = checker.validates_parameters([("a:b:c", "val")])
        self.assertEqual(err_id, CheckerErrorType.FORMAT_ERROR)

    def test_validates_parameters_multiple_errors_branch_coverage(self) -> None:
        bundle = CheckerBundleFactory.create_bundle()
        checker = Checker(bundle)
        
        # Mock is_match to raise error after first failure
        calls = 0
        def mock_is_match(inst, ptype):
            nonlocal calls
            calls += 1
            if calls == 1:
                return False
            raise ATSValueError("mock type error")
            
        checker._type_validator.is_match = mock_is_match
        msg, err_id = checker.validates_parameters([
            ("str:param1", "val1"),
            ("str:param2", "val2")
        ])
        self.assertEqual(err_id, CheckerErrorType.TYPE_ERROR)


if __name__ == "__main__":
    unittest.main()
