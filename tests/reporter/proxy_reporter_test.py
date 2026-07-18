# -*- coding: UTF-8 -*-

'''
Module
    proxy_reporter_test.py
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
    Unit tests for @vreport decorator in proxy_reporter.py.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.exceptions import ATSAttributeError, ATSRuntimeError, ATSValueError
from ats_utilities.reporter.proxy_reporter import vreport

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ProxyReporterTest(unittest.TestCase):
    '''
        Defines class ProxyReporterTest with attribute(s) and method(s).
        Tests @vreport decorator.

        It defines:

            :attributes: None.
            :methods:
                | test_decorator_empty_templates - Tests decorator with empty templates list.
                | test_decorator_not_method - Tests decorator on a non-method function.
                | test_decorator_missing_reporter - Tests decorator when class has no reporter.
                | test_decorator_success_formatting - Tests placeholder formatting logic.
                | test_decorator_formatting_error_fallback - Tests fallback when format fails.
    '''

    def test_decorator_empty_templates(self) -> None:
        with self.assertRaises(ATSValueError):
            vreport([])

    def test_decorator_not_method(self) -> None:
        @vreport("template")
        def dummy_func() -> None:
            pass

        with self.assertRaises(ATSRuntimeError):
            dummy_func()

    def test_decorator_missing_reporter(self) -> None:
        class Dummy:
            @vreport("template")
            def do_something(self) -> None:
                pass

        d = Dummy()
        with self.assertRaises(ATSAttributeError):
            d.do_something()

    def test_decorator_success_formatting(self) -> None:
        mock_reporter = MagicMock()
        mock_reporter.verbose = MagicMock()

        class MyClass:
            def __init__(self) -> None:
                self._reporter = mock_reporter
                self._verbose = True
                # Mangled private attribute
                self.__private_val = "private"
                # Protected attribute
                self._protected_val = "protected"
                # Public attribute in __dict__
                self.public_val = "public"
                # Attribute not in __dict__, but available via property
                self._prop_val = "property"

            @property
            def prop_val(self) -> str:
                return self._prop_val

            @vreport([
                "Private: {private_val}",
                "Protected: {protected_val}",
                "Public: {public_val}",
                "Prop: {prop_val}",
                "Result: {my_method}",
                "Missing: {missing_val}"
            ])
            def my_method(self) -> str:
                return "result_value"

        obj = MyClass()
        res = obj.my_method()
        self.assertEqual(res, "result_value")

        expected_messages = [
            "Private: private",
            "Protected: protected",
            "Public: public",
            "Prop: property",
            "Result: result_value",
            "Missing: None"
        ]
        mock_reporter.verbose.assert_called_once_with(True, expected_messages)

    def test_decorator_formatting_error_fallback(self) -> None:
        mock_reporter = MagicMock()
        mock_reporter.verbose = MagicMock()

        class ErrorClass:
            def __init__(self) -> None:
                self._reporter = mock_reporter
                self._verbose = False

            # Template referencing index or invalid key that causes formatting error
            @vreport("Invalid: {0} {non_existent}")
            def call_me(self) -> None:
                pass

        obj = ErrorClass()
        obj.call_me()
        # Should fallback to passing the unformatted template
        mock_reporter.verbose.assert_called_once_with(False, ["Invalid: {0} {non_existent}"])


if __name__ == "__main__":
    unittest.main()
