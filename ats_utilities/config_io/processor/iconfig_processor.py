# -*- coding: UTF-8 -*-

'''
Module
    iconfig_processor.py
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
    Defines abstract class IConfigProcessor with method(s).
    Creates an interface for processing configuration content.
    1th level of configuration loader/storer interface.
'''

from __future__ import annotations

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


class IConfigProcessor(ABC):
    '''
        Defines abstract class IConfigProcessor with method(s).
        Creates an interface for processing configuration content.
        1th level of configuration loader/storer interface.

        It defines:

            :methods:
                | deserialize - Loads and parses configuration from a raw source (string, stream, or lines).
                | serialize - Converts the internal configuration structure back to a formatted string representation.
                | update_data - Updates the internal configuration data and validates it against the scheme.
                | to_dict - Returns the parsed configuration as a flat or structured dictionary.
                | validate_by_scheme - Validates the internal parsed data structure against the provided scheme.
                | __str__ - Returns the configuration processor as string representation.

        Understanding the `scheme` Parameter
        ------------------------------------

        The ``scheme`` is a :class:`~collections.abc.Mapping` of ``str`` to ``str``
        that defines the expected structure, required keys, and locations of 
        configuration data. It serves as the source of truth for both parsing 
        (``to_dict``) and validation (``validate_by_scheme``).

        The concrete format of the scheme depends on the implementation of the 
        processor (flat, section-based, or hierarchical). Refer to the specific 
        processor class documentation for concrete examples.
    '''

    @abstractmethod
    def deserialize(self, content: Any) -> bool:
        '''
            Loads and parses configuration from a raw source (string, stream, or lines).

            :param content: Raw configuration data (str, stream, or sequence).
            :type content: <Any>
            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def serialize(self) -> str:
        '''
            Converts the internal configuration structure back to a formatted string representation.

            :return: Configuration content as string.
            :rtype: <str>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def update_data(self, new_data: Mapping[str, str]) -> bool:
        '''
            Updates the internal configuration data and validates it against the scheme.

            :param new_data: Mapping containing configuration keys and values.
            :type new_data: <Mapping[str, str]>
            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def to_dict(self) -> dict[str, str]:
        '''
            Returns the parsed configuration as a flat or structured dictionary.

            :return: Dictionary with configuration information.
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def validate_by_scheme(self) -> bool:
        '''
            Validates the internal parsed data structure against the provided scheme.

            :return: <True> if data matches the scheme, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the configuration processor as string representation.

            :return: The configuration processor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
