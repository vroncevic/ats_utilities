# -*- coding: UTF-8 -*-
# ats_logger.py
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
from os.path import exists
from logging import (
    getLogger, basicConfig, DEBUG, WARNING, CRITICAL, ERROR, INFO
)

try:
    from ats_utilities.logging.ats_logger_base import ATSLoggerBase
    from ats_utilities.error.ats_value_error import ATSValueError
    from ats_utilities.error.ats_file_error import ATSFileError
    from ats_utilities.text.stdout_text import ATS, DBG, ERR, RST
    from ats_utilities.text import COut
except ImportError as e:
    msg = "\n{0}\n".format(e)
    sys.exit(msg)  # Force close python ATS ###################################

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
        attribute:
            VERBOSE - Verbose prefix console text
            LOG_MSG_FORMAT - Log message format
            LOG_DATE_FORMAT - Log date format
            ATS_DEBUG - Debug log level
            ATS_WARNING - Warning log level
            ATS_CRITICAL - Critical log level
            ATS_ERROR - Error log level
            ATS_INFO - Info log level
        method:
            __init__ - Initial constructor
            write_log - Write message to log file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = 'ATS_LOGGER'
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
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}".format('Initial logger')
        COut.print_console_msg(msg, verbose=verbose)
        super(ATSLogger, self).__init__(verbose)
        path_exists = exists(ats_log_file)
        if ats_log_file and path_exists and ats_name:
            self.set_log_file(ats_log_file, verbose)
            basicConfig(
                format=cls.LOG_MSG_FORMAT, datefmt=cls.LOG_DATE_FORMAT,
                filename=self.get_log_file(verbose), level=DEBUG
            )
            logger = getLogger(ats_name)
            self.set_logger(logger, verbose)
            self.set_logger_name(ats_name, verbose)
            self.set_logger_status(True)
        else:
            msg = "\n{0} {1}{2} {3} \n{4}\n".format(
                cls.VERBOSE, ERR, ATS, 'check log file path',
                ats_log_file, RST
            )
            raise ATSFileError(msg)

    def write_log(self, msg, ctrl, verbose=False):
        """
        Write message to log file.
        :param msg: Log message
        :type msg: <str>
        :param ctrl: Control flag (debug, warning, critical, error, info)
        :type ctrl: <int>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: True (success) | False
        :rtype: <bool>
        """
        cls, status = self.__class__, False
        msg = "{0}".format('Write log message')
        COut.print_console_msg(msg, verbose=verbose)
        try:
            enabled_log = self.get_logger_status(verbose)
            if enabled_log:
                switch_dict = {
                    cls.ATS_DEBUG: self.get_logger().debug,
                    cls.ATS_WARNING: self.get_logger().warning,
                    cls.ATS_CRITICAL: self.get_logger().critical,
                    cls.ATS_ERROR: self.get_logger().error,
                    cls.ATS_INFO: self.get_logger().info
                }
                ctrl_options = [
                    cls.ATS_DEBUG, cls.ATS_WARNING, cls.ATS_CRITICAL,
                    cls.ATS_ERROR, cls.ATS_INFO
                ]
                ctrl_is_int = isinstance(ctrl, int)
                if ctrl_is_int and ctrl in ctrl_options:
                    switch_dict[ctrl](msg)
                else:
                    msg = "\n{0} {1}{2} [{3}]{4}\n".format(
                        cls.VERBOSE, ERR, 'Not supported log level', ctrl, RST
                    )
                    raise ATSValueError(msg)
            else:
                msg = "\n{0} {1}{2} [{3}]{4}\n".format(
                    cls.VERBOSE, ERR, 'Not enabled logging', ctrl, RST
                )
                raise ATSValueError(msg)
        except ATSValueError as e:
            print(e)
        else:
            status = True
        return True if status else False

    def __str__(self):
        """
        Return human readable string (ATSLogger).
        :return: String representation of ATSLogger
        :rtype: <str>
        """
        log_file_path = self.get_log_file()
        return "{0} log file \n{1}".format(ATS, log_file_path)

    def __repr__(self):
        """
        Return unambiguous string (ATSLogger).
        :return: String representation of ATSLogger
        :rtype: <str>
        """
        logger_name = self.get_logger_name()
        log_file = self.get_log_file()
        return "{0}(\'{1}\', \'{2}\')".format(
            type(self).__name__, logger_name, log_file
        )
