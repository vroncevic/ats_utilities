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
    Factory for creating info bundle instance.
'''

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import Any, override

from ats_utilities.utils.setup.ifactory import IFactory
from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.setup.dependencies import InfoDependencies
from ats_utilities.info.setup.options import InfoOptions
from ats_utilities.info.setup.opt_validator import InfoOptionsValidator
from ats_utilities.info.setup.registry import InfoRegistry

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class InfoFactory(IFactory[InfoBundle, InfoOptions]):
    '''
        Factory for creating InfoBundle instance.

        It defines:

            :methods:
                | create_bundle - Creates a info bundle with pre-configured options.
    '''

    @classmethod
    @override
    def create_bundle(cls, options: InfoOptions) -> InfoBundle:
        '''
            Creates a info bundle with pre-configured options.

            :param options: Dictionary containing options.
            :return: Info bundle instance.
            :exceptions:
                | ATSValueError: Info options must be provided and have proper values.
                | ATSTypeError:  Info options must be an instance of InfoOptions and its
                |                attributes must be instances of their respective types.
        '''
        InfoOptionsValidator.validate(options)

        info: Mapping[str, Any] = options.get(InfoKeys.OPTION_INFO)
        context_bundle: ContextBundle = options.get(InfoKeys.OPTION_CONTEXT_BUNDLE)

        key_to_type: MappingProxyType[str, type] = InfoKeys.get_config_key_to_type()
        bundle_kwargs: dict[str, Any] = {}

        for key, engine_class in key_to_type.items():
            engine_instance: Any = engine_class(context_bundle=context_bundle)
            attr_name: str = InfoKeys.get_name_of_config_key(key)
            val: Any = info.get(key)

            if val is not None and key is InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE:
                if isinstance(val, str):
                    val = True if val == 'True' else False

            if val is not None:
                setattr(engine_instance, attr_name, val)

            bundle_kwargs[attr_name] = engine_instance

        bundle_kwargs[InfoKeys.OPTION_CONTEXT_BUNDLE] = context_bundle

        return InfoRegistry.create_bundle(
            InfoDependencies(
                name=bundle_kwargs.get(InfoKeys.DEPENDENCY_NAME),
                version=bundle_kwargs.get(InfoKeys.DEPENDENCY_VERSION),
                licence=bundle_kwargs.get(InfoKeys.DEPENDENCY_LICENCE),
                build_date=bundle_kwargs.get(InfoKeys.DEPENDENCY_BUILD_DATE),
                repository=bundle_kwargs.get(InfoKeys.DEPENDENCY_REPOSITORY),
                organization=bundle_kwargs.get(InfoKeys.DEPENDENCY_ORGANIZATION),
                use_github=bundle_kwargs.get(InfoKeys.DEPENDENCY_USE_GITHUB_INFRASTRUCTURE),
                logo=bundle_kwargs.get(InfoKeys.DEPENDENCY_LOGO_PATH),
                log_file=bundle_kwargs.get(InfoKeys.DEPENDENCY_LOG_FILE),
                info_ok=bundle_kwargs.get(InfoKeys.DEPENDENCY_INFO_OK),
                context_bundle=bundle_kwargs.get(InfoKeys.OPTION_CONTEXT_BUNDLE)
            )
        )
