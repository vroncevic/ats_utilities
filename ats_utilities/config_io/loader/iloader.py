# -*- coding: UTF-8 -*-

'''
Module
    iloader.py
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
    Defines abstract class ILoader with method(s).
    Creates an interface for loading the configuration from configuration reader.
    2st level of configuration loader interface.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ILoader(ABC):
    '''
        Defines abstract class ILoader with method(s).
        Creates an interface for loading the configuration from configuration reader.
        1st level of configuration loader interface.

        It defines:

            :methods:
                | load_configuration - Returns configuration in dict format from configuration reader.
                | __str__ - Returns the loader instance as string representation.
    '''

    @abstractmethod
    def load_configuration(self) -> dict[str, Any]:
        '''
            Returns configuration in dict format from configuration reader.

            :return: Dictionary with configuration content.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the loader instance as string representation.

            :return: The loader instance as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
