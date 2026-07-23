# -*- coding: UTF-8 -*-

'''
Module
    validator.py
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
    Validator for splash bundle instance.
'''

from __future__ import annotations

from typing import override
from collections.abc import Mapping

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.splasher.setup.bundle import SplashBundle
from ats_utilities.splasher.property.isplash_property import ISplashProperty
from ats_utilities.splasher.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.progressbar.iprogress_bar import IProgressBar
from ats_utilities.utils.ivalidator import IValidator
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


class SplashValidator(IValidator[SplashBundle]):
    '''
        Validator for splash bundle instance.

        It defines:

            :methods:
                | validate - Validates splash bundle instance.
    '''

    @classmethod
    @override
    def validate(cls, bundle: SplashBundle) -> None:
        '''
            Validates splash bundle instance.

            :param bundle: Splash bundle instance to be validated.
            :type bundle: SplashBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Properties dictionary must be provided.
                | ATSValueError: Splash property must be provided.
                | ATSValueError: Property validated flag must be provided.
                | ATSValueError: Terminal properties must be provided.
                | ATSValueError: External infrastructure must be provided.
                | ATSValueError: Progress bar must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of SplashBundle.
                | ATSTypeError: Properties dictionary must be an instance of Mapping.
                | ATSTypeError: Splash property must be an instance of ISplashProperty.
                | ATSTypeError: Property validated flag must be an instance of bool.
                | ATSTypeError: Terminal properties must be an instance of ITerminalProperties.
                | ATSTypeError: External infrastructure must be an instance of IExtInfrastructure.
                | ATSTypeError: Progress bar must be an instance of IProgressBar.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        ctx: str = r'splash_validator::validate(...)'

        not_none(bundle, ctx, r'bundle must be provided')
        istype(bundle, SplashBundle, ctx, r'bundle must be an instance of SplashBundle')

        not_none(bundle.prop, ctx, r'properties dictionary must be provided')
        not_none(bundle.splash_property, ctx, r'splash property must be provided')
        not_none(bundle.property_validated, ctx, r'property validated flag must be provided')
        not_none(bundle.terminal_property, ctx, r'terminal properties must be provided')
        not_none(bundle.ext, ctx, r'external infrastructure must be provided')
        not_none(bundle.pb, ctx, r'progress bar must be provided')
        not_none(bundle.context_bundle, ctx, r'context bundle must be provided')

        istype(bundle.prop, Mapping, ctx, r'properties dictionary must be a Mapping[str, Any] instance')
        istype(bundle.splash_property, ISplashProperty, ctx, r'splash property must be an ISplashProperty instance')
        istype(bundle.property_validated, bool, ctx, r'property validated flag must be an instance of bool')
        istype(bundle.terminal_property, ITerminalProperties, ctx, r'terminal properties must be an ITerminalProperties instance')
        istype(bundle.ext, IExtInfrastructure, ctx, r'external infrastructure must be an IExtInfrastructure instance')
        istype(bundle.pb, IProgressBar, ctx, r'progress bar must be an IProgressBar instance')
        istype(bundle.context_bundle, ContextBundle, ctx, r'context bundle must be a ContextBundle instance')
