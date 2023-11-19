# -*- coding: UTF-8 -*-

'''
 Module
     ats_info_test.py
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
     Defined classes ATSInfoTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of ATSInfo.
 Execute
     python -m unittest -v ats_info_test
'''

import sys
import unittest

try:
    from ats_utilities.info import ATSInfo
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSInfoTestCase(unittest.TestCase):
    '''
        Defined classes ATSInfoTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ATSInfo.
        It defines:

            :attributes:
                | base_info - dict with base info.
                | ats_info - API for base info.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_show_base_info - test for base info.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.base_info = {
            'ats_name': 'Simple Tool',
            'ats_version': '1.0.0',
            'ats_licence': 'GPLv3',
            'ats_build_date': 'Sun 25 Apr 2021 08:12:40 PM CEST'
        }
        self.ats_info = ATSInfo(self.base_info)

    def tearDown(self):
        '''Call after test case.'''
        self.base_info = None
        self.ats_info = None

    def test_show_base_info(self):
        '''Test base info.'''
        self.ats_info.show_base_info()


if __name__ == '__main__':
    unittest.main()
