# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating config I/O bundle instance.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.utils.ifactory import IFactory
from ats_utilities.config_io.setup.bundle import ConfigIOBundle
from ats_utilities.config_io.setup.dependencies import ConfigIOOptions, ConfigIODependencies
from ats_utilities.config_io.setup.registry import ConfigIORegistry
from ats_utilities.config_io.processor.factory_processor import ConfigProcessorFactory
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ConfigIOFactory(IFactory[ConfigIOBundle, ConfigIOOptions]):
    '''
        Factory for creating config I/O bundle instance.

        It defines:

            :methods:
                | create_default_bundle - Creates a default config I/O bundle using configuration options.
    '''

    @classmethod
    @override
    def create_default_bundle(cls, options: ConfigIOOptions) -> ConfigIOBundle:
        '''
            Creates a default config I/O bundle using configuration options.

            :param options: Creation options/parameters for the bundle.
            :type options: ConfigIOOptions
            :return: Config I/O bundle instance.
            :rtype: ConfigIOBundle
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a dictionary.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSValueError: Bundle must be provided.
                | ATSValueError: File path must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Processor must be provided.
                | ATSTypeError: Bundle must be an instance of ConfigIOBundle.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: Scheme must be an instance of Mapping interface.
                | ATSTypeError: Processor must be an instance of IConfigProcessor interface.
        '''
        ctx: str = r'config_io_factory::create_default_bundle(...)'
        not_none(options, ctx, r'options must be provided')
        istype(options, dict, ctx, r'options must be a dictionary')

        context_bundle: ContextBundle = options.get('context_bundle')
        not_none(context_bundle, ctx, r'context_bundle must be provided')
        istype(context_bundle, ContextBundle, ctx, r'context_bundle must be a ContextBundle instance')

        file_path: str = options.get('file_path', '')
        scheme: Mapping[str, str] = options.get('scheme', {})
        processor: IConfigProcessor | None = options.get('processor')

        if processor is None:
            processor = ConfigProcessorFactory.create_from_file_path(
                file_path=file_path,
                scheme=scheme
            )

        return ConfigIORegistry.create_bundle(
            ConfigIODependencies(
                file_path=file_path,
                scheme=scheme,
                processor=processor,
                context_bundle=context_bundle
            )
        )
