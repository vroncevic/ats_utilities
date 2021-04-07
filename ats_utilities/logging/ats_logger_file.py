# -*- coding: UTF-8 -*-

'''
 Module
     ats_logger_file.py
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
     Defined class ATSLoggerFile with attribute(s) and method(s).
     Created API for App/Tool/Script logger file path in one propery object.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggerFile(object):
    '''
        Defined class ATSLoggerFile with attribute(s) and method(s).
        Created API for App/Tool/Script logger file path in one propery object.
        It defines:

            :attributes:
                | __log_file - Log file path.
            :methods:
                | __init__ - Initial constructor.
                | log_file - Property methods for set/get operations.
                | __str__ - Dunder method for ATSLoggerFile.
    '''

    def __init__(self):
        '''
            Initial constructor.

            :exceptions: None
        '''
        self.__log_file = None

    @property
    def log_file(self):
        '''
            Property method for getting log file path.

            :return: Log file path | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__log_file

    @log_file.setter
    def log_file(self, log_file):
        '''
            Property method for setting log file path.

            :param log_file: Log file path.
            :type log_file: <str>
            :exceptions: None
        '''
        self.__log_file = log_file

    def __str__(self):
        '''
            Dunder method for ATSLoggerFile.

            :return: String representaiton of ATSLoggerFile.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(self.__class__.__name__, self.__log_file)
