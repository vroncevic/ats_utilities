# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines class LogFile with attribute(s) and method(s).
    Creates an API for the log file path in one property object.
'''

from __future__ import annotations

from typing import override

from ats_utilities.info.log_file.ilog_file import ILogFile
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.context.context_bundle_inject import inject_context_bundle
from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class LogFile(ILogFile):
    '''
        Defines class LogFile with attribute(s) and method(s).
        Creates an API for the log file path in one property object.
        Note: Log file path is only prepared when it is set by user (not None).

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger for logging (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _log_file - The log file path for App/Tool/Script (default None).
            :methods:
                | __init__ - Initializes LogFile constructor.
                | log_file - Property methods for set/get log_file.
                | not_none - Checks is log file path not None.
                | __str__ - Returns the LogFile as string representation.
    '''

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _log_file: str | None

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes LogFile constructor.

            :param context_bundle: Context bundle for log_file.
            :type context_bundle: <ContextBundle>
            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        inject_context_bundle(self, context_bundle)
        self._log_file = None

    @property
    @vreport('getting log file {log_file}')
    @override
    def log_file(self) -> str | None:
        '''
            Property method for getting log file path.
            Note: Log file path is only prepared when it is set by user (not None).

            :return: The log file path in string format | None.
            :rtype: <str | None>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._log_file

    @log_file.setter
    @mcheck([('str:log_file', None)])
    @vreport('setting log file {log_file}')
    @override
    def log_file(self, log_file: str) -> None:
        '''
            Property method for setting log file path.
            Note: Log file path is only prepared when it is set by user (not None).

            :param log_file: The log file path in string format.
            :type log_file: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._log_file = log_file

    @vreport('checking log file {log_file}')
    @override
    def not_none(self) -> bool:
        '''
            Checks is log file path not None.
            Note: Log file path is only prepared when it is set by user (not None).

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._log_file is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the LogFile as string representation.

            :return: The LogFile as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
