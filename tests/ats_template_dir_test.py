# -*- coding: UTF-8 -*-

'''
Module
    ats_template_dir_test.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines classes ProNameTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of TemplateDir.
Execute
    python3 -m unittest -v ats_template_dir_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from ats_utilities.pro_config.template_dir import TemplateDir
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProNameTestCase(TestCase):
    '''
        Defines class ProNameTestCase with attribute(s) and method(s).
        Creates test cases for checking TemplateDir interfaces.
        TemplateDir unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default create.
                | test_set_dir_empty - Sets empty template dir.
                | test_set_dir_none - Sets None template dir.
                | test_set_dir - Sets simple template dir.
                | test_get_dir - Gets simple template dir.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default create'''
        template: TemplateDir = TemplateDir()
        self.assertIsNotNone(template)

    def test_set_dir_empty(self) -> None:
        '''Sets empty template dir'''
        template: TemplateDir = TemplateDir()
        empty_dir: str | None = ""
        template.template_dir = empty_dir
        self.assertFalse(template.is_template_dir_ok())

    def test_set_dir_none(self) -> None:
        '''Sets None template dir'''
        template: TemplateDir = TemplateDir()
        none_dir: str | None = None
        with self.assertRaises(ATSTypeError):
            template.template_dir = none_dir

    def test_dir(self) -> None:
        '''Sets simple template dir'''
        template: TemplateDir = TemplateDir()
        test_dir: str | None = "/opt"
        template.template_dir = test_dir
        self.assertTrue(template.is_template_dir_ok())

    def test_get_dir(self) -> None:
        '''Gets simple template dir'''
        template: TemplateDir = TemplateDir()
        test_dir: str | None = "/opt"
        template.template_dir = test_dir
        self.assertIsNotNone(template.template_dir)


if __name__ == '__main__':
    main()
