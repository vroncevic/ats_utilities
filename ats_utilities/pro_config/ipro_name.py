# -*- coding: UTF-8 -*-

'''
Module
    ipro_name.py
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
    Defines interface IProName with attribute(s) and method(s).
    Interface for the project name mechanism.
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


class IProName(ABC):
    '''
        Defines interface IProName with attribute(s) and method(s).
        Interface for the project name mechanism.

        It defines:

            :attributes: None.
            :methods:
                | pro_name - Property methods for set/get operations.
                | is_pro_name_ok - Checks is project name ok.
    '''

    @property
    @abstractmethod
    def pro_name(self) -> Optional[str]:
        '''
            Property method for getting project name.

            :return: Formatted project name | None
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method pro_name() must be implemented.")

    @pro_name.setter
    @abstractmethod
    def pro_name(self, name: str) -> None:
        '''
            Property method for setting project name.

            :param name: Project name | None
            :type name: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method pro_name() must be implemented.")

    @abstractmethod
    def is_pro_name_ok(self) -> bool:
        '''
            Checks is project name ok.

            :return: True (project name is ok) | False
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method is_pro_name_ok() must be implemented.")
