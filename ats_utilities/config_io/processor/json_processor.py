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
    Defines the JSONProcessor class with attribute(s) and method(s).
    Provides an API to process configuration in JSON format.
    1th level of configuration loader/storer implementation.
'''

from __future__ import annotations

from collections.abc import Mapping
from json import loads, dumps, JSONDecodeError

from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'

class JSONProcessor:
    '''
        Defines the JSONProcessor class with attribute(s) and method(s).
        Provides an API to process configuration in JSON format.
        1th level of configuration loader/storer implementation.

        It defines:

            :attributes:
                | _data - The internal dict to store configuration data (default {}).
                | _scheme - The mapping with configuration scheme (default: None).
            :methods:
                | __init__ - Initializes the JSONProcessor instance.
                | deserialize - Loads and parses configuration from a raw source (string, stream, or lines).
                | serialize - Converts the internal configuration structure back to a formatted string representation.
                | update_data - Updates the internal configuration data and Validates the it against the scheme instance.
                | to_dict - Returns the parsed configuration as a flat or structured dictionary.
                | validate_by_scheme - Validates the internal parsed data structure against the provided scheme instance.
                | __str__ - Returns the JSONProcessor instance as a string representation.

        Flat Format Config Scheme
        -------------------------

        Since this format is flat, there are no sections or parent elements. 
        In the ``scheme`` mapping, the key represents the required parameter name, 
        and the value **must** be an empty string (``""``).

        .. code-block:: python

            scheme = {
                "hostname": "",
                "port": "",
                "verbose": ""
            }
    '''

    _data: dict[str, str]
    _scheme: Mapping[str, str] | None

    def __init__(self, scheme: Mapping[str, str] | None = None) -> None:
        '''
            Initializes the JSONProcessor instance.

            :param scheme: Mapping with configuration scheme | None.
            :exceptions: None.
        '''
        self._data = {}
        self._scheme = scheme

    def deserialize(self, content: object) -> bool:
        '''
            Loads and parses configuration from a raw source (string, stream, or lines).

            :param content: The raw configuration data (str, stream, or sequence).
            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        try:
            self._data = loads(str(content))

            return self.validate_by_scheme()

        except JSONDecodeError:
            return False

    def serialize(self) -> str:
        '''
            Converts the internal configuration structure back to a formatted string representation.

            :return: The configuration content as a string.
            :exceptions: None.
        '''
        return dumps(self._data, indent=4)

    def update_data(self, new_data: Mapping[str, str]) -> bool:
        '''
            Updates the internal configuration data and Validates the it against the scheme instance.

            :param new_data: The mapping containing configuration keys and values.
            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        old_data = self._data.copy()

        self._data.update(new_data)

        if not self.validate_by_scheme():
            self._data = old_data

            return False

        return True

    def to_dict(self) -> dict[str, str]:
        '''
            Returns the parsed configuration as a flat or structured dictionary.

            :return: The dictionary with configuration information.
            :exceptions: None.
        '''
        return self._data

    def validate_by_scheme(self) -> bool:
        '''
            Validates the internal parsed data structure against the provided scheme instance.

            :return: True if successful, otherwise False.
            :exceptions: None.
        '''
        if self._scheme is None:
            return True

        for expected_key in self._scheme.keys():
            if expected_key not in self._data:
                return False

        return True

    def __str__(self) -> str:
        '''
            Returns the JSONProcessor instance as a string representation.

            :return: The JSONProcessor instance as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
