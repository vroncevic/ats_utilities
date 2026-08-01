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
    A validator for the splash bundle instance.
'''

from __future__ import annotations

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
from ats_utilities.splash.setup.bundle import SplashBundle
from ats_utilities.splash.property.isplash_property import ISplashProperty
from ats_utilities.splash.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splash.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splash.progressbar.iprogress_bar import IProgressBar
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none
from ats_utilities.utils.files import check_file_exists

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class SplashValidator:
    '''
        A validator for the splash bundle instance.

        It defines:

            :methods:
                | validate - Validates the splash bundle instance.
    '''

    @classmethod
    def validate(cls, bundle: SplashBundle) -> None:
        '''
            Validates the splash bundle instance.

            :param bundle: The splash bundle instance to be validated.
            :exceptions:
                | ATSValueError: Option bundle must be provided and have proper values.
                | ATSTypeError:  Option bundle must be an instance of OptionBundle and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'splash_validator::validate(...)'
        msg_bundle_none: str = 'bundle must be provided'
        msg_bundle_type: str = 'bundle must be an instance of SplashBundle'
        msg_splash_property_none: str = 'splash property must be provided'
        msg_splash_property_type: str = 'splash property must be an ISplashProperty instance'
        msg_terminal_property_none: str = 'terminal properties must be provided'
        msg_terminal_property_type: str = 'terminal properties must be an ITerminalProperties instance'
        msg_ext_none: str = 'external infrastructure must be provided'
        msg_ext_type: str = 'external infrastructure must be an IExtInfrastructure instance'
        msg_pb_none: str = 'progress bar must be provided'
        msg_pb_type: str = 'progress bar must be an IProgressBar instance'
        msg_context_bundle_none: str = 'context bundle must be provided'
        msg_context_bundle_type: str = 'context bundle must be a ContextBundle instance'
        msg_logo_path: str = 'the App/Tool/Script logo file path not correct'

        not_none(bundle, ctx, msg_bundle_none)
        istype(bundle, SplashBundle, ctx, msg_bundle_type)

        not_none(bundle.splash_property, ctx, msg_splash_property_none)
        not_none(bundle.terminal_property, ctx, msg_terminal_property_none)
        not_none(bundle.ext, ctx, msg_ext_none)
        not_none(bundle.pb, ctx, msg_pb_none)
        not_none(bundle.context_bundle, ctx, msg_context_bundle_none)

        istype(bundle.splash_property, ISplashProperty, ctx, msg_splash_property_type)
        istype(bundle.terminal_property, ITerminalProperties, ctx, msg_terminal_property_type)
        istype(bundle.ext, IExtInfrastructure, ctx, msg_ext_type)
        istype(bundle.pb, IProgressBar, ctx, msg_pb_type)
        istype(bundle.context_bundle, ContextBundle, ctx, msg_context_bundle_type)

        ContextValidator.validate(bundle.context_bundle)

        if bundle.splash_property.is_settings_enabled():
            check_file_exists(bundle.splash_property.get_logo(), ctx, msg_logo_path)
