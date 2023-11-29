# -*- coding: utf-8 -*-

'''
Module
    file_check.py
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
    Defines class FileCheck with attribute(s) and method(s).
    Creates API for checking operations with files.
'''

import sys
from os.path import splitext, isfile

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
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


class FileCheck(ATSChecker):
    '''
        Defines class FileCheck with attribute(s) and method(s).
        Creates API for checking operations with files.
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
                | __init__ - Initial FileCheck constructor.
                | check_path - Check file path.
                | check_mode -  Check operation mode for file.
                | check_format - Check file format by extension.
                | is_file_ok - Status of file for processing.
    '''

    MODES: list[str] = ['r', 'w', 'a', 'b', 'x', 't', '+']
    TRUSTED_EXTENSIONS: list[str] = ['makefile']

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial FileCheck constructor.

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

    def check_path(self, file_path: str | None, verbose: bool = False) -> None:
        '''
            Check file path.

            :param file_path: File path
            :type file_path: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('str:file_path', file_path)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        file_path = str(object=file_path)
        if not isfile(path=file_path):
            self._file_path_ok = False
            error_message(list(f'check file {file_path}'))
        else:
            self._file_path_ok = True
            verbose_message(
                self._verbose or verbose, [f'check file path {file_path}']
            )

    def check_mode(self, file_mode: str | None, verbose: bool = False) -> None:
        '''
            Check operation mode for file.

            :param file_mode: File mode ('r', 'w', 'a', 'b', 'x', 't', '+')
            :type file_mode: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:file_mode', file_mode)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
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
        file_path: str | None,
        file_format: str | None,
        verbose: bool = False
    ) -> None:
        '''
            Check file format by extension.

            :param file_path: File path
            :type file_path: <str> | <NoneType>
            :param file_format: File format (file extension)
            :type file_format: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('str:file_path', file_path), ('str:file_format', file_format)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        extension: str | None = None
        file_format, file_path = str(file_format), str(file_path)
        if file_format not in FileCheck.TRUSTED_EXTENSIONS:
            extension = splitext(file_path)[1]
            extension = extension.replace('.', '')
            if extension == '':
                extension = file_format
        else:
            if file_format.capitalize() in file_path:
                extension = 'makefile'
            else:
                extension = 'wrong_format'
        if not extension == file_format or extension == 'wrong_format':
            error_message([f'check extension [{file_format}] {file_path}'])
            self._file_format_ok = False
        else:
            self._file_format_ok = True
        verbose_message(
            self._verbose or verbose, [f'checked file format of {file_path}']
        )

    def is_file_ok(self) -> bool:
        '''
            Status of file for checking.

            :return: True (file validated) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return all([
            self._file_path_ok, self._file_mode_ok, self._file_format_ok
        ])
