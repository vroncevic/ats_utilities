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

from typing import override

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.info.iinfo_manager import IInfoManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.utils.ivalidator import IValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class BaseValidator(IValidator[BaseBundle]):
    '''
        Validator for base bundle instance.

        It defines:

            :methods:
                | validate - Validates base bundle instance.
    '''

    @classmethod
    @override
    def validate(cls, bundle: BaseBundle) -> None:
        '''
            Validates base bundle instance.

            :param bundle: Base bundle instance to be validated.
            :type bundle: BaseBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Information file must be provided.
                | ATSValueError: Config loader must be provided.
                | ATSValueError: Info manager must be provided.
                | ATSValueError: Options parser must be provided.
                | ATSValueError: Splasher must be provided.
                | ATSValueError: Use generator flag must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of BaseBundle.
                | ATSTypeError: Information file must be an instance of str.
                | ATSTypeError: Config loader must be an instance of ILoader.
                | ATSTypeError: Info manager must be an instance of IInfoManager.
                | ATSTypeError: Options parser must be an instance of IOptionManager.
                | ATSTypeError: Splasher must be an instance of ISplasher.
                | ATSTypeError: Use generator flag must be an instance of bool.
                | ATSTypeError: Generator must be an instance of IGenerator or None.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        ctx: str = r'base_validator::validate(...)'

        not_none(bundle, ctx, r'bundle must be provided')
        istype(bundle, BaseBundle, ctx, r'bundle must be an instance of BaseBundle')

        not_none(bundle.info_file, ctx, r'information file must be provided')
        not_none(bundle.config_loader, ctx, r'config loader must be provided')
        not_none(bundle.info_manager, ctx, r'info manager must be provided')
        not_none(bundle.options_parser, ctx, r'options parser must be provided')
        not_none(bundle.splasher, ctx, r'splasher must be provided')
        not_none(bundle.use_generator, ctx, r'use_generator must be provided')
        not_none(bundle.context_bundle, ctx, r'context bundle must be provided')

        istype(bundle.info_file, str, ctx, r'information file must be str')
        istype(bundle.config_loader, ILoader, ctx, r'config loader must be an ILoader interface')
        istype(bundle.info_manager, IInfoManager, ctx, r'info manager must be an IInfoManager interface')
        istype(bundle.options_parser, IOptionManager, ctx, r'options parser must be an IOptionManager interface')
        istype(bundle.splasher, ISplasher, ctx, r'splasher must be an ISplasher interface')
        istype(bundle.use_generator, bool, ctx, r'use generator flag must be a bool')
        istype(bundle.generator, (IGenerator, type(None)), ctx, r'generator must be an IGenerator interface or None')
        istype(bundle.context_bundle, ContextBundle, ctx, r'context bundle must be a ContextBundle instance')
