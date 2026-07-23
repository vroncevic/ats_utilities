# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core config I/O components for simplification of ConfigIOBundle creation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.config_io.setup.bundle import ConfigIOBundle
from ats_utilities.config_io.setup.dependencies import ConfigIODependencies
from ats_utilities.config_io.setup.validator import ConfigIOValidator
from ats_utilities.config_io.processor.factory_processor import ConfigProcessorFactory
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.context.bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ConfigIORegistry(IRegistry[ConfigIOBundle, ConfigIODependencies]):
    '''
        Encapsulates core config I/O components for simplification of ConfigIOBundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates a ConfigIOBundle instance.
                | create_config_io_bundle_by_file_path_and_scheme - Creates a ConfigIOBundle based on file path and scheme.
                | create_config_io_bundle_by_injected_processor - Creates a ConfigIOBundle with injected processor.
    '''

    @classmethod
    @override
    def create_bundle(cls, dependencies: ConfigIODependencies) -> ConfigIOBundle:
        '''
            Orchestrates dependency injection and creates a ConfigIOBundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :type dependencies: ConfigIODependencies
            :return: ConfigIOBundle instance.
            :rtype: ConfigIOBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: File path must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Processor must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of ConfigIOBundle.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: Scheme must be an instance of Mapping interface.
                | ATSTypeError: Processor must be an instance of IConfigProcessor interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle interface.
        '''
        bundle = ConfigIOBundle(
            file_path=dependencies.get('file_path'),
            scheme=dependencies.get('scheme'),
            processor=dependencies.get('processor'),
            context_bundle=dependencies.get('context_bundle')
        )

        ConfigIOValidator.validate(bundle)

        return bundle

    @classmethod
    def create_config_io_bundle_by_file_path_and_scheme(
        cls,
        file_path: str,
        scheme: Mapping[str, str],
        context_bundle: ContextBundle
    ) -> ConfigIOBundle:
        '''
            Creates a ConfigIOBundle with pre-configured components based on file path and scheme.
            Kept for backward compatibility.

            :param file_path: Config file path.
            :type file_path: str
            :param scheme: Config scheme.
            :type scheme: Mapping[str, str]
            :param context_bundle: Context bundle for dependency injection.
            :type context_bundle: ContextBundle
            :return: ConfigIOBundle instance.
            :rtype: ConfigIOBundle
            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: Scheme must be an instance of Mapping interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle interface.
        '''
        processor: IConfigProcessor = ConfigProcessorFactory.create_from_file_path(
            file_path=file_path,
            scheme=scheme
        )

        return cls.create_bundle(
            ConfigIODependencies(
                file_path=file_path,
                scheme=scheme,
                processor=processor,
                context_bundle=context_bundle
            )
        )

    @classmethod
    def create_config_io_bundle_by_injected_processor(
        cls,
        processor: IConfigProcessor,
        context_bundle: ContextBundle
    ) -> ConfigIOBundle:
        '''
            Creates a ConfigIOBundle with injected processor.
            Kept for backward compatibility.

            :param processor: Config processor.
            :type processor: IConfigProcessor
            :param context_bundle: Context bundle for dependency injection.
            :type context_bundle: ContextBundle
            :return: ConfigIOBundle instance.
            :rtype: ConfigIOBundle
            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: Scheme must be an instance of Mapping interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle interface.
        '''
        return cls.create_bundle(
            ConfigIODependencies(
                file_path='',
                scheme={},
                processor=processor,
                context_bundle=context_bundle
            )
        )
