# -*- coding: UTF-8 -*-

'''
 Module
     ats_logger_status.py
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
     Defined class ATSLoggerStatus with attribute(s) and method(s).
     Created API for App/Tool/Script logger status in one propery object.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggerStatus(object):
    '''
        Defined class ATSLoggerStatus with attribute(s) and method(s).
        Created API for App/Tool/Script logger status in one propery object.
        It defines:

            :attributes:
                | __log_status - Logger status (enabled/disabled).
            :methods:
                | __init__ - Initial constructor.
                | logger_status - Property methods for set/get operations.
                | __str__ - Dunder method for ATSLoggerStatus.
    '''

    def __init__(self):
        '''
            Initial constructor.

            :exceptions: None
        '''
        self.__log_status = None

    @property
    def logger_status(self):
        '''
            Property method for getting logger status.

            :return: True (logger operative) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return self.__log_status

    @logger_status.setter
    def logger_status(self, log_status):
        '''
            Property method for setting logger status.

            :param log_status: Logger status (enable/disable logging).
            :type log_status: <bool>
            :exceptions: None
        '''
        self.__log_status = log_status

    def __str__(self):
        '''
            Dunder method for ATSLoggerStatus.

            :return: String representaiton of ATSLoggerStatus.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(self.__class__.__name__, self.__log_status)
