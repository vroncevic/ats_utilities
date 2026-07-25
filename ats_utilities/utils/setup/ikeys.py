# -*- coding: UTF-8 -*-

'''
Module
    ikeys.py
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
    Abstract interface for keys used in setup process.
    Defines standard attribute-to-interface mapping behavior across all setup keys.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from types import MappingProxyType

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IKeys[AttributeType, InterfaceType](ABC):
    '''
        Abstract interface for keys used in setup process.
        Defines standard attribute-to-interface mapping behavior across all setup keys.

        :methods:
            | get_attr_to_interface - Returns mapping of bundle component attributes to their expected interfaces.
            | get_option_to_type - Returns mapping of option attributes to their expected types.
    '''

    @classmethod
    @abstractmethod
    def get_attr_to_interface(cls) -> MappingProxyType[AttributeType, InterfaceType]:
        '''
            Returns mapping of bundle component attributes to their expected interfaces.

            :return: Mapping of bundle component attributes to their expected interfaces.
            :exceptions: None.
        '''
        pass

    @classmethod
    @abstractmethod
    def get_option_to_type(cls) -> MappingProxyType[AttributeType, InterfaceType]:
        '''
            Returns mapping of option attributes to their expected types.

            :return: Mapping of option attributes to their expected types.
            :exceptions: None.
        '''
        pass
