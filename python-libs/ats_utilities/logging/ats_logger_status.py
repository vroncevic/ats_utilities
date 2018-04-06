# -*- coding: UTF-8 -*-
# ats_logger_status.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# ats_utilities is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ats_utilities is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from inspect import stack

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggerStatus(object):
    """
        Define class ATSLoggerStatus with attribute(s) and method(s).
        Logging mechanism for App/Tool/Script.
        It defines:
            attribute:
                VERBOSE - Console text indicator for current process-phase
                __log_status - Logger operative (enabled/disabled)
            method:
                __init__ - Initial constructor
                set_logger_status - Setting logger status
                get_logger_status - Getting logger status
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    VERBOSE = 'ATS_UTILITIES::LOGGING::ATS_LOGGER_STATUS'

    def __init__(self, log_status=False, verbose=False):
        """
            Initial constructor.
            :param log_status: Logger status
            :type log_status: <bool>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = ATSLoggerStatus
        verbose_message(cls.VERBOSE, verbose, 'Initial ATS logger Status')
        self.__log_status = log_status

    def set_logger_status(self, status, verbose=False):
        """
            Setting logger status.
            :param status: Logger status (enable/disable logging mechanism)
            :type status: <bool>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func = ATSLoggerStatus, stack()[0][3]
        status_txt = 'Argument: expected status <bool> object'
        status_msg = "{0} {1} {2}".format('def', func, status_txt)
        if status is None:
            raise ATSBadCallError(status_msg)
        if not isinstance(status, bool):
            raise ATSTypeError(status_msg)
        verbose_message(cls.VERBOSE, verbose, 'Set ATS logger status', status)
        self.__log_status = status

    def get_logger_status(self, verbose=False):
        """
            Getting logger status.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (logger operative) | False
            :rtype: <bool>
        """
        cls = ATSLoggerStatus
        verbose_message(
            cls.VERBOSE, verbose, 'ATS logger status', self.__log_status
        )
        return self.__log_status

    def __str__(self):
        """
            Return human readable string (ATSLoggerStatus).
            :return: String representation of ATSLoggerStatus
            :rtype: <str>
        """
        cls = ATSLoggerStatus
        return "{0} Logger status {1}".format(cls.__name__, self.__log_status)

    def __repr__(self):
        """
            Return unambiguous string (ATSLoggerStatus).
            :return: String representation of ATSLoggerStatus
            :rtype: <str>
        """
        cls = ATSLoggerStatus
        return "{0}(\'{1}\')".format(cls.__name__, self.__log_status)
