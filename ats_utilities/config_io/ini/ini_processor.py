
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
    Default implementation for processing INI content.
'''

from typing import Any
from configparser import ConfigParser, Error as ConfigParserError
from ats_utilities.config_io.ini.iini_processor import IINIProcessor
from ats_utilities.factory_class import format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class INIProcessor(IINIProcessor):
    '''
        Defines class INIProcessor with attribute(s) and method(s).
        Default implementation for processing INI content.

        It defines:

            :attributes:
                | _SECTION - Section name for ATS configuration.
                | _NAME - Option name for ATS configuration.
                | _VERSION - Option version for ATS configuration.
                | _BUILD_DATE - Option build date for ATS configuration.
                | _LICENCE - Option licence for ATS configuration.
                | _config - ConfigParser instance for INI parsing.
            :methods:
                | __init__ - Initializes INIProcessor constructor.
                | from_stream - Loads INI configuration from a stream.
                | to_stream - Converts INI configuration to a stream.
                | to_dict - Converts INI configuration to dictionary.
                | __str__ - Returns the INIProcessor as string representation.
    '''

    _SECTION: str = 'ats_info'
    _NAME: str = 'ats_name'
    _VERSION: str = 'ats_version'
    _BUILD_DATE: str = 'ats_build_date'
    _LICENCE: str = 'ats_licence'

    def __init__(self) -> None:
        '''
            Initializes INIProcessor constructor.

            :exceptions: None.
        '''
        self._config = ConfigParser()

    def from_stream(self, stream: Any) -> bool:
        '''
            Loads INI configuration from a stream.

            :param stream: INI content stream.
            :type stream: <Any>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        try:
            self._config.read_file(stream)
            return True
        except (OSError, ConfigParserError):
            return False

    def to_stream(self, stream: Any) -> bool:
        '''
            Converts INI configuration to a stream.

            :param stream: INI content stream.
            :type stream: <Any>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        try:
            self._config.write(stream, space_around_delimiters=True)
            return True
        except (OSError, ConfigParserError):
            return False

    def to_dict(self) -> dict[str, str]:
        '''
            Converts INI configuration to dictionary.

            :return: Dictionary with ATS information.
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        if not self._config.has_section(self._SECTION):
            return {}
        return {
            self._NAME: str(self._config.get(self._SECTION, self._NAME, fallback='')),
            self._VERSION: str(self._config.get(self._SECTION, self._VERSION, fallback='')),
            self._BUILD_DATE: str(self._config.get(self._SECTION, self._BUILD_DATE, fallback='')),
            self._LICENCE: str(self._config.get(self._SECTION, self._LICENCE, fallback=''))
        }

    def __str__(self) -> str:
        '''
            Returns the INIProcessor as string representation.

            :return: The INIProcessor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
