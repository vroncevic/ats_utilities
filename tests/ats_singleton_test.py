# -*- coding: UTF-8 -*-

'''
 Module
     ats_singleton_test.py
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
     Defined class ATSSingletonTestCase with attribute(s) and method(s).
     Created test case for checking functionalities of singleton.
 Execute
     python -m unittest -v ats_singleton_test
'''

import sys
import unittest

try:
    from ats_utilities.singleton.base import Singleton
    from ats_utilities.singleton.meta import SingletonMeta
    from ats_utilities.singleton.functional import FunctionalSingleton
    from ats_utilities.singleton.meta_thread import ThreadSafeSingletonMeta
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.8.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSSingletonClassTestBase(Singleton):
    '''Simple Class for checking Singleton based on base class.'''

    def __init__(self):
        '''Initial constructor.'''
        self.source_field = None
        self.target_field = None


class ATSSingletonClassTestMeta:
    '''Simple Class for checking Singleton based on meta class.'''

    __metaclass__ = SingletonMeta

    def __init__(self):
        '''Initial constructor.'''
        self.source_field = None
        self.target_field = None


@FunctionalSingleton
class ATSSingletonClassTestFunctional:
    '''Simple Class for checking Singleton based on decorator.'''

    def __init__(self):
        '''Initial constructor.'''
        self.source_field = None
        self.target_field = None


class ATSSingletonClassTestMetaThread:
    '''Simple Class for checking Singleton based on meta thread class.'''

    __metaclass__ = ThreadSafeSingletonMeta

    def __init__(self):
        '''Initial constructor.'''
        self.source_field = None
        self.target_field = None


class ATSSingletonTestCase(unittest.TestCase):
    '''
        Defined class ATSSingletonTestCase with attribute(s) and method(s).
        Created test case for checking functionalities of singleton.
        It defines:

            :attributes:
                | class_obj_one_base - API object for checking singleton.
                | class_obj_two_base - API object for checking singleton.
                | class_obj_one_meta - API object for checking singleton.
                | class_obj_two_meta - API object for checking singleton.
                | class_obj_one_func - API object for checking singleton.
                | class_obj_two_func - API object for checking singleton.
                | class_obj_one_thread - API object for checking singleton.
                | class_obj_two_thread - API object for checking singleton.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_same_object_base - test singleton-check objects.
                | test_class_id_base - test singleton-check ids.
                | test_same_object_meta - test singleton-check objects.
                | test_class_id_meta - test singleton-check ids.
                | test_same_object_func - test singleton-check objects.
                | test_class_id_func - test singleton-check ids.
                | test_same_object_meta_thread - test singleton-check objects.
                | test_class_id_meta_thread - test singleton-check ids.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.class_obj_one_base = ATSSingletonClassTestBase()
        self.class_obj_two_base = ATSSingletonClassTestBase()
        self.class_obj_one_meta = ATSSingletonClassTestMeta()
        self.class_obj_two_meta = ATSSingletonClassTestMeta()
        self.class_obj_one_func = ATSSingletonClassTestFunctional()
        self.class_obj_two_func = ATSSingletonClassTestFunctional()
        self.class_obj_one_thread = ATSSingletonClassTestMetaThread()
        self.class_obj_two_thread = ATSSingletonClassTestMetaThread()

    def tearDown(self):
        '''Call after test case.'''
        self.class_obj_one_base = None
        self.class_obj_two_base = None
        self.class_obj_one_meta = None
        self.class_obj_two_meta = None
        self.class_obj_one_func = None
        self.class_obj_two_func = None
        self.class_obj_one_thread = None
        self.class_obj_two_thread = None

    def test_same_object_base(self):
        '''Test for singleton (Base) - check objects.'''
        self.assertTrue(
            self.class_obj_one_base is self.class_obj_two_base,
            'it is not same object - checked by objects'
        )

    def test_class_id_base(self):
        '''Test for singleton (Base) - check ids.'''
        id_one = id(ATSSingletonClassTestBase())
        id_two = id(ATSSingletonClassTestBase())
        self.assertTrue(
            id_one == id_two, 'it is not same object - checked by ids'
        )

    def test_same_object_meta(self):
        '''Test for singleton (Meta) - check objects.'''
        self.assertTrue(
            self.class_obj_one_meta is self.class_obj_two_meta,
            'it is not same object - checked by objects'
        )

    def test_class_id_meta(self):
        '''Test for singleton (Meta) - check ids.'''
        id_one = id(ATSSingletonClassTestMeta())
        id_two = id(ATSSingletonClassTestMeta())
        self.assertTrue(
            id_one == id_two, 'it is not same object - checked by ids'
        )

    def test_same_object_func(self):
        '''Test for singleton (Func) - check objects.'''
        self.assertTrue(
            self.class_obj_one_func is self.class_obj_two_func,
            'it is not same object - checked by objects'
        )

    def test_class_id_func(self):
        '''Test for singleton (Func) - check ids.'''
        id_one = id(ATSSingletonClassTestFunctional())
        id_two = id(ATSSingletonClassTestFunctional())
        self.assertTrue(
            id_one == id_two, 'it is not same object - checked by ids'
        )

    def test_same_object_meta_thread(self):
        '''Test for singleton (MetaThread) - check objects.'''
        self.assertTrue(
            self.class_obj_one_thread is self.class_obj_two_thread,
            'it is not same object - checked by objects'
        )

    def test_class_id_meta_thread(self):
        '''Test for singleton (MetaThread) - check ids.'''
        id_one = id(ATSSingletonClassTestMetaThread())
        id_two = id(ATSSingletonClassTestMetaThread())
        self.assertTrue(
            id_one == id_two, 'it is not same object - checked by ids'
        )

if __name__ == '__main__':
    unittest.main()
