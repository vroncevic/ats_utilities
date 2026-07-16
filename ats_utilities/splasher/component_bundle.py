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

from __future__ import annotations

from typing import Any
from collections.abc import Mapping
from dataclasses import dataclass

from ats_utilities.splasher.property.isplash_property import ISplashProperty
from ats_utilities.splasher.property.splash_property import SplashProperty
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.splasher.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.terminal.terminal_properties import TerminalProperties
from ats_utilities.splasher.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.external.ext_infrastructure import ExtInfrastructure
from ats_utilities.splasher.external.github_infrastructure import GitHubInfrastructure
from ats_utilities.splasher.progressbar.iprogress_bar import IProgressBar
from ats_utilities.splasher.progressbar.progress_bar import ProgressBar
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.context.context_registry import ContextRegistry
from ats_utilities.utils.component import make_component, validate_component
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


@dataclass(slots=True, kw_only=True)
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
                | __post_init__ - Post initials SplashComponentBundle constructor.
                | validate - Validates that SplashComponentBundle is valid (can be called after merge).
                | merge - Merges non-None values from another SplashComponentBundle into this one.
                | to_dict - Converts the SplashComponentBundle instance to a dictionary.
    '''

    prop: Mapping[str, Any] | None = None
    splash_property: ISplashProperty | None = None
    property_validated: bool = False
    terminal_property: ITerminalProperties | None = None
    github: IExtInfrastructure | None = None
    ext: IExtInfrastructure | None = None
    pb: IProgressBar | None = None
    context_bundle: ContextBundle | None = None

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to set up default components if not provided.

            :exceptions:
                | ATSTypeError: Property 'prop' must be a Mapping[str, Any] instance.
                | ATSTypeError: Property 'context_bundle' must be a ContextBundle instance.
                | ATSTypeError: Property 'splash_property' must be an ISplashProperty instance.
                | ATSTypeError: Property 'terminal_property' must be an ITerminalProperties instance.
                | ATSTypeError: Property 'github' must be an IExtInfrastructure instance.
                | ATSTypeError: Property 'ext' must be an IExtInfrastructure instance.
                | ATSTypeError: Property 'pb' must be an IProgressBar instance.
        '''
        if self.prop is not None:
            istype(self.prop, Mapping, r'prop must be a Mapping[str, Any] instance')

        if self.context_bundle is None:
            self.context_bundle = ContextRegistry.create_default_context_bundle()

        factory_args: dict[str, Any] = {'context_bundle': self.context_bundle}

        self.splash_property = make_component(self.splash_property, SplashProperty, factory_args)
        validate_component(self.splash_property, ISplashProperty, r'splash_property must be an ISplashProperty instance')

        if self.prop is not None:
            self.splash_property.splash_keys = self.prop
            self.property_validated = self.splash_property.validates()

        self.terminal_property = make_component(self.terminal_property, TerminalProperties, factory_args)
        validate_component(
            self.terminal_property, ITerminalProperties, r'terminal_property must be an ITerminalProperties instance'
        )

        size: tuple[Any, ...] = self.terminal_property.size()

        self.github = make_component(self.github, GitHubInfrastructure, factory_args)
        validate_component(self.github, IExtInfrastructure, r'github must be an IExtInfrastructure instance')

        self.ext = make_component(self.ext, ExtInfrastructure, factory_args)
        validate_component(self.ext, IExtInfrastructure, r'ext must be an IExtInfrastructure instance')

        if self.property_validated and self.prop is not None:
            is_enabled = bool(self.prop.get('enabled', True))

            if is_enabled:
                use_github = bool(self.prop.get(SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE, False))

                if use_github:
                    self.github.infrastructure_property = self.prop
                else:
                    self.ext.infrastructure_property = self.prop

        self.pb = make_component(self.pb, ProgressBar, {'end': int(size[1]) - int(int(size[1]) / 2)})
        validate_component(self.pb, IProgressBar, r'pb must be an IProgressBar instance')

    def validate(self) -> None:
        '''
            Validates that SplashComponentBundle is valid (can be called after merge).
            Performs validation of splash keys, terminal properties, GitHub infrastructure, 
            external infrastructure, progress bar and context bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Properties dictionary 'prop' must be provided.
                | ATSValueError: Splash property 'splash_property' must be provided.
                | ATSValueError: Terminal properties 'terminal_property' must be provided.
                | ATSValueError: GitHub infrastructure 'github' must be provided.
                | ATSValueError: External infrastructure 'ext' must be provided.
                | ATSValueError: Progress bar 'pb' must be provided.
                | ATSValueError: Context bundle 'context_bundle' must be provided.
                | ATSTypeError: Property 'prop' must be a Mapping[str, Any] instance.
                | ATSTypeError: Splash property 'splash_property' must be an ISplashProperty instance.
                | ATSTypeError: Terminal properties 'terminal_property' must be an ITerminalProperties instance.
                | ATSTypeError: GitHub infrastructure 'github' must be an IExtInfrastructure instance.
                | ATSTypeError: External infrastructure 'ext' must be an IExtInfrastructure instance.
                | ATSTypeError: Progress bar 'pb' must be an IProgressBar instance.
                | ATSTypeError: Context bundle 'context_bundle' must be a ContextBundle instance.
        '''
        not_none(self.prop, r'properties dictionary prop must be provided')
        not_none(self.splash_property, r'splash property splash_property must be provided')
        not_none(self.terminal_property, r'terminal properties terminal_property must be provided')
        not_none(self.github, r'gitHub infrastructure github must be provided')
        not_none(self.ext, r'external infrastructure ext must be provided')
        not_none(self.pb, r'progress bar pb must be provided')
        not_none(self.context_bundle, r'context bundle context_bundle must be provided')
        istype(self.prop, Mapping, r'properties dictionary prop must be a Mapping[str, Any] instance')
        istype(self.splash_property, ISplashProperty, r'splash property splash_property must be an ISplashProperty instance')
        istype(self.terminal_property, ITerminalProperties, r'terminal properties terminal_property must be an ITerminalProperties instance')
        istype(self.github, IExtInfrastructure, r'gitHub infrastructure github must be an IExtInfrastructure instance')
        istype(self.ext, IExtInfrastructure, r'external infrastructure ext must be an IExtInfrastructure instance')
        istype(self.pb, IProgressBar, r'progress bar pb must be an IProgressBar instance')
        istype(self.context_bundle, ContextBundle, r'context bundle context_bundle must be a ContextBundle instance')

    def merge(self, other: SplashComponentBundle) -> None:
        '''
            Merges non-None values from another SplashComponentBundle into this one.

            :param other: Another SplashComponentBundle to merge into this one.
            :type other: <SplashComponentBundle>
            :exceptions:
                | ATSValueError: Other SplashComponentBundle must be provided.
                | ATSTypeError: Other must be a SplashComponentBundle instance.
        '''
        not_none(other, r'other SplashComponentBundle must be provided')
        istype(other, SplashComponentBundle, r'other must be a SplashComponentBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the SplashComponentBundle instance to a dictionary.

            :return: Dictionary representation of the SplashComponentBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
