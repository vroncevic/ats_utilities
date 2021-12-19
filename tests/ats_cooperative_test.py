# -*- coding: UTF-8 -*-

'''
 Module
     ats_cooperative_test.py
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
     Defined class ATSCooperativeTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of CooperativeMeta.
 Execute
     python -m unittest -v ats_cooperative_test
'''

import sys
import unittest

try:
    from ats_utilities.cooperative import CooperativeMeta
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.1.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MetaType(type):
    '''Simple Class for checking CooperativeMeta.'''
    pass


class MetaValue(type):
    '''Simple Class for checking CooperativeMeta.'''
    pass


class MetaInstance(type):
    '''Simple Class for checking CooperativeMeta.'''
    pass


class MetaClass(type):
    '''Simple Class for checking CooperativeMeta.'''
    pass


class SetupType:
    '''Simple Class for checking CooperativeMeta.'''
    __metaclass__ = MetaType


class SetupValue:
    '''Simple Class for checking CooperativeMeta.'''
    __metaclass__ = MetaValue


class SetupInstance:
    '''Simple Class for checking CooperativeMeta.'''
    __metaclass__ = MetaInstance


class SetupClass:
    '''Simple Class for checking CooperativeMeta.'''
    __metaclass__ = MetaClass


class Fixed(SetupType, SetupValue, SetupInstance, SetupClass):
    '''Simple Class for checking CooperativeMeta.'''
    __metaclass__ = CooperativeMeta


class ATSCooperativeTestCase(unittest.TestCase):
    '''
        Defined class ATSCooperativeTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of CooperativeMeta.
        It defines:

            :attributes:
                | None
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_cooperative_meta - test for cooperative meta.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.fixed_object = None

    def tearDown(self):
        '''Call after test case.'''
        self.fixed_object = None

    def test_cooperative_meta(self):
        '''Test for cooperative meta.'''
        self.fixed_object = Fixed()


if __name__ == '__main__':
    unittest.main()
