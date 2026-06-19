# -*- coding: utf-8 -*-

'''
Module
    splash_center_bundle.py
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
    Defines splash screen bundle for centering console output.
'''

from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field
from ats_utilities.splasher.isplash_property import ISplashProperty
from ats_utilities.splasher.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.iprogress_bar import IProgressBar
from ats_utilities.context_bundle import ContextBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class SplashCenterBundle:
    '''
        Defines splash screen bundle for centering console output.

        It defines:

            :attributes:
                | columns - Column count for console session (default 0).
                | additional_shifter - Additional shifters (default 0).
                | text - Text for console session (default None).
            :methods: None
    '''

    columns: int = 0
    additional_shifter: int = 0
    text: Optional[str] = None
