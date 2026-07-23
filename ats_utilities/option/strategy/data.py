# -*- coding: UTF-8 -*-

'''
Module
    data.py
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
    StrategyData class.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.option.parser.iarg_parser import IArgParser
from ats_utilities.option.parser.engine import ArgParser
from ats_utilities.utils.reflection import instance_to_dict

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class StrategyData:
    '''
        Encapsulates core strategy components for StrategyData.

        It defines:

            :attributes:
                | parameters - Configuration parameters.
                | context_bundle - Context bundle for strategy.
                | parser_class - Injected parser class type.
            :methods:
                | to_dict - Converts StrategyData instance to dictionary.
    '''

    parameters: Mapping[str, str]
    context_bundle: ContextBundle
    parser_class: type[IArgParser] = ArgParser

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts StrategyData instance to dictionary.

            :return: Dictionary representation of StrategyData.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return instance_to_dict(self)
