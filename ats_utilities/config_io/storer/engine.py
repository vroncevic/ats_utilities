# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines class Storer with attribute(s) and method(s).
    Creates an API for storing the configuration from mapping format to configuration file.
    2nd level of configuration storer implementation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.config_io.storer.istorer import IStorer
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.config_io.config_io_bundle import ConfigIOBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.conf_file_bundle import ConfFileBundle
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.config_io.processor.factory_processor import ConfigProcessorFactory
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Storer(IStorer):
    '''
        Defines class Storer with attribute(s) and method(s).
        Creates an API for storing the configuration from mapping format to configuration file.
        2nd level of configuration storer implementation.

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
                | __init__ - Initializes Storer constructor.
                | get_shared_context - Returns the shared context.
                | store_configuration - Stores configuration content from mapping to configuration file.
                | __str__ - Returns the Storer as string representation.
    '''

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _context_bundle_shared: ContextBundle
    _processor: IConfigProcessor | None
    _conf_file_bundle: ConfFileBundle

    def __init__(self, component_bundle: ConfigIOBundle | None = None) -> None:
        '''
            Initializes Storer constructor.

            :param format_type: Type of format (xml, json, yaml, ini, cfg).
            :type format_type: <str>
            :param config_file: Configuration file path in string format | None.
            :type config_file: <str | None>
            :param config_bundle: Configuration file bundle parameters | None.
            :type config_bundle: <ConfigFileBundle | None>
            :exceptions:
                | ATSValueError: File path must be provided when processor is None.
                | ATSTypeError: File path must be a string.
                | ATSValueError: File does not exist.
                | ATSValueError: Extension must be provided.
                | ATSTypeError: Extension must be a string.
                | ATSValueError: Extension is not supported.
                | ATSTypeError: Validation of processor instance failed.
        '''
        bundle: ConfigIOBundle = component_bundle or ConfigIOBundle()
        self._context_bundle_shared = bundle.context
        factory_context_bundle(self, self._context_bundle_shared)
        self._processor = ConfigProcessorFactory.create_from_file_path(
            bundle.file_path, bundle.scheme, bundle.processor
        )
        self._conf_file_bundle = ConfFileBundle(
            file_path=bundle.file_path,
            file_mode=bundle.WRITE_MODE,
            context_bundle=self._context_bundle_shared
        )

    @override
    def get_shared_context(self) -> ContextBundle:
        '''
            Returns the shared context.

            :return: Shared context.
            :rtype: <ContextBundle>
            :exceptions: None.
        '''
        return self._context_bundle_shared

    @override
    def store_configuration(self, config: Mapping[str, str]) -> bool:
        '''
            Writes configuration to a file.

            :param config: Configuration object.
            :type config: <Mapping[str, str]>
            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        if not config:
            return False

        if not self._processor.update_data(config):
            return False

        content = self._processor.serialize()

        try:
            with ConfFile(self._conf_file_bundle) as config_file:
                if config_file:
                    return config_file.write(content)

        except Exception:
            return False

        return False

    @override
    def __str__(self) -> str:
        '''
            Returns the Storer instance as string representation.

            :return: The Storer instance as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
