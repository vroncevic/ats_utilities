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
from ats_utilities.factory_class import inject, get_private_attr, format_instance_to_string
from ats_utilities.config_io.iconf_file import IConfFile
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import ATSChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import ATSReporter
from ats_utilities.reporter.proxy_reporter import vreporter
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
        checker: Optional[IChecker] = None,
        reporter: Optional[IReporter] = None,
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
            :type checker: <Optional[IChecker]>
            :param reporter: Reporter for messaging (default set ATSReporter) | None
            :type reporter: <Optional[IReporter]>
            :param file_checker: Checking operations (default set FileCheck) | None
            :type file_checker: <Optional[IFileCheck]>
            :param verbose: Enable/Disable verbose option (default False)
            :type verbose: <bool>
            :exceptions: ATSValueError
        '''
        # No dependency injection then use default ones.
        inject(
            self,
            ('checker', checker, ATSChecker, None),
            ('reporter', reporter, ATSReporter, ['checker']),
            ('verbose', verbose, False, None),
            ('file_checker', file_checker, FileCheck, ['checker', 'reporter', 'verbose'])
        )

        if not bool(file_path):
            raise ATSValueError('missing file path')

        if not bool(file_mode):
            raise ATSValueError('missing file mode')

        if not bool(file_format):
            raise ATSValueError('missing file format')

        self.__file: Optional[File] = None
        self.__file_path: Optional[str] = None
        self.__file_mode: Optional[str] = None

        self._file_checker.check_path(file_path)
        self._file_checker.check_mode(file_mode)
        self._file_checker.check_format(file_path, file_format)

        if self._file_checker.is_file_ok():
            self.__file_path = file_path
            self.__file_mode = file_mode

    @vreporter('open file {file_path} with mode {file_mode}')
    def __enter__(self) -> Optional[File]:
        '''
            Opens configuration file in mode.

            :return: File IO object | None
            :rtype: <File>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        if self.__file_path and self.__file_mode:
            self.__file = open(self.__file_path, self.__file_mode, encoding='utf-8')

        return self.__file

    @vreporter('close file {file_path}')
    def __exit__(self, *args: Tuple[Any, ...], **kwargs: Dict[Any, Any]) -> None:
        '''
            Closes configuration file.

            :param *args: List of arguments
            :type *args: <Tuple[Any, ...]>
            :param **kwargs: Dictionary of mapped arguments
            :type **kwargs: <Dict[Any, Any]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        if self.__file and not self.__file.closed:
            self.__file.close()

    @property
    def _file_checker(self) -> IFileCheck:
        '''
            Property method for getting the internal file checker instance.

            :return: The file checker instance in IFileCheck format
            :rtype: <IFileCheck>
            :exceptions: None
        '''
        return get_private_attr(self, 'file_checker')

    def __str__(self) -> str:
        '''
            Returns the string representation of configuration file component.

            :return: The configuration file component as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
