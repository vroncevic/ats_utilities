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
    Defines component bundle dataclass for dependency grouping and management.
    Encapsulates base components to minimize constructor overhead.
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
        Defines component bundle dataclass for dependency grouping and management.
        Encapsulates base components to minimize constructor overhead.

        It defines:

            :attributes:
                | info_file - Information file path.
                | config_loader - Configuration loader.
                | info_manager - Information manager.
                | options_parser - Options parser.
                | splasher - Splasher.
                | generator - Generator.
                | use_generator - Enable/Disable generator usage.
                | context_bundle - Context bundle for dependency injection.
            :methods:
                | validate - Validates that essential components are set.
                | to_dict - Converts the BaseBundle instance to a dictionary.
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
            Post-initialization hook for automatic component creation.

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
        not_none(self.info_file, r'information file must be provided')
        not_none(self.config_loader, r'config loader must be provided')
        not_none(self.info_manager, r'info manager must be provided')
        not_none(self.options_parser, r'options parser must be provided')
        not_none(self.splasher, r'splasher must be provided')
        not_none(self.use_generator, r'use_generator must be provided')
        not_none(self.context_bundle, r'context bundle must be provided')
        istype(self.info_file, str, r'information file must be str')
        istype(self.config_loader, ILoader, r'config loader must be an ILoader interface')
        istype(self.info_manager, IInfoManager, r'info manager must be an IInfoManager interface')
        istype(self.options_parser, IOptionManager, r'options parser must be an IOptionManager interface')
        istype(self.splasher, ISplasher, r'splasher must be an ISplasher interface')
        istype(self.use_generator, bool, r'use generator flag must be a bool')
        istype(self.generator, (IGenerator, type(None)), r'generator must be IGenerator interface or None')
        istype(self.context_bundle, ContextBundle, r'context bundle must be a ContextBundle instance')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the BaseBundle instance to a dictionary.

            :return: Dictionary representation of the BaseBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
