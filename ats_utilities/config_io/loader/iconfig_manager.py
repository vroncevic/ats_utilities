# -*- coding: UTF-8 -*-

'''
Module
    iconfig_loader.py
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
    Defines abstract class IConfigLoadManager with method(s).
    Creates and interface for managing configuration loaders.
    3nd level of configuration loader interface.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

from ats_utilities.config_io.loader.iloader import ILoader

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IConfigLoadManager(ABC):
    '''
        Defines abstract class IConfigLoadManager with method(s).
        Creates and interface for managing configuration loaders.
        2nd level of configuration loader interface.

        It defines:

            :methods:
                | setup_loader - Setup configuration loader.
                | __str__ - Returns the config loader manager as string representation.
    '''

    @abstractmethod
    def setup_loader(self) -> ILoader:
        '''
            Setup configuration loader.

            :return: Configuration loader interface.
            :rtype: <ILoader>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the config loader manager as string representation.

            :return: The config loader manager as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
