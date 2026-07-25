# -*- coding: UTF-8 -*-

'''
Module
    dep_validator.py
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
    Validator for option dependencies.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.option.setup.dependencies import OptionDependencies
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.utils.setup.idep_validator import IDependenciesValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class OptionDependenciesValidator(IDependenciesValidator[OptionDependencies]):
    '''
        Validator for option dependencies.

        It defines:

            :methods:
                | validate - Validates option dependencies instance.
    '''

    @classmethod
    @override
    def validate(cls, dependencies: OptionDependencies) -> None:
        '''
            Validates option dependencies instance.

            :param dependencies: Option dependencies instance to be validated.
            :exceptions:
                | ATSValueError: Dependencies must be provided.
                | ATSTypeError: Dependencies must be a Mapping.
                | ATSTypeError: Parameters must be a Mapping.
                | ATSTypeError: Strategy must be an instance of IParserStrategy.
                | ATSTypeError: Context bundle must be a ContextBundle.
        '''
        ctx: str = r'option_dependencies_validator::validate(...)'

        not_none(dependencies, ctx, r'dependencies must be provided')
        istype(dependencies, Mapping, ctx, r'dependencies must be a Mapping')

        parameters = dependencies.get('parameters')
        not_none(parameters, ctx, r'parameters must be provided')
        istype(parameters, Mapping, ctx, r'parameters must be a Mapping')

        strategy = dependencies.get('strategy')
        not_none(strategy, ctx, r'strategy must be provided')
        istype(strategy, IParserStrategy, ctx, r'strategy must be an instance of IParserStrategy')

        context_bundle = dependencies.get('context_bundle')
        not_none(context_bundle, ctx, r'context bundle must be provided')
        istype(context_bundle, ContextBundle, ctx, r'context bundle must be an instance of ContextBundle')
