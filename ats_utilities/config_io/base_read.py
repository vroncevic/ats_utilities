# -*- coding: UTF-8 -*-

'''
 Module
     base_read.py
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
     Defined class BaseReadConfig with attribute(s) and method(s).
     Created API for read operation for configuration files.
'''

import sys

try:
    from ats_utilities.abstract import abstract_method
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class BaseReadConfig(object):
    '''
        Defined class BaseReadConfig with attribute(s) and method(s).
        Created API for read operation for configuration files.
        It defines:

            :attributes:
                | __file_path - Configuration file path.
            :methods:
                | __init__ - Initial constructor.
                | file_path - Property methods for set/get operations.
                | is_not_none - Checking is file path None.
                | read_configuration - Read configuration (Abstract method).
                | __str__ - Dunder method for BaseReadConfig.
    '''

    def __init__(self):
        '''
            Initial constructor.

            :exceptions: None
        '''
        self.__file_path = None

    @property
    def file_path(self):
        '''
            Property method for getting file path.

            :return: Configuration file path | None.
            :rtype: <str> | <NoneType>
            :exception: None
        '''
        return self.__file_path

    @file_path.setter
    def file_path(self, file_path):
        '''
            Property method for setting file path.

            :param file_path: Configuration file path.
            :type file_path: <str>
            :exceptions: None
        '''
        self.__file_path = file_path

    def is_not_none(self):
        '''
            Checking is file path None.

            :return: True (file path) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return True if self.__file_path is not None else False

    @abstract_method
    def read_configuration(self):
        '''
            Read configuration from file (Abstract method).

            :exception: NotImplementedError
        '''
        pass

    def __str__(self):
        '''
            Dunder method for BaseReadConfig.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(self.__class__.__name__, self.__file_path)
