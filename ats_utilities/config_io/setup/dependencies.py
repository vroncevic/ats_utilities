# -*- coding: UTF-8 -*-

'''
Module
    dependencies.py
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
    Config I/O dependencies and options for config I/O bundle creation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import TypedDict, NotRequired

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ConfigIODependencies(TypedDict):
    '''
        Config I/O dependencies for config I/O bundle creation.

        It defines:

            :attributes:
                | file_path: Configuration file path.
                | scheme: Configuration scheme.
                | processor: Configuration processor.
                | context_bundle: Context bundle.
    '''

    file_path: str
    scheme: Mapping[str, str]
    processor: IConfigProcessor
    context_bundle: ContextBundle


class ConfigIOOptions(TypedDict):
    '''
        Config I/O options for config I/O bundle creation.

        It defines:

            :attributes:
                | file_path: Configuration file path.
                | scheme: Configuration scheme.
                | processor: Configuration processor.
                | context_bundle: Context bundle.
    '''

    file_path: NotRequired[str]
    scheme: NotRequired[Mapping[str, str] | None]
    processor: NotRequired[IConfigProcessor | None]
    context_bundle: ContextBundle
