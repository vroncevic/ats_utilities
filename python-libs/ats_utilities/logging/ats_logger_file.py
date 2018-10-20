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
    sys.exit(msg)  # Force close python ATS ##################################

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
        Logging mechanism for App/Tool/Script, keep, set, get logger file path.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __log_file - Log file path
            method:
                __init__ - Initial constructor
                log_file - Getting/Setting log file path
    """

    __slots__ = ('VERBOSE', '__log_file')
    VERBOSE = 'ATS_UTILITIES::LOGGING::ATS_LOGGER_FILE'

    def __init__(self, logger_file=None, verbose=False):
        """
            Initial constructor.
            :param logger_file: Log file path
            :type logger_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            ATSLoggerFile.VERBOSE, verbose, 'Initial ATS logger file'
        )
        self.__log_file = logger_file

    @property
    def log_file(self, verbose=False):
        """
            Getting log file path.
            :return: Log file path
            :rtype: <str>
            :exceptions: None
        """
        return self.__log_file

    @log_file.setter
    def log_file(self, log_file_path, verbose=False):
        """
            Setting log file path.
            :param log_file_path: Log file path
            :type log_file_path: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        log_file_txt = 'Argument: expected log_file_path <str> object'
        log_file_msg = "{0} {1} {2}".format('def', func, log_file_txt)
        if log_file_path is None or not log_file_path:
            raise ATSBadCallError(log_file_msg)
        if not isinstance(log_file_path, str):
            raise ATSTypeError(log_file_msg)
        self.__log_file = log_file_path

