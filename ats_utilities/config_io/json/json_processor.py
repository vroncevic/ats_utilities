# -*- coding: UTF-8 -*-

'''
Module
    json_processor.py
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
    Defines class ATSJSONProcessor with attribute(s) and method(s).
    Provides a default implementation for processing JSON content.
'''
import json
from typing import Any, Dict, List
from ats_utilities.config_io.json.ijson_processor import IJSONProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

class ATSJSONProcessor(IJSONProcessor):
    '''
        Defines class ATSJSONProcessor with attribute(s) and method(s).
        Provides a default implementation for processing JSON content.

        It defines:

            :attributes:
                | __data - Internal dictionary to store JSON data.
            :methods:
                | __init__ - Initials ATSJSONProcessor constructor.
                | decode - Convert raw JSON text to an internal object/structure.
                | encode - Convert an internal object/structure back to a JSON string.
                | to_dict - Return data as a flat dictionary.
    '''

    def __init__(self) -> None:
        '''
            Initials ATSJSONProcessor constructor.
        '''
        self.__data: Dict[Any, Any] = {}

    def decode(self, json_string: str) -> bool:
        '''
            Convert raw JSON text to an internal object/structure.

            :param json_string: Raw JSON text
            :type json_string: <str>
            :return: True (content decoded) | False
            :rtype: <bool>
        '''
        try:
            self.__data = json.loads(json_string)
            return True
        except json.JSONDecodeError:
            return False

    def encode(self) -> str:
        '''
            Convert an internal object/structure back to a JSON string.

            :return: JSON content as string
            :rtype: <str>
        '''
        return json.dumps(self.__data, indent=4)

    def to_dict(self) -> Dict[Any, Any]:
        '''
            Return data as a flat dictionary.

            :return: Dictionary with JSON information
            :rtype: <Dict[Any, Any]>
        '''
        return self.__data
