# -*- coding: UTF-8 -*-

'''
Module
    dependencies.py
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
    Base dependencies and options for base bundle creation.
'''

from __future__ import annotations

from typing import TypedDict, NotRequired

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.generation.imanager import IGeneratorManager

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class BaseDependencies(TypedDict):
    '''
        Base dependencies for base bundle creation.

        It defines:

            :attributes:
                | info_file: Information file path for App/Tool/Script.
                | config_loader: Configuration loader instance.
                | info_manager: Information manager instance.
                | options_parser: Options parser instance.
                | splasher: SplashManager instance.
                | generator: GeneratorManager instance or None.
                | use_generator: Enable/Disable generator usage flag.
                | context_bundle: Context bundle instance.
    '''
    info_file: str
    config_loader: ILoader
    info_manager: IInfoManager
    options_parser: IOptionManager
    splasher: ISplashManager
    generator: IGeneratorManager | None
    use_generator: bool
    context_bundle: ContextBundle


class BaseOptions(TypedDict):
    '''
        Base options for base bundle creation.

        It defines:

            :attributes:
                | info_file: Information file path for App/Tool/Script.
                | context_bundle: Context bundle instance.
                | use_generator: Enable/Disable generator usage flag.
    '''
    info_file: str
    context_bundle: ContextBundle
    use_generator: NotRequired[bool]
