# -*- coding: UTF-8 -*-

'''
Module
    ats_logger_status.py
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
    Defines class ATSLoggerStatus with attribute(s) and method(s).
    Creates API for ATS logger status in one propery object.
'''

import sys

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggerStatus(ATSChecker):
    '''
        Defines class ATSLoggerStatus with attribute(s) and method(s).
        Creates API for ATS logger status in one propery object.
        Logging control mechanism.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _log_status - Logger status (enabled/disabled).
            :methods:
                | __init__ - Initial ATSLoggerStatus constructor.
                | logger_status - Property methods for set/get operations.
    '''

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial ATSLoggerStatus constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__()
        self._verbose: bool = verbose
        self._log_status: bool = False

    @property
    def logger_status(self) -> bool:
        '''
            Property method for getting logger status.

            :return: True (logger operative) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return self._log_status

    @logger_status.setter
    def logger_status(self, log_status: bool) -> None:
        '''
            Property method for setting logger status.

            :param log_status: Logger status (enable/disable logging)
            :type log_status: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('bool:log_status', log_status)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        self._log_status = log_status
        verbose_message(self._verbose, [f'logger status {log_status}'])
