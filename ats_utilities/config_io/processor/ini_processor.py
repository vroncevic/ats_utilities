
# -*- coding: UTF-8 -*-

'''
Module
    ini_processor.py
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
    Defines class INIProcessor with attribute(s) and method(s).
    Creates an API to process configuration in INI format.
    1th level of configuration loader/storer implementation.
'''

from __future__ import annotations

from copy import deepcopy
from collections.abc import Mapping
from configparser import ConfigParser, Error as ConfigParserError
from io import StringIO
from typing import Any, override

from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.utils.reflection import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class INIProcessor(IConfigProcessor):
    '''
        Defines class INIProcessor with attribute(s) and method(s).
        Creates an API to process configuration in INI format.
        1th level of configuration loader/storer implementation.

        It defines:

            :attributes:
                | _config - Internal instance to store configuration data (default ConfigParser()).
                | _scheme - Mapping with configuration scheme (default None).
            :methods:
                | __init__ - Initializes INIProcessor constructor.
                | deserialize - Loads and parses configuration from a raw source (string, stream, or lines).
                | serialize - Converts the internal configuration structure back to a formatted string representation.
                | update_data - Updates the internal configuration data and validates it against the scheme.
                | to_dict - Returns the parsed configuration as a flat or structured dictionary.
                | validate_by_scheme - Validates the internal parsed data structure against the provided scheme.
                | __str__ - Returns the INIProcessor instance as string representation.

        INI Format Config Scheme
        ------------------------

        For INI configurations, the value in the ``scheme`` mapping **must** be 
        the section name under which the key (parameter) is located.

        .. code-block:: python

            scheme = {
                "ats_name": "ats_info",       # Maps to: [ats_info] -> ats_name
                "ats_version": "ats_info",    # Maps to: [ats_info] -> ats_version
                "hostname": "connection"      # Maps to: [connection] -> hostname
            }
    '''

    _config: ConfigParser
    _scheme: Mapping[str, str] | None

    def __init__(self, scheme: Mapping[str, str] | None = None) -> None:
        '''
            Initializes INIProcessor constructor.

            :param scheme: Mapping with configuration scheme | None.
            :type scheme: Mapping[str, str] | None
            :exceptions: None.
        '''
        self._config = ConfigParser()
        self._scheme = scheme

    @override
    def deserialize(self, content: Any) -> bool:
        '''
            Loads and parses configuration from a raw source (string, stream, or lines).

            :param content: Raw configuration data (str, stream, or sequence).
            :type content: Any
            :return: True if successfully, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        try:
            if isinstance(content, str):
                self._config.read_string(content)
            else:
                self._config.read_file(content)

            return self.validate_by_scheme()

        except (OSError, ConfigParserError):
            return False

    @override
    def serialize(self) -> str:
        '''
            Converts the internal configuration structure back to a formatted string representation.

            :return: Configuration content as string.
            :rtype: str
            :exceptions: None.
        '''
        try:
            stream = StringIO()
            self._config.write(stream, space_around_delimiters=True)

            return stream.getvalue()

        except (OSError, ConfigParserError):
            return ''

    @override
    def update_data(self, new_data: Mapping[str, str]) -> bool:
        '''
            Updates the internal configuration data and validates it against the scheme.

            :param new_data: Mapping containing configuration keys and values.
            :type new_data: Mapping[str, str]
            :return: True if successfully, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        if self._scheme is None:
            return False

        old_config = deepcopy(self._config)

        for key, value in new_data.items():
            section = self._scheme.get(key)

            if section:
                if not self._config.has_section(section):
                    self._config.add_section(section)

                self._config.set(section, key, str(value))
            else:
                if self._config.sections():
                    self._config.set(self._config.sections()[0], key, str(value))

        if not self.validate_by_scheme():
            self._config = old_config

            return False

        return True

    @override
    def to_dict(self) -> dict[str, str]:
        '''
            Returns the parsed configuration as a flat or structured dictionary.

            :return: Dictionary with configuration information.
            :rtype: dict[str, str]
            :exceptions: None.
        '''
        if not self._config.sections():
            return {}

        if self._scheme is not None:
            result: dict[str, str] = {}

            for key, section in self._scheme.items():
                if section and self._config.has_section(section):
                    if self._config.has_option(section, key):
                        result[key] = str(self._config.get(section, key))
                    else:
                        result[key] = ''
                else:
                    found = False

                    for s in self._config.sections():
                        if self._config.has_option(s, key):
                            result[key] = str(self._config.get(s, key))
                            found = True
                            break

                    if not found:
                        result[key] = ''

            return result

        first_section = self._config.sections()[0]

        return {k: str(v) for k, v in self._config.items(first_section)}

    @override
    def validate_by_scheme(self) -> bool:
        '''
            Validates the internal parsed data structure against the provided scheme.

            :return: True if successfully, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        if self._scheme is None:
            return True

        for key, section in self._scheme.items():
            if section:
                if not self._config.has_section(section):
                    return False

                if not self._config.has_option(section, key):
                    return False

            else:
                if not any(self._config.has_option(s, key) for s in self._config.sections()):
                    return False

        return True

    @override
    def __str__(self) -> str:
        '''
            Returns the INIProcessor instance as string representation.

            :return: The INIProcessor instance as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
