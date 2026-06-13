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
    Defines interface IATSInfoOk with attribute(s) and method(s).
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


class IATSInfoOk(ABC):
    '''
        Defines interface IATSInfoOk with attribute(s) and method(s).
        Interface for the ATS info status mechanism.

        It defines:

            :attributes: None.
            :methods:
                | ats_info_ok - Property methods for set/get operations.
    '''

    @property
    @abstractmethod
    def ats_info_ok(self) -> bool:
        '''
            Property method for getting ATS information status.

            :return: The ATS information status
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement ats_info_ok getter")

    @ats_info_ok.setter
    @abstractmethod
    def ats_info_ok(self, ats_info_ok: bool) -> None:
        '''
            Property method for setting ATS information status.

            :param ats_info_ok: The ATS information status
            :type ats_info_ok: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement ats_info_ok setter")
