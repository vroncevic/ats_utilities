# -*- coding: UTF-8 -*-

'''
 Module
     ats_logger_name.py
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
     Defined class ATSLoggerName with attribute(s) and method(s).
     Created API for App/Tool/Script logger name in one propery object.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggerName(object):
    '''
        Defined class ATSLoggerName with attribute(s) and method(s).
        Created API for App/Tool/Script logger name in one propery object.
        It defines:

            :attributes:
                | __logger_name - Logger name.
            :methods:
                | __init__ - Initial constructor.
                | logger_name - Property methods for set/get operations.
                | __str__ - Dunder method for ATSLoggerName.
    '''

    def __init__(self):
        '''
            Initial constructor.

            :exceptions: None
        '''
        self.__logger_name = None

    @property
    def logger_name(self):
        '''
            Property method for getting logger name.

            :return: Logger name | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__logger_name

    @logger_name.setter
    def logger_name(self, logger_name):
        '''
            Property method for setting logger name.

            :param logger_name: Logger name.
            :type logger_name: <str>
            :exceptions: None
        '''
        self.__logger_name = logger_name

    def __str__(self):
        '''
            Dunder method for ATSLoggerName.

            :return: String representaiton of ATSLoggerName.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(self.__class__.__name__, self.__logger_name)
