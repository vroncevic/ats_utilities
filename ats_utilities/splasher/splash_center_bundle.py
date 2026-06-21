# -*- coding: UTF-8 -*-

'''
Module
    splash_center_bundle.py
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
    Defines splash screen bundle for centering console output.
'''

from dataclasses import dataclass
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class SplashCenterBundle:
    '''
        Defines splash screen bundle for centering console output.

        It defines:

            :attributes:
                | columns - Column count for console session (default 0).
                | additional_shifter - Additional shifters (default 0).
                | text - Text for console session (default None).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    columns: int = 0
    additional_shifter: int = 0
    text: str | None = None

    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions: ATSTypeError, ATSValueError.
        '''
        if not isinstance(self.columns, int):
            raise ATSTypeError("Columns count 'columns' must be an integer.")

        if self.columns < 0:
            raise ATSValueError("Columns count 'columns' must be greater than 0.")

        if not isinstance(self.additional_shifter, int):
            raise ATSTypeError("Additional shifter 'additional_shifter' must be an integer.")

        if self.additional_shifter < 0:
            raise ATSValueError("Additional shifter 'additional_shifter' must be greater than or equal to 0.")

        if not isinstance(self.text, str) and self.text is not None:
            raise ATSTypeError("Text 'text' must be a string or None.")

        if isinstance(self.text, str) and not self.text.strip():
            raise ATSValueError("Text 'text' cannot be empty.")

    def merge(self, other: 'SplashCenterBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <SplashCenterBundle>
            :exceptions: None.
        '''
        for field_name in self.__dataclass_fields__:
            other_value = getattr(other, field_name)
            if other_value is not None:
                setattr(self, field_name, other_value)

    def to_dict(self) -> dict:
        '''
            Converts the bundle attributes to a dictionary.

            :return: Dictionary representation of the bundle attributes.
            :rtype: <dict>
            :exceptions: None.
        '''
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_')
        }

