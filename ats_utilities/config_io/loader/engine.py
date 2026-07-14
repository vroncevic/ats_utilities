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
    Defines class Loader with attribute(s) and method(s).
    Creates an API for loading configuration from file and deploying as object.
    2nd level of configuration loader implementation.
'''

from __future__ import annotations

from typing import override, Any

from ats_utilities.config_io.loader.iloader import ILoader
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


class Loader(ILoader):
    '''
        Defines class Loader with attribute(s) and method(s).
        Creates an API for loading configuration from file and deploying as object.
        2nd level of configuration loader implementation.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger for logging (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _context_bundle_shared - Injected shared context bundle (default ContextBundle).
                | _processor - Format-specific file processor (provided/inferred).
                | _conf_file_bundle - Bundle for file operations.
            :methods:
                | __init__ - Initializes Loader constructor.
                | get_shared_context - Returns the shared context.
                | load_configuration - Reads configuration from a file.
                | __str__ - Returns the Loader as string representation.
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
            Initializes Loader constructor.

            :param component_bundle: Component bundle for dependency injection | None.
            :type component_bundle: <ConfigIOBundle | None>
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
        self._context_bundle_shared = bundle.context_bundle
        factory_context_bundle(self, self._context_bundle_shared)
        self._processor = ConfigProcessorFactory.create_from_file_path(
            bundle.file_path, bundle.scheme, bundle.processor
        )
        self._conf_file_bundle = ConfFileBundle(
            file_path=bundle.file_path,
            file_mode=bundle.READ_MODE,
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
    def load_configuration(self) -> dict[str, Any]:
        '''
            Loads configuration from file and returns dictionary with configuration content.

            :return: Configuration dictionary.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        content: str | None = None

        try:
            with ConfFile(self._conf_file_bundle) as config_file:
                if config_file:
                    content = config_file.read()
        except Exception:
            return {}

        if content is None:
            return {}

        if self._processor.deserialize(content):
            return self._processor.to_dict()

        return {}

    @override
    def __str__(self) -> str:
        '''
            Returns the Loader as string representation.

            :return: The Loader as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
