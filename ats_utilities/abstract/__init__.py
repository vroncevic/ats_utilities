# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Defined class abstract_method with attribute(s) and method(s).
     Created abstract decorator for object methods.
'''

from inspect import stack

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/master/LICENSE'
__version__ = '1.5.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class abstract_method(object):
    '''
        Defined class abstract_method with attribute(s) and method(s).
        Created abstract decorator for object methods.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | method_name - Object method name.
                | method_class_name - Class name of method.
                | method_type - Type of object method.
                | method - Method object-reference.
            :methods:
                | __init__ - Initial constructor.
                | __call__ - Raise exception NotImplementedError on call.
                | __str__ - Dunder method for abstract_method.
    '''

    __slots__ = (
        'VERBOSE', 'method_name', 'method_class_name', 'method_type', 'method'
    )
    VERBOSE = 'ATS_UTILITIES::ABSTRACT::ABSTRACT_METHOD'

    def __init__(self, method_to_abstract):
        '''
            Initial constructor.

            :param method_to_abstract: Method object-reference.
            :type method_to_abstract: <function>
            :exceptions: None
        '''
        self.method_name = method_to_abstract.__name__
        self.method_class_name = stack()[1][3]
        self.method_type = type(method_to_abstract)
        self.method = method_to_abstract

    def __call__(self, *args, **kwargs):
        '''
            Raise exception NotImplementedError on call.

            :param *args: Iteration object.
            :type *args: <iter>
            :param **kwargs: Iteration object.
            :type **kwargs: <dict>
            :exception: NotImplementedError
        '''
        abstract_msg = 'from class {0}::{1}() not implemented'.format(
            self.method_class_name, self.method_name
        )
        raise NotImplementedError(abstract_msg)

    def __str__(self):
        '''
            Dunder method for abstract_method.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4})'.format(
            self.__class__.__name__, self.method_name,
            self.method_class_name, self.method_type, self.method
        )
