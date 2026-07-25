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
    Encapsulates core runtime components for simplification of context bundle creation.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.setup.iregistry import IRegistry
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.dependencies import ContextDependencies
from ats_utilities.context.validator import ContextValidator
from ats_utilities.context.dep_validator import ContextDependenciesValidator
from ats_utilities.context.keys import ContextKeys

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ContextRegistry(IRegistry[ContextBundle, ContextDependencies]):
    '''
        Encapsulates core runtime components for simplification of context bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates a context bundle instance.
    '''

    @classmethod
    @override
    def create_bundle(cls, dependencies: ContextDependencies) -> ContextBundle:
        '''
            Orchestrates dependency injection and creates a context bundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :return: Context bundle instance.
            :exceptions:
                | ATSValueError: Dependencies must be provided and have proper values.
                | ATSTypeError:  Dependencies must be an instance of ContextDependencies
                |                and its attributes must be instances of their
                |                respective types.
        '''
        ContextDependenciesValidator.validate(dependencies)

        bundle: ContextBundle = ContextBundle(
            checker=dependencies.get(ContextKeys.DEPENDENCY_CHECKER),
            logger=dependencies.get(ContextKeys.DEPENDENCY_LOGGER),
            reporter=dependencies.get(ContextKeys.DEPENDENCY_REPORTER),
            verbose=dependencies.get(ContextKeys.DEPENDENCY_VERBOSE, False)
        )

        ContextValidator.validate(bundle)

        return bundle
