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
    Encapsulates core runtime components for simplification of splash bundle.
'''

from __future__ import annotations

from ats_utilities.splash.setup.bundle import SplashBundle
from ats_utilities.splash.setup.dependencies import SplashBundleDependencies
from ats_utilities.splash.setup.keys import SplashKeys
from ats_utilities.splash.setup.validator import SplashBundleValidator
from ats_utilities.splash.setup.dep_validator import SplashBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class SplashBundleRegistry:
    '''
        Encapsulates core runtime components for simplification of splash bundle.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates a splash bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: SplashBundleDependencies) -> SplashBundle:
        '''
            Orchestrates dependency injection and creates a splash bundle.

            :param dependencies: The registry-specific orchestration dependencies.
            :return: The splash bundle.
            :exceptions:
                | ATSValueError: The splash bundle dependencies must be provided and have proper attributes.
                | ATSTypeError:  The splash bundle dependencies must be an instance of Mapping and its attributes
                |                must be instances of their respective types.
                | ATSValueError: The splash bundle must be provided and have proper values.
                | ATSTypeError:  The splash bundle must be an instance of SplashBundle and its
                |                attributes must be instances of their respective types.
        '''
        SplashBundleDependenciesValidator.validate(dependencies)

        bundle: SplashBundle = SplashBundle(
            splash_property=dependencies.get(SplashKeys.DEPENDENCY_SPLASH_PROPERTY) if dependencies else None,
            terminal_property=dependencies.get(SplashKeys.DEPENDENCY_TERMINAL_PROPERTY) if dependencies else None,
            ext=dependencies.get(SplashKeys.DEPENDENCY_EXT) if dependencies else None,
            pb=dependencies.get(SplashKeys.DEPENDENCY_PB) if dependencies else None,
            context_bundle=dependencies.get(SplashKeys.DEPENDENCY_CONTEXT_BUNDLE) if dependencies else None
        )

        SplashBundleValidator.validate(bundle)

        return bundle
