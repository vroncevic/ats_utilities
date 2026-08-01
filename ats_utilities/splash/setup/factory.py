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
    A factory for creating an splash bundle instance.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.splash.setup.bundle import SplashBundle
from ats_utilities.splash.setup.options import SplashOptions
from ats_utilities.splash.setup.opt_validator import SplashOptionsValidator
from ats_utilities.splash.setup.dependencies import SplashDependencies
from ats_utilities.splash.setup.registry import SplashRegistry
from ats_utilities.splash.property.isplash_property import ISplashProperty
from ats_utilities.splash.property.splash_property import SplashProperty
from ats_utilities.splash.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splash.terminal.terminal_properties import TerminalProperties
from ats_utilities.splash.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splash.external.ext_infrastructure import ExtInfrastructure
from ats_utilities.splash.external.github_infrastructure import GitHubInfrastructure
from ats_utilities.splash.progressbar.iprogress_bar import IProgressBar
from ats_utilities.splash.progressbar.progress_bar import ProgressBar
from ats_utilities.splash.setup.keys import SplashKeys
from ats_utilities.context.bundle import ContextBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class SplashFactory:
    '''
        A factory for creating an splash bundle instance.

        It defines:

            :methods:
                | create_bundle - Creates a splash bundle using configuration options.
                | create_splash_bundle_from_dict - Creates a default splash bundle using configuration options.
    '''

    @classmethod
    def create_bundle(cls, options: SplashOptions) -> SplashBundle:
        '''
            Creates a splash bundle using configuration options.

            :param options: The creation options/parameters for the bundle.
            :return: The splash bundle instance.
            :exceptions:
                | ATSValueError: Splash options must be provided and have proper values.
                | ATSTypeError:  Splash options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        SplashOptionsValidator.validate(options)

        prop: Mapping[str, object] = options.get(SplashKeys.PROP)
        context_bundle: ContextBundle = options.get(SplashKeys.CONTEXT_BUNDLE)

        splash_property: ISplashProperty = SplashProperty(context_bundle)
        splash_property.settings = prop

        if splash_property.settings.get(SplashProperty.GITHUB_SETTING):
            ext: IExtInfrastructure = GitHubInfrastructure(context_bundle)
        else:
            ext: IExtInfrastructure = ExtInfrastructure(context_bundle)

        ext.infrastructure_property = splash_property.settings
        terminal_property: ITerminalProperties = TerminalProperties(context_bundle)
        size: tuple[object, ...] = terminal_property.size()
        pb: IProgressBar = ProgressBar(int(size[1]) - int(int(size[1]) / 2))

        return SplashRegistry.create_bundle(
            dependencies=SplashDependencies(
                splash_property=splash_property,
                terminal_property=terminal_property,
                ext=ext,
                pb=pb,
                context_bundle=context_bundle
            )
        )
