# -*- coding: UTF-8 -*-

'''
Module
    ilicence.py
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
    Defines interface IATSLicence with attribute(s) and method(s).
    Interface for the ATS licence mechanism.
'''

from abc import ABC, abstractmethod
from typing import List, Optional

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IATSLicence(ABC):
    '''
        Defines interface IATSLicence with attribute(s) and method(s).
        Interface for the ATS licence mechanism.

        It defines:

            :attributes: None.
            :methods:
                | licence - Property methods for set/get operations.
                | is_licence_not_none - Checks is ATS licence not None.
                | __str__ - Returns the string representation of ATS licence.
    '''

    @property
    @abstractmethod
    def licence(self) -> Optional[str]:
        '''
            Property method for getting ATS licence.

            :return: The ATS licence | None
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement licence getter")

    @licence.setter
    @abstractmethod
    def licence(self, licence: Optional[str]) -> None:
        '''
            Property method for setting ATS licence.

            :param licence: The ATS licence | None
            :type licence: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement licence setter")

    @abstractmethod
    def is_licence_not_none(self) -> bool:
        '''
            Checks is ATS licence not None.

            :return: True (ATS licence is not None) | False.
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement is_licence_not_none method")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of ATS licence.

            :return: The ATS licence string
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement __str__ method")
