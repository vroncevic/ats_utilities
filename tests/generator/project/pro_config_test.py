# -*- coding: UTF-8 -*-

'''
Module
    pro_config_test.py
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
    Unit tests for ProConfig class.
'''

from __future__ import annotations

import unittest

from ats_utilities.context.factory import ContextFactory
from ats_utilities.exceptions import ATSTypeError
from ats_utilities.generator.project.pro_config import ProConfig

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ProConfigTest(unittest.TestCase):
    '''
        Defines class ProConfigTest with attribute(s) and method(s).
        Tests ProConfig container logic.
    '''

    def test_init(self) -> None:
        context_bundle = ContextFactory.create_default_bundle()
        pro_config_obj = ProConfig(context_bundle)
        self.assertIsNone(pro_config_obj.config)
        self.assertFalse(pro_config_obj.not_none())

    def test_get_set_pro_config(self) -> None:
        context_bundle = ContextFactory.create_default_bundle()
        pro_config_obj = ProConfig(context_bundle)
        config_data = {
            "key1": "value1",
            "key2": 123
        }
        pro_config_obj.config = config_data
        self.assertEqual(pro_config_obj.config, config_data)
        self.assertTrue(pro_config_obj.not_none())

    def test_set_pro_config_invalid_type(self) -> None:
        context_bundle = ContextFactory.create_default_bundle()
        pro_config_obj = ProConfig(context_bundle)
        with self.assertRaises(ATSTypeError):
            pro_config_obj.config = 123  # type: ignore

    def test_str(self) -> None:
        context_bundle = ContextFactory.create_default_bundle()
        pro_config_obj = ProConfig(context_bundle)
        self.assertIn("ProConfig", str(pro_config_obj))


if __name__ == "__main__":
    unittest.main()
