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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.config_io.iconf_file import IConfFile
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.iconf_file import File
from ats_utilities.config_io.file_bundle import FileBundle
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import to_str
from ats_utilities.factory_value import require_not_empty
from ats_utilities.factory_type import check_type

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ConfFile(IConfFile):
    '''
        Defines class ConfFile with attribute(s) and method(s).
        Creates an API for the configuration context manager.
        Configuration file context manager.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger for logging (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _file_path - Configuration file path (default None).
                | _file_mode - Configuration file mode (default None).
                | _file - File object (default None).
            :methods:
                | __init__ - Initializes ConfFile constructor.
                | __enter__ - Opens configuration file in mode.
                | __exit__ - Closes configuration file.
                | __str__ - Returns the ConfFile as string representation.
    '''

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _file: File | None
    _file_path: str | None
    _file_mode: str | None

    def __init__(
        self,
        file_bundle: FileBundle | None = None,
        config_file_bundle: ConfigFileBundle | None = None
    ) -> None:
        '''
            Initializes ConfFile constructor.

            :param file_bundle: File bundle parameters | None.
            :type file_bundle: <FileBundle | None>
            :param config_file_bundle: File configuration bundle parameters | None.
            :type config_file_bundle: <ConfigFileBundle | None>
            :exceptions:
                | ATSTypeError: File bundle must be a FileBundle instance or None.
                | ATSTypeError: Config file bundle must be a ConfigFileBundle instance or None.
                | ATSValueError: Missing file path.
                | ATSValueError: Missing file mode.
                | ATSValueError: Missing file format.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: File mode must be a string.
                | ATSTypeError: File format must be a string.
        '''
        bundle: FileBundle = file_bundle or FileBundle()
        config_bundle: ConfigFileBundle = config_file_bundle or ConfigFileBundle()
        factory_context_bundle(self, config_bundle.context)
        shared_bundle: ContextBundle = ContextBundle(
            checker=self._checker, reporter=self._reporter, verbose=self._verbose
        )
        file_checker: IFileCheck = make_component(config_bundle.file_checker, FileCheck, {'config_bundle': shared_bundle})
        validate_component(file_checker, IFileCheck, r'file_checker must be an IFileCheck instance')

        require_not_empty(bundle.file_path, r'missing file path')
        require_not_empty(bundle.file_mode, r'missing file mode')
        require_not_empty(bundle.file_format, r'missing file format')
        check_type(bundle.file_path, str, r'file_path must be a string')
        check_type(bundle.file_mode, str, r'file_mode must be a string')
        check_type(bundle.file_format, str, r'file_format must be a string')

        self._file = None
        self._file_path = None
        self._file_mode = None

        file_checker.check_path(bundle.file_path)
        file_checker.check_mode(bundle.file_mode)
        file_checker.check_format(bundle.file_path, bundle.file_format)

        if file_checker.is_file_ok():
            self._file_path = bundle.file_path
            self._file_mode = bundle.file_mode

    @vreport('open file {file_path} with mode {file_mode}')
    @override
    def __enter__(self) -> File | None:
        '''
            Opens configuration file in mode.

            :return: File IO object | None.
            :rtype: <File>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        if self._file_path and self._file_mode:
            self._file = open(self._file_path, self._file_mode, encoding='utf-8')

        return self._file

    @vreport('close file {file_path}')
    @override
    def __exit__(self, *args: tuple[Any, ...], **kwargs: Mapping[Any, Any]) -> None:
        '''
            Closes configuration file.

            :param args: List of arguments.
            :type args: <tuple[Any, ...]>
            :param kwargs: Dictionary of mapped arguments.
            :type kwargs: <Mapping[Any, Any]>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        if self._file and not self._file.closed:
            self._file.close()

    @override
    def __str__(self) -> str:
        '''
            Returns the ConfFile as string representation.

            :return: The ConfFile as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
