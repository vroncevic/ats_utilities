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
    Defines classes ATSInfoTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ATSInfo.
Execute
    python -m unittest -v ats_info_test
'''

import sys
from unittest import TestCase, main

try:
    from ats_utilities.info import ATSInfo
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSInfoTestCase(TestCase):
    '''
        Defines classes ATSInfoTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATSInfo.

        It defines:

            :attributes:
                | base_info - Dict with base info.
                | ats_info - API for base info.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_show_base_info - Test for base info.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.base_info: dict[str, str] = {
            'ats_name': 'Simple Tool',
            'ats_version': '1.0.0',
            'ats_licence': 'GPLv3',
            'ats_build_date': 'Sun 25 Apr 2021 08:12:40 PM CEST'
        }
        self.ats_info = ATSInfo(self.base_info)

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_show_base_info(self) -> None:
        '''Test base info.'''
        self.ats_info.show_base_info()


if __name__ == '__main__':
    main()
