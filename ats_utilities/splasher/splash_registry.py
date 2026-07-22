# -*- coding: UTF-8 -*-

'''
Module
    splash_registry.py
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
    Encapsulates splash screen components for simplification of SplashBundle creation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.splasher.splash_bundle import SplashBundle
from ats_utilities.splasher.splash_params import SplashParams
from ats_utilities.context.bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class SplashRegistry(IRegistry[SplashBundle, SplashParams]):
    '''
        Encapsulates splash screen components for simplification of SplashBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a SplashBundle.
    '''

    @classmethod
    @override
    def create_bundle(cls, params: SplashParams) -> SplashBundle:
        '''
            Creates a SplashBundle instance.

            :param params: Registry-specific orchestration parameters.
            :type params: SplashParams
            :return: SplashBundle instance.
            :rtype: <SplashBundle>
            :exceptions:
                | ATSValueError: Context bundle must not be provided.
                | ATSTypeError: Context bundle must be of type ContextBundle.
        '''
        return SplashBundle(
            prop=params.get('prop'),
            splash_property=params.get('splash_property'),
            property_validated=params.get('property_validated'),
            terminal_property=params.get('terminal_property'),
            ext=params.get('ext'),
            pb=params.get('pb'),
            context_bundle=params.get('context_bundle')
        )

