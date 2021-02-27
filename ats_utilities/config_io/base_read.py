# -*- coding: UTF-8 -*-

'''
 Module
     base_read.py
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
     Define class BaseReadConfig with attribute(s) and method(s).
     Read operation for configuration files.
'''

import sys

try:
    from ats_utilities.abstract import abstract_method
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class BaseReadConfig(object):
    '''
        Define class BaseReadConfig with attribute(s) and method(s).
        Read operation for configuration files.
        It defines:

            :attributes:
                | __file_path - Configuration file path.
            :methods:
                | __init__ - Initial constructor.
                | file_path - Property methods for set/get operations.
                | read_configuration - Read configuration (Abstract method).
    '''

    def __init__(self):
        '''
            Initial constructor.

            :exceptions: None
        '''
        self.__file_path = ''

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

    @abstract_method
    def read_configuration(self, verbose=False):
        '''
            Read configuration from file (Abstract method).

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exception: NotImplementedError
        '''
        pass
