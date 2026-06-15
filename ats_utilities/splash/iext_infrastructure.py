# -*- coding: UTF-8 -*-

'''
Module
    iext_infrastructure.py
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
    Defines interface IExtInfrastructure with attribute(s) and method(s).
    Interface for processing hyperlinks for splash screen.
'''

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class IExtInfrastructure(ABC):
    '''
        Defines interface IExtInfrastructure with attribute(s) and method(s).
        Interface for processing hyperlinks for splash screen.

        It defines:

            :attributes: None
            :methods:
                | infrastructure_property - Property method for get/set infrastructure property (abstract).
                | get_info_text - Pre-processes info text (abstract).
                | get_issue_text - Pre-processes issue text (abstract).
                | get_author_text - Pre-processes author text (abstract).
                | __str__ - Returns the string representation of external infrastructure (abstract).
    '''

    @property
    @abstractmethod
    def infrastructure_property(self) -> Optional[Dict[Any, Any]]:
        '''
            Property method for getting infrastructure property.

            :return: Formatted infrastructure property in dict format | None
            :rtype: <Optional[str]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement get_info_text method")

    @infrastructure_property.setter
    @abstractmethod
    def infrastructure_property(self, infrastructure_property_setup: Optional[Dict[Any, Any]]) -> None:
        '''
            Property method for setting project infrastructure property.

            :param infrastructure_property_setup: Project infrastructure property in dict format | None
            :type infrastructure_property_setup: <Optional[Dict[Any, Any]]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement get_info_text method")

    @abstractmethod
    def get_info_text(self) -> str:
        '''
            Pre-processes info text for splash.

            :return: Hyperlink with info text
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement get_info_text method")

    @abstractmethod
    def get_issue_text(self) -> str:
        '''
            Pre-processes issue text for splash.

            :return: Hyperlink with issue info
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement get_issue_text method")

    @abstractmethod
    def get_author_text(self) -> str:
        '''
            Pre-processes author text for splash.

            :return: Hyperlink with author info
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement get_author_text method")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of external infrastructure.

            :return: The external infrastructure as string
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Subclasses must implement __str__ method")
