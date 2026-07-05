# -*- coding: utf-8 -*-

'''
Module
    story_ats_checker.py
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
    Use cases for ATS checker.
'''

from __future__ import annotations

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.factory_class import to_str

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class TestData:
    '''
        Defines class Version with attribute(s) and method(s).
        Creates an API for the ATS version in one property object.

        It defines:

            :attributes:
                | _checker - Checker with parameters validation capabilities (default Checker).
                | _data - Dictionary for testing (default {}).
            :methods:
                | __init__ - Initializes TestData constructor.
                | data - Property methods for set/get data.
                | __str__ - Returns the TestData as string representation.
    '''

    _checker: IChecker

    def __init__(self) -> None:
        '''
            Initializes TestData constructor.

            :exceptions: None.
        '''
        self._checker = Checker()
        self._data: dict[str, int] = {}

    @property
    def data(self) -> dict[str, int]:
        '''
            Property method for getting data.

            :return: The data as dictionary representation.
            :rtype: <dict[str, int]>
            :exceptions: None.
        '''
        return self._data

    @data.setter
    @vcheck([('dict[str, int]:data', None)])
    def data(self, data: dict[str, int]) -> None:
        '''
            Property method for setting data.

            :param data: The data as dictionary representation.
            :type data: <dict[str, int]>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_checker' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._data = data

    @vcheck([('dict[str, int]:data', None)])
    def set_my_data(self, data: dict[str, int]) -> None:
        """
         set_my_data method.

        :param data: The data as dictionary representation.
        :type data: <dict[str, int]>
        :exceptions:
            | ATSRuntimeError: Decorator cannot be used on a standalone function.
            | ATSAttributeError: Class is required to provide a '_checker' object to
            |                    use the @vreport decorator.
            | ATSTypeError: Parameter type validation failed.
            | ATSValueError: Parameter format validation failed.
            | ATSRuntimeError: Decorator used on a non-class method.
            | ATSAttributeError: Class does not provide a '_checker' object.
        """
        self._data = data

    def __str__(self) -> str:
        '''
            Returns the TestData as string representation.

            :return: The TestData as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)


test_data = TestData()

try:
    test_data.data = {'a': 1, 'b': 2}
    print(f"test_data.data: {test_data.data}\n")

except Exception as exc:
    print(f"Caught expected error: {exc}\n")

try:
    test_data.data = {}
    print(f"test_data.data: {test_data.data}\n")

except Exception as exc:
    print(f"Caught expected error: {exc}\n")

try:
    test_data.data = {'a': 1, 'b': 'c'}
    print(f"test_data.data: {test_data.data}\n")

except Exception as exc:
    print(f"Caught expected error: {exc}\n")

try:
    test_data.data = tuple()
    print(f"test_data.data: {test_data.data}\n")

except Exception as exc:
    print(f"Caught expected error: {exc}\n")

try:
    test_data.data = (2, 'a')
    print(f"test_data.data: {test_data.data}\n")

except Exception as exc:
    print(f"Caught expected error: {exc}\n")

try:
    test_data.data = tuple()
    print(f"test_data.data: {test_data.data}\n")

except Exception as exc:
    print(f"Caught expected error: {exc}\n")

try:
    test_data.data = (2, 'a')
    print(f"test_data.data: {test_data.data}\n")

except Exception as exc:
    print(f"Caught expected error: {exc}\n")

try:
    test_data.set_my_data(('a', 'b', 'c'))
    print(f"test_data.data: {test_data.data}\n")

except Exception as exc:
    print(f"Caught expected error: {exc}\n")
