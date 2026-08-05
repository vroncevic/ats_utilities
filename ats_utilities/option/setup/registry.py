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
    Encapsulates core runtime components for simplification of option bundle.
'''

from __future__ import annotations

from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.setup.dependencies import OptionBundleDependencies
from ats_utilities.option.setup.keys import OptionBundleKeys
from ats_utilities.option.setup.validator import OptionBundleValidator
from ats_utilities.option.setup.dep_validator import OptionBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class OptionBundleRegistry:
    '''
        Encapsulates core runtime components for simplification of option bundle.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates an option bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: OptionBundleDependencies) -> OptionBundle:
        '''
            Orchestrates dependency injection and creates an option bundle.

            :param dependencies: The registry-specific orchestration dependencies.
            :return: The option bundle.
            :exceptions:
                | ATSValueError: The option bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The option bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The option bundle must be provided and have proper values.
                | ATSTypeError:  The option bundle must be an instance of OptionBundle and its
                |                attributes must be instances of their respective types.
        '''
        OptionBundleDependenciesValidator.validate(dependencies)

        bundle: OptionBundle = OptionBundle(
            strategy=dependencies.get(OptionBundleKeys.DEPENDENCY_STRATEGY) if dependencies else None,
            context_bundle=dependencies.get(OptionBundleKeys.DEPENDENCY_CONTEXT_BUNDLE) if dependencies else None
        )

        OptionBundleValidator.validate(bundle)

        return bundle
