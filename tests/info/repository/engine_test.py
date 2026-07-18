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
    Unit tests for Repository class.
'''

from __future__ import annotations

import unittest

from ats_utilities.context.context_registry import ContextRegistry
from ats_utilities.info.repository.engine import Repository

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests Repository component.

        It defines:

            :attributes: None.
            :methods:
                | test_init - Tests Repository initialization.
                | test_property_get_set - Tests repository setter/getter.
                | test_not_none - Tests not_none checks.
                | test_str - Tests __str__ method.
    '''

    def test_init(self) -> None:
        context_bundle = ContextRegistry.create_default_context_bundle()
        inst = Repository(context_bundle)
        self.assertEqual(inst.repository, None)

    def test_property_get_set(self) -> None:
        context_bundle = ContextRegistry.create_default_context_bundle()
        inst = Repository(context_bundle)
        inst.repository = 'https://github.com/vroncevic/ats_utilities'
        self.assertEqual(inst.repository, 'https://github.com/vroncevic/ats_utilities')

    def test_not_none(self) -> None:
        context_bundle = ContextRegistry.create_default_context_bundle()
        inst = Repository(context_bundle)
        self.assertEqual(inst.not_none(), False)
        inst.repository = 'https://github.com/vroncevic/ats_utilities'
        self.assertTrue(inst.not_none())

    def test_str(self) -> None:
        context_bundle = ContextRegistry.create_default_context_bundle()
        inst = Repository(context_bundle)
        self.assertIn("Repository", str(inst))


if __name__ == "__main__":
    unittest.main()
