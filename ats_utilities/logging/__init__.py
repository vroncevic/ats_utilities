# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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

import sys
from typing import List
from logging import (
    getLogger, basicConfig, Logger, DEBUG, WARNING, CRITICAL, ERROR, INFO
)

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.logging.ats_logger_file import ATSLoggerFile
    from ats_utilities.logging.ats_logger_name import ATSLoggerName
    from ats_utilities.logging.ats_logger_status import ATSLoggerStatus
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLogger(ATSLoggerName, ATSLoggerStatus, ATSLoggerFile):
    '''
        Defines class ATSLogger with attribute(s) and method(s).
        Creates an API for the ATS logging mechanism.
        ATS logger mechanism.

        It defines:

            :attributes:
                | LOG_MSG_FORMAT - Log message format.
                | LOG_DATE_FORMAT - Log date format.
                | ATS_DEBUG - Debug log level.
                | ATS_WARNING - Warning log level.
                | ATS_CRITICAL - Critical log level.
                | ATS_ERROR - Error log level.
                | ATS_INFO - Info log level.
                | _verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials ATSLogger constructor.
                | write_log - Writes message to log file.
    '''

    LOG_MSG_FORMAT: str = '%(asctime)s - %(levelname)s - %(message)s'
    LOG_DATE_FORMAT: str = '%m/%d/%Y %I:%M:%S %p'
    ATS_DEBUG: int = DEBUG
    ATS_WARNING: int = WARNING
    ATS_CRITICAL: int = CRITICAL
    ATS_ERROR: int = ERROR
    ATS_INFO: int = INFO

    def __init__(
        self,
        ats_name: str | None,
        ats_log_file: str | None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSLogger constructor.

            :param ats_name: ATS name | None
            :type ats_name: <str> | <NoneType>
            :param ats_log_file: Log file path of ATS | None
            :type ats_log_file: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        ATSLoggerName.__init__(self, verbose)
        ATSLoggerStatus.__init__(self, verbose)
        ATSLoggerFile.__init__(self, verbose)
        self._verbose: bool = verbose
        self.logger_path = str(ats_log_file)
        self.logger_name = str(ats_name)
        basicConfig(
            format=self.LOG_MSG_FORMAT,
            datefmt=self.LOG_DATE_FORMAT,
            filename=self.logger_path,
            level=DEBUG
        )
        self.logger: Logger = getLogger(self.logger_name)
        self.logger_status = True
        verbose_message(self._verbose, ['init ATS logger'])

    def write_log(
        self, message: str | None, ctrl: int, verbose: bool = False
    ) -> bool:
        '''
            Writes message to log file.

            :param message: Log message for log file | None
            :type message: <str> | <NoneType>
            :param ctrl: Control flag (debug, warning, critical, errors, info)
            :type ctrl: <int>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (successful written log) | False
            :rtype: <bool>
            :exceptions: ATSTypeError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('str:message', message), ('int:ctrl', ctrl)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        status: bool = False
        verbose_message(self._verbose or verbose, [f'{message} {str(ctrl)}'])
        if self.logger_status:
            match ctrl:
                case self.ATS_DEBUG:
                    self.logger.debug(message)
                    status = True
                case self.ATS_WARNING:
                    self.logger.warning(message)
                    status = True
                case self.ATS_CRITICAL:
                    self.logger.critical(message)
                    status = True
                case self.ATS_ERROR:
                    self.logger.error(message)
                    status = True
                case self.ATS_INFO:
                    self.logger.info(message)
                    status = True
                case _:
                    raise ATSBadCallError(
                        f'not supported log level [{str(ctrl)}]'
                    )
        return status
