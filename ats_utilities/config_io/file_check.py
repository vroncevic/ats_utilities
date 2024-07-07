# -*- coding: utf-8 -*-

'''
Module
    file_check.py
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
    Defines class FileCheck with attribute(s) and method(s).
    Creates an API for checking operations with files.
'''

import sys
from typing import List, Optional
from os.path import splitext, isfile

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
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


class FileCheck(ATSChecker):
    '''
        Defines class FileCheck with attribute(s) and method(s).
        Creates an API for checking operations with files.
        Mechanism for checking files.

        It defines:

            :attributes:
                | MODES - Mode file operations.
                | TRUSTED_EXTENSIONS - List of trusted file extensions.
                | _verbose - Enable/Disable verbose option.
                | _file_path_ok - File exist, path ok.
                | _file_mode_ok - Supported file mode.
                | _file_format_ok - File format is (not) expected.
            :methods:
                | __init__ - Initials FileCheck constructor.
                | check_path - Checks file path.
                | check_mode -  Checks operation mode for file.
                | check_format - Checks file format by extension.
                | is_file_ok - Returns status for file.
    '''

    MODES: list[str] = ['r', 'w', 'a', 'b', 'x', 't', '+']
    TRUSTED_EXTENSIONS: list[str] = ['makefile']

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials FileCheck constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__()
        self._verbose: bool = verbose
        self._file_path_ok: bool = False
        self._file_mode_ok: bool = False
        self._file_format_ok: bool = False
        verbose_message(self._verbose, ['init ATS check file'])

    def check_path(
        self, file_path: Optional[str], verbose: bool = False
    ) -> None:
        '''
            Checks file path.

            :param file_path: File path | None
            :type file_path: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('str:file_path', file_path)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        file_path = str(file_path)
        if not isfile(file_path):
            self._file_path_ok = False
            error_message([f'check file {file_path}'])
        else:
            self._file_path_ok = True
            verbose_message(
                self._verbose or verbose, [f'check file path {file_path}']
            )

    def check_mode(
        self, file_mode: Optional[str], verbose: bool = False
    ) -> None:
        '''
            Checks operation mode for file.

            :param file_mode: File mode ('r', 'w', 'a', 'b', 'x', 't', '+')
            :type file_mode: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([('str:file_mode', file_mode)])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        file_mode = str(file_mode)
        mode_checks: list[bool] = []
        for mode in list(file_mode):
            if mode not in self.MODES:
                mode_checks.append(False)
            else:
                mode_checks.append(True)
        if all(mode_checks):
            self._file_mode_ok = True
            verbose_message(
                self._verbose or verbose,
                [f'supported file mode [{file_mode}]']
            )
        else:
            self._file_mode_ok = False
            error_message([f'not supported file mode [{file_mode}]'])

    def check_format(
        self,
        file_path: Optional[str],
        file_format: Optional[str],
        verbose: bool = False
    ) -> None:
        '''
            Checks file format by extension.

            :param file_path: File path | None
            :type file_path: <Optional[str]>
            :param file_format: File format (file extension) | None
            :type file_format: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('str:file_path', file_path), ('str:file_format', file_format)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        extension: Optional[str] = None
        file_format, file_path = str(file_format), str(file_path)
        if file_format not in self.TRUSTED_EXTENSIONS:
            extension = splitext(file_path)[1]
            extension = extension.replace('.', '')
            if extension == '':
                extension = file_format
        else:
            if file_format.capitalize() in file_path:
                extension = 'makefile'
        if not extension == file_format:
            error_message([f'check extension [{file_format}] {file_path}'])
            self._file_format_ok = False
        else:
            self._file_format_ok = True
        verbose_message(
            self._verbose or verbose, [f'checked file format {file_path}']
        )

    def is_file_ok(self) -> bool:
        '''
            Returns status for file.

            :return: True (file validated and ok) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return all([
            self._file_path_ok, self._file_mode_ok, self._file_format_ok
        ])
