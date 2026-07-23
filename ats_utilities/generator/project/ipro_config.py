# -*- coding: UTF-8 -*-

'''
Module
    ipro_config.py
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
    Defines abstract class IProConfig with method(s).
    Interface for the project configuration mechanism.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import Any

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IProConfig(ABC):
    '''
        Defines abstract class IProConfig with method(s).
        Interface for the project configuration mechanism.

        It defines:

            :methods:
                | config - Property methods for set/get operations.
                | not_none - Checks if project configuration is not None.
                | __str__ - Returns the ATS project configuration as string representation.
    '''

    @property
    @abstractmethod
    def config(self) -> Mapping[str, Any] | None:
        '''
            Property method for getting project configuration.

            :return: Formatted project configuration in Mapping format | None
            :rtype: <Mapping[str, Any] | None>
            :exceptions: None.
        '''
        pass

    @config.setter
    @abstractmethod
    def config(self, pro_config: Mapping[str, Any] | None) -> None:
        '''
            Property method for setting project configuration.

            :param pro_config: Project configuration in Mapping format | None
            :type pro_config: <Mapping[str, Any] | None>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def not_none(self) -> bool:
        '''
            Checks if project configuration is not None.

            :return: True if successfully, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the ATS project configuration as string representation.

            :return: The ATS project configuration as string representation.
            :rtype: str
            :exceptions: None.
        '''
        pass
