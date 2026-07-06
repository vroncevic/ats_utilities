# -*- coding: UTF-8 -*-

'''
Module
    cfg2object.py
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
    Defines class Cfg2Object with attribute(s) and method(s).
    Creates an API for reading configuration from a CFG file.
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
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor
from ats_utilities.config_io.cfg.cfg_processor import CFGProcessor
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import to_str

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Cfg2Object(IRead):
    '''
        Defines class Cfg2Object with attribute(s) and method(s).
        Creates an API for reading configuration from a CFG file.
        Conversion of CFG content to Python object.

        It defines:

            :attributes:
                | _EXT - File extension of the configuration file.
                | _MODE - File open mode.
                | _config_file_bundle - Configuration file bundle parameters (default None).
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _file_checker - FileCheck for checking file (default FileCheck).
                | _cfg_processor - Processor for CFG content (default CFGProcessor).
                | _file_path - Configuration file path (default None).
                | _file_bundle_shared - File bundle parameters (default None).
            :methods:
                | __init__ - Initializes Cfg2Object constructor.
                | read_configuration - Reads configuration from a CFG file.
                | __str__ - Returns the Cfg2Object as string representation.
    '''

    _EXT: str = 'cfg'
    _MODE: str = 'r'
    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _config_file_bundle: ConfigFileBundle
    _file_checker: IFileCheck
    _cfg_processor: ICFGProcessor
    _file_path: str
    _file_bundle_shared: FileBundle

    def __init__(
        self,
        config_file: str | None,
        config_bundle: ConfigFileBundle | None = None,
        cfg_processor: ICFGProcessor | None = None
    ) -> None:
        '''
            Initializes Cfg2Object constructor.

            :param config_file: Configuration file path in string format | None.
            :type config_file: <str | None>
            :param config_bundle: Configuration file bundle parameters | None.
            :type config_bundle: <ConfigFileBundle | None>
            :param cfg_processor: Processor for CFG content | None.
            :type cfg_processor: <ICFGProcessor | None>
            :exceptions:
                | ATSTypeError: Invalid type in constructor arguments.
        '''
        self._config_file_bundle = config_bundle or ConfigFileBundle()
        factory_context_bundle(self, self._config_file_bundle.context)
        self._file_checker = make_component(
            self._config_file_bundle.file_checker, FileCheck,
            {'config_bundle': ContextBundle(checker=self._checker, reporter=self._reporter, verbose=self._verbose)}
        )
        validate_component(self._file_checker, IFileCheck, 'file_checker must be an IFileCheck instance')
        self._cfg_processor = make_component(cfg_processor, CFGProcessor, None)
        validate_component(self._cfg_processor, ICFGProcessor, 'cfg_processor must be an ICFGProcessor instance')
        self._file_path = str(config_file)
        self._file_bundle_shared = FileBundle()
        self._file_bundle_shared.file_path = self._file_path
        self._file_bundle_shared.file_mode = self._MODE
        self._file_bundle_shared.file_format = self._EXT

    @vreport('read configuration from file {file_path}')
    @override
    def read_configuration(self) -> ICFGProcessor | None:
        '''
            Reads a configuration from a CFG file.

            :return: Configuration object | None.
            :rtype: <ICFGProcessor | None>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        with ConfFile(self._file_bundle_shared, self._config_file_bundle) as cfg:
            if bool(cfg):
                lines: list[str] = cfg.readlines()
                if self._cfg_processor.from_lines(lines):
                    return self._cfg_processor

        return None

    @override
    def __str__(self) -> str:
        '''
            Returns the Cfg2Object as string representation.

            :return: The Cfg2Object as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
