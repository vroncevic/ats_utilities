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
    Unit tests for UseGitHub class.
'''

from __future__ import annotations

import unittest

from ats_utilities.context.factory import ContextFactory
from ats_utilities.info.use_github.engine import UseGitHub

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class EngineTest(unittest.TestCase):
    '''
        Defines class EngineTest with attribute(s) and method(s).
        Tests UseGitHub component.

        It defines:

            :attributes: None.
            :methods:
                | test_init - Tests UseGitHub initialization.
                | test_property_get_set - Tests use_github setter/getter.
                | test_not_none - Tests not_none checks.
                | test_str - Tests __str__ method.
    '''

    def test_init(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        inst = UseGitHub(context_bundle)
        self.assertEqual(inst.use_github, False)

    def test_property_get_set(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        inst = UseGitHub(context_bundle)
        inst.use_github = True
        self.assertEqual(inst.use_github, True)

    def test_not_none(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        inst = UseGitHub(context_bundle)
        self.assertEqual(inst.not_none(), True)
        inst.use_github = True
        self.assertTrue(inst.not_none())

    def test_str(self) -> None:
        context_bundle = ContextFactory.create_default_context_bundle()
        inst = UseGitHub(context_bundle)
        self.assertIn("UseGitHub", str(inst))


if __name__ == "__main__":
    unittest.main()
