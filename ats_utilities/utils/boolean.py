# -*- coding: UTF-8 -*-

'''
Module
    boolean.py
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
    Defines factory boolean utilities.
'''

from __future__ import annotations

from ats_utilities.exceptions import ATSValueError
from ats_utilities.validation.context_error import raise_error

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


def str_bool_to_bool(
    value: str,
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> bool:
    '''
        Converts a string boolean to a boolean.

        :param value: String boolean to convert to a boolean.
        :param exc_context: Context representation in string format.
        :return: Boolean value.
        :exceptions:
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    match value:
        case 'True':
            return True
        case 'False':
            return False
        case _:
            raise_error(
                fallback_context='boolean::str_bool_to_bool(...)',
                fallback_msg=f'can not convert {value} to bool',
                exc_context=exc_context,
                exc_message=exc_message,
                exc_class=exc_class
            )
