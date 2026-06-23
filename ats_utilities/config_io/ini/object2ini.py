# -*- coding: UTF-8 -*-

'''
Module
    object2ini.py
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
    Defines class Object2Ini with attribute(s) and method(s).
    Creates an API for writing configuration to an INI file.
'''

from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.file_bundle import ATSFileBundle
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.ini.iini_processor import IINIProcessor
from ats_utilities.reporter.proxy_reporter import vreporter
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import get_private_attr, format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Object2Ini(IWrite):
    '''
        Defines class Object2Ini with attribute(s) and method(s).
        Creates an API for writing configuration to an INI file.
        Conversion of Python object to INI content.

        It defines:

            :attributes:
                | _EXT - File extension of the configuration file.
                | _MODE - File open mode.
                | _config_file_bundle - Configuration file bundle parameters (default None).
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _file_checker - FileCheck for checking file (default FileCheck).
                | _file_path - Configuration file path (default None).
                | _file_bundle_shared - File bundle parameters (default None).
            :methods:
                | __init__ - Initializes Object2Ini constructor.
                | write_configuration - Writes configuration to an INI file.
                | __str__ - Returns the Object2Ini as string representation.
    '''

    _EXT: str = 'ini'
    _MODE: str = 'w'

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(
        self,
        config_file: str | None,
        config_bundle: ATSConfigFileBundle | None = None
    ) -> None:
        '''
            Initializes Object2Ini constructor.

            :param config_file: Configuration file path in string format | None.
            :type config_file: <str | None>
            :param config_bundle: Configuration file bundle parameters | None.
            :type config_bundle: <ATSConfigFileBundle | None>
            :exceptions: ATSTypeError.
        '''
        self._config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, self._config_file_bundle.context)
        context_bundle_shared: ContextBundle = ContextBundle(
            checker=self._checker, reporter=self._reporter, verbose=self._verbose
        )
        self._file_checker: IFileCheck = make_component(
            self._config_file_bundle.file_checker, FileCheck, {'config_bundle': context_bundle_shared}
        )
        validate_component(self._file_checker, FileCheck)
        self._file_path: str = str(config_file)
        self._file_bundle_shared: ATSFileBundle = ATSFileBundle()
        self._file_bundle_shared.file_path = self._file_path
        self._file_bundle_shared.file_mode = self._MODE
        self._file_bundle_shared.file_format = self._EXT

    @validator([('IINIProcessor | None:config', None)])
    @vreporter('write configuration to file {file_path}')
    def write_configuration(self, config: IINIProcessor | None) -> bool:
        '''
            Writes configuration to an INI file.

            :param config: Configuration object | None.
            :type config: <IINIProcessor | None>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError.
        '''
        status: bool = False

        if not bool(config):
            return status

        with ConfFile(self._file_bundle_shared, self._config_file_bundle) as ini:
            if bool(ini):
                if config.to_stream(ini):
                    status = True

        return status

    def __str__(self) -> str:
        '''
            Returns the Object2Ini as string representation.

            :return: The Object2Ini as string representation.
            :rtype: <str>
            :exceptions: None..
        '''
        return format_instance_to_string(self)
