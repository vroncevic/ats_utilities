# -*- coding: UTF-8 -*-

'''
Module
    parser_strategy_registry.py
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
    Defines class ParserStrategyRegistry with attribute(s) and method(s).
    Encapsulates core parser strategy components for simplification of ParserStrategyBundle creation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.parser.engine import ArgParser
from ats_utilities.option.strategy.parser_strategy_bundle import ParserStrategyBundle
from ats_utilities.info.info_keys import InfoKeys

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ParserStrategyRegistry(IRegistry[ParserStrategyBundle]):
    '''
        Encapsulates core parser components for simplification of ParserStrategyBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a ParserStrategyBundle.
                | create_parser_strategy_bundle_from_dict - Creates a ParserStrategyBundle from dict parameters.
    '''

    @override
    def create_bundle(cls, **kwargs: Any) -> ParserStrategyBundle:
        '''
            Creates a ParserStrategyBundle instance.

            :param kwargs: Additional registry-specific orchestration parameters.
            :return: ParserStrategyBundle instance.
            :rtype: <ParserStrategyBundle>
            :exceptions:
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Parameters must be a mapping.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        parameters: Mapping[str, str] = kwargs.get('parameters')
        context_bundle: ContextBundle = kwargs.get('context_bundle')
        parser_class: type[IArgParser] = kwargs.get('parser_class', ArgParser)

        return cls.create_parser_strategy_bundle_from_dict(
            parameters=parameters,
            context_bundle=context_bundle,
            parser_class=parser_class,
        )

    @classmethod
    def create_parser_strategy_bundle_from_dict(
        cls,
        parameters: Mapping[str, str],
        context_bundle: ContextBundle,
        parser_class: type[IArgParser] = ArgParser,
    ) -> ParserStrategyBundle:
        '''
            Creates a ParserStrategyBundle from parameters in mapping format.

            :param parameters: Metadata parameters in mapping format.
            :type parameters: <Mapping[str, str]>
            :param context_bundle: Context bundle for option bundle.
            :type context_bundle: <ContextBundle>
            :param parser_class: Parser class to use.
            :type parser_class: <type[IArgParser]>
            :return: ParserStrategyBundle instance.
            :rtype: <ParserStrategyBundle>
            :exceptions: None.
        '''
        return ParserStrategyBundle(
            parameters=parameters,
            context_bundle=context_bundle,
            parser_class=parser_class,
        )
