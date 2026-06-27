# -*- coding: UTF-8 -*-

'''
Module
    iyaml_processor.py
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
    Defines abstract class IYAMLProcessor with method(s).
    Creates an interface for processing YAML content.
'''
from abc import ABC, abstractmethod

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

class IYAMLProcessor(ABC):
    '''
        Defines abstract class IYAMLProcessor with method(s).
        Interface for processing YAML content.

        It defines:

            :attributes: None
            :methods:
                | decode - Converts raw YAML text to an internal object/structure.
                | encode - Converts an internal object/structure back to a YAML string.
                | to_dict - Returns configuration as a flat dictionary.
                | __str__ - Returns the YAML processor as string representation.
    '''

    @abstractmethod
    def decode(self, yaml_string: str) -> bool:
        '''
            Converts raw YAML text to an internal object/structure.

            :param yaml_string: Raw YAML text
            :type yaml_string: <str>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def encode(self) -> str:
        '''
            Converts an internal object/structure back to a YAML string.

            :return: YAML content as string
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def to_dict(self) -> dict[str, str]:
        '''
            Returns configuration as a flat dictionary.

            :return: Dictionary with YAML configuration
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the YAML processor as string representation.

            :return: The YAML processor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
