# -*- coding: UTF-8 -*-

'''
Module
    dicts.py
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
    Defines factory dict utility functions.
'''

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from ats_utilities.exceptions import ATSValueError
from ats_utilities.validation.context_error import raise_error
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def cherry_pick_dict(source: Mapping[Any, Any], keys: frozenset[str]) -> dict[Any, Any]:
    '''
        Cherry picks keys from a source dictionary.

        :param source: Source dictionary from which to pick keys.
        :param keys: Set of keys to pick from the source dictionary.
        :return: Dictionary with cherry picked keys.
        :exceptions: None.
    '''
    if not source or not keys:
        return {}

    return {key: source[key] for key in keys if key in source}


def has_required_keys(source: Mapping[Any, Any], keys: frozenset[str]) -> bool:
    '''
        Checks if all required keys are present in the source dictionary.

        :param source: Source dictionary to check.
        :param keys: Set of mandatory keys.
        :return: True (passed), False (failed).
        :exceptions: None.
    '''
    return keys.issubset(source or {})


def require_keys(
    source: Mapping[Any, Any],
    keys: frozenset[str],
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> None:
    '''
        Requires all keys to be present in the source dictionary.

        :param source: Source dictionary to check.
        :param keys: Set of mandatory keys.
        :param exc_context: Context representation in string format.
        :param exc_message: Message to include in the exception message.
        :param exc_class: The exception class to raise if value is None.
        :exceptions:
            | ATSTypeError: Parameters (source and keys) types validation failed.
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    istype(source, Mapping, exc_context, exc_message)
    istype(keys, frozenset, exc_context, exc_message)

    if not has_required_keys(source, keys):
        missing = list(keys - frozenset(source.keys() if source else []))

        raise_error(
            fallback_context=r'dicts::require_keys(...)',
            fallback_msg=f'mapping is missing required keys: {missing}',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )


def get_first_available(
    source: Mapping[Any, Any],
    keys: Sequence[Any],
    exc_context: str | None = None,
    exc_message: str | None = None
) -> Any | None:
    '''
        Retrieves the first available value from a list of keys in priority order.
        Simulates the logic of: source.get(key1) or source.get(key2) ...

        :param source: Source dictionary/mapping to search.
        :param keys: Sequence of keys to check in order of priority.
        :param exc_context: Context representation in string format.
        :param exc_message: Message to include in the exception message.
        :return: The first non-empty value found, or None if none of the keys exist/have value.
        :exceptions:
            | ATSTypeError: Parameters (source and keys) types validation failed.
    '''
    istype(source, Mapping, exc_context, exc_message)
    istype(keys, Sequence, exc_context, exc_message)

    if not source or not keys:
        return None

    for key in keys:
        value = source.get(key)

        if bool(value) or value == 0 or value == False:
            return value

    return None
