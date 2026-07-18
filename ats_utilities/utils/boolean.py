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

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def str_bool_to_bool(
    val: str,
    exc_message: str | None = None,
    exception_class: type[BaseException] = ATSValueError
) -> bool:
    '''
        Converts a string boolean to a boolean.

        :param val: String boolean to convert to a boolean.
        :type val: <str>
        :return: Boolean value.
        :rtype: <bool>
        :exceptions:
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    match val:
        case 'True':
            return True
        case 'False':
            return False
        case _:
            raise_error(
                fallback_prefix=r'boolean::str_bool_to_bool',
                fallback_msg=f'cannot convert {val} to bool',
                exc_message=exc_message,
                exception_class=exception_class,
                depth=3
            )
