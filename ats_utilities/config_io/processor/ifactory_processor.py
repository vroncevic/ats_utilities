# -*- coding: UTF-8 -*-

'''
Module
    ifactory_processor.py
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
    Defines abstract interface for configuration processor factories.
    1th level of configuration loader/storer interface.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol, runtime_checkable

from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@runtime_checkable
class IConfigProcessorFactory(Protocol):
    '''
        Abstract interface for ConfigProcessorFactory.
        Defines the factory orchestrations for generating configuration processors.
        1th level of configuration loader/storer interface.

        It defines:

            :methods:
                | get_processor_class - Returns the processor class for a specific file extension.
                | create_from_extension - Creates a processor instance based on a raw extension string.
                | create_from_file_path - Creates a processor instance based on a file path.
    '''

    @classmethod
    def get_processor_class(cls, extension: str) -> type[IConfigProcessor]:
        '''
            Returns the processor class for a specific file extension.

            :param extension: The file extension.
            :return: The processor class.
        '''
        ...

    @classmethod
    def create_from_extension(
        cls, 
        extension: str | None = None,
        scheme: Mapping[str, str] | None = None,
        processor: IConfigProcessor | None = None
    ) -> IConfigProcessor:
        '''
            Creates a processor instance based on a raw extension string.

            :param extension: File extension | None.
            :param scheme: Scheme for the processor | None.
            :param processor: Instance to be used as the processor | None.
            :return: The processor.
        '''
        ...

    @classmethod
    def create_from_file_path(
        cls, 
        file_path: str | None = None,
        scheme: Mapping[str, str] | None = None,
        processor: IConfigProcessor | None = None
    ) -> IConfigProcessor:
        '''
            Creates a processor instance based on a file path.

            :param file_path: Path to the configuration file | None.
            :param scheme: Scheme for the processor | None.
            :param processor: Instance to be used as the processor | None.
            :return: The processor.
        '''
        ...
