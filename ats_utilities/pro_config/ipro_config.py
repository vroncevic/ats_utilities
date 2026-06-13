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
    Defines interface IProConfig with attribute(s) and method(s).
    Interface for the project configuration mechanism.
'''

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IProConfig(ABC):
    '''
        Defines interface IProConfig with attribute(s) and method(s).
        Interface for the project configuration mechanism.

        It defines:

            :attributes: None.
            :methods:
                | config - Property methods for set/get operations.
                | is_config_ok - Checks is project configuration ok.
    '''

    @property
    @abstractmethod
    def config(self) -> Optional[Dict[Any, Any]]:
        '''
            Property method for getting project configuration.

            :return: Formatted project configuration | None
            :rtype: <Optional[Dict[Any, Any]]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method config() must be implement")

    @config.setter
    @abstractmethod
    def config(self, pro_config: Dict[Any, Any]) -> None:
        '''
            Property method for setting project configuration.

            :param pro_config: Project configuration in dict format | None
            :type pro_config: <Dict[Any, Any]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method config() must be implement")

    @abstractmethod
    def is_config_ok(self) -> bool:
        '''
            Checks is project configuration ok.

            :return: True (configuration is ok) | False
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method is_config_ok() must be implement")
