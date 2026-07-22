# -*- coding: UTF-8 -*-

'''
Module
    info_factory.py
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
    Factory for creating InfoBundle components.
'''

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import Any, Final

from ats_utilities.info.info_bundle import InfoBundle
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
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class InfoFactory:
    '''
        Factory for creating InfoBundle components.
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
    def create_info_bundle_from_dict(
        cls,
        info: Mapping[str, Any],
        context_bundle: ContextBundle
    ) -> InfoBundle:
        '''
            Creates a default InfoBundle with pre-configured components.

            :param info: Dictionary containing info components.
            :type info: <Mapping[str, Any]>
            :param context_bundle: ContextBundle instance.
            :type context_bundle: <ContextBundle>
            :return: Default InfoBundle instance.
            :rtype: <InfoBundle>
            :exceptions: None.
        '''
        context: str = r'info_factory::create_info_bundle_from_dict(...)'
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

        return InfoBundle(**bundle_kwargs)
