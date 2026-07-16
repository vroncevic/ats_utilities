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

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.option.parser.parser_bundle import ParserBundle
from ats_utilities.info.info_keys import InfoKeys

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ParserRegistry:
    '''
        Encapsulates core parser components for simplification of ParserBundle creation.

        It defines:

            :methods:
                | create_parser_bundle_from_dict - Creates a ParserBundle from dict parameters.
    '''

    @staticmethod
    def create_parser_bundle_from_dict(
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
