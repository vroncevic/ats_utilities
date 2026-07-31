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
    Validator for base bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.context.validator import ContextValidator
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.generation.imanager import IGeneratorManager
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


class BaseValidator:
    '''
        Validator for base bundle.

        It defines:

            :methods:
                | validate - Validates base bundle.
    '''

    @classmethod
    def validate(cls, bundle: BaseBundle) -> None:
        '''
            Validates base bundle.

            :param bundle: Base bundle to be validated.
            :exceptions:
                | ATSValueError: Base bundle must be provided and have proper values.
                | ATSTypeError:  Base bundle must be an instance of BaseBundle
                |                and its attributes must be instances of their
                |                respective interfaces and types.
        '''
        ctx: str = 'base_validator::validate(...)'
        msg_bundle_none: str = 'base bundle must be provided'
        msg_bundle_istype: str = 'base bundle must be an instance of BaseBundle'
        msg_info_manager_none: str = 'info manager must be provided'
        msg_info_manager_istype: str = 'info manager must be an IInfoManager'
        msg_option_manager_none: str = 'option manager must be provided'
        msg_option_manager_istype: str = 'option manager must be an IOptionManager'
        msg_splash_manager_none: str = 'splash manager must be provided'
        msg_splash_manager_istype: str = 'splash manager must be an ISplashManager'
        msg_generation_manager_istype: str = 'generation manager must be an IGeneratorManager or None'

        not_none(bundle, ctx, msg_bundle_none)
        istype(bundle, BaseBundle, ctx, msg_bundle_istype)

        ContextValidator.validate(bundle.context_bundle)

        not_none(bundle.info_manager, ctx, msg_info_manager_none)
        not_none(bundle.option_manager, ctx, msg_option_manager_none)
        not_none(bundle.splash_manager, ctx, msg_splash_manager_none)

        istype(bundle.info_manager, IInfoManager, ctx, msg_info_manager_istype)
        istype(bundle.option_manager, IOptionManager, ctx, msg_option_manager_istype)
        istype(bundle.splash_manager, ISplashManager, ctx, msg_splash_manager_istype)

        if bundle.generation_manager is not None:
            istype(bundle.generation_manager, IGeneratorManager, ctx, msg_generation_manager_istype)
