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

from argparse import ArgumentParser
from collections.abc import Mapping

from ats_utilities.utils.setup.ifactory import IFactory
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.setup.options import OptionOptions
from ats_utilities.option.setup.dependencies import OptionDependencies
from ats_utilities.option.setup.keys import OptionKeys
from ats_utilities.option.setup.opt_validator import OptionOptionsValidator
from ats_utilities.option.setup.registry import OptionRegistry
from ats_utilities.option.strategy.engine import ParserStrategy
from ats_utilities.option.strategy.data import StrategyData
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.underlying.iunderlying import IUnderlyingParser
from ats_utilities.option.underlying.engine import ParserAdapter

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class OptionFactory(IFactory[OptionBundle, OptionOptions]):
    '''
        Factory for creating option bundle instance.

        It defines:

            :methods:
                | create_bundle - Creates an option bundle using configuration options.
    '''

    @classmethod
    def create_bundle(cls, options: OptionOptions) -> OptionBundle:
        '''
            Creates an option bundle using configuration options.

            :param options: Creation options/parameters for the bundle.
            :return: Option bundle instance.
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a Mapping.
                | ATSTypeError: Parameters must be a Mapping.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
                | ATSTypeError: Parser must be an instance of IUnderlyingParser.
                | ATSValueError: Option bundle must be provided.
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Strategy must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Option bundle must be an instance of OptionBundle.
                | ATSTypeError: Parameters must be a Mapping[str, str] instance.
                | ATSTypeError: Strategy must be an IParserStrategy instance.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        OptionOptionsValidator.validate(options)

        parameters: Mapping[str, str] = options.get(OptionKeys.OPTION_PARAMETERS)
        context_bundle: ContextBundle = options.get(OptionKeys.OPTION_CONTEXT_BUNDLE)
        parser: IUnderlyingParser = options.get(OptionKeys.OPTION_PARSER)

        if parser is None:
            parser = ParserAdapter(parser=ArgumentParser())

        strategy: ParserStrategy = ParserStrategy(
            strategy_data=StrategyData(
                parameters=parameters,
                context_bundle=context_bundle,
                parser=parser
            )
        )

        return OptionRegistry.create_bundle(
            dependencies=OptionDependencies(
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
        parser_class: type | None = None,
        parser: IUnderlyingParser | None = None
    ) -> OptionBundle:
        '''
            Creates an option bundle from parameters in mapping format.
            Kept for backward compatibility.

            :param parameters: Metadata parameters in mapping format (read only data).
            :param context_bundle: Context bundle for option bundle.
            :param parser_class: Injected parser class type (legacy support).
            :param parser: Injected parser instance.
            :return: Option bundle instance.
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
        if parser is None:
            if parser_class is not None:
                if issubclass(parser_class, ArgumentParser):
                    parser = ParserAdapter(parser=parser_class())
                else:
                    parser = parser_class()

        options = OptionOptions(
            parameters=parameters,
            context_bundle=context_bundle
        )
        if parser is not None:
            options[OptionKeys.OPTION_PARSER] = parser

        return cls.create_bundle(options)
