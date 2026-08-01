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
    A factory for creating an option bundle instance.
'''

from __future__ import annotations

from argparse import ArgumentParser
from collections.abc import Mapping

from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.setup.options import OptionOptions
from ats_utilities.option.setup.dependencies import OptionDependencies
from ats_utilities.option.setup.keys import OptionKeys
from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.option.setup.opt_validator import OptionOptionsValidator
from ats_utilities.option.setup.registry import OptionRegistry
from ats_utilities.option.strategy.engine import ParserStrategy
from ats_utilities.option.strategy.data import StrategyData
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.underlying.engine import ParserAdapter

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class OptionFactory:
    '''
        A factory for creating an option bundle instance.

        It defines:

            :methods:
                | create_bundle - Creates an option bundle using configuration options.
    '''

    @classmethod
    def create_bundle(cls, options: OptionOptions) -> OptionBundle:
        '''
            Creates an option bundle using configuration options.

            :param options: The creation options/parameters for the bundle.
            :return: The option bundle instance.
            :exceptions:
                | ATSValueError: Options must be provided and have proper values.
                | ATSTypeError:  Options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        OptionOptionsValidator.validate(options)

        parameters: Mapping[str, str] = options.get(OptionKeys.OPTION_PARAMETERS)
        context_bundle: ContextBundle = options.get(OptionKeys.OPTION_CONTEXT_BUNDLE)
        parser: ParserAdapter = ParserAdapter(
            parser=ArgumentParser(
                prog=f'{InfoKeys.get_name(parameters)} {InfoKeys.get_version(parameters)}',
                epilog=f'{InfoKeys.get_name(parameters)} copyright (c) {InfoKeys.get_licence(parameters)}',
                description=f'{InfoKeys.get_name(parameters)} build date {InfoKeys.get_build_date(parameters)}'
            )
        )

        strategy: ParserStrategy = ParserStrategy(
            strategy_data=StrategyData(
                context_bundle=context_bundle,
                parser=parser
            )
        )

        return OptionRegistry.create_bundle(
            dependencies=OptionDependencies(
                strategy=strategy,
                context_bundle=context_bundle
            )
        )
