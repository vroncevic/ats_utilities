# -*- coding: UTF-8 -*-

'''
Module
    iinfo_ok.py
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
    Defines interface IInfoOk with attribute(s) and method(s).
    Interface for the ATS info status mechanism.
'''

from abc import ABC, abstractmethod
from typing import List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IInfoOk(ABC):
    '''
        Defines interface IInfoOk with attribute(s) and method(s).
        Interface for the ATS info status mechanism.

        It defines:

            :attributes: None.
            :methods:
                | info_ok - Property methods for set/get operations (abstract).
                | __str__ - Returns the string representation of ATS info status (abstract).
    '''

    @property
    @abstractmethod
    def info_ok(self) -> bool:
        '''
            Property method for getting ATS information status.

            :return: The ATS information status in bool format
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method info_ok must be implemented.")

    @info_ok.setter
    @abstractmethod
    def info_ok(self, info_ok: bool) -> None:
        '''
            Property method for setting ATS information status.

            :param info_ok: The ATS information status in bool format
            :type info_ok: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method info_ok() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of ATS info status.

            :return: The ATS info status instance as string representation
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
