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
    Encapsulates runtime parameters for centering console output.
'''

from __future__ import annotations

from typing import Any
from dataclasses import dataclass, asdict

from ats_utilities.factory_type import check_type
from ats_utilities.factory_value import require_not_satisfied

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


@dataclass(slots=True, kw_only=True)
class SplashCenterBundle:
    '''
        Encapsulates runtime parameters for console output centering.

        It defines:

            :attributes:
                | columns - Column count for console session (default 0).
                | additional_shifter - Additional shifters (default 0).
                | text - Text for console session (default None).
            :methods:
                | __post_init__ - Post initialization of the SplashCenterBundle.
                | validate - Validates that SplashCenterBundle is valid (can be called after merge).
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the SplashCenterBundle instance to a dictionary.
    '''

    columns: int = 0
    additional_shifter: int = 0
    text: str | None = None

    def __post_init__(self) -> None:
        '''
            Post initialization of the SplashCenterBundle.

            Sets default values for columns and additional_shifter if they are less than 0.
            Sets default value for text if it is None.

            :exceptions:
                | ATSTypeError: Columns count 'columns' is not an integer.
                | ATSTypeError: Additional shifter 'additional_shifter' is not an integer.
        '''
        check_type(self.columns, int, "columns must be an integer.")

        if self.columns < 0:
            self.columns = 0

        check_type(self.additional_shifter, int, "additional_shifter must be an integer.")

        if self.additional_shifter < 0:
            self.additional_shifter = 0

        if self.text is None:
            self.text = ""

    def validate(self) -> None:
        '''
            Validates that SplashCenterBundle is valid (can be called after merge).
            Performs validation of columns, additional_shifter and text attributes.
            Columns must be non-None and an instance of integer.
            Additional_shifter must be non-None and an instance of integer.
            Text must be non-None and an instance of string.

            :exceptions:
                | ATSTypeError: Columns count 'columns' is not an integer.
                | ATSValueError: Columns count 'columns' cannot be negative.
                | ATSTypeError: Additional shifter 'additional_shifter' is not an integer.
                | ATSValueError: Additional shifter 'additional_shifter' cannot be negative.
                | ATSTypeError: Text 'text' must be a string.
                | ATSValueError: Text 'text' cannot be empty.
        '''
        check_type(self.columns, int, "columns count 'columns' must be an integer.")
        require_not_satisfied(self.columns < 0, "columns count 'columns' cannot be negative.")
        check_type(self.additional_shifter, int, "additional_shifter must be an integer.")
        require_not_satisfied(self.additional_shifter < 0, "additional_shifter 'additional_shifter' cannot be negative.")
        check_type(self.text, str, "text 'text' must be a string or None.")
        require_not_satisfied(not self.text.strip(), "text 'text' cannot be empty.")

    def merge(self, other: SplashCenterBundle) -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <SplashCenterBundle>
            :exceptions:
                | ATSTypeError: Other must be a SplashCenterBundle instance.
        '''
        check_type(other, SplashCenterBundle, "other must be a SplashCenterBundle instance.")

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the SplashCenterBundle instance to a dictionary.

            :return: Dictionary representation of the SplashCenterBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return asdict(self)
