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
    Provides an interface for processing configuration content.
    1th level of configuration loader/storer interface.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IConfigProcessor[DataType](Protocol):
    '''
        Defines abstract class IConfigProcessor with method(s).
        Provides an interface for processing configuration content.
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

    def deserialize(self, content: object) -> bool:
        '''
            Loads and parses configuration from a raw source (string, stream, or lines).

            :param content: Raw configuration data (str, stream, or sequence).
            :return: True if successfully, otherwise False.
        '''
        ...

    def serialize(self) -> str:
        '''
            Converts internal configuration structure back to a formatted string representation.

            :return: Configuration content as string.
        '''
        ...

    def update_data(self, new_data: DataType) -> bool:
        '''
            Updates internal configuration data and validates it against the scheme.

            :param new_data: Configuration data.
            :return: True if successfully, otherwise False.
        '''
        ...

    def to_dict(self) -> DataType:
        '''
            Returns parsed configuration as a flat or structured dictionary.

            :return: Configuration.
        '''
        ...

    def validate_by_scheme(self) -> bool:
        '''
            Validates internal parsed data structure against the provided scheme.

            :return: True if successfully, otherwise False.
        '''
        ...

    def __str__(self) -> str:
        '''
            Returns configuration processor as string representation.

            :return: Configuration processor as string representation.
        '''
        ...
