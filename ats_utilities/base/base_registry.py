# -*- coding: UTF-8 -*-

'''
Module
    base_registry.py
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
    Encapsulates core runtime components for simplification of BaseBundle creation.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.base.base_bundle import BaseBundle
from ats_utilities.base.base_params import BaseParams

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class BaseRegistry(IRegistry[BaseBundle, BaseParams]):
    '''
        Encapsulates core runtime components for simplification of BaseBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a BaseBundle.
    '''

    @classmethod
    @override
    def create_bundle(cls, params: BaseParams) -> BaseBundle:
        '''
            Creates a BaseBundle.

            :param params: Registry-specific orchestration parameters.
            :type params: BaseParams
            :return: BaseBundle instance.
            :rtype: <BaseBundle>
            :exceptions:
                | ATSValueError: Info file must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Info file must be a string.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Use generator must be a boolean.
        '''
        return BaseBundle(
            info_file=params.get('info_file'),
            config_loader=params.get('config_loader'),
            info_manager=params.get('info_manager'),
            options_parser=params.get('options_parser'),
            splasher=params.get('splasher'),
            generator=params.get('generator'),
            use_generator=params.get('use_generator', False),
            context_bundle=params.get('context_bundle')
        )

