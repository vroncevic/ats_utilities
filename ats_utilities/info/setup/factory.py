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
from typing import Any, Final, override

from ats_utilities.utils.ifactory import IFactory
from ats_utilities.info.info_keys import InfoKeys
from ats_utilities.info.name.engine import Name
from ats_utilities.info.version.engine import Version
from ats_utilities.info.licence.engine import Licence
from ats_utilities.info.build_date.engine import BuildDate
from ats_utilities.info.repository.engine import Repository
from ats_utilities.info.organization.engine import Organization
from ats_utilities.info.use_github.engine import UseGitHub
from ats_utilities.info.logo.engine import Logo
from ats_utilities.info.log_file.engine import LogFile
from ats_utilities.info.info_ok.engine import InfoOk
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.setup.dependencies import InfoOptions, InfoDependencies
from ats_utilities.info.setup.registry import InfoRegistry
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
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

            :attributes:
                | _ATTR_TO_CLASS - Mapping of info keys to their corresponding engine classes.
            :methods:
                | create_default_bundle - Creates a default info bundle with pre-configured options.
                | create_info_bundle_from_dict - Creates an info bundle from a dictionary.
    '''

    _ATTR_TO_CLASS: Final[Mapping[str, Any]] = MappingProxyType({
        InfoKeys.ATS_NAME: Name,
        InfoKeys.ATS_VERSION: Version,
        InfoKeys.ATS_LICENCE: Licence,
        InfoKeys.ATS_BUILD_DATE: BuildDate,
        InfoKeys.ATS_REPOSITORY: Repository,
        InfoKeys.ATS_ORGANIZATION: Organization,
        InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: UseGitHub,
        InfoKeys.ATS_LOGO_PATH: Logo,
        InfoKeys.ATS_LOG_FILE: LogFile,
        InfoKeys.ATS_INFO_OK: InfoOk
    })

    @classmethod
    @override
    def create_default_bundle(cls, options: InfoOptions) -> InfoBundle:
        '''
            Creates a default info bundle with pre-configured options.

            :param options: Dictionary containing options.
            :type options: InfoOptions
            :return: Default info bundle instance.
            :rtype: InfoBundle
            :exceptions:
                | ATSValueError: Name must be provided.
                | ATSValueError: Version must be provided.
                | ATSValueError: Licence must be provided.
                | ATSValueError: Build date must be provided.
                | ATSValueError: Repository must be provided.
                | ATSValueError: Organization must be provided.
                | ATSValueError: Use GitHub must be provided.
                | ATSValueError: Logo path must be provided.
                | ATSValueError: Info ok must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Name must be an instance of IName interface.
                | ATSTypeError: Version must be an instance of IVersion interface.
                | ATSTypeError: Licence must be an instance of ILicence interface.
                | ATSTypeError: Build date must be an instance of IBuildDate interface.
                | ATSTypeError: Repository must be an instance of IRepository interface.
                | ATSTypeError: Organization must be an instance of IOrganization interface.
                | ATSTypeError: Use GitHub must be an instance of IUseGitHub interface.
                | ATSTypeError: Logo path must be an instance of ILogo interface.
                | ATSTypeError: Info ok must be an instance of IInfoOk interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle class.
        '''
        context: str = r'info_factory::create_default_bundle(...)'
        not_none(options, context, r'options must be provided')
        istype(options, dict, context, r'options must be a dictionary')
        
        info: Mapping[str, Any] = options.get('info')
        context_bundle: ContextBundle = options.get('context_bundle')

        not_none(context_bundle, context, r'context_bundle must be provided')
        not_none(info, context, r'info must be provided')
        istype(context_bundle, ContextBundle, context, r'context_bundle must be ContextBundle instance')
        istype(info, Mapping, context, r'info must be Mapping instance')

        key_to_attr: MappingProxyType[str, str] = InfoKeys.get_key_to_attr()
        bundle_kwargs: dict[str, Any] = {}

        for raw_key, attr_name in key_to_attr.items():
            engine_class: type[Any] = cls._ATTR_TO_CLASS.get(raw_key)

            if engine_class is None:
                continue

            engine_instance: Any = engine_class(context_bundle=context_bundle)
            val: Any = info.get(raw_key)

            if raw_key == InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE and val is not None:
                if isinstance(val, str):
                    val = True if val == 'True' else False

            if val is not None:
                setattr(engine_instance, attr_name, val)

            bundle_kwargs[attr_name] = engine_instance

        bundle_kwargs['context_bundle'] = context_bundle

        bundle: InfoBundle = InfoRegistry.create_bundle(
            InfoDependencies(
                name=bundle_kwargs.get('name'),
                version=bundle_kwargs.get('version'),
                licence=bundle_kwargs.get('licence'),
                build_date=bundle_kwargs.get('build_date'),
                repository=bundle_kwargs.get('repository'),
                organization=bundle_kwargs.get('organization'),
                use_github=bundle_kwargs.get('use_github'),
                logo=bundle_kwargs.get('logo'),
                log_file=bundle_kwargs.get('log_file'),
                info_ok=bundle_kwargs.get('info_ok'),
                context_bundle=bundle_kwargs.get('context_bundle')
            )
        )

        return bundle

    @classmethod
    def create_info_bundle_from_dict(
        cls,
        info: Mapping[str, Any],
        context_bundle: ContextBundle
    ) -> InfoBundle:
        '''
            Creates an info bundle from a dictionary.

            :param info: Dictionary containing info.
            :type info: Mapping[str, Any]
            :param context_bundle: Context bundle.
            :type context_bundle: ContextBundle
            :return: InfoBundle instance.
            :rtype: InfoBundle
            :exceptions:
                | ATSValueError: Name must be provided.
                | ATSValueError: Version must be provided.
                | ATSValueError: Licence must be provided.
                | ATSValueError: Build date must be provided.
                | ATSValueError: Repository must be provided.
                | ATSValueError: Organization must be provided.
                | ATSValueError: Use GitHub must be provided.
                | ATSValueError: Logo path must be provided.
                | ATSValueError: Info ok must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Name must be an instance of IName interface.
                | ATSTypeError: Version must be an instance of IVersion interface.
                | ATSTypeError: Licence must be an instance of ILicence interface.
                | ATSTypeError: Build date must be an instance of IBuildDate interface.
                | ATSTypeError: Repository must be an instance of IRepository interface.
                | ATSTypeError: Organization must be an instance of IOrganization interface.
                | ATSTypeError: Use GitHub must be an instance of IUseGitHub interface.
                | ATSTypeError: Logo path must be an instance of ILogo interface.
                | ATSTypeError: Info ok must be an instance of IInfoOk interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle class.
        '''
        return cls.create_default_bundle({
            'info': info,
            'context_bundle': context_bundle
        })
