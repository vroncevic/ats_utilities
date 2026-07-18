# -*- coding: UTF-8 -*-

'''
Module
    config_io_registry.py
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
from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.config_io.config_io_bundle import ConfigIOBundle
from ats_utilities.config_io.processor.factory_processor import ConfigProcessorFactory
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.context.context_bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ConfigIORegistry(IRegistry[ConfigIOBundle]):
    '''
        Encapsulates core config I/O components for simplification of ConfigIOBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a ConfigIOBundle instance using either file path and scheme or injected processor.
                | create_config_io_bundle_by_file_path_and_scheme - Creates a ConfigIOBundle based on file path and scheme.
                | create_config_io_bundle_by_injected_processor - Creates a ConfigIOBundle with injected processor.
    '''

    @classmethod
    @override
    def create_bundle(cls, **kwargs: Any) -> ConfigIOBundle:
        '''
            Creates a ConfigIOBundle instance using either file path and scheme or injected processor.

            :param kwargs: Additional registry-specific orchestration parameters.
            :return: ConfigIOBundle instance.
            :rtype: <ConfigIOBundle>
            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: Scheme must be an instance of Mapping interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle interface.
        '''
        file_path: str = kwargs.get('file_path')
        scheme: Mapping[str, str] | None = kwargs.get('scheme')
        context_bundle: ContextBundle = kwargs.get('context_bundle')
        processor: IConfigProcessor | None = kwargs.get('processor')

        return cls.create_config_io_bundle_by_file_path_and_scheme(
            file_path=file_path,
            scheme=scheme,
            context_bundle=context_bundle
        ) if processor is None else cls.create_config_io_bundle_by_injected_processor(
            processor=processor,
            context_bundle=context_bundle
        )

    @classmethod
    def create_config_io_bundle_by_file_path_and_scheme(
        cls,
        file_path: str,
        scheme: Mapping[str, str],
        context_bundle: ContextBundle
    ) -> ConfigIOBundle:
        '''
            Creates a ConfigIOBundle with pre-configured components based on file path and scheme.

            :param file_path: Config file path.
            :type file_path: <str>
            :param scheme: Config scheme.
            :type scheme: <Mapping[str, str]>
            :param context_bundle: Context bundle for dependency injection.
            :type context_bundle: <ContextBundle>
            :return: ConfigIOBundle instance.
            :rtype: <ConfigIOBundle>
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

        return ConfigIOBundle(
            file_path=file_path,
            scheme=scheme,
            processor=processor,
            context_bundle=context_bundle
        )

    @classmethod
    def create_config_io_bundle_by_injected_processor(
        cls,
        processor: IConfigProcessor,
        context_bundle: ContextBundle
    ) -> ConfigIOBundle:
        '''
            Creates a ConfigIOBundle with injected processor.

            :param processor: Config processor.
            :type processor: <IConfigProcessor>
            :param context_bundle: Context bundle for dependency injection.
            :type context_bundle: <ContextBundle>
            :return: ConfigIOBundle instance.
            :rtype: <ConfigIOBundle>
            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: Scheme must be an instance of Mapping interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle interface.
        '''
        return ConfigIOBundle(
            file_path='',
            scheme={},
            processor=processor,
            context_bundle=context_bundle
        )
    