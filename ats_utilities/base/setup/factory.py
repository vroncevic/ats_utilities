# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating base bundle instance.
'''

from __future__ import annotations

from os.path import dirname

from ats_utilities.utils.setup.ifactory import IFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.dependencies import BaseOptions, BaseDependencies
from ats_utilities.base.setup.registry import BaseRegistry
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.loader.engine import Loader
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.info.engine import InfoManager
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.engine import SplashManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.generation.engine import GeneratorManager
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.config_io.setup.registry import ConfigIORegistry
from ats_utilities.info.setup.factory import InfoFactory
from ats_utilities.option.setup.factory import OptionFactory
from ats_utilities.splash.setup.factory import SplashFactory
from ats_utilities.generation.setup.factory import GeneratorFactory
from ats_utilities.utils.dicts import get_first_available
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class BaseFactory(IFactory[BaseBundle, BaseOptions]):
    '''
        Factory for creating base bundle instance.

        It defines:

            :methods:
                | create_default_bundle - Creates a default base bundle using configuration options.
                | create_default_base_bundle - Creates a default base bundle.
    '''

    @classmethod
    def create_default_bundle(cls, options: BaseOptions) -> BaseBundle:
        '''
            Creates a default base bundle using configuration options.

            :param options: Creation options/parameters for the bundle.
            :return: Base bundle instance.
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a dictionary.
                | ATSValueError: Information file must be provided.
                | ATSTypeError: Information file must be a string.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Use generator must be a boolean.
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Config loader must be provided.
                | ATSValueError: Info manager must be provided.
                | ATSValueError: Options parser must be provided.
                | ATSValueError: SplashManager must be provided.
                | ATSValueError: Use generator flag must be provided.
                | ATSTypeError: Bundle must be an instance of BaseBundle.
                | ATSTypeError: Config loader must be an instance of ILoader.
                | ATSTypeError: Info manager must be an instance of IInfoManager.
                | ATSTypeError: Options parser must be an instance of IOptionManager.
                | ATSTypeError: SplashManager must be an instance of ISplashManager.
                | ATSTypeError: Use generator flag must be an instance of bool.
                | ATSTypeError: GeneratorManager must be an instance of IGeneratorManager or None.
        '''
        ctx: str = 'base_factory::create_default_bundle(...)'
        not_none(options, ctx, 'options must be provided')
        istype(options, dict, ctx, 'options must be a dictionary')

        info_file: str = options.get('info_file')
        context_bundle: ContextBundle = options.get('context_bundle')
        use_generator: bool = options.get('use_generator', False)

        not_none(info_file, ctx, 'info file must be provided')
        not_none(context_bundle, ctx, 'context bundle must be provided')
        istype(info_file, str, ctx, 'info file must be a string')
        istype(context_bundle, ContextBundle, ctx, 'context bundle must be a ContextBundle instance')
        istype(use_generator, bool, ctx, 'use generator must be a boolean')

        config_loader: ILoader[ContextBundle] = Loader(
            own=ConfigIORegistry.create_config_io_bundle_by_file_path_and_scheme(
                file_path=info_file,
                scheme={},
                context_bundle=context_bundle
            )
        )
        config_data: dict[str, object] = config_loader.load_configuration()
        log_file: str = get_first_available(config_data, ('ats_log_path', 'ats_log_file'))

        if log_file and hasattr(context_bundle.logger, 'set_log_file'):
            context_bundle.logger.set_log_file(log_file)

        info_manager: IInfoManager[ContextBundle] = InfoManager(
            own=InfoFactory.create_info_bundle_from_dict(
                info=config_data,
                context_bundle=context_bundle
            )
        )
        logo_path: str = info_manager.logo
        info_manager.logo = f'{dirname(info_file)}/{logo_path}'

        splasher: ISplashManager[ContextBundle, object] = SplashManager(
            own=SplashFactory.create_splash_bundle_from_dict(
                prop=info_manager.get_info(),
                context_bundle=context_bundle
            )
        )
        options_parser: IOptionManager[ContextBundle] = OptionManager(
            own=OptionFactory.create_bundle({
                'parameters': info_manager.get_info(),
                'context_bundle': context_bundle
            })
        )
        generator: IGeneratorManager[ContextBundle] | None = GeneratorManager(
            own=GeneratorFactory.create_default_generator_bundle(
                context_bundle=context_bundle
            )
        ) if use_generator else None

        if hasattr(context_bundle.logger, 'stop_buffering'):
            context_bundle.logger.stop_buffering()

        return BaseRegistry.create_bundle(
            BaseDependencies(
                info_file=info_file,
                config_loader=config_loader,
                info_manager=info_manager,
                options_parser=options_parser,
                splasher=splasher,
                generator=generator,
                use_generator=use_generator,
                context_bundle=context_bundle
            )
        )

    @classmethod
    def create_default_base_bundle(
        cls,
        info_file: str,
        context_bundle: ContextBundle,
        use_generator: bool = False
    ) -> BaseBundle:
        '''
            Creates a default base bundle.
            Kept for backward compatibility.

            :param info_file: Path to the info file.
            :param context_bundle: ContextBundle instance.
            :param use_generator: Whether to use the generator (default False).
            :return: Default base bundle instance.
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a dictionary.
                | ATSValueError: Information file must be provided.
                | ATSTypeError: Information file must be a string.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Use generator must be a boolean.
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Config loader must be provided.
                | ATSValueError: Info manager must be provided.
                | ATSValueError: Options parser must be provided.
                | ATSValueError: SplashManager must be provided.
                | ATSValueError: Use generator flag must be provided.
                | ATSTypeError: Bundle must be an instance of BaseBundle.
                | ATSTypeError: Config loader must be an instance of ILoader.
                | ATSTypeError: Info manager must be an instance of IInfoManager.
                | ATSTypeError: Options parser must be an instance of IOptionManager.
                | ATSTypeError: SplashManager must be an instance of ISplashManager.
                | ATSTypeError: Use generator flag must be an instance of bool.
                | ATSTypeError: GeneratorManager must be an instance of IGeneratorManager or None.
        '''
        return cls.create_default_bundle(
            BaseOptions(
                info_file=info_file,
                context_bundle=context_bundle,
                use_generator=use_generator
            )
        )
