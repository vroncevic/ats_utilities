# -*- coding: UTF-8 -*-

"""
 Module
     ats_logger_file.py
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
     Define class ATSLoggerFile with attribute(s) and method(s).
     Logging mechanism for App/Tool/Script, keep, set, get logger file path.
"""

import sys

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggerFile(object):
    """
        Define class ATSLoggerFile with attribute(s) and method(s).
        Logging mechanism for App/Tool/Script, keep, set, get logger file path.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __checker - ATS checker for parameters
                | __log_file - Log file path
            :methods:
                | __init__ - Initial constructor
                | log_file - Getting/Setting log file path
    """

    __slots__ = ('VERBOSE', '__log_file', '__checker')
    VERBOSE = 'ATS_UTILITIES::LOGGING::ATS_LOGGER_FILE'

    def __init__(self, log_file=None, verbose=False):
        """
            Initial constructor.

            :param log_file: Log file path
            :type log_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        """
        self.__checker = ATSChecker()
        error, status = self.__checker.check_params(
            [('str:log_file', log_file)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        verbose_message(
            ATSLoggerFile.VERBOSE, verbose, 'Initial ATS logger file'
        )
        self.__log_file = log_file

    @property
    def log_file(self):
        """
            Getting log file path.

            :return: Log file path
            :rtype: <str>
            :exceptions: None
        """
        return self.__log_file

    @log_file.setter
    def log_file(self, log_file):
        """
            Setting log file path.

            :param log_file: Log file path
            :type log_file: <str>
            :exceptions: ATSTypeError | ATSBadCallError
        """
        error, status = self.__checker.check_params(
            [('str:log_file', log_file)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        self.__log_file = log_file
