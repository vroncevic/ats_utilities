# -*- coding: UTF-8 -*-

'''
Module
    config_file_bundle.py
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
    Defines parameter bundle data classes for dependency group simplification.
    Encapsulates file check configuration to minimize constructor overhead.
'''

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass(slots=True, kw_only=True)
class ConfigFileBundle:
    '''
        Defines class ConfigFileBundle with attribute(s) and method(s).
        Encapsulates file check configuration to minimize constructor overhead.

        It defines:

            :attributes:
                | context - Context bundle for checker, reporter and verbose (default None).
                | file_checker - Parameters checker implementation (default None).
            :methods:
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from ConfigFileBundle instance into this one.
                | to_dict - Converts the ConfigFileBundle instance to a dictionary.
    '''

    context: ContextBundle | None = None
    file_checker: IFileCheck | None = None

    def validate(self) -> None:
        '''
            Validates that ConfigFileBundle is valid (can be called after merge).
            Performs validation of context and file_checker attributes.
            Context must be non-None and an instance of ContextBundle.
            File_checker must be non-None and an instance of IFileCheck interface.

            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSValueError: File check implementation must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
                | ATSTypeError: File check implementation must be an instance of IFileCheck interface.
        '''
        require_not_none(self.context, 'context bundle must be provided')
        require_not_none(self.file_checker, 'file checker implementation must be provided')
        check_type(self.context, ContextBundle, 'context bundle must be an instance of ContextBundle')
        check_type(self.file_checker, IFileCheck, 'file checker implementation must be an instance of IFileCheck interface')

    def merge(self, other: ConfigFileBundle) -> None:
        '''
            Merges non-None values from ConfigFileBundle instance into this one.

            :param other: Another ConfigFileBundle instance to merge into this one.
            :type other: <ConfigFileBundle>
            :exceptions:
                | ATSTypeError: Other must be a ConfigFileBundle instance.
        '''
        check_type(other, ConfigFileBundle, 'other must be a ConfigFileBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the ConfigFileBundle instance to a dictionary.

            :return: Dictionary representation of the ConfigFileBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return asdict(self)
