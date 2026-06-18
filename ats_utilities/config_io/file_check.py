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
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.proxy_reporter import vreporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import get_private_attr, format_instance_to_string

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
                | __checker - Factoriezed parameters checker (default ATSChecker).
                | __reporter - Factoriezed reporter for messaging (default ATSReporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __file_path_ok - File exist, path ok (default False).
                | __file_mode_ok - Supported file mode (default False).
                | __file_format_ok - File format is (not) expected (default False).
            :methods:
                | __init__ - Initials FileCheck constructor.
                | check_path - Checks file path.
                | check_mode -  Checks operation mode for file.
                | check_format - Checks file format by extension.
                | is_file_ok - Returns status for file.
                | _reporter - Property method for getting the internal reporter instance.
                | __str__ - Returns the string representation of file check component.
    '''

    def __init__(self, config_bundle: Optional[ContextBundle] = None) -> None:
        '''
            Initials FileCheck constructor.

            :param config_bundle: Bundle with checker, reporter and verbose | None
            :type config_bundle: <Optional[ContextBundle]>
            :exceptions: None
        '''
        factory_context_bundle(self, config_bundle)
        self.__file_path_ok: bool = False
        self.__file_mode_ok: bool = False
        self.__file_format_ok: bool = False

    @validator([('Optional[str]:file_path', None)])
    @vreporter('check file path {file_path_ok}')
    def check_path(self, file_path: Optional[str]) -> None:
        '''
            Checks file path in string format.

            :param file_path: File path in string format | None
            :type file_path: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__file_path_ok = isfile(file_path)  # type: ignore

        if not self.__file_path_ok:
            self._reporter.error([f'check file {file_path}'])

    @validator([('Optional[str]:file_mode', None)])
    @vreporter('check file mode {file_mode_ok}')
    def check_mode(self, file_mode: Optional[str]) -> None:
        '''
            Checks operation mode for file.

            :param file_mode: File mode in string format ('r', 'w', 'a', 'b', 'x', 't', '+')
            :type file_mode: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__file_mode_ok = bool(file_mode) and all(
            char in self.MODES for char in file_mode  # type: ignore
        )

        if not self.__file_mode_ok:
            self._reporter.error([f'not supported file mode [{file_mode}]'])

    @validator([('Optional[str]:file_path', None), ('Optional[str]:file_format', None)])
    @vreporter('check file format {file_format_ok}')
    def check_format(self, file_path: Optional[str], file_format: Optional[str]) -> None:
        '''
            Checks file format by extension.

            :param file_path: File path in string format | None
            :type file_path: <Optional[str]>
            :param file_format: File format (file extension) | None
            :type file_format: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
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
            self._reporter.error([f'check extension [{fmt_str}] {path_str}'])
            self.__file_format_ok = False
        else:
            self.__file_format_ok = True

    @vreporter('check is file ok path: {file_path_ok}, mode: {file_mode_ok}, format: {file_format_ok}')
    def is_file_ok(self) -> bool:
        '''
            Returns status for file.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return all([self.__file_path_ok, self.__file_mode_ok, self.__file_format_ok])

    @property
    def _reporter(self) -> IReporter:
        '''
            Property method for getting the internal reporter instance.

            :return: The reporter instance in IReporter format
            :rtype: <IReporter>
            :exceptions: None
        '''
        return get_private_attr(self, 'reporter')

    def __str__(self) -> str:
        '''
            Returns the string representation of file check component.

            :return: The file check component as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
