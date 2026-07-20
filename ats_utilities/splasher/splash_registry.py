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
from ats_utilities.context.context_bundle import ContextBundle
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
                | create_splash_bundle_from_dict - Creates a SplashBundle from properties.
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
        prop: Mapping[str, Any] = params.get('prop')
        splash_property: ISplashProperty = params.get('splash_property')
        property_validated: bool = params.get('property_validated')
        terminal_property: ITerminalProperties = params.get('terminal_property')
        ext: IExtInfrastructure = params.get('ext')
        pb: IProgressBar = params.get('pb')
        context_bundle: ContextBundle = params.get('context_bundle')

        return SplashBundle(
            prop=prop,
            splash_property=splash_property,
            property_validated=property_validated,
            terminal_property=terminal_property,
            ext=ext,
            pb=pb,
            context_bundle=context_bundle
        )

    @classmethod
    def create_splash_bundle_from_dict(
        cls,
        prop: Mapping[str, Any],
        context_bundle: ContextBundle
    ) -> SplashBundle:
        '''
            Creates a SplashBundle from properties.

            :param prop: Properties.
            :type prop: <Mapping[str, Any]>
            :param context_bundle: Context bundle.
            :type context_bundle: <ContextBundle>
            :return: SplashBundle instance.
            :rtype: <SplashBundle>
            :exceptions:
                | ATSValueError: Context bundle must not be provided.
                | ATSTypeError: Context bundle must be of type ContextBundle.
        '''
        splash_property: ISplashProperty = SplashProperty(context_bundle)
        property_validated: bool = False

        if prop is not None:
            splash_property.splash_keys = prop
            property_validated = splash_property.validates()

        if prop.get(SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE, False):
            ext: IExtInfrastructure = GitHubInfrastructure(context_bundle)
        else:
            ext: IExtInfrastructure = ExtInfrastructure(context_bundle)

        terminal_property: ITerminalProperties = TerminalProperties(context_bundle)

        if property_validated and prop is not None:

            if prop.get('enabled', True):
                ext.infrastructure_property = prop

        size: tuple[Any, ...] = terminal_property.size()
        pb: IProgressBar = ProgressBar(int(size[1]) - int(int(size[1]) / 2))

        return SplashBundle(
            prop=prop if prop is not None else {},
            splash_property=splash_property,
            property_validated=property_validated,
            terminal_property=terminal_property,
            ext=ext,
            pb=pb,
            context_bundle=context_bundle
        )
