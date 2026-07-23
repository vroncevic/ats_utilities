# -*- coding: UTF-8 -*-

'''
Module
    option_namespace_test.py
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
    Unit tests for OptionNamespace protocol.
'''

from __future__ import annotations

import unittest
from typing import Any

from ats_utilities.option.option_namespace import OptionNamespace

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyNamespace:
    '''
        A dummy class that implements the OptionNamespace protocol.
    '''
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)


class OptionNamespaceTest(unittest.TestCase):
    '''
        Defines class OptionNamespaceTest with attribute(s) and method(s).
        Tests OptionNamespace protocol compatibility.

        It defines:

            :attributes: None.
            :methods:
                | test_protocol_implementation - Tests protocol implementation.
    '''

    def test_protocol_implementation(self) -> None:
        '''
            Tests protocol implementation.

            :exceptions: None.
        '''
        instance: OptionNamespace = DummyNamespace(arg1="val1", arg2=123)
        self.assertEqual(instance.__dict__["arg1"], "val1")
        self.assertEqual(instance.__dict__["arg2"], 123)


if __name__ == "__main__":
    unittest.main()
