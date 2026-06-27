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

from typing import Any
from dataclasses import dataclass
from ats_utilities.splasher.isplash_property import ISplashProperty
from ats_utilities.splasher.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.iprogress_bar import IProgressBar
from ats_utilities.context_bundle import ContextBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
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
                | context_bundle - Context bundle for dependency injection (default None).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    prop: dict[Any, Any] | None = None
    splash_property: ISplashProperty | None = None
    terminal_property: ITerminalProperties | None = None
    github: IExtInfrastructure | None = None
    ext: IExtInfrastructure | None = None
    pb: IProgressBar | None = None
    context_bundle: ContextBundle | None = None

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ValueError: Properties dictionary 'prop' must be provided.
                | ValueError: Splash property 'splash_property' must be provided.
                | ValueError: Terminal properties 'terminal_property' must be provided.
                | ValueError: GitHub infrastructure 'github' must be provided.
                | ValueError: External infrastructure 'ext' must be provided.
                | ValueError: Progress bar 'pb' must be provided.
                | ValueError: Context bundle 'context_bundle' must be provided.
        '''
        if self.prop is None:
            raise ValueError("properties dictionary 'prop' must be provided.")

        if self.splash_property is None:
            raise ValueError("splash property 'splash_property' must be provided.")

        if self.terminal_property is None:
            raise ValueError("terminal properties 'terminal_property' must be provided.")

        if self.github is None:
            raise ValueError("gitHub infrastructure 'github' must be provided.")

        if self.ext is None:
            raise ValueError("external infrastructure 'ext' must be provided.")

        if self.pb is None:
            raise ValueError("progress bar 'pb' must be provided.")

        if self.context_bundle is None:
            raise ValueError("context bundle 'context_bundle' must be provided.")

    def merge(self, other: 'SplashComponentBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <SplashComponentBundle>
            :exceptions: None.
        '''
        for field_name in self.__dataclass_fields__:
            other_value = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the bundle attributes to a dictionary.

            :return: Dictionary representation of the bundle attributes.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_')
        }

