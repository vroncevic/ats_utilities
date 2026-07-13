# -*- coding: UTF-8 -*-

'''
Module
    object2file.py
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
    Defines class Object2File with attribute(s) and method(s).
    Creates an API for writing configuration to a file from an object.
'''

from __future__ import annotations

from typing import override, Any

from ats_utilities.exceptions import ATSValueError
from ats_utilities.config_io.storer.iwrite import IWrite
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.file_bundle import FileBundle
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

class Object2File(IWrite):
    '''
        Defines class Object2File with attribute(s) and method(s).
        Creates an API for writing configuration to a file from an object.
        Conversion of Python object to file content.

        It defines:

            :attributes:
                | _MODE - File open mode.
                | _config_file_bundle - Configuration file bundle parameters (default None).
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger for logging (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _file_checker - FileCheck for checking file (default FileCheck).
                | _file_path - Configuration file path (default None).
                | _file_bundle_shared - File bundle parameters (default None).
                | _format_type - File format extension.
            :methods:
                | __init__ - Initializes Object2File constructor.
                | write_configuration - Writes configuration to a file.
                | _serialize_content - Serializes and writes the configuration to a stream.
                | __str__ - Returns the Object2File as string representation.
    '''

    _VALID_FORMATS: set[str] = {'xml', 'json', 'yaml', 'ini', 'cfg'}
    _MODE: str = 'w'
    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _config_file_bundle: ConfigFileBundle
    _file_checker: IFileCheck
    _file_path: str
    _file_bundle_shared: FileBundle
    _format_type: str

    def __init__(
        self,
        format_type: str,
        config_file: str | None,
        config_bundle: ConfigFileBundle | None = None
    ) -> None:
        '''
            Initializes Object2File constructor.

            :param format_type: Type of format (xml, json, yaml, ini, cfg).
            :type format_type: <str>
            :param config_file: Configuration file path in string format | None.
            :type config_file: <str | None>
            :param config_bundle: Configuration file bundle parameters | None.
            :type config_bundle: <ConfigFileBundle | None>
            :exceptions:
                | ATSTypeError: Invalid type in constructor arguments.
                | ATSValueError: Unsupported format type.
        '''
        self._format_type = str(format_type).lower()
        if self._format_type not in self._VALID_FORMATS:
            raise ATSValueError(f'Unsupported format type: {self._format_type}')

        self._config_file_bundle = config_bundle or ConfigFileBundle()
        factory_context_bundle(self, self._config_file_bundle.context)
        self._file_checker = make_component(
            self._config_file_bundle.file_checker, FileCheck,
            {'config_bundle': ContextBundle(checker=self._checker, reporter=self._reporter, verbose=self._verbose)}
        )
        validate_component(self._file_checker, IFileCheck, r'file_checker must be an IFileCheck instance')
        self._file_path = str(config_file)
        self._file_bundle_shared = FileBundle()
        self._file_bundle_shared.file_path = self._file_path
        self._file_bundle_shared.file_mode = self._MODE
        self._file_bundle_shared.file_format = self._format_type

    @vreport('write configuration to file {file_path}')
    @override
    def write_configuration(self, config: Any) -> bool:
        '''
            Writes configuration to a file.

            :param config: Configuration object.
            :type config: <Any>
            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        status: bool = False

        if not bool(config):
            return status

        with ConfFile(self._file_bundle_shared, self._config_file_bundle) as f:
            if bool(f):
                status = self._serialize_content(config, f)

        return status

    def _serialize_content(self, config: Any, f: Any) -> bool:
        '''
            Serializes and writes the configuration to a stream.

            :param config: Configuration object.
            :type config: <Any>
            :param f: Opened file object (stream).
            :type f: <Any>
            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
        '''
        if self._format_type in ('xml', 'cfg'):
            return bool(f.write(config.to_string()))
        if self._format_type in ('json', 'yaml'):
            return bool(f.write(config.encode()))
        if self._format_type == 'ini':
            return config.to_stream(f)
        return False

    @override
    def __str__(self) -> str:
        '''
            Returns the Object2File as string representation.

            :return: The Object2File as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
