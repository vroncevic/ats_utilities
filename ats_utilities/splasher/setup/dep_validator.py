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
from typing import override

from ats_utilities.splasher.setup.dependencies import SplashDependencies
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.splasher.property.isplash_property import ISplashProperty
from ats_utilities.splasher.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.progressbar.iprogress_bar import IProgressBar
from ats_utilities.utils.setup.idep_validator import IDependenciesValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class SplashDependenciesValidator(IDependenciesValidator[SplashDependencies]):
    '''
        Validator for splash dependencies.

        It defines:

            :methods:
                | validate - Validates splash dependencies instance.
    '''

    @classmethod
    @override
    def validate(cls, dependencies: SplashDependencies) -> None:
        '''
            Validates splash dependencies instance.

            :param dependencies: Splash dependencies instance to be validated.
            :type dependencies: SplashDependencies
            :exceptions:
                | ATSValueError: Dependencies must be provided.
                | ATSTypeError: Dependencies must be a Mapping.
                | ATSTypeError: Properties dictionary must be a Mapping.
                | ATSTypeError: Splash property must be an instance of ISplashProperty.
                | ATSTypeError: Property validated flag must be a boolean.
                | ATSTypeError: Terminal properties must be an instance of ITerminalProperties.
                | ATSTypeError: External infrastructure must be an instance of IExtInfrastructure.
                | ATSTypeError: Progress bar must be an instance of IProgressBar.
                | ATSTypeError: Context bundle must be a ContextBundle.
        '''
        ctx: str = r'splash_dependencies_validator::validate(...)'

        not_none(dependencies, ctx, r'dependencies must be provided')
        istype(dependencies, Mapping, ctx, r'dependencies must be a Mapping')

        prop = dependencies.get('prop')
        not_none(prop, ctx, r'prop must be provided')
        istype(prop, Mapping, ctx, r'prop must be a Mapping')

        splash_property = dependencies.get('splash_property')
        not_none(splash_property, ctx, r'splash_property must be provided')
        istype(splash_property, ISplashProperty, ctx, r'splash_property must be an instance of ISplashProperty')

        property_validated = dependencies.get('property_validated')
        not_none(property_validated, ctx, r'property_validated must be provided')
        istype(property_validated, bool, ctx, r'property_validated must be a boolean')

        terminal_property = dependencies.get('terminal_property')
        not_none(terminal_property, ctx, r'terminal_property must be provided')
        istype(terminal_property, ITerminalProperties, ctx, r'terminal_property must be an instance of ITerminalProperties')

        ext = dependencies.get('ext')
        not_none(ext, ctx, r'ext must be provided')
        istype(ext, IExtInfrastructure, ctx, r'ext must be an instance of IExtInfrastructure')

        pb = dependencies.get('pb')
        not_none(pb, ctx, r'pb must be provided')
        istype(pb, IProgressBar, ctx, r'pb must be an instance of IProgressBar')

        context_bundle = dependencies.get('context_bundle')
        not_none(context_bundle, ctx, r'context bundle must be provided')
        istype(context_bundle, ContextBundle, ctx, r'context bundle must be an instance of ContextBundle')
