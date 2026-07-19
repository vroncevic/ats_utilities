# -*- coding: UTF-8 -*-

'''
Module
    splash_center_registry.py
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
    Encapsulates splash screen components for simplification of SplashCenterBundle creation.
'''

from __future__ import annotations

from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.splasher.splash_center_bundle import SplashCenterBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class SplashCenterRegistry(IRegistry[SplashCenterBundle]):
    '''
        Encapsulates splash screen components for simplification of SplashCenterBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a SplashCenterBundle.
                | create_splash_center_bundle - Creates a SplashCenterBundle.
    '''

    @classmethod
    @override
    def create_bundle(cls, **kwargs: Any) -> SplashCenterBundle:
        '''
            Creates a SplashCenterBundle instance.

            :param kwargs: Additional registry-specific orchestration parameters.
            :return: SplashCenterBundle instance.
            :rtype: <SplashCenterBundle>
            :exceptions:
                | ATSValueError: Columns must be provided.
                | ATSValueError: Additional shifter must be provided.
                | ATSTypeError: Columns must be an integer.
                | ATSTypeError: Additional shifter must be an integer.
        '''
        columns: int = kwargs.get('columns')
        additional_shifter: int = kwargs.get('additional_shifter')

        return cls.create_splash_center_bundle(
            columns=columns,
            additional_shifter=additional_shifter,
        )

    @classmethod
    def create_splash_center_bundle(
        cls, 
        columns: int, 
        additional_shifter: int
    ) -> SplashCenterBundle:
        '''
            Creates a SplashCenterBundle.

            :param columns: Columns count.
            :type columns: <int>
            :param additional_shifter: Additional shifter.
            :type additional_shifter: <int>
            :return: SplashCenterBundle instance.
            :rtype: <SplashCenterBundle>
            :exceptions: None.
        '''
        return SplashCenterBundle(
            columns=columns,
            additional_shifter=additional_shifter,
        )
