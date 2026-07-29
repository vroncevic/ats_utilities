# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core runtime components for simplification of option bundle creation.
'''

from __future__ import annotations

from ats_utilities.utils.setup.iregistry import IRegistry
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.setup.dependencies import OptionDependencies
from ats_utilities.option.setup.keys import OptionKeys
from ats_utilities.option.setup.validator import OptionValidator
from ats_utilities.option.setup.dep_validator import OptionDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class OptionRegistry(IRegistry[OptionBundle, OptionDependencies]):
    '''
        Encapsulates core runtime components for simplification of option bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates an option bundle instance.
    '''

    @classmethod
    def create_bundle(cls, dependencies: OptionDependencies) -> OptionBundle:
        '''
            Orchestrates dependency injection and creates an option bundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :return: Option bundle instance.
            :exceptions:
                | ATSValueError: Dependencies must be provided.
                | ATSTypeError: Dependencies must be a Mapping.
                | ATSTypeError: Parameters must be a Mapping.
                | ATSTypeError: Strategy must be an instance of IParserStrategy.
                | ATSTypeError: Context bundle must be a ContextBundle.
                | ATSValueError: Option bundle must be provided.
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Strategy must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Option bundle must be an instance of OptionBundle.
                | ATSTypeError: Parameters must be a Mapping[str, str] instance.
                | ATSTypeError: Strategy must be an IParserStrategy instance.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        OptionDependenciesValidator.validate(dependencies)

        bundle: OptionBundle = OptionBundle(
            parameters=dependencies.get(OptionKeys.DEPENDENCY_PARAMETERS) if dependencies else None,
            strategy=dependencies.get(OptionKeys.DEPENDENCY_STRATEGY) if dependencies else None,
            context_bundle=dependencies.get(OptionKeys.DEPENDENCY_CONTEXT_BUNDLE) if dependencies else None
        )

        OptionValidator.validate(bundle)

        return bundle
