# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Creates API for ATS logging mechanism.
'''

import sys
from os.path import isfile
from logging import (
    getLogger, basicConfig, Logger, DEBUG, WARNING, CRITICAL, ERROR, INFO
)

try:
    from ats_utilities import auto_str, VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.logging.ats_logger_file import ATSLoggerFile
    from ats_utilities.logging.ats_logger_name import ATSLoggerName
    from ats_utilities.exceptions.ats_file_error import ATSFileError
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.logging.ats_logger_status import ATSLoggerStatus
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@auto_str
class ATSLogger(metaclass=VerboseRoot):
    '''
        Defines class ATSLogger with attribute(s) and method(s).
        Creates API for ATS logging mechanism.
        ATS logger mechanism.

        It defines:

            :attributes:
                | log_msg_format - log message format.
                | log_date_format - log date format.
                | ats_debug - debug log level.
                | ats_warning - warning log level.
                | ats_critical - critical log level.
                | ats_error - error log level.
                | ats_info - info log level.
                | _verbose - enable/disable verbose option.
                | _ats_logger_name - Instance of logger name.
                | _ats_logger_status - Instance of logger status.
                | _ats_logger_file - Instance of logger file.
            :methods:
                | __init__ - Initial ATSLogger constructor.
                | write_log - Write message to log file.
    '''

    log_msg_format: str = '%(asctime)s - %(levelname)s - %(message)s'
    log_date_format: str = '%m/%d/%Y %I:%M:%S %p'
    ats_debug: int = DEBUG
    ats_warning: int = WARNING
    ats_critical: int = CRITICAL
    ats_error: int = ERROR
    ats_info: int = INFO

    _verbose: bool
    _ats_logger_name: ATSLoggerName | None
    _ats_logger_status: ATSLoggerStatus | None
    _ats_logger_file: ATSLoggerFile | None

    def __init__(
        self, ats_name: str, ats_log_file: str, verbose: bool = False
    ) -> None:
        '''
            Initial ATSLogger constructor.

            :param ats_name: ATS name
            :type ats_name: <str>
            :param ats_log_file: Log file path of ATS
            :type ats_log_file: <str>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError | ATSFileError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:ats_name', ats_name), ('str:ats_log_file', ats_log_file)
        ])
        if error_id == ATSChecker.type_error:
            raise ATSTypeError(error_msg)
        if error_id == ATSChecker.value_error:
            raise ATSBadCallError(error_msg)
        self._verbose = verbose
        self._ats_logger_name = ATSLoggerName(verbose=verbose)
        self._ats_logger_status = ATSLoggerStatus(verbose=verbose)
        self._ats_logger_file = ATSLoggerFile(verbose=verbose)
        if isfile(ats_log_file):
            self._ats_logger_file.logger_file = ats_log_file
            basicConfig(
                format=ATSLogger.log_msg_format,
                datefmt=ATSLogger.log_date_format,
                filename=self._ats_logger_file.logger_file,
                level=DEBUG
            )
            self.logger: Logger = getLogger(self._ats_logger_name.logger_name)
            self._ats_logger_status.logger_status = True
        else:
            raise ATSFileError(f'Check ATS log file path {ats_log_file}')
        verbose_message(
            ATSLogger.verbose,  # pylint: disable=no-member
            verbose,
            tuple('init ATS logger')
        )

    def write_log(
        self, message: str, ctrl: int, verbose: bool = False
    ) -> bool:
        '''
            Write message to log file.

            :param message: Log message to log file
            :type message: <str>
            :param ctrl: Control flag (debug, warning, critical, errors, info)
            :type ctrl: <int>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (successful written log) | False
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:message', message), ('int:ctrl', ctrl)
        ])
        if error_id == ATSChecker.type_error:
            raise ATSTypeError(error_msg)
        if error_id == ATSChecker.value_error:
            raise ATSBadCallError(error_msg)
        status: bool = False
        verbose_message(
            ATSLogger.verbose,  # pylint: disable=no-member
            self._verbose or verbose,
            tuple(f'{message} {str(ctrl)}')
        )
        if bool(self._ats_logger_status):
            match ctrl:
                case ATSLogger.ats_debug:
                    self.logger.debug(message)
                    status = True
                case ATSLogger.ats_warning:
                    self.logger.warning(message)
                    status = True
                case ATSLogger.ats_critical:
                    self.logger.critical(message)
                    status = True
                case ATSLogger.ats_error:
                    self.logger.error(message)
                    status = True
                case ATSLogger.ats_info:
                    self.logger.info(message)
                    status = True
                case _:
                    error_message(
                        ATSLogger.verbose,  # pylint: disable=no-member
                        tuple(f'not supported log level [{str(ctrl)}]')
                    )
        return status
