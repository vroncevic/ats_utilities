# -*- coding: UTF-8 -*-

'''
Module
    conf_file.py
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
    Defines class ConfFile with attribute(s) and method(s).
    Creates an API for the configuration context manager.
'''

from typing import Any, List, Tuple, Dict, Optional
from ats_utilities.config_io.iconf_file import IConfFile
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.iconf_file import File
from ats_utilities.checker.decorator import validates_parameters

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ConfFile(IConfFile):
    '''
        Defines class ConfFile with attribute(s) and method(s).
        Creates an API for the configuration context manager.
        Configuration file context manager.

        It defines:

            :attributes:
                | __reporter - ATSReporter for check operations.
                | __file_path - Configuration file name.
                | __file_mode - File mode.
                | __file_format - File format.
                | __file - File object.
            :methods:
                | __init__ - Initials ConfFile constructor.
                | __enter__ - Opens configuration file in mode.
                | __exit__ - Closes configuration file.
    '''

    @validates_parameters([
        ('Optional[str]:file_path', None),
        ('Optional[str]:file_mode', None),
        ('Optional[str]:file', None)
    ])
    def __init__(
        self,
        file_path: Optional[str],
        file_mode: Optional[str],
        file_format: Optional[str],
        reporter: Optional[IATSReporter] = None,
        file_checker: Optional[IFileCheck] = None,
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
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IATSReporter]>
            :param file_checker: IFileCheck for file checking operations | None
            :type file_checker: <Optional[IFileCheck]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__file_checker: IFileCheck = file_checker or FileCheck(reporter, verbose)
        self.__verbose: bool = verbose

        if not bool(file_path):
            raise ATSValueError('missing file path')

        if not bool(file_mode):
            raise ATSValueError('missing file mode')

        if not bool(file_format):
            raise ATSValueError('missing file format')

        self.__file: File = None
        self.__file_path: Optional[str] = None
        self.__file_mode: Optional[str] = None
        self.__file_format: Optional[str] = None

        self.__file_checker.check_path(str(file_path), self.__verbose)
        self.__file_checker.check_mode(str(file_mode), self.__verbose)
        self.__file_checker.check_format(str(file_path), str(file_format), self.__verbose)

        if self.__file_checker.is_file_ok():
            self.__file_path = file_path
            self.__file_mode = file_mode
            self.__file_format = file_format

        self.__reporter.verbose(self.__verbose, [f'set file {file_path} {file_mode}'])

    def __enter__(self) -> File:
        '''
            Opens configuration file in mode.

            :return: File IO object | None
            :rtype: <File>
            :exceptions: None
        '''
        if self.__file_checker.is_file_ok():
            mode: str = self.__file_mode or "r"
            self.__file = open(str(self.__file_path), mode, encoding='utf-8')
            self.__reporter.verbose(self.__verbose, [f'open file {str(self.__file_path)} in mode [{mode}]'])
            self.__reporter.verbose(self.__verbose, [f'format file {str(self.__file_format)} is open for processing'])
        else:
            self.__reporter.error([f'check file {str(self.__file_path)}'])
            self.__file = None

        return self.__file

    def __exit__(self, *args: Tuple[Any, ...], **kwargs: Dict[Any, Any]) -> None:
        '''
            Closes configuration file.

            :param *args: List of arguments
            :type *args: <Tuple[Any, ...]>
            :param **kwargs: Dictionary of mapped arguments
            :type **kwargs: <Dict[Any, Any]>
            :exceptions: None
        '''
        if self.__file is not None and not self.__file.closed:
            self.__file.close()
            self.__reporter.verbose(self.__verbose, [f'close file {str(self.__file_path)}'])
