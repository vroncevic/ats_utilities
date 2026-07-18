# -*- coding: UTF-8 -*-

'''
Module
    ats_key_error_test.py
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
    Unit tests for ATSKeyError exception class.
'''

from __future__ import annotations

import unittest

from ats_utilities.exceptions.ats_error import ATSError
from ats_utilities.exceptions.ats_key_error import ATSKeyError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ATSKeyErrorTest(unittest.TestCase):
    '''
        Defines class ATSKeyErrorTest with attribute(s) and method(s).
        Tests ATSKeyError exception class.

        It defines:

            :attributes: None.
            :methods:
                | test_exception_raise - Tests raising ATSKeyError.
    '''

    def test_exception_raise(self) -> None:
        '''
            Tests raising ATSKeyError.

            :exceptions: None.
        '''
        # KeyError formats its arguments differently, usually as repr(arg)
        with self.assertRaises(ATSKeyError) as ctx:
            raise ATSKeyError("test key error message")
        self.assertIn("test key error message", str(ctx.exception))
        self.assertIsInstance(ctx.exception, ATSError)
        self.assertIsInstance(ctx.exception, KeyError)


if __name__ == "__main__":
    unittest.main()
