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
    Encapsulates core runtime components for simplification of the context bundle.
'''

from __future__ import annotations

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.dependencies import ContextBundleDependencies
from ats_utilities.context.validator import ContextBundleValidator
from ats_utilities.context.dep_validator import ContextBundleDependenciesValidator
from ats_utilities.context.keys import ContextBundleKeys

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ContextBundleRegistry:
    '''
        Encapsulates core runtime components for simplification of the context bundle.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates the context bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: ContextBundleDependencies) -> ContextBundle:
        '''
            Orchestrates dependency injection and creates the context bundle.

            :param dependencies: The registry-specific orchestration dependencies.
            :return: The context bundle.
            :exceptions:
                | ATSValueError: The context bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The context bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The context bundle must be provided and have proper values.
                | ATSTypeError:  The context bundle must be an instance of ContextBundle and
                |                its attributes must be instances of their respective types.
        '''
        ContextBundleDependenciesValidator.validate(dependencies)

        bundle: ContextBundle = ContextBundle(
            checker=dependencies.get(ContextBundleKeys.DEPENDENCY_CHECKER) if dependencies else None,
            logger=dependencies.get(ContextBundleKeys.DEPENDENCY_LOGGER) if dependencies else None,
            reporter=dependencies.get(ContextBundleKeys.DEPENDENCY_REPORTER) if dependencies else None,
            verbose=dependencies.get(ContextBundleKeys.DEPENDENCY_VERBOSE) if dependencies else False
        )

        ContextBundleValidator.validate(bundle)

        return bundle
