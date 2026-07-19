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
    Defines abstract class IExtInfrastructure with method(s).
    Interface for processing hyperlinks for splash screen.
'''

from __future__ import annotations

from ats_utilities.context.icontext_support import IContextSupport

from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import Any

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class IExtInfrastructure(IContextSupport, ABC):
    '''
        Defines abstract class IExtInfrastructure with method(s).
        Interface for processing hyperlinks for splash screen.
        Note: Splash screen infrastructure comes from info configuration file as read only data.

        It defines:

            :methods:
                | infrastructure_property - Property methods for set/get operations.
                | get_info_text - Pre-processes info text for splash screen.
                | get_issue_text - Pre-processes issue text for splash screen.
                | get_author_text - Pre-processes author text for splash screen.
                | __str__ - Returns the external infrastructure as string representation.
    '''

    @property
    @abstractmethod
    def infrastructure_property(self) -> Mapping[str, Any]:
        '''
            Property method for getting infrastructure property.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Formatted infrastructure property in Mapping format (read only data).
            :rtype: <Mapping[str, Any]>
            :exceptions: None.
        '''
        pass

    @infrastructure_property.setter
    @abstractmethod
    def infrastructure_property(self, setup: Mapping[str, Any]) -> None:
        '''
            Property method for setting project infrastructure property.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :param setup: Project infrastructure property in Mapping format (read only data).
            :type setup: <Mapping[str, Any]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def get_info_text(self) -> str:
        '''
            Pre-processes info text for splash screen.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Hyperlink with info text.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def get_issue_text(self) -> str:
        '''
            Pre-processes issue text for splash screen.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Hyperlink with issue info.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def get_author_text(self) -> str:
        '''
            Pre-processes author text for splash screen.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Hyperlink with author info.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the external infrastructure as string representation.

            :return: The external infrastructure as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
