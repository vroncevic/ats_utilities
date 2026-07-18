# -*- coding: UTF-8 -*-

'''
Module
    pro_name_test.py
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
    Unit tests for ProName class.
'''

from __future__ import annotations

import unittest

from ats_utilities.context.context_registry import ContextRegistry
from ats_utilities.exceptions import ATSTypeError
from ats_utilities.project_setup.pro_name import ProName

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ProNameTest(unittest.TestCase):
    '''
        Defines class ProNameTest with attribute(s) and method(s).
        Tests ProName container logic.

        It defines:

            :attributes: None.
            :methods:
                | test_init - Tests ProName constructor and initial state.
                | test_get_set_pro_name - Tests getting/setting project name and not_none.
                | test_set_pro_name_invalid_type - Tests setting invalid name type.
                | test_str - Tests __str__ representation.
    '''

    def test_init(self) -> None:
        '''
            Tests ProName constructor and initial state.

            :exceptions: None.
        '''
        context_bundle = ContextRegistry.create_default_context_bundle()
        pro_name_obj = ProName(context_bundle)
        self.assertIsNone(pro_name_obj.pro_name)
        self.assertFalse(pro_name_obj.not_none())

    def test_get_set_pro_name(self) -> None:
        '''
            Tests getting/setting project name and not_none.

            :exceptions: None.
        '''
        context_bundle = ContextRegistry.create_default_context_bundle()
        pro_name_obj = ProName(context_bundle)
        pro_name_obj.pro_name = "test_project"
        self.assertEqual(pro_name_obj.pro_name, "test_project")
        self.assertTrue(pro_name_obj.not_none())

    def test_set_pro_name_invalid_type(self) -> None:
        '''
            Tests setting invalid name type.

            :exceptions: None.
        '''
        context_bundle = ContextRegistry.create_default_context_bundle()
        pro_name_obj = ProName(context_bundle)
        with self.assertRaises(ATSTypeError):
            pro_name_obj.pro_name = 123  # type: ignore

    def test_str(self) -> None:
        '''
            Tests __str__ representation.

            :exceptions: None.
        '''
        context_bundle = ContextRegistry.create_default_context_bundle()
        pro_name_obj = ProName(context_bundle)
        self.assertIn("ProName", str(pro_name_obj))


if __name__ == "__main__":
    unittest.main()
