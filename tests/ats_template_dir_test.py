# -*- coding: UTF-8 -*-

'''
Module
    ats_template_dir_test.py
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
    Defines classes TemplateDirTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of TemplateDir.
Execute
    python3 -m unittest -v ats_template_dir_test
'''

from typing import List, Optional
from unittest import TestCase, main
from ats_utilities.pro_config.template_dir import TemplateDir
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBaseTemplateDir(TemplateDir):
    '''Simple Class for checking TemplateDir.'''

    def __init__(self, reporter: IATSReporter = ATSReporter(), verbose: bool = False) -> None:
        '''Initial constructor.'''
        super().__init__()
        self._verbose = verbose
        if self.is_tool_ok():
            reporter.success(['init template dir'])

    def is_tool_ok(self) -> bool:
        '''
            Check is template dir operational.

            :return: Is template dir operational
            :rtype: <bool>
        '''
        return bool(self.template_dir)


class TemplateDirTestCase(TestCase):
    '''
        Defines class TemplateDirTestCase with attribute(s) and method(s).
        Creates test cases for checking TemplateDir interfaces.
        TemplateDir unit tests.

        It defines:

            :attributes:
                | ats_base_template_dir - API for checking base TemplateDir.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseTemplateDir not None.
                | test_tool_operational - Test is tool operational.
                | test_set_dir_empty - Sets empty template dir.
                | test_set_dir_none - Sets None template dir.
                | test_set_dir - Sets simple template dir.
                | test_get_dir - Gets simple template dir.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_base_template_dir: ATSBaseTemplateDir = ATSBaseTemplateDir()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create TemplateDir'''
        self.assertIsNotNone(self.ats_base_template_dir)

    def test_tool_operational(self) -> None:
        '''Test is tool operational'''
        self.assertFalse(self.ats_base_template_dir.is_tool_ok())

    def test_set_dir_empty(self) -> None:
        '''Sets empty template dir'''
        empty_dir: Optional[str] = ""
        self.ats_base_template_dir.template_dir = empty_dir
        self.assertFalse(self.ats_base_template_dir.is_tool_ok())

    def test_set_dir_none(self) -> None:
        '''Sets None template dir'''
        none_dir: Optional[str] = None
        with self.assertRaises(ATSTypeError):
            self.ats_base_template_dir.template_dir = none_dir

    def test_set_dir(self) -> None:
        '''Sets simple template dir'''
        test_dir: Optional[str] = "/opt"
        self.ats_base_template_dir.template_dir = test_dir
        self.assertTrue(self.ats_base_template_dir.is_tool_ok())

    def test_get_dir(self) -> None:
        '''Gets simple template dir'''
        test_dir: Optional[str] = "/opt"
        self.ats_base_template_dir.template_dir = test_dir
        self.assertIsNotNone(self.ats_base_template_dir.template_dir)


if __name__ == '__main__':
    main()
