
# -*- coding: UTF-8 -*-

'''
Module
    default_ini_processor.py
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
    Defines class ATSINIProcessor with attribute(s) and method(s).
    Default implementation for processing INI content.
'''
from configparser import ConfigParser, Error as ConfigParserError
from typing import Any, Dict
from ats_utilities.config_io.ini.iini_processor import IINIProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSINIProcessor(IINIProcessor):
    '''
        Defines class ATSINIProcessor with attribute(s) and method(s).
        Default implementation for processing INI content.

        It defines:

            :attributes:
                | __config - ConfigParser instance for INI parsing.
            :methods:
                | __init__ - Initializes ATSINIProcessor constructor.
                | from_stream - Load INI content from a stream.
                | to_stream - Write INI content to a stream.
                | get_ats_info - Get ATS information from INI.
    '''

    def __init__(self) -> None:
        '''
            Initializes ATSINIProcessor constructor.
        '''
        self.__config = ConfigParser()

    def from_stream(self, stream: Any) -> bool:
        '''
            Load INI content from a stream.

            :param stream: INI content stream
            :type stream: <Any>
            :return: True (content loaded) | False
            :rtype: <bool>
            :exceptions: None
        '''
        try:
            self.__config.read_file(stream)
            return True
        except (OSError, ConfigParserError):
            return False

    def to_stream(self, stream: Any) -> bool:
        '''
            Write INI content to a stream.

            :param stream: INI content stream
            :type stream: <Any>
            :return: True (content written) | False
            :rtype: <bool>
            :exceptions: None
        '''
        try:
            self.__config.write(stream, space_around_delimiters=True)
            return True
        except (OSError, ConfigParserError):
            return False

    def get_ats_info(self) -> Dict[str, str]:
        '''
            Get ATS information from INI.

            :return: Dictionary with ATS information
            :rtype: <Dict[str, str]>
            :exceptions: None
        '''
        if not self.__config.has_section('ats_info'):
            return {}
        return {
            'ats_name': str(self.__config.get('ats_info', 'ats_name', fallback='')),
            'ats_version': str(self.__config.get('ats_info', 'ats_version', fallback='')),
            'ats_build_date': str(self.__config.get('ats_info', 'ats_build_date', fallback='')),
            'ats_licence': str(self.__config.get('ats_info', 'ats_licence', fallback='')),
        }
