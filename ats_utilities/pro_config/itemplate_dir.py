# -*- coding: UTF-8 -*-

'''
Module
    itemplate_dir.py
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
    Defines interface ITemplateDir with attribute(s) and method(s).
    Interface for the project template directory mechanism.
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


class ITemplateDir(ABC):
    '''
        Defines interface ITemplateDir with attribute(s) and method(s).
        Interface for the project template directory mechanism.

        It defines:

            :attributes: None.
            :methods:
                | template_dir - Property methods for set/get operations.
                | is_template_dir_ok - Checks is template dir ok.
                | __str__ - Returns the string representation of ATS project directory.
    '''

    @property
    @abstractmethod
    def template_dir(self) -> Optional[str]:
        '''
            Property method for getting template dir.

            :return: Formatted template dir in string format | None
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method template_dir() must be implemented.")

    @template_dir.setter
    @abstractmethod
    def template_dir(self, dir_path: str) -> None:
        '''
            Property method for setting project template dir.

            :param dir_path: Project template dir path in string format | None
            :type dir_path: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method template_dir() must be implemented.")

    @abstractmethod
    def is_template_dir_ok(self) -> bool:
        '''
            Checks is project template dir ok.

            :return: True (template dir is ok) | False (template dir is not ok)
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method is_template_dir_ok() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of ATS project template directory.

            :return: The ATS project directory as string
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement __str__ method")
