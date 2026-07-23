# -*- coding: UTF-8 -*-

'''
Module
    base_factory.py
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
    Factory for creating BaseBundle components.
'''

from __future__ import annotations

from os.path import dirname
from typing import Any

from ats_utilities.base.base_bundle import BaseBundle
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.loader.engine import Loader
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.info.engine import InfoManager
from ats_utilities.info.iinfo_manager import IInfoManager
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.splasher.engine import Splasher
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.generator.engine import Generator
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.config_io.config_io_registry import ConfigIORegistry
from ats_utilities.info.setup.factory import InfoFactory
from ats_utilities.option.setup.factory import OptionFactory
from ats_utilities.splasher.splash_factory import SplashFactory
from ats_utilities.generator.generator_factory import GeneratorFactory
from ats_utilities.utils.dicts import get_first_available
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class BaseFactory:
    '''
        Factory for creating BaseBundle components.
    '''

    @classmethod
    def create_default_base_bundle(
        cls,
        info_file: str,
        context_bundle: ContextBundle,
        use_generator: bool = False
    ) -> BaseBundle:
        '''
            Creates a default BaseBundle with pre-configured components.

            :param info_file: Path to the info file.
            :type info_file: <str>
            :param context_bundle: ContextBundle instance.
            :type context_bundle: <ContextBundle>
            :param use_generator: Whether to use the generator (default False).
            :type use_generator: <bool>
            :return: Default BaseBundle instance.
            :rtype: <BaseBundle>
            :exceptions:
                | ATSValueError: Info file must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Info file must be a string.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Use generator must be a boolean.
        '''
        context: str = r'base_factory::create_default_base_bundle(...)'
        not_none(info_file, context, r'info file must be provided')
        not_none(context_bundle, context, r'context bundle must be provided')
        istype(info_file, str, context, r'info file must be a string')
        istype(context_bundle, ContextBundle, context, r'context bundle must be a ContextBundle instance')
        istype(use_generator, bool, context, r'use generator must be a boolean')

        config_loader: ILoader = Loader(
            own=ConfigIORegistry.create_config_io_bundle_by_file_path_and_scheme(
                file_path=info_file,
                scheme={},
                context_bundle=context_bundle
            )
        )
        config_data: dict[str, Any] = config_loader.load_configuration()
        log_file: str = get_first_available(config_data, ('ats_log_path', 'ats_log_file'))

        if log_file and hasattr(context_bundle.logger, 'set_log_file'):
            context_bundle.logger.set_log_file(log_file)

        info_manager: IInfoManager = InfoManager(
            own=InfoFactory.create_info_bundle_from_dict(
                info=config_data,
                context_bundle=context_bundle
            )
        )
        logo_path: str = info_manager.logo
        info_manager.logo = f'{dirname(info_file)}/{logo_path}'

        splasher: ISplasher = Splasher(
            own=SplashFactory.create_splash_bundle_from_dict(
                prop=info_manager.get_info(),
                context_bundle=context_bundle
            )
        )
        options_parser: IOptionManager = OptionManager(
            own=OptionFactory.create_option_bundle_from_dict(
                parameters=info_manager.get_info(),
                context_bundle=context_bundle
            )
        )
        generator: IGenerator | None = Generator(
            own=GeneratorFactory.create_default_generator_bundle(
                context_bundle=context_bundle
            )
        ) if use_generator else None

        if hasattr(context_bundle.logger, 'stop_buffering'):
            context_bundle.logger.stop_buffering()

        return BaseBundle(
            info_file=info_file,
            config_loader=config_loader,
            info_manager=info_manager,
            options_parser=options_parser,
            splasher=splasher,
            generator=generator,
            use_generator=use_generator,
            context_bundle=context_bundle
        )
