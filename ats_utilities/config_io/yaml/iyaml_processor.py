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
    Defines abstract class IYAMLProcessor with attribute(s) and method(s).
    Creates an interface for processing YAML content.
'''
from abc import ABC, abstractmethod
from typing import Any, Dict, List

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

class IYAMLProcessor(ABC):
    '''
        Defines interface IYAMLProcessor with attribute(s) and method(s).
        Interface for processing YAML content.

        It defines:

            :attributes: None
            :methods:
                | decode - Convert raw YAML text to an internal object/structure (abstract).
                | encode - Convert an internal object/structure back to a YAML string (abstract).
                | to_dict - Return data as a flat dictionary required for ATSInfo (abstract).
                | __str__ - Returns the string representation of YAML configuration processor component (abstract).
    '''

    @abstractmethod
    def decode(self, yaml_string: str) -> bool:
        '''
            Convert raw YAML text to an internal object/structure.

            :param yaml_string: Raw YAML text
            :type yaml_string: <str>
            :return: True (content decoded) | False
            :rtype: <bool>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method decode() must be implemented.")

    @abstractmethod
    def encode(self) -> str:
        '''
            Convert an internal object/structure back to a YAML string.

            :return: YAML content as string
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method encode() must be implemented.")

    @abstractmethod
    def to_dict(self) -> Dict[Any, Any]:
        '''
            Return data as a flat dictionary.

            :return: Dictionary with YAML information
            :rtype: <Dict[Any, Any]>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method to_dict() must be implemented.")

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the string representation of YAML configuration processor component.

            :return: The YAML configuration processor component as string
            :rtype: <str>
            :exceptions: NotImplementedError
        '''
        raise NotImplementedError("Method __str__() must be implemented.")
