# -*- coding: UTF-8 -*-

'''
Module
    ischeme_loader.py
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
    Defines abstract class ISchemeLoader with method(s).
    Interface for loading/resolving generation scheme.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from collections.abc import Mapping

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ISchemeLoader(ABC):
    '''
        Defines abstract class ISchemeLoader with method(s).
        Interface for loading/resolving generation scheme.

        It defines:

            :methods:
                | load - Loads and resolves the scheme from dict or path.
                | is_initialized - Checks if the loader is initialized.
                | __str__ - Returns the loader as string representation.
    '''

    @abstractmethod
    def load(self, scheme: str | Mapping[str, Any]) -> dict[str, Any]:
        '''
            Loads and resolves the scheme.

            :param scheme: Generation scheme file path or preloaded scheme.
            :type scheme: <str | Mapping[str, Any]>
            :return: The resolved scheme dictionary.
            :rtype: dict[str, Any]
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if component is initialized.

            :return: True if successful, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the component as string representation.

            :return: String representation.
            :rtype: str
            :exceptions: None.
        '''
        pass
