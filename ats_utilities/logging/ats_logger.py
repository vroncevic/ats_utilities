# -*- coding: UTF-8 -*-

"""
 Module
     ats_logger.py
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
     Define class ATSLogger with attribute(s) and method(s).
     Logging mechanism for App/Tool/Script.
"""

import sys
from inspect import stack
from logging import (
    getLogger, basicConfig, DEBUG, WARNING, CRITICAL, ERROR, INFO
)

try:
    from pathlib import Path

    from ats_utilities.logging.ats_logger_base import ATSLoggerBase
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_file_error import ATSFileError
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLogger(ATSLoggerBase):
    """
        Define class ATSLogger with attribute(s) and method(s).
        Logging mechanism for App/Tool/Script.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | LOG_MSG_FORMAT - Log message format
                | LOG_DATE_FORMAT - Log date format
                | ATS_DEBUG - Debug log level
                | ATS_WARNING - Warning log level
                | ATS_CRITICAL - Critical log level
                | ATS_ERROR - Error log level
                | ATS_INFO - Info log level
            :methods:
                | __init__ - Initial constructor
                | write_log - Write message to log file
    """

    __slots__ = (
        'VERBOSE', 'LOG_MSG_FORMAT', 'LOG_DATE_FORMAT', 'ATS_DEBUG',
        'ATS_WARNING', 'ATS_CRITICAL', 'ATS_ERROR', 'ATS_INFO'
    )
    VERBOSE = 'ATS_UTILITIES::LOGGING::ATS_LOGGER'
    LOG_MSG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    LOG_DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'
    ATS_DEBUG, ATS_WARNING, ATS_CRITICAL, ATS_ERROR, ATS_INFO = (
        DEBUG, WARNING, CRITICAL, ERROR, INFO
    )

    def __init__(self, ats_name, ats_log_file, verbose=False):
        """
            Setting log file path, and default debug log level.

            :param ats_name: App/Tool/Script name
            :type ats_name: <str>
            :param ats_log_file: Log file path of App/Tool/Script
            :type ats_log_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError | ATSFileError
        """
        func = stack()[0][3]
        ats_name_txt = 'First argument: expected ats_name <str> object'
        ats_name_msg = "{0} {1} {2}".format('def', func, ats_name_txt)
        ats_log_txt = 'Second argument: expected ats_log_file <str> object'
        ats_log_msg = "{0} {1} {2}".format('def', func, ats_log_txt)
        if ats_name is None or not ats_name:
            raise ATSBadCallError(ats_name_msg)
        if not isinstance(ats_name, str):
            raise ATSTypeError(ats_name_msg)
        if ats_log_file is None or not ats_log_file:
            raise ATSBadCallError(ats_log_msg)
        if not isinstance(ats_log_file, str):
            raise ATSTypeError(ats_log_msg)
        verbose_message(ATSLogger.VERBOSE, verbose, 'Initial ATS logger')
        ATSLoggerBase.__init__(self, verbose=verbose)
        path_exists = Path(ats_log_file).is_file()
        if ats_log_file and path_exists and ats_name:
            self.logger_file = ats_log_file
            basicConfig(
                format=ATSLogger.LOG_MSG_FORMAT,
                datefmt=ATSLogger.LOG_DATE_FORMAT,
                filename=self.logger_file,
                level=DEBUG
            )
            logger = getLogger(ats_name)
            self.logger = logger
            self.logger_name = ats_name
            self.logger_status = True
        else:
            txt = "{0} {1}".format('Check ATS log file path', ats_log_file)
            message = "{0} {1}".format(ATSLogger.VERBOSE, txt)
            raise ATSFileError(message)

    def write_log(self, message, ctrl, verbose=False):
        """
            Write log message to log file.

            :param message: Log message
            :type message: <str>
            :param ctrl: Control flag (debug, warning, critical, errors, info)
            :type ctrl: <int>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, status = stack()[0][3], False
        msg_txt = 'First argument: expected msg <str> object'
        msg_msg = "{0} {1} {2}".format('def', func, msg_txt)
        ctrl_txt = 'Second argument: expected ctrl <int> object'
        ctrl_msg = "{0} {1} {2}".format('def', func, ctrl_txt)
        if message is None or not message:
            raise ATSBadCallError(msg_msg)
        if not isinstance(message, str):
            raise ATSTypeError(msg_msg)
        if ctrl is None or not ctrl:
            raise ATSBadCallError(ctrl_msg)
        if not isinstance(ctrl, int):
            raise ATSTypeError(ctrl_msg)
        verbose_message(ATSLogger.VERBOSE, verbose, 'Write ATS log message')
        if self.logger_status:
            switch_dict = {
                ATSLogger.ATS_DEBUG: self.logger.debug,
                ATSLogger.ATS_WARNING: self.logger.warning,
                ATSLogger.ATS_CRITICAL: self.logger.critical,
                ATSLogger.ATS_ERROR: self.logger.error,
                ATSLogger.ATS_INFO: self.logger.info
            }
            ctrl_options = [
                ATSLogger.ATS_DEBUG,
                ATSLogger.ATS_WARNING,
                ATSLogger.ATS_CRITICAL,
                ATSLogger.ATS_ERROR,
                ATSLogger.ATS_INFO
            ]
            if ctrl in ctrl_options:
                switch_dict[ctrl](message)
                status = True
            else:
                message = "{0} [{1}]".format('Not supported log level', ctrl)
                error_message(ATSLogger.VERBOSE, message)
        return True if status else False
