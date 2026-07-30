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
    Defines class LogFormatter with attribute(s) and method(s).
    Provides an API for log formatting (removing color codes, etc.).
'''

from __future__ import annotations

from ats_utilities.validation.check_value import not_none, not_empty
from ats_utilities.validation.check_type import istype
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class LogFormatter:
    '''
        Defines class LogFormatter with attribute(s) and method(s).
        Provides an API for log formatting.

        It defines:

            :attributes:
                | _ANSI_ESCAPE - Regex pattern for ANSI escape codes.
                | DEFAULT_LOG_FORMAT - Default log message format.
                | DEFAULT_LOG_DATEFMT - Default log message date format.
                | _log_format - Log message format.
                | _log_datefmt - Log message date format.
            :methods:
                | __init__ - Initializes log formatter.
                | set_format - Sets the log format.
                | get_format - Gets the log format.
                | set_date_format - Sets the log date format.
                | get_date_format - Gets the log date format.
                | __str__ - Returns log formatter as string representation.
    '''

    DEFAULT_LOG_FORMAT: str = '%(asctime)s - %(levelname)s - %(message)s'
    DEFAULT_LOG_DATEFMT: str = '%m/%d/%Y %I:%M:%S %p'
    _log_format: str
    _log_datefmt: str

    def __init__(self, log_format: str | None, log_datefmt: str | None) -> None:
        '''
            Initializes log formatter.

            :param log_format: Log message format.
            :param log_datefmt: Log message date format.
            :exceptions:
                | ATSTypeError: Log format or date format is not a string.
                | ATSValueError: Log format or date format is empty.
        '''
        ctx: str = 'log_formatter::init(...)'

        if log_format is not None:
            msg_log_format_istype: str = 'log format must be a string'
            msg_log_format_empty: str = 'log format cannot be empty'

            istype(log_format, str, ctx, msg_log_format_istype)
            not_empty(log_format, ctx, msg_log_format_empty)

            self._log_format = log_format
        else:
            self._log_format = self.DEFAULT_LOG_FORMAT

        if log_datefmt is not None:
            msg_log_datefmt_istype: str = 'log date format must be a string'
            msg_log_datefmt_empty: str = 'log date format cannot be empty'

            istype(log_datefmt, str, ctx, msg_log_datefmt_istype)
            not_empty(log_datefmt, ctx, msg_log_datefmt_empty)

            self._log_datefmt = log_datefmt
        else:
            self._log_datefmt = self.DEFAULT_LOG_DATEFMT

    def set_format(self, log_format: str) -> None:
        '''
            Sets the log format.

            :param log_format: The log format.
            :exceptions:
                | ATSValueError: Log format must be provided and not empty.
                | ATSTypeError:  Log format must be a string.
        '''
        ctx: str = 'log_formatter::set_format(...)'

        msg_log_format_none: str = 'log format must be provided'
        msg_log_format_istype: str = 'log format must be a string'
        msg_log_format_empty: str = 'log format cannot be empty'

        not_none(log_format, ctx, msg_log_format_none)
        istype(log_format, str, ctx, msg_log_format_istype)
        not_empty(log_format, ctx, msg_log_format_empty)

        self._log_format = log_format

    def get_format(self) -> str:
        '''
            Gets the log format.

            :return: The log format.
            :exceptions: None.
        '''
        return self._log_format

    def set_date_format(self, log_datefmt: str) -> None:
        '''
            Sets the log date format.

            :param log_datefmt: The log date format.
            :exceptions:
                | ATSValueError: Log date format must be provided and not empty.
                | ATSTypeError:  Log date format must be a string.
        '''
        ctx: str = 'log_formatter::set_date_format(...)'

        msg_log_datefmt_none: str = 'log date format must be provided'
        msg_log_datefmt_istype: str = 'log date format must be a string'
        msg_log_datefmt_empty: str = 'log date format cannot be empty'

        not_none(log_datefmt, ctx, msg_log_datefmt_none)
        istype(log_datefmt, str, ctx, msg_log_datefmt_istype)
        not_empty(log_datefmt, ctx, msg_log_datefmt_empty)

        self._log_datefmt = log_datefmt

    def get_date_format(self) -> str:
        '''
            Gets the log date format.

            :return: The log date format.
            :exceptions: None.
        '''
        return self._log_datefmt

    def __str__(self) -> str:
        '''
            Returns log formatter as string representation.

            :return: Log formatter as string representation.
            :exceptions: None.
        '''
        return to_str(self)
