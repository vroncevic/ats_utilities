# -*- coding: UTF-8 -*-

"""
 Module
     ats_logger_base.py
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
     Define class ATSLoggerBase with attribute(s) and method(s).
     Base container for logging mechanism.
"""

import sys
from logging import Logger
from inspect import stack

try:
    from ats_utilities.logging.ats_logger_status import ATSLoggerStatus
    from ats_utilities.logging.ats_logger_file import ATSLoggerFile
    from ats_utilities.logging.ats_logger_name import ATSLoggerName
    from ats_utilities.abstract import abstract_method
    from ats_utilities.console_io.verbose import verbose_message
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


class ATSLoggerBase(object):
    """
        Define class ATSLoggerBase with attribute(s) and method(s).
        Base container for logging mechanism.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __logger_name - Logger name
                | __logger_status - Logger info status
                | __logger_file - Logger file path
                | __logger - Object logger
            :methods:
                | __init__ - Initial constructor
                | logger - Getting/Setting logger object
                | write_log - Write message to log file (Abstract method)
    """

    __slots__ = (
        'VERBOSE',
        'logger_name',
        'logger_status',
        'logger_file',
        '__logger'
    )
    VERBOSE = 'ATS_UTILITIES::LOGGING::ATS_BASE_LOGGER'

    def __init__(self, verbose=False):
        """
            Initial constructor.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            ATSLoggerBase.VERBOSE, verbose, 'Initial ATS logger base'
        )
        self.logger_name = ATSLoggerName(verbose=verbose)
        self.logger_status = ATSLoggerStatus(verbose=verbose)
        self.logger_file = ATSLoggerFile(verbose=verbose)
        self.__logger = None

    @property
    def logger(self):
        """
            Getting logger object.

            :return: Logger object
            :rtype: <logging.Logger>
            :exceptions: None
        """
        return self.__logger

    @logger.setter
    def logger(self, logger):
        """
            Setting logger object.

            :param logger: Logger object
            :type logger: <logging.Logger>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        logger_txt = 'Argument: expected logger <logging.Logger> object'
        logger_msg = "{0} {1} {2}".format('def', func, logger_txt)
        if logger is None or not logger:
            raise ATSBadCallError(logger_msg)
        if not isinstance(logger, Logger):
            raise ATSTypeError(logger_msg)
        self.__logger = logger

    @abstract_method
    def write_log(self, message, ctrl, verbose=False):
        """
            Write message to log file (Abstract method).

            :param message: Log message
            :type message: <str>
            :param ctrl: Control flag (debug, warning, critical, errors, info)
            :type ctrl: <int>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exception: NotImplementedError
        """
        pass
