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
     Defined class ATSAbstractTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of AbstractMethod.
 Execute
     python -m unittest -v ats_option_test
'''

import sys
import unittest

try:
    from ats_utilities.option import ATSOptionParser
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.9.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSOptionTestCase(unittest.TestCase):
    '''
        Defined class ATSOptionTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of option parser.
        It defines:

            :attributes:
                | OPS - defined options.
                | option_ats - API for option parser.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_option_parser_short - test short.
                | test_option_parser_long - test long.
                | test_option_parser_with_verbose_short - test verbose short.
                | test_option_parser_with_verbose_long - test verbose long.
                | test_option_parser_all_short - test all short.
                | test_option_parser_all_long - test all long.
    '''

    OPS = ['-g', '--gen', '-vv', '--verbose']

    def setUp(self):
        '''Call before test case.'''
        self.option_ats = ATSOptionParser('1.0.0', 'xyz', 'abc')
        self.option_ats.add_operation(
            ATSOptionTestCase.OPS[0],
            ATSOptionTestCase.OPS[1],
            dest='gen', help='simple operation'
        )
        self.option_ats.add_operation(
            ATSOptionTestCase.OPS[2],
            ATSOptionTestCase.OPS[3],
            action='store_true', default=False,
            help='activate verbose mode for generation'
        )

    def tearDown(self):
        '''Call after test case.'''
        self.option_ats = None

    def test_option_parser_short(self):
        '''Test option parser short.'''
        arguments = ['-g', 'Test']
        args = self.option_ats.parse_args(arguments)

    def test_option_parser_long(self):
        '''Test option parser long.'''
        arguments = ['--gen', 'Test']
        args = self.option_ats.parse_args(arguments)

    def test_option_parser_with_verbose_short(self):
        '''Test option parser with verbose short.'''
        arguments = ['-vv']
        args = self.option_ats.parse_args(arguments)

    def test_option_parser_with_verbose_long(self):
        '''Test option parser with verbose long.'''
        arguments = ['--verbose']
        args = self.option_ats.parse_args(arguments)

    def test_option_parser_all_short(self):
        '''Test all combined short options.'''
        arguments = ['-g', 'Test', '-vv']
        args = self.option_ats.parse_args(arguments)

    def test_option_parser_all_long(self):
        '''Test all combined long options.'''
        arguments = ['--gen', 'Test', '--verbose']
        args = self.option_ats.parse_args(arguments)


if __name__ == '__main__':
    unittest.main()
