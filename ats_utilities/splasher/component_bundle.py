# -*- coding: UTF-8 -*-

'''
Module
    component_bundle.py
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
    Defines component bundle dataclass for dependency grouping and management.
    Encapsulates splash screen components to minimize constructor overhead.
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
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class SplashComponentBundle:
    '''
        Defines component bundle dataclass for dependency grouping and management.
        Encapsulates splash screen components to minimize constructor overhead.

        It defines:

            :attributes:
                | prop - Splash screen property in dict format (default None).
                | splash_property - Splash screen property API (default None).
                | terminal_property - Terminal properties API (default None).
                | github - GitHub infrastructure for hyperlinks (default None).
                | ext - Generic external infrastructure for hyperlinks (default None).
                | pb - Progress bar component (default None).
                | context_bundle - Context bundle for dependency injection (default ContextBundle).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    prop: Optional[Dict[Any, Any]] = None
    splash_property: Optional[ISplashProperty] = None
    terminal_property: Optional[ITerminalProperties] = None
    github: Optional[IExtInfrastructure] = None
    ext: Optional[IExtInfrastructure] = None
    pb: Optional[IProgressBar] = None
    context_bundle: Optional[ContextBundle] = field(default_factory=ContextBundle)

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :return: None
            :rtype: <None>
            :exceptions: ValueError
        '''
        if self.prop is None:
            raise ValueError("Properties dictionary 'prop' must be provided.")

    def merge(self, other: 'SplashComponentBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <SplashComponentBundle>
            :return: None
            :rtype: <None>
            :exceptions: None
        '''
        for field_name in self.__dataclass_fields__:
            other_value = getattr(other, field_name)
            if other_value is not None:
                setattr(self, field_name, other_value)

    def to_dict(self) -> dict:
        '''
            Converts the bundle attributes to a dictionary.

            :return: Dictionary representation of the bundle attributes.
            :rtype: <dict>
            :exceptions: None
        '''
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_')
        }

