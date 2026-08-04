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
    Encapsulates core runtime components for simplification of base bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.dependencies import BaseBundleDependencies
from ats_utilities.base.setup.dep_validator import BaseBundleDependenciesValidator
from ats_utilities.base.setup.keys import BaseBundleKeys
from ats_utilities.base.setup.validator import BaseBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class BaseBundleRegistry:
    '''
        Encapsulates core runtime components for simplification of base bundle.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates a base bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: BaseBundleDependencies) -> BaseBundle:
        '''
            Orchestrates dependency injection and creates a base bundle.

            :param dependencies: The registry-specific orchestration dependencies.
            :return: The base bundle.
            :exceptions:
                | ATSValueError: The base bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The base bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The base bundle for base engine must be provided and have proper values.
                | ATSTypeError:  The base bundle for base engine must be an instance of BaseBundle and its
                |                attributes must be instances of their respective interfaces and types.
        '''
        BaseBundleDependenciesValidator.validate(dependencies)

        bundle: BaseBundle = BaseBundle(
            context_bundle=dependencies.get(BaseBundleKeys.DEPENDENCY_CONTEXT_BUNDLE) if dependencies else None,
            info_manager=dependencies.get(BaseBundleKeys.DEPENDENCY_INFO_MANAGER) if dependencies else None,
            option_manager=dependencies.get(BaseBundleKeys.DEPENDENCY_OPTION_MANAGER) if dependencies else None,
            splash_manager=dependencies.get(BaseBundleKeys.DEPENDENCY_SPLASH_MANAGER) if dependencies else None,
            generation_manager=dependencies.get(BaseBundleKeys.DEPENDENCY_GENERATION_MANAGER) if dependencies else None
        )

        BaseBundleValidator.validate(bundle)

        return bundle
