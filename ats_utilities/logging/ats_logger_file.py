# -*- coding: UTF-8 -*-

'''
Module
    ats_logger_file.py
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
    Defines class ATSLoggerFile with attribute(s) and method(s).
    Creates API for ATS logger file path in one propery object.
'''

import sys
from os.path import isfile

try:
    from ats_utilities import auto_str, VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
    from ats_utilities.exceptions.ats_file_error import ATSFileError
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
class ATSLoggerFile(metaclass=VerboseRoot):
    '''
        Defines class ATSLoggerFile with attribute(s) and method(s).
        Creates API for ATS logger file path in one propery object.
        Log file property.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _logger_file - Log file path.
            :methods:
                | __init__ - Initial ATSLoggerFile constructor.
                | logger_file - property methods for set/get operations.
                | __str__ - str dunder method for ATSLoggerFile.
    '''

    _verbose: bool
    _logger_file: str | None

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial ATSLoggerFile constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self._verbose = verbose
        self._logger_file = None

    @property
    def logger_file(self) -> str | None:
        '''
            Property method for getting log file path.

            :return: log file path | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self._logger_file

    @logger_file.setter
    def logger_file(self, logger_file: str | None) -> None:
        '''
            Property method for setting log file path.

            :param logger_file: Log file path
            :type logger_file: <str> | <NoneType>
            :exceptions: ATSTypeError | ATSBadCallError | ATSFileError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:logger_file', logger_file)
        ])
        if error_id == ATSChecker.type_error:
            raise ATSTypeError(error_msg)
        if error_id == ATSChecker.value_error:
            raise ATSBadCallError(error_msg)
        if isfile(str(logger_file)):
            self._logger_file = logger_file
            verbose_message(
                ATSLoggerFile.verbose,  # pylint: disable=no-member
                self._verbose,
                tuple(str(logger_file))
            )
        else:
            raise ATSFileError(f'Check ATS log file path {logger_file}')
