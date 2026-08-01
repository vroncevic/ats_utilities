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
    Factory for creating base bundle.
'''

from __future__ import annotations

from os.path import dirname

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseOptions
from ats_utilities.base.setup.keys import BaseKeys
from ats_utilities.base.setup.opt_validator import BaseOptionsValidator
from ats_utilities.base.setup.dependencies import BaseDependencies
from ats_utilities.base.setup.registry import BaseRegistry
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.loader.engine import Loader
from ats_utilities.config_io.setup.factory import ConfigIOFactory
from ats_utilities.config_io.setup.options import ConfigIOOptions
from ats_utilities.info.engine import InfoManager
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.info.setup.factory import InfoFactory
from ats_utilities.info.setup.options import InfoOptions
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.option.setup.factory import OptionFactory
from ats_utilities.option.setup.options import OptionOptions
from ats_utilities.splash.engine import SplashManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.splash.setup.factory import SplashFactory
from ats_utilities.splash.setup.options import SplashOptions
from ats_utilities.generation.engine import GeneratorManager
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.generation.setup.factory import GeneratorFactory
from ats_utilities.generation.setup.options import GeneratorOptions
from ats_utilities.utils.dicts import get_first_available

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class BaseFactory:
    '''
        Factory for creating base bundle.

        It defines:

            :methods:
                | create_bundle - Creates a base bundle using configuration options.
    '''

    @classmethod
    def create_bundle(cls, options: BaseOptions) -> BaseBundle:
        '''
            Creates a base bundle using configuration options.

            :param options: The creation options/parameters for the bundle.
            :return: The base bundle.
            :exceptions:
                | ATSValueError: The base options must be provided and have proper values.
                | ATSTypeError:  The base options must be an instance of Mapping and its attributes
                |                must be instances of their respective types.
        '''
        BaseOptionsValidator.validate(options)

        info_file: str = options.get(BaseKeys.OPTION_INFO_FILE)
        use_generator: bool = options.get(BaseKeys.OPTION_USE_GENERATOR)
        context_bundle: ContextBundle = options.get(BaseKeys.OPTION_CONTEXT_BUNDLE)

        config_loader: Loader = Loader(
            own=ConfigIOFactory.create_bundle(
                options=ConfigIOOptions(file_path=info_file, scheme={}, context_bundle=context_bundle)
            )
        )
        config_data: dict[str, object] = config_loader.load_configuration()
        log_file: str = get_first_available(config_data, ('ats_log_path', 'ats_log_file'))

        if log_file and hasattr(context_bundle.logger, 'set_log_file'):
            context_bundle.logger.set_log_file(log_file)

        info_manager: IInfoManager = InfoManager(
            own=InfoFactory.create_bundle(
                options=InfoOptions(info=config_data, context_bundle=context_bundle)
            )
        )
        logo_path: str = info_manager.logo
        info_manager.logo = f'{dirname(info_file)}/{logo_path}'

        splash_manager: ISplashManager = SplashManager(
            own=SplashFactory.create_bundle(
                options=SplashOptions(prop=info_manager.get_info(), context_bundle=context_bundle)
            )
        )

        option_manager: IOptionManager = OptionManager(
            own=OptionFactory.create_bundle(
                options=OptionOptions(parameters=info_manager.get_info(), context_bundle=context_bundle)
            )
        )

        generation_manager: IGeneratorManager | None = GeneratorManager(
            own=GeneratorFactory.create_bundle(
                options=GeneratorOptions(context_bundle=context_bundle)
            )
        ) if use_generator else None

        if hasattr(context_bundle.logger, 'stop_buffering'):
            context_bundle.logger.stop_buffering()

        return BaseRegistry.create_bundle(
            BaseDependencies(
                context_bundle=context_bundle,
                info_manager=info_manager,
                option_manager=option_manager,
                splash_manager=splash_manager,
                generation_manager=generation_manager
            )
        )
