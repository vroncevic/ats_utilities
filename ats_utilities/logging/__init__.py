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
     Defined class ATSLogger with attribute(s) and method(s).
     Created API for ATS logging mechanism.
'''

import sys
from os.path import isfile
from logging import (
    getLogger, basicConfig, DEBUG, WARNING, CRITICAL, ERROR, INFO
)

try:
    from six import add_metaclass
    from ats_utilities.checker import ATSChecker
    from ats_utilities.cooperative import CooperativeMeta
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.logging.ats_logger_file import ATSLoggerFile
    from ats_utilities.logging.ats_logger_name import ATSLoggerName
    from ats_utilities.exceptions.ats_file_error import ATSFileError
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.logging.ats_logger_status import ATSLoggerStatus
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(CooperativeMeta)
class ATSLogger(ATSLoggerName, ATSLoggerFile, ATSLoggerStatus):
    '''
        Defined class ATSLogger with attribute(s) and method(s).
        Created API for ATS logging mechanism.
        It defines:

            :attributes:
                | LOG_MSG_FORMAT - log message format.
                | LOG_DATE_FORMAT - log date format.
                | ATS_DEBUG - debug log level.
                | ATS_WARNING - warning log level.
                | ATS_CRITICAL - critical log level.
                | ATS_ERROR - error log level.
                | ATS_INFO - info log level.
                | __verbose - enable/disable verbose option.
            :methods:
                | __init__ - initial constructor.
                | write_log - write message to log file.
                | __str__ - str dunder method for ATSLogger.
    '''

    LOG_MSG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    LOG_DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'
    ATS_DEBUG, ATS_WARNING, ATS_CRITICAL, ATS_ERROR, ATS_INFO = (
        DEBUG, WARNING, CRITICAL, ERROR, INFO
    )

    def __init__(self, ats_name, ats_log_file, verbose=False):
        '''
            Initial constructor.

            :param ats_name: ATS name.
            :type ats_name: <str>
            :param ats_log_file: log file path of ATS.
            :type ats_log_file: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError | ATSFileError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:ats_name', ats_name), ('str:ats_log_file', ats_log_file)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        ATSLoggerName.__init__(self, verbose=verbose)
        ATSLoggerFile.__init__(self, verbose=verbose)
        ATSLoggerStatus.__init__(self, verbose=verbose)
        self.__verbose = verbose
        if isfile(ats_log_file):
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
            error = '{0} {1}'.format(
                ATSLogger.VERBOSE, '{0} {1}'.format(
                    'check ATS log file path', ats_log_file
                )
            )
            raise ATSFileError(error)
        verbose_message(ATSLogger.VERBOSE, verbose, 'init ATS logger')

    def write_log(self, message, ctrl, verbose=False):
        '''
            Write message to log file.

            :param message: log message.
            :type message: <str>
            :param ctrl: control flag (debug, warning, critical, errors, info).
            :type ctrl: <int>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:message', message), ('int:ctrl', ctrl)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status = False
        verbose_message(
            ATSLogger.VERBOSE, self.__verbose or verbose, message, ctrl
        )
        if self.logger_status:
            switch_dict = {
                ATSLogger.ATS_DEBUG: self.logger.debug,
                ATSLogger.ATS_WARNING: self.logger.warning,
                ATSLogger.ATS_CRITICAL: self.logger.critical,
                ATSLogger.ATS_ERROR: self.logger.error,
                ATSLogger.ATS_INFO: self.logger.info
            }
            ctrl_options = [
                ATSLogger.ATS_DEBUG, ATSLogger.ATS_WARNING,
                ATSLogger.ATS_CRITICAL, ATSLogger.ATS_ERROR,
                ATSLogger.ATS_INFO
            ]
            if ctrl in ctrl_options:
                switch_dict[ctrl](message)
                status = True
            else:
                message = '{0} [{1}]'.format('not supported log level', ctrl)
                error_message(ATSLogger.VERBOSE, message)
        return status

    def __str__(self):
        '''
            Dunder str method for ATSLogger.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4}, {5})'.format(
            self.__class__.__name__, ATSLoggerName.__str__(self),
            ATSLoggerFile.__str__(self), ATSLoggerStatus.__str__(self),
            str(self.__verbose), str(self.logger)
        )
