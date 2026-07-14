# -*- coding: UTF-8 -*-

'''
Module
    istorer.py
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
    Defines abstract class IStorer with method(s).
    Creates an interface for storing the configuration to writer.
    2nd level of configuration storer interface.
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping

from ats_utilities.context_bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IStorer(ABC):
    '''
        Defines abstract class IStorer with method(s).
        Creates an interface for storing the configuration to writer.
        2nd level of configuration storer interface.

        It defines:

            :methods:
                | get_shared_context - Returns the shared context.
                | store_configuration - Stores configuration content from mapping to configuration file.
                | __str__ - Returns the storer instance as string representation.
    '''

    @abstractmethod
    def get_shared_context(self) -> ContextBundle:
        '''
            Returns the shared context.

            :return: Shared context.
            :rtype: <ContextBundle>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def store_configuration(self, config: Mapping[str, str]) -> bool:
        '''
            Stores configuration content from mapping to configuration file.

            :param config: Mapping with configuration information (read only data).
            :type config: <Mapping[str, str]>
            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the storer instance as string representation.

            :return: The storer instance as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
