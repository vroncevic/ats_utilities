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

from typing import Any, TypedDict, NotRequired

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.info.iinfo_manager import IInfoManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.generator.igenerator import IGenerator

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
                | splasher: Splasher instance.
                | generator: Generator instance or None.
                | use_generator: Enable/Disable generator usage flag.
                | context_bundle: Context bundle instance.
    '''
    info_file: str
    config_loader: ILoader[ContextBundle]
    info_manager: IInfoManager[ContextBundle]
    options_parser: IOptionManager[ContextBundle]
    splasher: ISplasher[ContextBundle, Any]
    generator: IGenerator[ContextBundle] | None
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
