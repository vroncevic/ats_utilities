# -*- coding: UTF-8 -*-

'''
Module
    factory_value.py
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
    Defines factory value utility functions.
'''

from __future__ import annotations

from typing import Any

from ats_utilities.factory_context_error import raise_context_error
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


def require_not_none(
    value: Any,
    exc_message_path: str | None = None,
    exception_class: type[Exception] = ATSValueError
) -> None:
    '''
        Requires a value to be not None.

        :param value: Value to check.
        :type value: <Any>
        :param exc_message_path: Path and details to include in the exception message.
        :type exc_message_path: <str | None>
        :param exception_class: The exception class to raise if value is None.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :exceptions:
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    if value is None:
        raise_context_error(
            fallback_prefix="factory_value::require_not_none",
            fallback_msg="value must not be None",
            exc_message_path=exc_message_path,
            exception_class=exception_class,
            depth=3
        )


def require_not_empty(
    value: Any,
    exc_message_path: str | None = None,
    exception_class: type[Exception] = ATSValueError
) -> None:
    '''
        Requires a value to be not empty (not None, not empty sequence/mapping).

        :param value: Value to check for emptiness.
        :type value: <Any>
        :param exc_message_path: Path and details to include in the exception message.
        :type exc_message_path: <str | None>
        :param exception_class: The exception class to raise if value is empty.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :exceptions:
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    if not bool(value) and value != 0 and value != False:
        raise_context_error(
            fallback_prefix="factory_value::require_not_empty",
            fallback_msg="value must not be empty",
            exc_message_path=exc_message_path,
            exception_class=exception_class,
            depth=3
        )


def require_not_satisfied(
    status: bool,
    exc_message_path: str | None = None,
    exception_class: type[Exception] = ATSValueError
) -> None:
    '''
        Requires a status to be True (statisfied condition for un happy flow).

        :param status: Status to check (not satisfied).
        :type status: <bool>
        :param exc_message_path: Path and details to include in the exception message (unhappy flow).
        :type exc_message_path: <str | None>
        :param exception_class: The exception class to raise if status is not True.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :exceptions:
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    if status:
        raise_context_error(
            fallback_prefix="factory_value::require_not_satisfied",
            fallback_msg="condition not satisfied",
            exc_message_path=exc_message_path,
            exception_class=exception_class,
            depth=3
        )
