# -*- coding: UTF-8 -*-

"""
 Module
     __init__.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class abstract_method with attribute(s) and method(s).
     Creating custom decorator for class methods.
"""

import sys
from inspect import stack

try:
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class abstract_method(object):
    """
        Define class abstract_method with attribute(s) and method(s).
        Creating custom decorator for class methods.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | method_name - Class method name
                | method_class_name - Method class name
                | method_type - Class method type
                | method - Class method
            :methods:
                | __init__ - Initial constructor
                | __call__ - Raise exception NotImplementedError
                             (mark as abstract method)
    """

    __slots__ = (
        'VERBOSE',
        'method_name',
        'method_class_name',
        'method_type',
        'method'
    )
    VERBOSE = 'ATS_UTILITIES::ABSTRACT_METHOD'

    def __init__(self, method_to_abstract, verbose=False):
        """
            Initial constructor

            :param method_to_abstract: Method from some class
            :type method_to_abstract: <function>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        cls = abstract_method
        verbose_message(cls.VERBOSE, verbose, 'Initial decorator')
        self.method_name = method_to_abstract.__name__
        self.method_class_name = stack()[1][3]
        self.method_type = type(method_to_abstract)
        self.method = method_to_abstract

    def __call__(self, verbose=False, *args, **kwargs):
        """
            Raise exception NotImplementedError (mark as abstract method)

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :param *args: Iteration object
            :type *args: <iter>
            :param **kwargs: Iteration object
            :type **kwargs: <dict>
            :exception: NotImplementedError
        """
        cls = abstract_method
        verbose_message(cls.VERBOSE, verbose, 'Raise abstract protection')
        abstract_msg = "{0} {1}::{2}() {3}".format(
            'from class', self.method_class_name,
            self.method_name, 'method not implemented !'
        )
        raise NotImplementedError(abstract_msg)
