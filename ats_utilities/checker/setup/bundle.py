# -*- coding: UTF-8 -*-

'''
Module
    bundle.py
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
    Encapsulates the checker runtime components for simplification of the checker bundle.
'''

from __future__ import annotations

from dataclasses import dataclass

from ats_utilities.checker.type.itype_validator import ITypeValidator
from ats_utilities.checker.format.iformat_validator import IFormatValidator
from ats_utilities.checker.context.icontext_provider import IContextProvider
from ats_utilities.checker.reporter.icheck_reporter import ICheckReporter
from ats_utilities.utils.reflection import instance_to_dict

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class CheckerBundle:
    '''
        Encapsulates the checker runtime components for the simplification of the checker bundle.

        It defines:

            :attributes:
                | format_validator - The validator for parameters format.
                | type_validator - The validator for parameters type.
                | context_provider - The provider for method call context.
                | check_reporter - The formatter for message reports.
            :methods:
                | to_dict - Converts the checker bundle to a dictionary.
    '''

    format_validator: IFormatValidator
    type_validator: ITypeValidator
    context_provider: IContextProvider
    check_reporter: ICheckReporter

    def to_dict(self) -> dict[str, object]:
        '''
            Converts the checker bundle to a dictionary.

            :return: The dictionary representation of the checker bundle.
            :exceptions:
                | ATSValueError: The instance must be provided.
                | ATSValueError: The instance must be a dataclass.
        '''
        return instance_to_dict(self)
