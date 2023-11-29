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
    Defines class ConfFile with attribute(s) and method(s).
    Creates API for information/configuration context manager.
'''

import sys
from typing import Any, Tuple, Dict, IO

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
    from ats_utilities.config_io.file_check import FileCheck
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


class ConfFile(FileCheck):
    '''
        Defines class ConfFile with attribute(s) and method(s).
        Creates API for information/configuration context manager.
        Configuration file context manager.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _file_path - Configuration file name.
                | _file_mode - File mode.
                | _file_format - File format.
                | _file - File object.
            :methods:
                | __init__ - Initial ConfFile constructor.
                | __enter__ - Open configuration file in mode.
                | __exit__ - Close configuration file.
    '''

    def __init__(
        self, file_path: str | None,
        file_mode: str | None,
        file_format: str | None,
        verbose: bool = False
    ) -> None:
        '''
            Initial ConfFile constructor.

            :param file_path: Configuration file name | None
            :type file_path: <str> | <NoneType>
            :param file_mode: Open configuration file in mode | None
            :type file_mode: <str> | <NoneType>
            :param file_format: File format | None
            :type file_format: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:file_path', file_path),
            ('str:file_mode', file_mode),
            ('str:file_format', file_format)
        ])
        if error_id == checker.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == checker.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        super().__init__(verbose)
        self._verbose: bool = verbose
        self._file: IO[str] | None = None
        self._file_path: str | None = None
        self._file_mode: str | None = None
        self._file_format: str | None = None
        self.check_path(str(file_path), self._verbose)
        self.check_mode(str(file_mode), self._verbose)
        self.check_format(str(file_format), file_format, self._verbose)
        if self.is_file_ok():
            self._file_path = file_path
            self._file_mode = file_mode
            self._file_format = file_format
        verbose_message(self._verbose, [f'set file {file_path} {file_mode}'])

    def __enter__(self) -> IO[str] | None:
        '''
            Open configuration file in mode.

            :return: file object | None
            :rtype: <IO[str]> | <NoneType>
            :exceptions: None
        '''
        if self.is_file_ok():
            mode: str = "r" if not bool(
                str(self._file_mode)
            ) else str(self._file_mode)
            self._file = open(
                str(self._file_path), mode, encoding="utf-8"
            )
        else:
            error_message([f'check file {str(self._file_path)}'])
            self._file = None
        return self._file

    def __exit__(
        self, *args: Tuple[Any, ...], **kwargs: Dict[Any, Any]
    ) -> None:
        '''
            Close configuration file.

            :param *args: List of arguments
            :type file_path: <Tuple[Any, ...]>
            :param **kwargs: Dictionary of mapped arguments
            :type file_path: <Dict[Any, Any]>
            :exceptions: None
        '''
        if self._file is not None:
            if not self._file.closed:
                self._file.close()
