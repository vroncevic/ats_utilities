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
from ats_utilities.checker.ichecker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.console_io.proxy_reporter import vreporter
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.iconf_file import File
from ats_utilities.exceptions.ats_value_error import ATSValueError

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
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __file_path - Configuration file path (default set None).
                | __file_mode - Configuration file mode (default set None).
                | __file_format - Configuration file format (default set None).
                | __file - File object (default set None).
                | __verbose - Enable/Disable verbose option (default False).
            :methods:
                | __init__ - Initials ConfFile constructor.
                | __enter__ - Opens configuration file in mode.
                | __exit__ - Closes configuration file.
                | __str__ - Returns the string representation of configuration file component.
    '''

    def __init__(
        self,
        file_path: Optional[str],
        file_mode: Optional[str],
        file_format: Optional[str],
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        file_checker: Optional[IFileCheck] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ConfFile constructor.

            :param file_path: Configuration file path (default set None) | None
            :type file_path: <Optional[str]>
            :param file_mode: Configuration file mode (default set None) | None
            :type file_mode: <Optional[str]>
            :param file_format: Configuration file format (default set None) | None
            :type file_format: <Optional[str]>
            :param checker: Parameters checker (default set ATSChecker) | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: Reporter for messaging (default set ATSReporter) | None
            :type reporter: <Optional[IATSReporter]>
            :param file_checker: Checking operations (default set FileCheck) | None
            :type file_checker: <Optional[IFileCheck]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        # No dependency injection then use default ones.
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter(checker=self.__checker)
        self.__verbose: bool = verbose
        self.__file_checker: IFileCheck = file_checker or FileCheck(
            checker=self.__checker, reporter=self.__reporter, verbose=self.__verbose
        )

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

        self.__file_checker.check_path(str(file_path))
        self.__file_checker.check_mode(str(file_mode))
        self.__file_checker.check_format(str(file_path), str(file_format))

        if self.__file_checker.is_file_ok():
            self.__file_path = file_path
            self.__file_mode = file_mode
            self.__file_format = file_format

        self.__reporter.verbose(self.__verbose, [f'set file {file_path} {file_mode}'])

    @vreporter('open file {file_path} with mode {file_mode}')
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
        else:
            self.__reporter.error([f'check file {str(self.__file_path)}'])
            self.__file = None

        return self.__file

    @vreporter('close file {file_path}')
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

    def __str__(self) -> str:
        '''
            Returns the string representation of configuration file component.

            :return: The configuration file component as string representation
            :rtype: <str>
            :exceptions: None
        '''
        file_path = str(self.__file_path).replace('\n', '\n    ')
        file_mode = str(self.__file_mode).replace('\n', '\n    ')
        file_format = str(self.__file_format).replace('\n', '\n    ')
        file = str(self.__file).replace('\n', '\n    ')
        checker = str(self.__checker).replace('\n', '\n    ')
        reporter = str(self.__reporter).replace('\n', '\n    ')
        verbose = str(self.__verbose).replace('\n', '\n    ')

        return (
            f'<{self.__class__.__name__}(\n'
            f'    file_path={file_path},\n'
            f'    file_mode={file_mode},\n'
            f'    file_format={file_format},\n'
            f'    file={file},\n'
            f'    checker={checker},\n'
            f'    reporter={reporter},\n'
            f'    verbose={verbose}\n)> at 0x{id(self):x}'
        )
