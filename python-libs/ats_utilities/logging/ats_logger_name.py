# -*- coding: UTF-8 -*-

"""
 Module
     ats_logger_name.py
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
     Define class ATSLoggerName with attribute(s) and method(s).
     Logging mechanism for App/Tool/Script, keep, set, get logger name.
"""

import sys
from inspect import stack

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE) # Force close python ATS ###############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggerName(object):
    """
        Define class ATSLoggerName with attribute(s) and method(s).
        Logging mechanism for App/Tool/Script, keep, set, get logger name.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __logger_name - Logger name
            method:
                __init__ - Initial constructor
                logger_name - Getting/Setting logger name
    """

    __slots__ = ('VERBOSE', '__logger_name')
    VERBOSE = 'ATS_UTILITIES::LOGGING::ATS_LOGGER_NAME'

    def __init__(self, logger_name=None, verbose=False):
        """
            Initial constructor.
            :param logger_name: Logger name
            :type logger_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            ATSLoggerName.VERBOSE, verbose, 'Initial ATS logger Name'
        )
        self.__logger_name = logger_name

    @property
    def logger_name(self):
        """
            Getting logger name.
            :return: Logger name
            :rtype: <str>
            :exceptions: None
        """
        return self.__logger_name

    @logger_name.setter
    def logger_name(self, logger_name):
        """
            Setting logger name.
            :param logger_name: Logger name
            :type logger_name: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        logger_name_txt = 'Argument: expected logger_name <str> object'
        logger_name_msg = "{0} {1} {2}".format('def', func, logger_name_txt)
        if logger_name is None or not logger_name:
            raise ATSBadCallError(logger_name_msg)
        if not isinstance(logger_name, str):
            raise ATSTypeError(logger_name_msg)
        self.__logger_name = logger_name
