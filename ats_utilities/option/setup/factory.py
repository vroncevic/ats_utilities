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
    Factory for creating option bundle instance.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.utils.ifactory import IFactory
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.setup.dependencies import OptionOptions, OptionDependencies
from ats_utilities.option.setup.registry import OptionRegistry
from ats_utilities.option.strategy.engine import ParserStrategy
from ats_utilities.option.strategy.parser_strategy_registry import ParserStrategyRegistry
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.parser.engine import ArgParser
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


class OptionFactory(IFactory[OptionBundle, OptionOptions]):
    '''
        Factory for creating option bundle instance.

        It defines:

            :methods:
                | create_default_bundle - Creates a default option bundle using configuration options.
    '''

    @classmethod
    @override
    def create_default_bundle(cls, options: OptionOptions) -> OptionBundle:
        '''
            Creates a default option bundle using configuration options.

            :param options: Creation options/parameters for the bundle.
            :type options: OptionOptions
            :return: Option bundle instance.
            :rtype: OptionBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Strategy must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of OptionBundle.
                | ATSTypeError: Parameters must be a Mapping[str, str] instance.
                | ATSTypeError: Strategy must be an IParserStrategy instance.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        ctx: str = r'option_factory::create_default_bundle(...)'
        not_none(options, ctx, r'options must be provided')
        istype(options, dict, ctx, r'options must be a dictionary')

        parameters: Mapping[str, str] = options.get('parameters')
        context_bundle: ContextBundle = options.get('context_bundle')
        parser_class: type[IArgParser] = options.get('parser_class', ArgParser)

        parser_strategy_bundle = ParserStrategyRegistry.create_parser_strategy_bundle_from_dict(
            parameters=parameters,
            context_bundle=context_bundle,
            parser_class=parser_class
        )
        strategy: ParserStrategy = ParserStrategy(own=parser_strategy_bundle)

        return OptionRegistry.create_bundle(
            OptionDependencies(
                parameters=parameters,
                strategy=strategy,
                context_bundle=context_bundle
            )
        )

    @classmethod
    def create_option_bundle_from_dict(
        cls,
        parameters: Mapping[str, str],
        context_bundle: ContextBundle,
        parser_class: type[IArgParser] = ArgParser
    ) -> OptionBundle:
        '''
            Creates an option bundle from parameters in mapping format.
            Kept for backward compatibility.

            :param parameters: Metadata parameters in mapping format (read only data).
            :type parameters: Mapping[str, str]
            :param context_bundle: Context bundle for option bundle.
            :type context_bundle: ContextBundle
            :param parser_class: Injected parser class type.
            :type parser_class: type[IArgParser]
            :return: Option bundle instance.
            :rtype: OptionBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Strategy must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of OptionBundle.
                | ATSTypeError: Parameters must be a Mapping[str, str] instance.
                | ATSTypeError: Strategy must be an IParserStrategy instance.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        return cls.create_default_bundle({
            'parameters': parameters,
            'context_bundle': context_bundle,
            'parser_class': parser_class
        })
