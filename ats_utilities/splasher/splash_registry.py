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
from typing import Any

from ats_utilities.splasher.splash_bundle import SplashBundle
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.splasher.property.splash_property import SplashProperty
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.splasher.terminal.terminal_properties import TerminalProperties
from ats_utilities.splasher.external.ext_infrastructure import ExtInfrastructure
from ats_utilities.splasher.external.github_infrastructure import GitHubInfrastructure
from ats_utilities.splasher.progressbar.progress_bar import ProgressBar

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class SplashRegistry:
    '''
        Encapsulates splash screen components for simplification of SplashBundle creation.

        It defines:

            :methods:
                | create_splash_bundle_from_dict - Creates a SplashBundle from properties.
    '''

    @classmethod
    def create_splash_bundle_from_dict(cls, prop: Mapping[str, Any], context_bundle: ContextBundle) -> SplashBundle:
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
        splash_property = SplashProperty(context_bundle)
        property_validated = False

        if prop is not None:
            splash_property.splash_keys = prop
            property_validated = splash_property.validates()

        terminal_property = TerminalProperties(context_bundle)
        github = GitHubInfrastructure(context_bundle)
        ext = ExtInfrastructure(context_bundle)

        if property_validated and prop is not None:
            is_enabled = bool(prop.get('enabled', True))

            if is_enabled:
                use_github = bool(prop.get(SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE, False))

                if use_github:
                    github.infrastructure_property = prop
                else:
                    ext.infrastructure_property = prop

        size: tuple[Any, ...] = terminal_property.size()
        pb = ProgressBar(int(size[1]) - int(int(size[1]) / 2))

        return SplashBundle(
            prop=prop if prop is not None else {},
            splash_property=splash_property,
            property_validated=property_validated,
            terminal_property=terminal_property,
            github=github,
            ext=ext,
            pb=pb,
            context_bundle=context_bundle
        )
