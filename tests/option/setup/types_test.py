# -*- coding: UTF-8 -*-

'''
Module
    types_test.py
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
    Unit tests for OptionNamespace protocol and type aliases.
'''

from __future__ import annotations

import unittest

from ats_utilities.option.setup.types import OptionNamespace


class DummyNamespace:
    '''
        A dummy class that implements the OptionNamespace protocol.
    '''
    def __init__(self, **kwargs: object) -> None:
        self.__dict__.update(kwargs)


class TypesTest(unittest.TestCase):
    '''
        Defines class TypesTest with attribute(s) and method(s).
        Tests OptionNamespace protocol compatibility.
    '''

    def test_protocol_implementation(self) -> None:
        instance: OptionNamespace = DummyNamespace(arg1="val1", arg2=123)
        self.assertEqual(instance.__dict__["arg1"], "val1")
        self.assertEqual(instance.__dict__["arg2"], 123)


if __name__ == "__main__":
    unittest.main()
