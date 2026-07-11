# -*- coding: UTF-8 -*-

'''
Module
    ini2object.py
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
    Defines class Ini2Object with attribute(s) and method(s).
    Creates an API for reading configuration from an INI file.
'''

from __future__ import annotations

from typing import override

from ats_utilities.config_io.iread import IRead
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.file_bundle import FileBundle
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.config_io.ini.iini_processor import IINIProcessor
from ats_utilities.config_io.ini.ini_processor import INIProcessor
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
__status__ = r'Updated'


class Ini2Object(IRead):
    '''
        Defines class Ini2Object with attribute(s) and method(s).
        Creates an API for reading configuration from an INI file.
        Conversion of INI config to Python object.

        It defines:

            :attributes:
                | _EXT - File extension of the configuration file.
                | _MODE - File open mode.
                | _config_file_bundle - Configuration file bundle parameters (default None).
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _file_checker - FileCheck for checking file (default FileCheck).
                | _ini_processor - Processor for INI content (default INIProcessor).
                | _file_path - Configuration file path (default None).
                | _file_bundle_shared - File bundle parameters (default None).
            :methods:
                | __init__ - Initializes Ini2Object constructor.
                | read_configuration - Reads configuration from an INI file.
                | __str__ - Returns the Ini2Object as string representation.
    '''

    _EXT: str = 'ini'
    _MODE: str = 'r'
    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _config_file_bundle: ConfigFileBundle
    _file_checker: IFileCheck
    _ini_processor: IINIProcessor
    _file_path: str
    _file_bundle_shared: FileBundle

    def __init__(
        self,
        config_file: str | None,
        config_bundle: ConfigFileBundle | None = None,
        ini_processor: IINIProcessor | None = None,
    ) -> None:
        '''
            Initializes Ini2Object constructor.

            :param config_file: Configuration file path in string format | None.
            :type config_file: <str | None>
            :param config_bundle: Configuration file bundle parameters | None.
            :type config_bundle: <ConfigFileBundle | None>
            :param ini_processor: Processor for INI content | None.
            :type ini_processor: <IINIProcessor | None>
            :exceptions:
                | ATSTypeError: Invalid type in constructor arguments.
        '''
        self._config_file_bundle = config_bundle or ConfigFileBundle()
        factory_context_bundle(self, self._config_file_bundle.context)
        self._file_checker = make_component(
            self._config_file_bundle.file_checker, FileCheck,
            {'config_bundle': ContextBundle(checker=self._checker, reporter=self._reporter, verbose=self._verbose)}
        )
        validate_component(self._file_checker, IFileCheck, r'file_checker must be an IFileCheck instance')
        self._ini_processor = make_component(ini_processor, INIProcessor, None)
        validate_component(self._ini_processor, IINIProcessor, r'ini_processor must be an IINIProcessor instance')
        self._file_path = str(config_file)
        self._file_bundle_shared = FileBundle()
        self._file_bundle_shared.file_path = self._file_path
        self._file_bundle_shared.file_mode = self._MODE
        self._file_bundle_shared.file_format = self._EXT

    @vreport('read configuration from file {file_path}')
    @override
    def read_configuration(self) -> IINIProcessor | None:
        '''
            Reads a configuration from an INI file.

            :return: Configuration object | None.
            :rtype: <IINIProcessor | None>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        with ConfFile(self._file_bundle_shared, self._config_file_bundle) as ini:
            if bool(ini):
                if self._ini_processor.from_stream(ini):
                    return self._ini_processor

        return None

    @override
    def __str__(self) -> str:
        '''
            Returns the Ini2Object as string representation.

            :return: The Ini2Object as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
