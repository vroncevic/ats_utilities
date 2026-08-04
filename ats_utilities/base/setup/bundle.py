# -*- coding: UTF-8 -*-

'''
Module
    bundle.py
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
    Encapsulates base runtime components for simplification of base bundle.
'''

from __future__ import annotations

from dataclasses import dataclass

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.utils.reflection import instance_to_dict

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class BaseBundle:
    '''
        Encapsulates base runtime components for simplification of base bundle.

        It defines:

            :attributes:
                | context_bundle - The context bundle for base engine.
                | info_manager - The information manager for base engine.
                | option_manager - The option manager for base engine.
                | splash_manager - The splash manager for base engine.
                | generation_manager - The generation manager for base engine.
            :methods:
                | to_dict - Converts the base bundle to a dictionary.
    '''

    context_bundle: ContextBundle
    info_manager: IInfoManager
    option_manager: IOptionManager
    splash_manager: ISplashManager
    generation_manager: IGeneratorManager | None

    def to_dict(self) -> dict[str, object]:
        '''
            Converts the base bundle to a dictionary.

            :return: The dictionary representation of the base bundle.
            :exceptions:
                | ATSValueError: The instance must be provided.
                | ATSValueError: The instance must be a dataclass.
        '''
        return instance_to_dict(self)
