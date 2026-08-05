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
    Encapsulates core runtime components for simplification of the checker bundle.
'''

from __future__ import annotations

from ats_utilities.checker.setup.bundle import CheckerBundle
from ats_utilities.checker.setup.dependencies import CheckerBundleDependencies
from ats_utilities.checker.setup.keys import CheckerBundleKeys
from ats_utilities.checker.setup.validator import CheckerBundleValidator
from ats_utilities.checker.setup.dep_validator import CheckerBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class CheckerBundleRegistry:
    '''
        Encapsulates core runtime components for simplification of the checker bundle.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates the checker bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: CheckerBundleDependencies) -> CheckerBundle:
        '''
            Orchestrates dependency injection and creates the checker bundle.

            :param dependencies: The registry-specific orchestration dependencies.
            :return: The checker bundle.
            :exceptions:
                | ATSValueError: The checker bundle dependencies must be provided and have proper attributes.
                | ATSTypeError:  The checker bundle dependencies must be an instance of Mapping and its attributes
                |                must be instances of their respective types.
                | ATSValueError: The checker bundle must be provided and have proper values.
                | ATSTypeError:  The checker bundle must be an instance of CheckerBundle
                |                and its attributes must be instances of their respective types.
        '''
        CheckerBundleDependenciesValidator.validate(dependencies)

        bundle: CheckerBundle = CheckerBundle(
            format_validator=dependencies.get(CheckerBundleKeys.DEPENDENCY_FORMAT_VALIDATOR),
            type_validator=dependencies.get(CheckerBundleKeys.DEPENDENCY_TYPE_VALIDATOR),
            context_provider=dependencies.get(CheckerBundleKeys.DEPENDENCY_CONTEXT_PROVIDER),
            check_reporter=dependencies.get(CheckerBundleKeys.DEPENDENCY_CHECK_REPORTER)
        )

        CheckerBundleValidator.validate(bundle)

        return bundle
