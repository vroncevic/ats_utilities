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
    A factory for creating an info bundle.
'''

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType

from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.setup.dependencies import InfoDependencies
from ats_utilities.info.setup.options import InfoOptions
from ats_utilities.info.setup.opt_validator import InfoOptionsValidator
from ats_utilities.info.setup.registry import InfoRegistry

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class InfoFactory:
    '''
        A factory for creating an InfoBundle.

        It defines:

            :methods:
                | create_bundle - Creates an info bundle with pre-configured options.
    '''

    @classmethod
    def create_bundle(cls, options: InfoOptions) -> InfoBundle:
        '''
            Creates an info bundle with pre-configured options.

            :param options: The dictionary containing info options.
            :return: The info bundle.
            :exceptions:
                | ATSValueError: Info options must be provided and have proper values.
                | ATSTypeError:  Info options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        InfoOptionsValidator.validate(options)

        info_configuration: Mapping[str, object] = options.get(InfoKeys.OPTION_INFO)
        context_bundle: ContextBundle = options.get(InfoKeys.OPTION_CONTEXT_BUNDLE)

        key_to_type: MappingProxyType[str, type] = InfoKeys.get_config_key_to_type()
        bundle_kwargs: dict[str, object] = {}

        for key, engine_class in key_to_type.items():
            engine_instance: object = engine_class(context_bundle=context_bundle)
            attr_name: str = InfoKeys.get_name_of_config_key(key)
            attribute: object = info_configuration.get(key)

            if attribute is not None and key is InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE:
                if isinstance(attribute, str):
                    attribute = True if attribute == 'True' else False

            if attribute is not None:
                setattr(engine_instance, attr_name, attribute)

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
