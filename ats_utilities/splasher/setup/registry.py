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
    Encapsulates core runtime components for simplification of splash bundle creation.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.splasher.setup.bundle import SplashBundle
from ats_utilities.splasher.setup.dependencies import SplashDependencies
from ats_utilities.splasher.setup.validator import SplashValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class SplashRegistry(IRegistry[SplashBundle, SplashDependencies]):
    '''
        Encapsulates core runtime components for simplification of splash bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates a splash bundle instance.
    '''

    @classmethod
    @override
    def create_bundle(cls, dependencies: SplashDependencies) -> SplashBundle:
        '''
            Orchestrates dependency injection and creates a splash bundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :type dependencies: SplashDependencies
            :return: Splash bundle instance.
            :rtype: SplashBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Properties dictionary must be provided.
                | ATSValueError: Splash property must be provided.
                | ATSValueError: Property validated flag must be provided.
                | ATSValueError: Terminal properties must be provided.
                | ATSValueError: External infrastructure must be provided.
                | ATSValueError: Progress bar must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of SplashBundle.
                | ATSTypeError: Properties dictionary must be an instance of Mapping.
                | ATSTypeError: Splash property must be an instance of ISplashProperty.
                | ATSTypeError: Property validated flag must be an instance of bool.
                | ATSTypeError: Terminal properties must be an instance of ITemplateDir.
                | ATSTypeError: External infrastructure must be an instance of IExtInfrastructure.
                | ATSTypeError: Progress bar must be an instance of IProgressBar.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        bundle: SplashBundle = SplashBundle(
            prop=dependencies.get('prop'),
            splash_property=dependencies.get('splash_property'),
            property_validated=dependencies.get('property_validated'),
            terminal_property=dependencies.get('terminal_property'),
            ext=dependencies.get('ext'),
            pb=dependencies.get('pb'),
            context_bundle=dependencies.get('context_bundle')
        )

        SplashValidator.validate(bundle)

        return bundle
