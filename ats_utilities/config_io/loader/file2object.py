# -*- coding: UTF-8 -*-

'''
Module
    file2object.py
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
    Defines class File2Object with attribute(s) and method(s).
    Creates an API for reading configuration from file and deploying as object.
    1th level of configuration loader implementation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override, Any

from ats_utilities.exceptions import ATSValueError
from ats_utilities.config_io.loader.iread import IRead
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

from ats_utilities.config_io.processor.xml_processor import XMLProcessor
from ats_utilities.config_io.processor.json_processor import JSONProcessor
from ats_utilities.config_io.processor.yaml_processor import YAMLProcessor
from ats_utilities.config_io.processor.ini_processor import INIProcessor
from ats_utilities.config_io.processor.cfg_processor import CFGProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class File2Object(IRead):
    '''
        Defines class File2Object with attribute(s) and method(s).
        Creates an API for reading configuration from file and deploying as object.
        0th level of configuration loader implementation.

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
                | _processor - Injected format-specific processor.
            :methods:
                | __init__ - Initializes File2Object constructor.
                | read_configuration - Reads configuration from a file.
                | _parse_content - Parses the content from the file stream.
                | __str__ - Returns the File2Object as string representation.
    '''

    _PROCESSOR_MAPPING: Mapping[str, type] = {
        'xml': XMLProcessor,
        'json': JSONProcessor,
        'yaml': YAMLProcessor,
        'ini': INIProcessor,
        'cfg': CFGProcessor
    }
    _MODE: str = 'r'
    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _config_file_bundle: ConfigFileBundle
    _file_checker: IFileCheck
    _file_path: str
    _file_bundle_shared: FileBundle
    _format_type: str
    _processor: Any

    def __init__(
        self,
        format_type: str,
        config_file: str | None,
        config_bundle: ConfigFileBundle | None = None,
        processor: Any = None
    ) -> None:
        '''
            Initializes File2Object constructor.

            :param format_type: Type of format (xml, json, yaml, ini, cfg).
            :type format_type: <str>
            :param config_file: Configuration file path in string format | None.
            :type config_file: <str | None>
            :param config_bundle: Configuration file bundle parameters | None.
            :type config_bundle: <ConfigFileBundle | None>
            :param processor: Processor for the content | None.
            :type processor: <Any>
            :exceptions:
                | ATSTypeError: Invalid type in constructor arguments.
                | ATSValueError: Unsupported format type.
        '''
        self._format_type = str(format_type).lower()
        if self._format_type not in self._PROCESSOR_MAPPING:
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

        # ovo je sve producer za processor
        proc_cls, proc_interface = self._PROCESSOR_MAPPING[self._format_type]
        self._processor = make_component(processor, proc_cls, None)
        validate_component(self._processor, proc_interface, f'processor must be an {proc_interface.__name__} instance')

    @vreport('read configuration from file {file_path}')
    @override
    def read_configuration(self) -> Any:
        '''
            Reads a configuration from a file.

            :return: Configuration object | None.
            :rtype: <Any>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        configuration: Any = None
        self._file_checker.check_path(self._file_path)
        self._file_checker.check_mode(self._MODE)
        self._file_checker.check_format(self._file_path, self._format_type)
        if self._file_checker.is_file_ok():
            with ConfFile(self._file_bundle_shared, self._config_file_bundle) as f:
                if bool(f):
                    configuration = self._parse_content(f)
        return configuration

    def _parse_content(self, f: Any) -> Any:
        '''
            Parses the content from the file stream.

            :param f: Opened file object (stream).
            :type f: <Any>
            :return: Decoded configuration object | None.
            :rtype: <Any>
        '''
        if self._format_type == 'xml':
            content = f.read()
            if content and self._processor.from_string(content):
                return self._processor
        elif self._format_type in ('json', 'yaml'):
            content = f.read()
            if content and self._processor.decode(content):
                return self._processor
        elif self._format_type == 'ini':
            if self._processor.from_stream(f):
                return self._processor
        elif self._format_type == 'cfg':
            lines = f.readlines()
            if self._processor.from_lines(lines):
                return self._processor
        return None

    @override
    def __str__(self) -> str:
        '''
            Returns the File2Object as string representation.

            :return: The File2Object as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
