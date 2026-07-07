# -*- coding: UTF-8 -*-

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

from __future__ import annotations

from os.path import splitext, isfile
from typing import override

from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class FileCheck(IFileCheck):
    '''
        Defines class FileCheck with attribute(s) and method(s).
        Creates an API for checking operations with files.
        Mechanism for checking files.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _file_path_ok - File exist, path ok (default False).
                | _file_mode_ok - Supported file mode (default False).
                | _file_format_ok - File format is (not) expected (default False).
            :methods:
                | __init__ - Initializes FileCheck constructor.
                | check_path - Checks file path.
                | check_mode - Checks operation mode for file.
                | check_format - Checks file format by extension.
                | is_file_ok - Returns status for file.
                | __str__ - Returns the FileCheck as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _file_path_ok: bool
    _file_mode_ok: bool
    _file_format_ok: bool

    def __init__(self, config_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes FileCheck constructor.

            :param config_bundle: Bundle with checker, reporter and verbose | None.
            :type config_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, config_bundle)
        self._file_path_ok = False
        self._file_mode_ok = False
        self._file_format_ok = False

    @vcheck([('str:file_path', None)])
    @vreport('check file path {file_path_ok}')
    @override
    def check_path(self, file_path: str) -> None:
        '''
            Checks file path in string format.

            :param file_path: File path in string format.
            :type file_path: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._file_path_ok = isfile(file_path) if file_path is not None else False

        if not self._file_path_ok:
            self._reporter.error([f'check file {file_path}'])


    @vcheck([('str:file_mode', None)])
    @vreport('check file mode {file_mode_ok}')
    @override
    def check_mode(self, file_mode: str) -> None:
        '''
            Checks operation mode for file.

            :param file_mode: File mode in string format ('r', 'w', 'a', 'b', 'x', 't', '+').
            :type file_mode: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._file_mode_ok = bool(file_mode) and all(
            char in self.MODES for char in file_mode  # type: ignore
        )

        if not self._file_mode_ok:
            self._reporter.error([f'not supported file mode [{file_mode}]'])

    @vcheck([('str:file_path', None), ('str:file_format', None)])
    @vreport('check file format {file_format_ok}')
    @override
    def check_format(self, file_path: str, file_format: str) -> None:
        '''
            Checks file format by extension.

            :param file_path: File path in string format.
            :type file_path: <str>
            :param file_format: File format (file extension).
            :type file_format: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        extension: str | None = None
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
            self._file_format_ok = False
        else:
            self._file_format_ok = True

    @vreport('check is file ok path: {file_path_ok}, mode: {file_mode_ok}, format: {file_format_ok}')
    @override
    def is_file_ok(self) -> bool:
        '''
            Returns status for file.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return all([self._file_path_ok, self._file_mode_ok, self._file_format_ok])


    @override
    def __str__(self) -> str:
        '''
            Returns the FileCheck as string representation.

            :return: The FileCheck as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
