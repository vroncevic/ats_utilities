# -*- coding: UTF-8 -*-

'''
Module
    ini_loader.py
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
    Defines class INILoader with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

from __future__ import annotations

from typing import override

from ats_utilities.config_io.iread import IRead
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.iloader import ILoader
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.config_io.ini.ini2object import Ini2Object
from ats_utilities.config_io.ini.ini_processor import INIProcessor
from ats_utilities.config_io.ini.iini_processor import IINIProcessor
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


class INILoader(ILoader):
    '''
        Defines class INILoader with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        INI configuration-based API support.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _configuration - INI processor configuration (default None).
            :methods:
                | __init__ - Initializes INILoader constructor.
                | load_configuration - Loads the ATS configuration in dictionary format.
                | __str__ - Returns the INILoader as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(
        self,
        info_file: str | None = None,
        ini2object: IRead | None = None,
        config_bundle: ConfigFileBundle | None = None,
        ini_processor: IINIProcessor | None = None
    ) -> None:
        '''
            Initializes INILoader constructor.

            :param info_file: Path to the info file | None.
            :type info_file: <str | None>
            :param ini2object: An API for information | None.
            :type ini2object: <IRead | None>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <ConfigFileBundle | None>
            :param ini_processor: Processor for INI content | None.
            :type ini_processor: <IINIProcessor | None>
            :exceptions:
                | ATSTypeError: Invalid type in constructor arguments.
        '''
        config_file_bundle: ConfigFileBundle = config_bundle or ConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        context_bundle_shared: ContextBundle = ContextBundle(
            checker=self._checker, reporter=self._reporter, verbose=self._verbose
        )
        file_checker: IFileCheck = make_component(
            config_file_bundle.file_checker, FileCheck, {'config_bundle': context_bundle_shared}
        )
        validate_component(file_checker, FileCheck)
        processor: IINIProcessor = make_component(ini_processor, INIProcessor, None)
        validate_component(processor, INIProcessor)
        ini2obj: IRead = make_component(ini2object, Ini2Object, {
            'config_file': info_file, 'config_bundle': config_file_bundle, 'ini_processor': processor
        })
        validate_component(ini2obj, Ini2Object)
        self._configuration: IINIProcessor | None = None

        if bool(ini2obj):
            self._configuration = ini2obj.read_configuration()

    @override
    def load_configuration(self) -> dict[str, str]:
        '''
            Loads the ATS configuration in dictionary format.

            :return: Dictionary with INI information.
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        if not self._configuration:
            return {}

        return self._configuration.to_dict()

    @override
    def __str__(self) -> str:
        '''
            Returns the INILoader as string representation.

            :return: The INILoader as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
