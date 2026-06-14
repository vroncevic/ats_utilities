# -*- coding: utf-8 -*-

'''
Module
    file_check.py
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
    Defines class FileCheck with attribute(s) and method(s).
    Creates an API for checking operations with files.
'''

from typing import List, Optional
from os.path import splitext, isfile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.checker.decorator import validates_parameters

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class FileCheck(IFileCheck):
    '''
        Defines class FileCheck with attribute(s) and method(s).
        Creates an API for checking operations with files.
        Mechanism for checking files.

        It defines:

            :attributes:
                | __reporter - ATSReporter for check operations.
                | __verbose - Enable/Disable verbose option.
                | __file_path_ok - File exist, path ok.
                | __file_mode_ok - Supported file mode.
                | __file_format_ok - File format is (not) expected.
            :methods:
                | __init__ - Initials FileCheck constructor.
                | check_path - Checks file path.
                | check_mode -  Checks operation mode for file.
                | check_format - Checks file format by extension.
                | is_file_ok - Returns status for file.
    '''

    def __init__(self, reporter: Optional[IATSReporter] = None, verbose: bool = False) -> None:
        '''
            Initials FileCheck constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IATSReporter]>
            :exceptions: None
        '''
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__file_path_ok: bool = False
        self.__file_mode_ok: bool = False
        self.__file_format_ok: bool = False
        self.__reporter.verbose(self.__verbose, ['init ATS check file'])

    @validates_parameters([('Optional[str]:file_path', None)])
    def check_path(self, file_path: Optional[str], verbose: bool = False) -> None:
        '''
            Checks file path.

            :param file_path: File path | None
            :type file_path: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError by validate_parameters
        '''
        # file_path is guaranteed to be str if no exception was raised
        self.__file_path_ok = isfile(file_path)  # type: ignore

        if self.__file_path_ok:
            self.__reporter.verbose(self.__verbose or verbose, [f'check file path {file_path}'])
        else:
            self.__reporter.error([f'check file {file_path}'])

    @validates_parameters([('Optional[str]:file_mode', None)])
    def check_mode(self, file_mode: Optional[str], verbose: bool = False) -> None:
        '''
            Checks operation mode for file.

            :param file_mode: File mode ('r', 'w', 'a', 'b', 'x', 't', '+')
            :type file_mode: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        # file_mode is guaranteed to be str
        self.__file_mode_ok = all(char in self.MODES for char in file_mode)  # type: ignore

        if self.__file_mode_ok:
            self.__reporter.verbose(self.__verbose or verbose, [f'supported file mode [{file_mode}]'])
        else:
            self.__reporter.error([f'not supported file mode [{file_mode}]'])

    @validates_parameters([('Optional[str]:file_path', None), ('Optional[str]:file_format', None)])
    def check_format(self, file_path: Optional[str], file_format: Optional[str], verbose: bool = False) -> None:
        '''
            Checks file format by extension.

            :param file_path: File path | None
            :type file_path: <Optional[str]>
            :param file_format: File format (file extension) | None
            :type file_format: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError by validate_parameters
        '''
        extension: Optional[str] = None
        fmt_str, path_str = str(file_format), str(file_path)

        if fmt_str not in self.TRUSTED_EXTENSIONS:
            extension = splitext(path_str)[1]
            extension = extension.replace('.', '')

            if extension == '':
                extension = fmt_str

        elif fmt_str.capitalize() in path_str:
            extension = 'makefile'

        if extension != fmt_str:
            self.__reporter.error([f'check extension [{fmt_str}] {path_str}'])
            self.__file_format_ok = False
        else:
            self.__file_format_ok = True

        self.__reporter.verbose(self.__verbose or verbose, [f'checked file format {path_str}'])

    def is_file_ok(self) -> bool:
        '''
            Returns status for file.

            :return: True (file validated and ok) | False
            :rtype: <bool>
            :exceptions: None
        '''
        return all([self.__file_path_ok, self.__file_mode_ok, self.__file_format_ok])
