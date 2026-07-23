# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating splash bundle instance.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.utils.ifactory import IFactory
from ats_utilities.splasher.setup.bundle import SplashBundle
from ats_utilities.splasher.setup.dependencies import SplashOptions, SplashDependencies
from ats_utilities.splasher.setup.registry import SplashRegistry
from ats_utilities.splasher.property.isplash_property import ISplashProperty
from ats_utilities.splasher.property.splash_property import SplashProperty
from ats_utilities.splasher.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.terminal.terminal_properties import TerminalProperties
from ats_utilities.splasher.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.external.ext_infrastructure import ExtInfrastructure
from ats_utilities.splasher.external.github_infrastructure import GitHubInfrastructure
from ats_utilities.splasher.progressbar.iprogress_bar import IProgressBar
from ats_utilities.splasher.progressbar.progress_bar import ProgressBar
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class SplashFactory(IFactory[SplashBundle, SplashOptions]):
    '''
        Factory for creating splash bundle instance.

        It defines:

            :methods:
                | create_default_bundle - Creates a default splash bundle using configuration options.
                | create_splash_bundle_from_dict - Creates a default splash bundle using configuration options.
    '''

    @classmethod
    @override
    def create_default_bundle(cls, options: SplashOptions) -> SplashBundle:
        '''
            Creates a default splash bundle using configuration options.

            :param options: Creation options/parameters for the bundle.
            :type options: SplashOptions
            :return: Splash bundle instance.
            :rtype: SplashBundle
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a dictionary.
                | ATSValueError: Properties dictionary must be provided.
                | ATSTypeError: Properties dictionary must be a Mapping instance.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Splash property must be provided.
                | ATSValueError: Property validated flag must be provided.
                | ATSValueError: Terminal properties must be provided.
                | ATSValueError: External infrastructure must be provided.
                | ATSValueError: Progress bar must be provided.
                | ATSTypeError: Bundle must be an instance of SplashBundle.
                | ATSTypeError: Splash property must be an instance of ISplashProperty.
                | ATSTypeError: Property validated flag must be an instance of bool.
                | ATSTypeError: Terminal properties must be an instance of ITerminalProperties.
                | ATSTypeError: External infrastructure must be an instance of IExtInfrastructure.
                | ATSTypeError: Progress bar must be an instance of IProgressBar.
        '''
        ctx: str = r'splash_factory::create_default_bundle(...)'
        not_none(options, ctx, r'options must be provided')
        istype(options, dict, ctx, r'options must be a dictionary')

        prop: Mapping[str, Any] | None = options.get('prop')
        context_bundle: ContextBundle = options.get('context_bundle')

        if prop is not None:
            istype(prop, Mapping, ctx, r'properties dictionary must be a Mapping instance')
        not_none(context_bundle, ctx, r'context_bundle must be provided')
        istype(context_bundle, ContextBundle, ctx, r'context_bundle must be ContextBundle instance')

        splash_property: ISplashProperty = SplashProperty(context_bundle)
        property_validated: bool = False

        if prop is not None:
            splash_property.splash_keys = prop
            property_validated = splash_property.validates()

        if prop is not None and prop.get(SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE, False):
            ext: IExtInfrastructure = GitHubInfrastructure(context_bundle)
        else:
            ext: IExtInfrastructure = ExtInfrastructure(context_bundle)

        terminal_property: ITerminalProperties = TerminalProperties(context_bundle)

        if property_validated and prop is not None:
            if prop.get('enabled', True):
                ext.infrastructure_property = prop

        size: tuple[Any, ...] = terminal_property.size()
        pb: IProgressBar = ProgressBar(int(size[1]) - int(int(size[1]) / 2))

        return SplashRegistry.create_bundle(
            SplashDependencies(
                prop=prop if prop is not None else {},
                splash_property=splash_property,
                property_validated=property_validated,
                terminal_property=terminal_property,
                ext=ext,
                pb=pb,
                context_bundle=context_bundle
            )
        )

    @classmethod
    def create_splash_bundle_from_dict(
        cls,
        prop: Mapping[str, Any],
        context_bundle: ContextBundle
    ) -> SplashBundle:
        '''
            Creates a default splash bundle.
            Kept for backward compatibility.

            :param prop: Properties.
            :type prop: Mapping[str, Any]
            :param context_bundle: Context bundle.
            :type context_bundle: ContextBundle
            :return: Splash bundle instance.
            :rtype: SplashBundle
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a dictionary.
                | ATSValueError: Properties dictionary must be provided.
                | ATSTypeError: Properties dictionary must be a Mapping instance.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Splash property must be provided.
                | ATSValueError: Property validated flag must be provided.
                | ATSValueError: Terminal properties must be provided.
                | ATSValueError: External infrastructure must be provided.
                | ATSValueError: Progress bar must be provided.
                | ATSTypeError: Bundle must be an instance of SplashBundle.
                | ATSTypeError: Splash property must be an instance of ISplashProperty.
                | ATSTypeError: Property validated flag must be an instance of bool.
                | ATSTypeError: Terminal properties must be an instance of ITerminalProperties.
                | ATSTypeError: External infrastructure must be an instance of IExtInfrastructure.
                | ATSTypeError: Progress bar must be an instance of IProgressBar.
        '''
        return cls.create_default_bundle(
            SplashOptions(prop=prop, context_bundle=context_bundle)
        )
