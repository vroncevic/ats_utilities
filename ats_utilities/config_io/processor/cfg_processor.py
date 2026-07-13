# -*- coding: UTF-8 -*-

'''
Module
    cfg_processor.py
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
    Defines class CFGProcessor with attribute(s) and method(s).
    Creates an API to process configuration in CFG format.
    0th level of configuration loader/storer implementation.
'''

from __future__ import annotations

from collections.abc import Mapping
from re import match
from typing import Any, override

from ats_utilities.factory_class import to_str
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CFGProcessor(IConfigProcessor):
    '''
        Defines class CFGProcessor with attribute(s) and method(s).
        Creates an API to process configuration in CFG format.
        0th level of configuration loader/storer implementation.

        It defines:

            :attributes:
                | _REGEX_EXP - Regular expression for matching line.
                | _data - Internal dict to store configuration data (default {}).
                | _scheme - Mapping with configuration scheme (default None).
            :methods:
                | __init__ - Initializes CFGProcessor constructor.
                | deserialize - Loads and parses configuration from a raw source (string, stream, or lines).
                | serialize - Converts the internal configuration structure back to a formatted string representation.
                | to_dict - Returns the parsed configuration as a flat or structured dictionary.
                | validate_by_scheme - Validates the internal parsed data structure against the provided scheme.
                | __str__ - Returns the CFGProcessor instance as string representation.

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

    _REGEX_EXP: str = r'^\s*$'
    _data: dict[str, str]
    _scheme: Mapping[str, str] | None

    def __init__(self, scheme: Mapping[str, str] | None = None) -> None:
        '''
            Initializes CFGProcessor constructor.

            :param scheme: Mapping with configuration scheme (default None).
            :type scheme: <Mapping[str, str] | None>
            :exceptions: None.
        '''
        self._data: dict[str, str] = {}
        self._scheme = scheme

    @override
    def deserialize(self, content: Any) -> bool:
        '''
            Loads and parses configuration from a raw source (string, stream, or lines).

            :param content: Raw configuration data (str, stream, or sequence).
            :type content: <Any>
            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        self._data.clear()
        lines = content.splitlines() if isinstance(content, str) else content

        for line in lines:
            if not match(self._REGEX_EXP, line):
                if '=' in line:
                    pair: tuple[str, str] = line.split('=', 1)
                    self._data[pair[0].strip()] = pair[1].strip()

        return self.validate_by_scheme()

    @override
    def serialize(self) -> str:
        '''
            Converts the internal configuration structure back to a formatted string representation.

            :return: Configuration content as string.
            :rtype: <str>
            :exceptions: None.
        '''
        return ''.join([f'{k} = {v}\n' for k, v in self._data.items()])

    @override
    def to_dict(self) -> dict[str, str]:
        '''
            Returns the parsed configuration as a flat or structured dictionary.

            :return: Dictionary with configuration information.
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        return self._data

    @override
    def validate_by_scheme(self) -> bool:
        '''
            Validates the internal parsed data structure against the provided scheme.

            :return: <True> if data matches the scheme, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        if self._scheme is None:
            return True

        for expected_key in self._scheme.keys():
            if expected_key not in self._data:
                return False

        return True

    @override
    def __str__(self) -> str:
        '''
            Returns the CFGProcessor instance as string representation.

            :return: The CFGProcessor instance as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
