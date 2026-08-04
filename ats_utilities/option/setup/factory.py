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
    A factory for creating an option bundle.
'''

from __future__ import annotations

from argparse import ArgumentParser
from collections.abc import Mapping

from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.setup.options import OptionBundleOptions
from ats_utilities.option.setup.dependencies import OptionBundleDependencies
from ats_utilities.option.setup.keys import OptionBundleKeys
from ats_utilities.info.setup.expose import InfoExpose
from ats_utilities.option.setup.opt_validator import OptionBundleOptionsValidator
from ats_utilities.option.setup.registry import OptionBundleRegistry
from ats_utilities.option.strategy.engine import ParserStrategy
from ats_utilities.option.strategy.data import StrategyData
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.underlying.engine import ParserAdapter

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class OptionBundleFactory:
    '''
        A factory for creating an option bundle.

        It defines:

            :methods:
                | create_bundle - Creates an option bundle using configuration options.
    '''

    @classmethod
    def create_bundle(cls, options: OptionBundleOptions) -> OptionBundle:
        '''
            Creates an option bundle using configuration options.

            :param options: The creation options/parameters for the bundle.
            :return: The option bundle.
            :exceptions:
                | ATSValueError: The option bundle options must be provided and have proper values.
                | ATSTypeError:  The option bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The option bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The option bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The option bundle must be provided and have proper values.
                | ATSTypeError:  The option bundle must be an instance of OptionBundle and its
                |                attributes must be instances of their respective types.
        '''
        OptionBundleOptionsValidator.validate(options)

        parameters: Mapping[str, str] = options.get(OptionBundleKeys.OPTION_PARAMETERS)
        context_bundle: ContextBundle = options.get(OptionBundleKeys.OPTION_CONTEXT_BUNDLE)
        parser: ParserAdapter = ParserAdapter(
            parser=ArgumentParser(
                prog=f'{InfoExpose.get_name(parameters)} {InfoExpose.get_version(parameters)}',
                epilog=f'{InfoExpose.get_name(parameters)} copyright (c) {InfoExpose.get_licence(parameters)}',
                description=f'{InfoExpose.get_name(parameters)} build date {InfoExpose.get_build_date(parameters)}'
            )
        )

        strategy: ParserStrategy = ParserStrategy(
            strategy_data=StrategyData(
                context_bundle=context_bundle,
                parser=parser
            )
        )

        return OptionBundleRegistry.create_bundle(
            dependencies=OptionBundleDependencies(strategy=strategy, context_bundle=context_bundle)
        )
