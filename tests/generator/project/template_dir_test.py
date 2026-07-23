# -*- coding: UTF-8 -*-

'''
Module
    template_dir_test.py
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
    Unit tests for TemplateDir class.
'''

from __future__ import annotations

import unittest

from ats_utilities.context.factory import ContextFactory
from ats_utilities.exceptions import ATSTypeError
from ats_utilities.generator.project.template_dir import TemplateDir

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TemplateDirTest(unittest.TestCase):
    '''
        Defines class TemplateDirTest with attribute(s) and method(s).
        Tests TemplateDir container logic.
    '''

    def test_init(self) -> None:
        context_bundle = ContextFactory.create_default_bundle()
        template_dir_obj = TemplateDir(context_bundle)
        self.assertIsNone(template_dir_obj.template_dir)
        self.assertFalse(template_dir_obj.not_none())

    def test_get_set_template_dir(self) -> None:
        context_bundle = ContextFactory.create_default_bundle()
        template_dir_obj = TemplateDir(context_bundle)
        dir_path = "/tmp/templates"
        template_dir_obj.template_dir = dir_path
        self.assertEqual(template_dir_obj.template_dir, dir_path)
        self.assertTrue(template_dir_obj.not_none())

    def test_set_template_dir_invalid_type(self) -> None:
        context_bundle = ContextFactory.create_default_bundle()
        template_dir_obj = TemplateDir(context_bundle)
        with self.assertRaises(ATSTypeError):
            template_dir_obj.template_dir = 123  # type: ignore

    def test_str(self) -> None:
        context_bundle = ContextFactory.create_default_bundle()
        template_dir_obj = TemplateDir(context_bundle)
        self.assertIn("TemplateDir", str(template_dir_obj))


if __name__ == "__main__":
    unittest.main()
