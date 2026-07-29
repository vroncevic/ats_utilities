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
    Validator for base bundle instance.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.generation.imanager import IGeneratorManager
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


class BaseValidator:
    '''
        Validator for base bundle instance.

        It defines:

            :methods:
                | validate - Validates base bundle instance.
    '''

    @classmethod
    def validate(cls, bundle: BaseBundle) -> None:
        '''
            Validates base bundle instance.

            :param bundle: Base bundle instance to be validated.
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Information file must be provided.
                | ATSValueError: Config loader must be provided.
                | ATSValueError: Info manager must be provided.
                | ATSValueError: Options parser must be provided.
                | ATSValueError: SplashManager must be provided.
                | ATSValueError: Use generator flag must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of BaseBundle.
                | ATSTypeError: Information file must be an instance of str.
                | ATSTypeError: Config loader must be an instance of ILoader.
                | ATSTypeError: Info manager must be an instance of IInfoManager.
                | ATSTypeError: Options parser must be an instance of IOptionManager.
                | ATSTypeError: SplashManager must be an instance of ISplashManager.
                | ATSTypeError: Use generator flag must be an instance of bool.
                | ATSTypeError: GeneratorManager must be an instance of IGeneratorManager or None.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        ctx: str = 'base_validator::validate(...)'

        not_none(bundle, ctx, 'bundle must be provided')
        istype(bundle, BaseBundle, ctx, 'bundle must be an instance of BaseBundle')

        not_none(bundle.info_file, ctx, 'information file must be provided')
        not_none(bundle.config_loader, ctx, 'config loader must be provided')
        not_none(bundle.info_manager, ctx, 'info manager must be provided')
        not_none(bundle.options_parser, ctx, 'options parser must be provided')
        not_none(bundle.splasher, ctx, 'splasher must be provided')
        not_none(bundle.use_generator, ctx, 'use_generator must be provided')
        not_none(bundle.context_bundle, ctx, 'context bundle must be provided')

        istype(bundle.info_file, str, ctx, 'information file must be str')
        istype(bundle.config_loader, ILoader, ctx, 'config loader must be an ILoader interface')
        istype(bundle.info_manager, IInfoManager, ctx, 'info manager must be an IInfoManager interface')
        istype(bundle.options_parser, IOptionManager, ctx, 'options parser must be an IOptionManager interface')
        istype(bundle.splasher, ISplashManager, ctx, 'splasher must be an ISplashManager interface')
        istype(bundle.use_generator, bool, ctx, 'use generator flag must be a bool')
        istype(bundle.generator, (IGeneratorManager, type(None)), ctx, 'generator must be an IGeneratorManager interface or None')
        istype(bundle.context_bundle, ContextBundle, ctx, 'context bundle must be a ContextBundle instance')
