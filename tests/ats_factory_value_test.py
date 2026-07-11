# -*- coding: UTF-8 -*-

'''
Module
    ats_factory_value_test.py
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
    Defines classes ATSFactoryValueTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATS Factory Value.
Execute
    python3 -m unittest -v tests/ats_factory_value_test.py
'''

from unittest import TestCase, main
from ats_utilities.factory_value import require_not_none, require_not_empty, require_not_satisfied
from ats_utilities.exceptions import ATSValueError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class ATSFactoryValueTestCase(TestCase):
    '''
        Defines classes ATSFactoryValueTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS Factory Value.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_require_not_none_success(self) -> None:
        '''Test require_not_none with a non-None value.'''
        require_not_none("test")
        require_not_none(0)
        require_not_none(False)

    def test_require_not_none_failure(self) -> None:
        '''Test require_not_none with None raises ATSValueError.'''
        with self.assertRaises(ATSValueError):
            require_not_none(None)

    def test_require_not_none_custom_exception(self) -> None:
        '''Test require_not_none raises custom exception.'''
        with self.assertRaises(ValueError):
            require_not_none(None, exception_class=ValueError)

    def test_require_not_none_message_path(self) -> None:
        '''Test require_not_none exception contains path details.'''
        with self.assertRaises(ATSValueError) as context:
            require_not_none(None, exc_message_path="some/config/path")
        self.assertIn("some/config/path", str(context.exception))

    def test_require_not_empty_success(self) -> None:
        '''Test require_not_empty with non-empty values.'''
        require_not_empty("test")
        require_not_empty([1, 2])
        require_not_empty(0)  # 0 is explicitly allowed
        require_not_empty(False)  # False is explicitly allowed

    def test_require_not_empty_failure(self) -> None:
        '''Test require_not_empty with empty values raises ATSValueError.'''
        with self.assertRaises(ATSValueError):
            require_not_empty(None)
        with self.assertRaises(ATSValueError):
            require_not_empty("")
        with self.assertRaises(ATSValueError):
            require_not_empty([])
        with self.assertRaises(ATSValueError):
            require_not_empty({})

    def test_require_not_empty_custom_exception(self) -> None:
        '''Test require_not_empty raises custom exception.'''
        with self.assertRaises(ValueError):
            require_not_empty("", exception_class=ValueError)

    def test_require_not_empty_message_path(self) -> None:
        '''Test require_not_empty exception contains path details.'''
        with self.assertRaises(ATSValueError) as context:
            require_not_empty("", exc_message_path="some/config/path")
        self.assertIn("some/config/path", str(context.exception))

    def test_require_not_satisfied_success(self) -> None:
        '''Test require_not_satisfied with False (happy path).'''
        require_not_satisfied(False)

    def test_require_not_satisfied_failure(self) -> None:
        '''Test require_not_satisfied with True raises ATSValueError.'''
        with self.assertRaises(ATSValueError):
            require_not_satisfied(True)

    def test_require_not_satisfied_custom_exception(self) -> None:
        '''Test require_not_satisfied raises custom exception.'''
        with self.assertRaises(ValueError):
            require_not_satisfied(True, exception_class=ValueError)

    def test_require_not_satisfied_message_path(self) -> None:
        '''Test require_not_satisfied exception contains path details.'''
        with self.assertRaises(ATSValueError) as context:
            require_not_satisfied(True, exc_message_path="some/config/path")
        self.assertIn("some/config/path", str(context.exception))


if __name__ == '__main__':
    main()
