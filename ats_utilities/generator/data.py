# -*- coding: UTF-8 -*-

'''
Module
    data.py
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
    Encapsulates generator runtime data.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from ats_utilities.utils.reflection import instance_to_dict

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

# Type alias for parameter metadata: (parameter name, expected type, actual value)
type ParamMetadata = tuple[str, str, Any]


@dataclass(slots=True, frozen=True, kw_only=True)
class GeneratorData:
    '''
        Encapsulates generator runtime data.

        It defines:

            :attributes:
                | archive_path - Path to the .tgz archive.
                | target_dir - Directory where the project will be generated.
                | template_key - Key for the template configuration.
                | scheme - Scheme configuration file path.
                | template_values - Template values for name case variations.
            :methods:
                | to_dict - Converts the generator data instance to a dictionary.
    '''

    archive_path: str
    target_dir: str
    template_key: str
    scheme: str | Mapping[str, Any]
    template_values: Mapping[str, str]

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the generator data instance to a dictionary.

            :return: Dictionary representation of the generator data instance.
            :rtype: dict[str, Any]
            :exceptions: None.
        '''
        return instance_to_dict(self)
