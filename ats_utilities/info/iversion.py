# -*- coding: UTF-8 -*-

'''
Module
    iversion.py
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
    Defines interface IATSVersion with attribute(s) and method(s).
    Interface for the ATS version mechanism.
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


class IATSVersion(ABC):
    '''
        Defines interface IATSVersion with attribute(s) and method(s).
        Interface for the ATS version mechanism.

        It defines:

            :attributes: None.
            :methods:
                | version - Property methods for set/get operations.
                | is_version_not_none - Checks is ATS version not None.
    '''

    @property
    @abstractmethod
    def version(self) -> Optional[str]:
        '''
            Property method for getting ATS version.

            :return: The ATS version | None
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement version getter")

    @version.setter
    @abstractmethod
    def version(self, version: Optional[str]) -> None:
        '''
            Property method for setting ATS version.

            :param version: The ATS version | None
            :type version: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement version setter")

    @abstractmethod
    def is_version_not_none(self) -> bool:
        '''
            Checks is ATS version not None.

            :return: True (ATS version is not None) | False.
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement is_version_not_none method")
