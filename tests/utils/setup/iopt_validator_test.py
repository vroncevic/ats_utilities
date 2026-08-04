# -*- coding: UTF-8 -*-

'''
Module
    iopt_validator_test.py
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
    Unit tests for IOptionsValidator protocol.
'''

from __future__ import annotations

import unittest

from ats_utilities.utils.setup.iopt_validator import IOptionsValidator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyOptValidatorValid:
    '''Dummy class that implements IOptionsValidator completely.'''

    @classmethod
    def validate(cls, options: object) -> None:
        if options is None:
            raise ValueError("Options cannot be None")


class DummyOptValidatorInvalid:
    '''Dummy class that does NOT implement IOptionsValidator.'''
    pass


class IOptionsValidatorTest(unittest.TestCase):
    '''
        Defines class IOptionsValidatorTest with method(s).
        Tests IOptionsValidator protocol behavior.

        It defines:

            :attributes: None.
            :methods:
                | test_isinstance_valid - Tests isinstance check with a valid implementation.
                | test_isinstance_invalid - Tests isinstance check with an invalid implementation.
    '''

    def test_isinstance_valid(self) -> None:
        '''
            Tests isinstance check with a valid implementation.

            :exceptions: None.
        '''
        dummy = DummyOptValidatorValid()
        self.assertIsInstance(dummy, IOptionsValidator)

    def test_isinstance_invalid(self) -> None:
        '''
            Tests isinstance check with an invalid implementation.

            :exceptions: None.
        '''
        dummy = DummyOptValidatorInvalid()
        self.assertNotIsInstance(dummy, IOptionsValidator)


if __name__ == "__main__":
    unittest.main()
