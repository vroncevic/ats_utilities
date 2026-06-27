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
    Defines class JSONProcessor with attribute(s) and method(s).
    Provides a default implementation for processing JSON content.
'''

from json import loads, dumps, JSONDecodeError
from typing import override
from ats_utilities.config_io.json.ijson_processor import IJSONProcessor
from ats_utilities.factory_class import format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

class JSONProcessor(IJSONProcessor):
    '''
        Defines class JSONProcessor with attribute(s) and method(s).
        Provides a default implementation for processing JSON content.

        It defines:

            :attributes:
                | _data - Internal dictionary to store JSON data.
            :methods:
                | __init__ - Initializes JSONProcessor constructor.
                | decode - Convert raw JSON text to an internal object/structure.
                | encode - Convert an internal object/structure back to a JSON string.
                | to_dict - Return data as a flat dictionary.
                | __str__ - Returns the JSONProcessor as string representation.
    '''

    def __init__(self) -> None:
        '''
            Initializes JSONProcessor constructor.

            :exceptions: None.
        '''
        self._data: dict[str, str] = {}

    @override
    def decode(self, json_string: str) -> bool:
        '''
            Converts raw JSON text to an internal object/structure.

            :param json_string: Raw JSON text in string format.
            :type json_string: <str>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        try:
            self._data = loads(json_string)
            return True
        except JSONDecodeError:
            return False

    @override
    def encode(self) -> str:
        '''
            Converts an internal object/structure back to a JSON string.

            :return: JSON content in string format.
            :rtype: <str>
            :exceptions: None.
        '''
        return dumps(self._data, indent=4)

    @override
    def to_dict(self) -> dict[str, str]:
        '''
            Converts data as a flat dictionary.

            :return: Dictionary with JSON configuration.
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        return self._data

    @override
    def __str__(self) -> str:
        '''
            Returns the JSONProcessor as string representation.

            :return: The JSONProcessor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
