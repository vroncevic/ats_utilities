# -*- coding: UTF-8 -*-

'''
Module
    iread.py
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
    Defines abstract class IRead with attribute(s) and method(s).
    Creates an interface for reading from configuration files.
'''

from abc import ABC, abstractmethod
from typing import Any

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IRead(ABC):
    '''
        Defines abstract class IRead with attribute(s) and method(s).
        Creates an interface for reading from configuration files.

        It defines:

            :attributes: None
            :methods:
                | read_configuration - Read configuration from file (abstract).
    '''

    @abstractmethod
    def read_configuration(self, verbose: bool = False) -> Any:
        '''
            Read configuration from file.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Configuration object
            :rtype: <Any>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method read_configuration() must be implement")
