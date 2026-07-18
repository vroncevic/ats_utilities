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
    Encapsulates components of splash screen for simplification of SplashCenterBundle creation.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none, not_satisfied

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class SplashCenterBundle:
    '''
        Encapsulates components of splash screen for simplification of SplashCenterBundle creation.

        It defines:

            :attributes:
                | columns - Column count for console session.
                | additional_shifter - Additional shifters.
            :methods:
                | __post_init__ - Post initialization of the SplashCenterBundle.
                | validate - Validates splash center bundle.
                | to_dict - Converts the splash center bundle instance to a dictionary.
    '''

    columns: int
    additional_shifter: int

    def __post_init__(self) -> None:
        '''
            Post initialization of the SplashCenterBundle.

            :exceptions:
                | ATSValueError: Columns count must be provided.
                | ATSTypeError: Columns count is not an integer.
                | ATSValueError: Columns count cannot be negative.
                | ATSValueError: Additional shifter must be provided.
                | ATSTypeError: Additional shifter is not an integer.
                | ATSValueError: Additional shifter cannot be negative.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates splash center bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Columns count must be provided.
                | ATSTypeError: Columns count is not an integer.
                | ATSValueError: Columns count cannot be negative.
                | ATSValueError: Additional shifter must be provided.
                | ATSTypeError: Additional shifter is not an integer.
                | ATSValueError: Additional shifter cannot be negative.
        '''
        not_none(self.columns, r'columns count must be provided')
        istype(self.columns, int, r'columns count must be an integer')
        not_satisfied(self.columns < 0, r'columns count cannot be negative')
        not_none(self.additional_shifter, r'additional shifter must be provided')
        istype(self.additional_shifter, int, r'additional shifter must be an integer')
        not_satisfied(self.additional_shifter < 0, r'additional shifter cannot be negative')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the splash center bundle instance to a dictionary.

            :return: Dictionary representation of the splash center bundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
