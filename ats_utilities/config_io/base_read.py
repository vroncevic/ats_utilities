# -*- coding: UTF-8 -*-

'''
Module
    base_read.py
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
    Defines class BaseReadConfig with attribute(s) and method(s).
    Creates API for read operation for information/configuration files.
'''

import sys
from abc import abstractmethod

try:
    from ats_utilities import auto_str, VerboseRoot
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
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@auto_str
class BaseReadConfig(metaclass=VerboseRoot):
    '''
        Defines class BaseReadConfig with attribute(s) and method(s).
        Creates API for read operation for information/configuration files.
        Base config file reading mechanism.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _file_path - Configuration file path.
            :methods:
                | __init__ - Initial BaseReadConfig constructor.
                | file_path - Property methods for set/get operations.
                | is_not_none - Check is file path not None.
                | read_configuration - Read configuration (Abstract method).
    '''

    _verbose: bool
    _file_path: str | None

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial BaseReadConfig constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self._verbose = verbose
        self._file_path = None

    @property
    def file_path(self) -> str | None:
        '''
            Property method for getting file path.

            :return: Configuration file path | None
            :rtype: <str> | <NoneType>
            :exception: None
        '''
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str | None) -> None:
        '''
            Property method for setting file path.

            :param file_path: Configuration file path | None
            :type file_path: <str> | <NoneType>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:file_path', file_path)
        ])
        if error_id == ATSChecker.type_error:
            raise ATSTypeError(error_msg)
        if error_id == ATSChecker.value_error:
            raise ATSBadCallError(error_msg)
        file_path = str(file_path)
        self._file_path = file_path
        verbose_message(
            BaseReadConfig.verbose,  # pylint: disable=no-member
            self._verbose,
            tuple(f'set file path {file_path}')
        )

    def is_not_none(self) -> bool:
        '''
            Checking is file path None.

            :return: True (file path is not None) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return bool(self._file_path)

    @abstractmethod
    def read_configuration(self, verbose: bool = False) -> None:
        '''
            Read configuration from file (Abstract method).

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exception: NotImplementedError
        '''
