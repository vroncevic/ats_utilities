# -*- coding: UTF-8 -*-

'''
Module
    isplash_screen.py
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
    Defines interface ISplashProperty with attribute(s) and method(s).
    Interface for checking splash property.
'''

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ISplashProperty(ABC):
    '''
        Defines interface ISplashProperty with attribute(s) and method(s).
        Interface for checking splash property.

        It defines:

            :attributes: None
            :methods:
                | validates - Validates splash property (abstract).
                | splash_property - Splash property (abstract).
                | __str__ - Returns the string representation of splash property (abstract).
    '''

    @property
    @abstractmethod
    def splash_property(self) -> Optional[Dict[Any, Any]]:
        '''
            Property method for getting splash property.

            :return: Formatted splash property in dict format | None
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method splash_property() must be implemented.")

    @splash_property.setter
    @abstractmethod
    def splash_property(self, splash_property_setup: Optional[Dict[Any, Any]]) -> None:
        '''
            Property method for setting project splash property.

            :param splash_property_setup: Project splash property in dict format | None
            :type splash_property_setup: <Optional[Dict[Any, Any]]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method splash_property() must be implemented.")

    @abstractmethod
    def validates(self) -> bool:
        '''
            Validates splash property.

            :return: True (property ok) else False (property not ok)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement validate method")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of splash property.

            :return: The splash property as string
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement __str__ method")
