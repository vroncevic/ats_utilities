# -*- coding: UTF-8 -*-

'''
Module
    dep_validator.py
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
    Validator for splash dependencies.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.splash.setup.dependencies import SplashDependencies
from ats_utilities.splash.property.isplash_property import ISplashProperty
from ats_utilities.splash.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splash.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splash.progressbar.iprogress_bar import IProgressBar
from ats_utilities.utils.setup.idep_validator import IDependenciesValidator
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class SplashDependenciesValidator(IDependenciesValidator[SplashDependencies]):
    '''
        Validator for splash dependencies.

        It defines:

            :methods:
                | validate - Validates splash dependencies instance.
    '''

    @classmethod
    def validate(cls, dependencies: SplashDependencies) -> None:
        '''
            Validates splash dependencies instance.

            :param dependencies: Splash dependencies instance to be validated.
            :exceptions:
                | ATSValueError: Dependencies must be provided and have proper attributes.
                | ATSTypeError:  Dependencies must be an instance of Mapping and its attributes
                |                must be instances of their respective types.
        '''
        ctx: str = 'splash_dependencies_validator::validate(...)'

        not_none(dependencies, ctx, 'dependencies must be provided')
        istype(dependencies, Mapping, ctx, 'dependencies must be a Mapping')

        prop = dependencies.get('prop')
        not_none(prop, ctx, 'prop must be provided')
        istype(prop, Mapping, ctx, 'prop must be a Mapping')

        splash_property = dependencies.get('splash_property')
        not_none(splash_property, ctx, 'splash_property must be provided')
        istype(splash_property, ISplashProperty, ctx, 'splash_property must be an instance of ISplashProperty')

        property_validated = dependencies.get('property_validated')
        not_none(property_validated, ctx, 'property_validated must be provided')
        istype(property_validated, bool, ctx, 'property_validated must be a boolean')

        terminal_property = dependencies.get('terminal_property')
        not_none(terminal_property, ctx, 'terminal_property must be provided')
        istype(terminal_property, ITerminalProperties, ctx, 'terminal_property must be an instance of ITerminalProperties')

        ext = dependencies.get('ext')
        not_none(ext, ctx, 'ext must be provided')
        istype(ext, IExtInfrastructure, ctx, 'ext must be an instance of IExtInfrastructure')

        pb = dependencies.get('pb')
        not_none(pb, ctx, 'pb must be provided')
        istype(pb, IProgressBar, ctx, 'pb must be an instance of IProgressBar')

        context_bundle = dependencies.get('context_bundle')
        not_none(context_bundle, ctx, 'context bundle must be provided')
        istype(context_bundle, ContextBundle, ctx, 'context bundle must be an instance of ContextBundle')
