# -*- coding: UTF-8 -*-

'''
Module
    ats_logger_file.py
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
    Defines class ATSLoggerFile with attribute(s) and method(s).
    Creates an API for the ATS logger file path in one property object.
'''

import sys
from typing import List
from os.path import isfile

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_file_error import ATSFileError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.1.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSLoggerFile(ATSChecker):
    '''
        Defines class ATSLoggerFile with attribute(s) and method(s).
        Creates an API for the ATS logger file path in one property object.
        Log file path property.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _logger_path - Log file path.
            :methods:
                | __init__ - Initials ATSLoggerFile constructor.
                | logger_path - Property methods for set/get operations.
    '''

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials ATSLoggerFile constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__()
        self._verbose: bool = verbose
        self._logger_path: str | None = None

    @property
    def logger_path(self) -> str | None:
        '''
            Property method for getting log file path.

            :return: Log file path | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self._logger_path

    @logger_path.setter
    def logger_path(self, file_path: str | None) -> None:
        '''
            Property method for setting log file path.

            :param file_path: Log file path | None
            :type file_path: <str> | <NoneType>
            :exceptions: ATSTypeError | ATSFileError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('str:file_path', file_path)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if isfile(str(file_path)):
            self._logger_path = file_path
            verbose_message(
                self._verbose, [f'logger path {self._logger_path}']
            )
        else:
            raise ATSFileError(f'Check ATS log file path {file_path}')
