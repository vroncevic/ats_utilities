# -*- coding: UTF-8 -*-

'''
Module
    info_registry.py
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
    Encapsulates core runtime components for simplification of InfoBundle creation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.info.info_bundle import InfoBundle
from ats_utilities.info.info_params import InfoParams
from ats_utilities.context.bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class InfoRegistry(IRegistry[InfoBundle, InfoParams]):
    '''
        Encapsulates core runtime components for simplification of InfoBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates an InfoBundle.
    '''

    @classmethod
    @override
    def create_bundle(cls, params: InfoParams) -> InfoBundle:
        '''
            Creates an InfoBundle instance.

            :param params: Registry-specific orchestration parameters.
            :type params: InfoParams
            :return: InfoBundle instance.
            :rtype: <InfoBundle>
            :exceptions:
                | ATSValueError: Info must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Info must be a mapping.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        return InfoBundle(
            name=params.get('name'),
            version=params.get('version'),
            licence=params.get('licence'),
            build_date=params.get('build_date'),
            repository=params.get('repository'),
            organization=params.get('organization'),
            use_github=params.get('use_github'),
            logo=params.get('logo'),
            log_file=params.get('log_file'),
            info_ok=params.get('info_ok'),
            context_bundle=params.get('context_bundle')
        )

