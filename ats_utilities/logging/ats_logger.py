# -*- coding: UTF-8 -*-

'''
Module
    ats_logger.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class ATSLogger with attribute(s) and method(s).
    Creates an API for the ATS logging mechanism.
'''

from typing import List, Optional
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.logging.ilogger import IATSLogger
from ats_utilities.logging.default_logger import DefaultLogger, DefaultLogLevels

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSLogger:
    '''
        Defines class ATSLogger with attribute(s) and method(s).
        Creates an API for the ATS logging mechanism.
        ATS logger mechanism.

        It defines:

            :attributes:
                | ATS_CRITICAL - Critical log level.
                | ATS_DEBUG - Debug log level.
                | ATS_ERROR - Error log level.
                | ATS_INFO - Info log level.
                | ATS_WARNING - Warning log level.
                | __logger - Prepared logger instance or default logger.
                | __reporter - Message reporter for logging operations.
                | __verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials ATSLogger constructor.
                | write_log - Writes message to log output.
    '''

    ATS_CRITICAL = DefaultLogLevels.ATS_LOG_CRITICAL
    ATS_DEBUG = DefaultLogLevels.ATS_LOG_DEBUG
    ATS_ERROR = DefaultLogLevels.ATS_LOG_ERROR
    ATS_INFO = DefaultLogLevels.ATS_LOG_INFO
    ATS_WARNING = DefaultLogLevels.ATS_LOG_WARNING

    def __init__(
        self,
        ats_name: Optional[str] = None,
        ats_log_stdout: bool = True,
        ats_log_file: Optional[str] = None,
        logger_instance: Optional[IATSLogger] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSLogger constructor.

            :param ats_name: ATS name | None
            :type ats_name: <Optional[str]>
            :param ats_log_stdout: Log to stdout (default True)
            :type ats_log_stdout: <bool>
            :param ats_log_file: Log to file (default None)
            :type ats_log_file: <Optional[str]>
            :param logger_instance: Pre-configured Logger instance | None
            :type logger_instance: <Optional[IATSLogger]>
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__logger: IATSLogger = logger_instance or DefaultLogger(
            ats_name, ats_log_stdout, ats_log_file, reporter=reporter, verbose=verbose
        )
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__reporter.verbose(self.__verbose, ['init ATS logger'])

    def write_log(self, message: Optional[str], ctrl: int, verbose: bool = False) -> bool:
        '''
            Writes message to log output.

            :param message: Log message for log output | None
            :type message: <Optional[str]>
            :param ctrl: Control flag (debug, warning, critical, errors, info)
            :type ctrl: <int>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (successfully logged message) | False
            :rtype: <bool>
            :exceptions: None
        '''
        self.__reporter.verbose(self.__verbose or verbose, [f'{message} {str(ctrl)}'])
        return self.__logger.write_log(message, ctrl, self.__verbose or verbose)
