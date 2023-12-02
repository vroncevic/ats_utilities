# -*- coding: UTF-8 -*-

'''
Module
    ats_option_test.py
Copyright
    Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class ATSAbstractTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of AbstractMethod.
Execute
    python3 -m unittest -v ats_option_test
'''

import sys
from unittest import TestCase, main
from argparse import Namespace

try:
    from ats_utilities.option import ATSOptionParser
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSOptionTestCase(TestCase):
    '''
        Defines class ATSOptionTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of option parser.

        It defines:

            :attributes:
                | OPS - Defined options.
                | option_ats - API for option parser.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_option_parser_short - Test short.
                | test_option_parser_long - Test long.
                | test_option_parser_with_verbose_short - Test verbose short.
                | test_option_parser_with_verbose_long - Test verbose long.
                | test_option_parser_all_short - Test all short.
                | test_option_parser_all_long - Test all long.
                | test_option_parser_wrong_argument - Test argument types.
    '''

    OPS: list[str] = ['-g', '--gen', '-vv', '--verbose']

    def setUp(self) -> None:
        '''Call before test case.'''
        self.option_ats = ATSOptionParser('1.0.0', 'xyz', 'abc')
        self.option_ats.add_operation(
            self.OPS[0], self.OPS[1], dest='gen', help='simple operation'
        )
        self.option_ats.add_operation(
            self.OPS[2], self.OPS[3],
            action='store_true', default=False,
            help='activate verbose mode for generation'
        )

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_create_with_wrong_arguments(self) -> None:
        '''Test wrong argument types'''
        with self.assertRaises(ATSTypeError):
            ATSOptionParser(None, None, None)

    def test_option_parser_short(self) -> None:
        '''Test option parser short.'''
        arguments: list[str] = ['-g', 'Test']
        args: Namespace = self.option_ats.parse_args(arguments)
        self.assertIsNotNone(args)

    def test_option_parser_long(self) -> None:
        '''Test option parser long.'''
        arguments: list[str] = ['--gen', 'Test']
        args: Namespace = self.option_ats.parse_args(arguments)
        self.assertIsNotNone(args)

    def test_option_parser_with_verbose_short(self) -> None:
        '''Test option parser with verbose short.'''
        arguments: list[str] = ['-vv']
        args: Namespace = self.option_ats.parse_args(arguments)
        self.assertIsNotNone(args)

    def test_option_parser_with_verbose_long(self) -> None:
        '''Test option parser with verbose long.'''
        arguments: list[str] = ['--verbose']
        args: Namespace = self.option_ats.parse_args(arguments)
        self.assertIsNotNone(args)

    def test_option_parser_all_short(self) -> None:
        '''Test all combined short options.'''
        arguments: list[str] = ['-g', 'Test', '-vv']
        args: Namespace = self.option_ats.parse_args(arguments)
        self.assertIsNotNone(args)

    def test_option_parser_all_long(self) -> None:
        '''Test all combined long options.'''
        arguments: list[str] = ['--gen', 'Test', '--verbose']
        args: Namespace = self.option_ats.parse_args(arguments)
        self.assertIsNotNone(args)


if __name__ == '__main__':
    main()
