# -*- coding: UTF-8 -*-

'''
Module
    component_bundle.py
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
from os.path import dirname, exists
from sys import stderr
from typing import Any

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.generator.component_bundle import GeneratorComponentBundle
from ats_utilities.config_io.loader.engine import Loader
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.config_io.config_io_bundle import ConfigIOBundle
from ats_utilities.generator.engine import Generator
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.info.component_bundle import InfoComponentBundle
from ats_utilities.info.engine import InfoManager
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.splasher.component_bundle import SplashComponentBundle
from ats_utilities.splasher.engine import Splasher
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.exceptions import ATSAttributeError, ATSRuntimeError, ATSTypeError, ATSValueError
from ats_utilities.factory_type import check_type
from ats_utilities.factory_value import require_not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, kw_only=True)
class BaseComponentBundle:
    '''
        Defines component bundle dataclass for dependency grouping and management.
        Encapsulates base components to minimize constructor overhead.

        It defines:

            :attributes:
                | info_file - Information file (default None).
                | config_loader - Configuration loader (default None).
                | info_manager - Information manager (default None).
                | options_parser - Options parser (default None).
                | splasher - Splasher (default None).
                | generator - Generator (default None).
                | use_generator - Enable/Disable generator usage (default False).
                | context_bundle - Context bundle for dependency injection (default None).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another BaseComponentBundle instance into this one.
                | to_dict - Converts the BaseComponentBundle instance to a dictionary.
    '''

    info_file: str | None = None
    config_loader: ILoader | None = None
    info_manager: IInfoManager | None = None
    options_parser: IOptionManager | None = None
    splasher: ISplasher | None = None
    generator: IGenerator | None = None
    use_generator: bool = False
    context_bundle: ContextBundle | None = None

    def __post_init__(self) -> None:
        '''
            Post-initialization hook for automatic component creation.

            :excpetions: None.
        '''
        if self.context_bundle is None:
            self.context_bundle = ContextBundle()

        if self.info_file is not None and exists(self.info_file):
            try:
                self._build_components()

            except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
                stderr.write(f'\x1b[31mBase {exc}\x1b[0m\n')

            except Exception as exc:
                stderr.write(f'\x1b[31mBase unexpected exception: {exc}\x1b[0m\n')

    def _build_components(self) -> None:
        '''
            Helper method to build all sub-components.

            :excpetions:
                | ATSTypeError - Component type is invalid.
        '''
        self.config_loader = make_component(
            self.config_loader, Loader,
            {
                'component_bundle': ConfigIOBundle(
                    file_path=self.info_file,
                    context_bundle=self.context_bundle
                )
            }
        )
        validate_component(self.config_loader, ILoader, r'config_loader must be an IConfigLoadManager instance')
        config_data = self.config_loader.load_configuration()

        log_file = config_data.get('ats_log_path') or config_data.get('ats_log_file')

        if log_file and hasattr(self.context_bundle.logger, 'set_log_file'):
            self.context_bundle.logger.set_log_file(log_file)

        self.info_manager = make_component(
            self.info_manager, InfoManager,
            {'component_bundle': InfoComponentBundle(context_bundle=self.context_bundle)}
        )
        validate_component(self.info_manager, IInfoManager, r'info_manager must be an IInfoManager instance')
        self.info_manager.set_info(config_data)

        logo_path = self.info_manager.logo
        self.info_manager.logo = f'{dirname(self.info_file)}/{logo_path}'

        self.splasher = make_component(
            self.splasher, Splasher,
            {
                'component_bundle': SplashComponentBundle(
                    prop=self.info_manager.get_info(), context_bundle=self.context_bundle
                )
            }
        )
        validate_component(self.splasher, ISplasher, r'splasher must be an ISplasher instance')

        self.options_parser = make_component(
            self.options_parser, OptionManager,
            {
                'component_bundle': OptionComponentBundle(
                    parameters=self.info_manager.get_info(),
                    context_bundle=self.context_bundle
                )
            }
        )
        validate_component(self.options_parser, IOptionManager, r'options_parser must be an IOptionManager instance')

        if self.use_generator:
            self.generator = make_component(
                self.generator, Generator,
                {'component_bundle': GeneratorComponentBundle(context_bundle=self.context_bundle)}
            )
            validate_component(self.generator, IGenerator, r'generator must be an IGenerator instance')

        if hasattr(self.context_bundle.logger, 'stop_buffering'):
            self.context_bundle.logger.stop_buffering()

    def validate(self, merge_op: bool = False) -> None:
        '''
            Validates that BaseComponentBundle is valid (can be called after merge).
            Performs validation of info_file, config_loader, info_manager, options_parser,
            splasher, generator.

            Info_file must be non-None and str.
            Config_loader must be non-None and IConfigLoadManager interface.
            Info_manager must be non-None and IInfoManager interface.
            Options_parser must be non-None and IOptionManager interface.
            Splasher must be non-None and ISplasher interface.
            Generator must be non-None and IGenerator interface.

            :param merge_op: Whether the validation is performed after a merge operation.
                If True, then all attributes are validated.
                If False, then only info_file is validated.
            :type merge_op: <bool>

            :exceptions:
                | ATSValueError: Information file must be provided.
                | ATSTypeError: Information file must be str.
                | ATSValueError: Config_loader must be provided.
                | ATSValueError: Info_manager must be provided.
                | ATSValueError: Options_parser must be provided.
                | ATSValueError: Splasher must be provided.
                | ATSValueError: Generator must be provided.
                | ATSTypeError: Config_loader must be IConfigLoadManager interface.
                | ATSTypeError: Info_manager must be IInfoManager interface.
                | ATSTypeError: Options_parser must be IOptionManager interface.
                | ATSTypeError: Splasher must be ISplasher interface.
                | ATSTypeError: Generator must be IGenerator interface.
        '''
        require_not_none(self.info_file, r'information file must be provided')
        check_type(self.info_file, str, r'information file must be str')

        if merge_op:
            require_not_none(self.config_loader, r'config_loader must be provided')
            require_not_none(self.info_manager, r'info_manager must be provided')
            require_not_none(self.options_parser, r'options_parser must be provided')
            require_not_none(self.splasher, r'splasher must be provided')
            check_type(self.config_loader, ILoader, r'config_loader must be an ILoader interface')
            check_type(self.info_manager, IInfoManager, r'info_manager must be an IInfoManager interface')
            check_type(self.options_parser, IOptionManager, r'options_parser must be an IOptionManager interface')
            check_type(self.splasher, ISplasher, r'splasher must be an ISplasher interface')

            if self.use_generator:
                require_not_none(self.generator, r'generator must be provided')
                check_type(self.generator, IGenerator, r'generator must be IGenerator interface')

    def merge(self, other: BaseComponentBundle) -> None:
        '''
            Merges non-None values from another BaseComponentBundle instance into this one.

            :param other: Another BaseComponentBundle instance to merge into this one.
            :type other: <BaseComponentBundle>
            :exceptions:
                | ATSValueError: Other BaseComponentBundle must be provided.
                | ATSTypeError: Other must be BaseComponentBundle instance.
        '''
        require_not_none(other, r'other BaseComponentBundle must be provided')
        check_type(other, BaseComponentBundle, r'other must be BaseComponentBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        if self.info_file is not None and exists(self.info_file):
            try:
                self._build_components()

            except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
                stderr.write(f'\x1b[31mBase {exc}\x1b[0m\n')

            except Exception as exc:
                stderr.write(f'\x1b[31mBase unexpected exception: {exc}\x1b[0m\n')

        self.validate(merge_op=True)

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the BaseComponentBundle instance to a dictionary.

            :return: Dictionary representation of the BaseComponentBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
