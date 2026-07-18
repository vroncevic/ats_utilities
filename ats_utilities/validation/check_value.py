# -*- coding: UTF-8 -*-

'''
Module
    check_value.py
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
    Defines value checking utility functions.
'''

from __future__ import annotations

from typing import Any

from ats_utilities.validation.context_error import raise_error
from ats_utilities.exceptions import ATSValueError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def not_none(
    value: Any,
    exc_message: str | None = None,
    exception_class: type[BaseException] = ATSValueError
) -> None:
    '''
        Requires a value to be not None.

        :param value: Value to check.
        :type value: <Any>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exception_class: The exception class to raise if value is None.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :exceptions:
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    if value is None:
        raise_error(
            fallback_prefix=r'check_value::not_none',
            fallback_msg=r'value must not be None',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )


def not_empty(
    value: Any,
    exc_message: str | None = None,
    exception_class: type[BaseException] = ATSValueError
) -> None:
    '''
        Requires a value to be not empty (not None, not empty sequence/mapping).

        :param value: Value to check for emptiness.
        :type value: <Any>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exception_class: The exception class to raise if value is empty.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :exceptions:
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    if not bool(value) and value != 0 and value != False:
        raise_error(
            fallback_prefix=r'check_value::not_empty',
            fallback_msg=r'value must not be empty',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )


def not_satisfied(
    status: bool,
    exc_message: str | None = None,
    exception_class: type[BaseException] = ATSValueError
) -> None:
    '''
        Ensures that an unhappy status is NOT True. 
        Raises an exception if status is True (unhappy flow detected).

        :param status: Status which indicates unhappy flow (True = unhappy flow).
        :type status: <bool>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exception_class: The exception class to raise if status is not True.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :exceptions:
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    if status:
        raise_error(
            fallback_prefix=r'check_value::not_satisfied',
            fallback_msg=r'condition not satisfied',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )
