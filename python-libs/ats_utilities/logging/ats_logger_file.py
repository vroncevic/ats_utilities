# -*- coding: UTF-8 -*-
# ats_logger_file.py
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


class ATSLoggerFile(object):
    """
        Define class ATSLoggerFile with attribute(s) and method(s).
        Logging mechanism for App/Tool/Script.
        It defines:
            attribute:
                VERBOSE - Console text indicator for current process-phase
                __log_file - Log file path
            method:
                __init__ - Initial constructor
                set_log_file - Setting log file path
                get_log_file - Getting log file path
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_UTILITIES::LOGGING::ATS_LOGGER_FILE]'

    def __init__(self, logger_file=None, verbose=False):
        """
            Initial constructor.
            :param logger_file: Log file path
            :type logger_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = self.__class__
        verbose_message(cls.VERBOSE, verbose, 'Initial Logger File')
        self.__log_file = logger_file

    def set_log_file(self, log_file_path, verbose=False):
        """
            Setting log file path.
            :param log_file_path: Log file path
            :type log_file_path: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func = self.__class__, stack()[0][3]
        log_file_txt = 'Argument: expected log_file_path <str> object'
        log_file_msg = "{0} {1} {2}".format(cls.VERBOSE, func, log_file_txt)
        if log_file_path is None or not log_file_path:
            raise ATSBadCallError(log_file_msg)
        if not isinstance(log_file_path, str):
            raise ATSTypeError(log_file_msg)
        verbose_message(cls.VERBOSE, verbose, 'Initial log', log_file_path)
        self.__log_file = log_file_path

    def get_log_file(self, verbose=False):
        """
            Getting log file path.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Log file path
            :rtype: <str>
        """
        cls = self.__class__
        verbose_message(cls.VERBOSE, verbose, 'Log file', self.__log_file)
        return self.__log_file

    def __str__(self):
        """
            Return human readable string (ATSLoggerFile).
            :return: String representation of ATSLoggerFile
            :rtype: <str>
        """
        return "{0} Logger file {1}".format(self.__class__, self.__log_file)

    def __repr__(self):
        """
            Return unambiguous string (ATSLoggerFile).
            :return: String representation of ATSLoggerFile
            :rtype: <str>
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__log_file)
