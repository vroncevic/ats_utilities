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
    Encapsulates core runtime components for simplification of checker bundle creation.
'''

from __future__ import annotations

from ats_utilities.checker.setup.bundle import CheckerBundle
from ats_utilities.checker.setup.dependencies import CheckerDependencies
from ats_utilities.checker.setup.keys import CheckerKeys
from ats_utilities.checker.setup.validator import CheckerValidator
from ats_utilities.checker.setup.dep_validator import CheckerDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class CheckerRegistry:
    '''
        Encapsulates core runtime components for simplification of checker bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates a checker bundle instance.
    '''

    @classmethod
    def create_bundle(cls, dependencies: CheckerDependencies | None = None) -> CheckerBundle:
        '''
            Orchestrates dependency injection and creates a checker bundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :return: Checker bundle instance.
            :exceptions:
                | ATSValueError: Dependencies must be provided and have proper values.
                | ATSTypeError:  Dependencies must be an instance of CheckerDependencies
                |                and its attributes must be instances of their
                |                respective interfaces and types.
        '''
        if dependencies is not None:
            CheckerDependenciesValidator.validate(dependencies)

        bundle: CheckerBundle = CheckerBundle(
            format_validator=dependencies.get(CheckerKeys.DEPENDENCY_FORMAT_VALIDATOR) if dependencies else None,
            type_validator=dependencies.get(CheckerKeys.DEPENDENCY_TYPE_VALIDATOR) if dependencies else None,
            context_provider=dependencies.get(CheckerKeys.DEPENDENCY_CONTEXT_PROVIDER) if dependencies else None,
            check_reporter=dependencies.get(CheckerKeys.DEPENDENCY_CHECK_REPORTER) if dependencies else None
        )

        CheckerValidator.validate(bundle)

        return bundle
