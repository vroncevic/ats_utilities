# -*- coding: UTF-8 -*-

'''
Module
    base_bundle.py
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
    Defines component bundle dataclass for dependency grouping and validation.
    Encapsulates base components for minimization of constructor overhead.
'''

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.info.iinfo_manager import IInfoManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.context.context_bundle import ContextBundle
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


@dataclass(slots=True, frozen=True, kw_only=True)
class BaseBundle:
    '''
        Defines component bundle dataclass for dependency grouping and validation.
        Encapsulates base components for minimization of constructor overhead.

        It defines:

            :attributes:
                | info_file - Information file path for App/Tool/Script.
                | config_loader - Configuration loader (loads configuration).
                | info_manager - Information manager (info configuration).
                | options_parser - Options parser (argument parser).
                | splasher - Splasher for App/Tool/Script (shows logo).
                | generator - Generator (if App/Tool/Script has ability geenration).
                | use_generator - Enable/Disable generator usage.
                | context_bundle - Context bundle for dependency injection.
            :methods:
                | __post_init__ - Post-initialization hook for base components validation.
                | validate - Validates that essential components are set.
                | to_dict - Returns a dictionary representation of the BaseBundle.
    '''

    info_file: str
    config_loader: ILoader
    info_manager: IInfoManager
    options_parser: IOptionManager
    splasher: ISplasher
    generator: IGenerator | None
    use_generator: bool
    context_bundle: ContextBundle

    def __post_init__(self) -> None:
        '''
            Post-initialization hook for base components validation.

            :exceptions:
                | ATSValueError: Information file must be provided.
                | ATSValueError: Config loader must be provided.
                | ATSValueError: Info manager must be provided.
                | ATSValueError: Options parser must be provided.
                | ATSValueError: Splasher must be provided.
                | ATSValueError: Use generator must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Information file must be str.
                | ATSTypeError: Config loader must be IConfigLoadManager interface.
                | ATSTypeError: Info manager must be IInfoManager interface.
                | ATSTypeError: Options parser must be IOptionManager interface.
                | ATSTypeError: Splasher must be ISplasher interface.
                | ATSTypeError: Use generator must be bool.
                | ATSTypeError: Generator must be IGenerator interface or None.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates base bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Information file must be provided.
                | ATSValueError: Config loader must be provided.
                | ATSValueError: Info manager must be provided.
                | ATSValueError: Options parser must be provided.
                | ATSValueError: Splasher must be provided.
                | ATSValueError: Use generator must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Information file must be str.
                | ATSTypeError: Config loader must be IConfigLoadManager interface.
                | ATSTypeError: Info manager must be IInfoManager interface.
                | ATSTypeError: Options parser must be IOptionManager interface.
                | ATSTypeError: Splasher must be ISplasher interface.
                | ATSTypeError: Use generator must be bool.
                | ATSTypeError: Generator must be IGenerator interface or None.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        context: str = r'base_bundle::validate(...)'
        not_none(self.info_file, context, r'information file must be provided')
        not_none(self.config_loader, context, r'config loader must be provided')
        not_none(self.info_manager, context, r'info manager must be provided')
        not_none(self.options_parser, context, r'options parser must be provided')
        not_none(self.splasher, context, r'splasher must be provided')
        not_none(self.use_generator, context, r'use_generator must be provided')
        not_none(self.context_bundle, context, r'context bundle must be provided')
        istype(self.info_file, str, context, r'information file must be str')
        istype(self.config_loader, ILoader, context, r'config loader must be an ILoader interface')
        istype(self.info_manager, IInfoManager, context, r'info manager must be an IInfoManager interface')
        istype(self.options_parser, IOptionManager, context, r'options parser must be an IOptionManager interface')
        istype(self.splasher, ISplasher, context, r'splasher must be an ISplasher interface')
        istype(self.use_generator, bool, context, r'use generator flag must be a bool')
        istype(self.generator, (IGenerator, type(None)), context, r'generator must be an IGenerator interface or None')
        istype(self.context_bundle, ContextBundle, context, r'context bundle must be a ContextBundle instance')

    def to_dict(self) -> dict[str, Any]:
        '''
            Returns a dictionary representation of the BaseBundle.

            :return: Dictionary representation of the BaseBundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
