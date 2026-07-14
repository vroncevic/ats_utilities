# -*- coding: UTF-8 -*-

'''
Module
    ats_proxy_reporter_test.py
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
    Defines class ProxyReporterTestCase with attribute(s) and method(s).
    Creates test cases for checking ProxyReporter (vreport decorator).
Execute
    python3 -m unittest -v tests/reporter/ats_proxy_reporter_test.py
'''

from __future__ import annotations

from unittest import TestCase, main, mock
from ats_utilities.exceptions import ATSAttributeError, ATSRuntimeError, ATSValueError
from ats_utilities.reporter.proxy_reporter import vreport

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ProxyReporterTestCase(TestCase):
    '''
        Defines class ProxyReporterTestCase with attribute(s) and method(s).
        Creates test cases for checking ProxyReporter (vreport decorator).
    '''

    def test_vreport_decorator_failures_and_features(self) -> None:
        '''Test various paths and errors in vreport decorator.'''
        # 1. Non-class method call
        @vreport("test")
        def dummy_func(*args, **kwargs):
            return True
        with self.assertRaises(ATSRuntimeError):
            dummy_func()

        # 2. Missing reporter
        class DummyNoReporter:
            @vreport("test")
            def some_method(self):
                return True

        with self.assertRaises(ATSAttributeError):
            DummyNoReporter().some_method()

        # 3. Private mangled attribute, public attribute, and result formatting
        mock_rep = mock.MagicMock()
        class DummyWithReporter:
            def __init__(self):
                self._reporter = mock_rep
                self._verbose = True
                self.__mangled = "mangled_val"
                self.public_val = "public_val"

            @vreport("mangled is {mangled}")
            def get_mangled(self):
                return True

            @vreport("public is {public_val}")
            def get_public(self):
                return True

            @vreport("res is {get_res}")
            def get_res(self):
                return "res_val"

            @vreport("test {0}")
            def trigger_index_err(self):
                return True

        d = DummyWithReporter()

        # Test private mangled
        d.get_mangled()
        mock_rep.verbose.assert_called_with(True, ["mangled is mangled_val"])

        # Test public
        d.get_public()
        mock_rep.verbose.assert_called_with(True, ["public is public_val"])

        # Test result placeholder
        d.get_res()
        mock_rep.verbose.assert_called_with(True, ["res is res_val"])

        # Test format error fallback
        d.trigger_index_err()

        with self.assertRaises(ATSValueError):
            @vreport([])
            def dummy_empty_list():
                pass



if __name__ == '__main__':
    main()
