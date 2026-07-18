# -*- coding: UTF-8 -*-

'''
Module
    conf_file_bundle.py
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
    Defines config I/O bundle data classes for dependency group simplification.
    Encapsulates core config I/O objects to minimize constructor overhead.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class ConfFileBundle:
    '''
        Defines config I/O bundle data classes for dependency group simplification.
        Encapsulates core config I/O objects to minimize constructor overhead.

        It defines:

            :attributes:
                | file_path - File path.
                | file_mode - File mode.
                | context_bundle - Context bundle for dependency injection.
            :methods:
                | __post_init__ - Post-initialization hook to validate conf file bundle.
                | validate - Validates conf file bundle.
                | to_dict - Converts the conf file bundle instance to a dictionary.
    '''

    file_path: str
    file_mode: str
    context_bundle: ContextBundle

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate conf file bundle.

            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: File mode must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: File mode must be a string.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates conf file bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: File path must be provided.
                | ATSValueError: File mode must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: File mode must be a string.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        not_none(self.file_path, r'file path must be provided')
        not_none(self.file_mode, r'file mode must be provided')
        not_none(self.context_bundle, r'context bundle must be provided')
        istype(self.file_path, str, r'file path must be a string')
        istype(self.file_mode, str, r'file mode must be a string')
        istype(self.context_bundle, ContextBundle, r'context bundle must be a ContextBundle instance')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the conf file bundle instance to a dictionary.

            :return: Dictionary representation of the conf file bundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
