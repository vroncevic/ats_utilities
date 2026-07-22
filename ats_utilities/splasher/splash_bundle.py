# -*- coding: UTF-8 -*-

'''
Module
    splash_bundle.py
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
    Encapsulates components of splash screen for simplification of SplashBundle creation.
'''

from __future__ import annotations

from typing import Any
from collections.abc import Mapping
from dataclasses import dataclass

from ats_utilities.splasher.property.isplash_property import ISplashProperty
from ats_utilities.splasher.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.progressbar.iprogress_bar import IProgressBar
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class SplashBundle:
    '''
        Encapsulates components of splash screen for simplification of SplashBundle creation.

        It defines:

            :attributes:
                | prop - Splash screen properties in dict format.
                | splash_property - Splash screen property instance.
                | terminal_property - Terminal properties instance.
                | ext - Generic external infrastructure instance.
                | pb - Progress bar component instance.
                | context_bundle - Context bundle instance.
            :methods:
                | __post_init__ - Post-initialization hook to validate splash bundle.
                | validate - Validates splash bundle.
                | to_dict - Converts the SplashBundle instance to a dictionary.
    '''

    prop: Mapping[str, Any]
    splash_property: ISplashProperty
    property_validated: bool
    terminal_property: ITerminalProperties
    ext: IExtInfrastructure
    pb: IProgressBar
    context_bundle: ContextBundle

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate splash bundle.

            :exceptions:
                | ATSValueError: Properties dictionary 'prop' must be provided.
                | ATSValueError: Splash property 'splash_property' must be provided.
                | ATSValueError: Terminal properties 'terminal_property' must be provided.
                | ATSValueError: External infrastructure 'ext' must be provided.
                | ATSValueError: Progress bar 'pb' must be provided.
                | ATSValueError: Context bundle 'context_bundle' must be provided.
                | ATSTypeError: Property 'prop' must be a Mapping[str, Any] instance.
                | ATSTypeError: Splash property 'splash_property' must be an ISplashProperty instance.
                | ATSTypeError: Terminal properties 'terminal_property' must be an ITerminalProperties instance.
                | ATSTypeError: External infrastructure 'ext' must be an IExtInfrastructure instance.
                | ATSTypeError: Progress bar 'pb' must be an IProgressBar instance.
                | ATSTypeError: Context bundle 'context_bundle' must be a ContextBundle instance.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates splash bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Properties dictionary 'prop' must be provided.
                | ATSValueError: Splash property 'splash_property' must be provided.
                | ATSValueError: Terminal properties 'terminal_property' must be provided.
                | ATSValueError: External infrastructure 'ext' must be provided.
                | ATSValueError: Progress bar 'pb' must be provided.
                | ATSValueError: Context bundle 'context_bundle' must be provided.
                | ATSTypeError: Property 'prop' must be a Mapping[str, Any] instance.
                | ATSTypeError: Splash property 'splash_property' must be an ISplashProperty instance.
                | ATSTypeError: Terminal properties 'terminal_property' must be an ITerminalProperties instance.
                | ATSTypeError: External infrastructure 'ext' must be an IExtInfrastructure instance.
                | ATSTypeError: Progress bar 'pb' must be an IProgressBar instance.
                | ATSTypeError: Context bundle 'context_bundle' must be a ContextBundle instance.
        '''
        context: str = r'splash_bundle::validate(...)'
        not_none(self.prop, context, r'properties dictionary must be provided')
        not_none(self.splash_property, context, r'splash property must be provided')
        not_none(self.terminal_property, context, r'terminal properties must be provided')
        not_none(self.ext, context, r'external infrastructure must be provided')
        not_none(self.pb, context, r'progress bar must be provided')
        not_none(self.context_bundle, context, r'context bundle must be provided')
        istype(self.prop, Mapping, context, r'properties dictionary must be a Mapping[str, Any] instance')
        istype(self.splash_property, ISplashProperty, context, r'splash property must be an ISplashProperty instance')
        istype(self.terminal_property, ITerminalProperties, context, r'terminal properties must be an ITerminalProperties instance')
        istype(self.ext, IExtInfrastructure, context, r'external infrastructure must be an IExtInfrastructure instance')
        istype(self.pb, IProgressBar, context, r'progress bar must be an IProgressBar instance')
        istype(self.context_bundle, ContextBundle, context, r'context bundle must be a ContextBundle instance')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the splash bundle instance to a dictionary.

            :return: Dictionary representation of the splash bundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
