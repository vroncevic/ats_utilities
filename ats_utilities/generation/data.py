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

from ats_utilities.utils.reflection import instance_to_dict

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class GeneratorData:
    '''
        Encapsulates generator runtime data.

        It defines:

            :attributes:
                | archive_path - The path to the .tgz archive.
                | target_dir - The directory where the project will be generated.
                | template_key - The key for the template configuration.
                | scheme - The scheme configuration file path.
                | template_values - The template values for name case variations.
            :methods:
                | to_dict - Converts the generator data instance to a dictionary.
    '''

    archive_path: str
    target_dir: str
    template_key: str
    scheme: str | Mapping[str, object]
    template_values: Mapping[str, str]

    def to_dict(self) -> dict[str, object]:
        '''
            Converts the generator data instance to a dictionary.

            :return: The dictionary representation of the generator data.
            :exceptions: None.
        '''
        return instance_to_dict(self)
