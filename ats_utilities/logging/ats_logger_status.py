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
     Created API for ATS logger status in one propery object.
'''

import sys

try:
    from six import add_metaclass
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(VerboseRoot)
class ATSLoggerStatus:
    '''
        Defined class ATSLoggerStatus with attribute(s) and method(s).
        Created API for ATS logger status in one propery object.
        It defines:

            :attributes:
                | __verbose - enable/disable verbose option.
                | __log_status - logger status (enabled/disabled).
            :methods:
                | __init__ - initial constructor.
                | logger_status - property methods for set/get operations.
                | __str__ - str dunder method for ATSLoggerStatus.
    '''

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__verbose = verbose
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

            :param log_status: logger status (enable/disable logging).
            :type log_status: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('bool:log_status', log_status)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__log_status = log_status
        verbose_message(ATSLoggerStatus.VERBOSE, self.__verbose, log_status)

    def __str__(self):
        '''
            Dunder str method for ATSLoggerStatus.

            :return: string representaiton of ATSLoggerStatus.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__verbose), self.__log_status
        )
