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
    Defines class ConfFile with attribute(s) and method(s).
    Creates an API for the configuration context manager.
'''

import sys
from typing import Any, List, Tuple, Dict, IO, Optional, TypeAlias

try:
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

# Optional bytes, str IO type
File: TypeAlias = Optional[IO[str]]


class ConfFile(FileCheck):
    '''
        Defines class ConfFile with attribute(s) and method(s).
        Creates an API for the configuration context manager.
        Configuration file context manager.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
                | _file_path - Configuration file name.
                | _file_mode - File mode.
                | _file_format - File format.
                | _file - File object.
            :methods:
                | __init__ - Initials ConfFile constructor.
                | __enter__ - Opens configuration file in mode.
                | __exit__ - Closes configuration file.
    '''

    def __init__(
        self,
        file_path: Optional[str],
        file_mode: Optional[str],
        file_format: Optional[str],
        verbose: bool = False
    ) -> None:
        '''
            Initials ConfFile constructor.

            :param file_path: Configuration file path | None
            :type file_path: <Optional[str]>
            :param file_mode: File mode for configuration file | None
            :type file_mode: <Optional[str]>
            :param file_format: File format | None
            :type file_format: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = checker.check_params([
            ('str:file_path', file_path),
            ('str:file_mode', file_mode),
            ('str:file_format', file_format)
        ])
        if error_id == checker.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(file_path):
            raise ATSValueError('mising file path')
        if not bool(file_mode):
            raise ATSValueError('missing file mode')
        if not bool(file_format):
            raise ATSValueError('missing file format')
        super().__init__(verbose)
        self._verbose: bool = verbose
        self._file: File = None
        self._file_path: Optional[str] = None
        self._file_mode: Optional[str] = None
        self._file_format: Optional[str] = None
        self.check_path(str(file_path), self._verbose)
        self.check_mode(str(file_mode), self._verbose)
        self.check_format(str(file_format), file_format, self._verbose)
        if self.is_file_ok():
            self._file_path = file_path
            self._file_mode = file_mode
            self._file_format = file_format
        verbose_message(self._verbose, [f'set file {file_path} {file_mode}'])

    def __enter__(self) -> File:
        '''
            Opens configuration file in mode.

            :return: File IO object | None
            :rtype: <File>
            :exceptions: None
        '''
        if self.is_file_ok():
            mode: str = "r" if not bool(
                str(self._file_mode)
            ) else str(self._file_mode)
            self._file = open(str(self._file_path), mode, encoding='utf-8')
        else:
            error_message([f'check file {str(self._file_path)}'])
            self._file = None
        return self._file

    def __exit__(
        self, *args: Tuple[Any, ...], **kwargs: Dict[Any, Any]
    ) -> None:
        '''
            Closes configuration file.

            :param *args: List of arguments
            :type file_path: <Tuple[Any, ...]>
            :param **kwargs: Dictionary of mapped arguments
            :type file_path: <Dict[Any, Any]>
            :exceptions: None
        '''
        if self._file is not None and not self._file.closed:
            self._file.close()
