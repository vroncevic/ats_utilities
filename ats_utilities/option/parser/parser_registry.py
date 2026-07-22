# -*- coding: UTF-8 -*-

'''
Module
    parser_registry.py
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
    Defines class ParserRegistry with attribute(s) and method(s).
    Encapsulates core parser components for simplification of ParserBundle creation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.parser.parser_bundle import ParserBundle
from ats_utilities.option.parser.parser_params import ParserParams
from ats_utilities.info.info_keys import InfoKeys

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ParserRegistry(IRegistry[ParserBundle, ParserParams]):
    '''
        Encapsulates core parser components for simplification of ParserBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a ParserBundle.
                | create_parser_bundle_from_dict - Creates a ParserBundle from dict parameters.
    '''

    @classmethod
    @override
    def create_bundle(cls, params: ParserParams) -> ParserBundle:
        '''
            Creates a ParserBundle instance.

            :param params: Registry-specific orchestration parameters.
            :type params: ParserParams
            :return: ParserBundle instance.
            :rtype: <ParserBundle>
            :exceptions:
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Parameters must be a mapping.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        parameters: Mapping[str, str] = params.get('parameters')
        context_bundle: ContextBundle = params.get('context_bundle')

        return cls.create_parser_bundle_from_dict(
            parameters=parameters,
            context_bundle=context_bundle,
        )

    @classmethod
    def create_parser_bundle_from_dict(
        cls,
        parameters: Mapping[str, str],
        context_bundle: ContextBundle
    ) -> ParserBundle:
        '''
            Creates a ParserBundle from parameters in mapping format.

            :param parameters: Metadata parameters in mapping format.
            :type parameters: <Mapping[str, str]>
            :param context_bundle: Context bundle for option bundle.
            :type context_bundle: <ContextBundle>
            :return: ParserBundle instance.
            :rtype: <ParserBundle>
            :exceptions: None.
        '''
        return ParserBundle(
            context_bundle=context_bundle,
            prog=f'{parameters.get(InfoKeys.ATS_NAME)} {parameters.get(InfoKeys.ATS_VERSION)}',
            epilog=f'{parameters.get(InfoKeys.ATS_NAME)} copyright (c) {parameters.get(InfoKeys.ATS_LICENCE)}',
            description=f'{parameters.get(InfoKeys.ATS_NAME)} build date {parameters.get(InfoKeys.ATS_BUILD_DATE)}'
        )
