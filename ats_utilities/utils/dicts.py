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

from collections.abc import Container, Mapping, Sequence

from ats_utilities.exceptions import ATSValueError
from ats_utilities.validation.context_error import raise_error
from ats_utilities.validation.check_type import istype

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


def cherry_pick_dict[K, V](source: Mapping[K, V] | None, keys: Container[object] | None) -> dict[K, V]:
    '''
        Cherry picks keys from a source dictionary.

        :param source: The source dictionary from which to pick keys.
        :param keys: The set of keys to pick from the source dictionary.
        :return: The dictionary with cherry picked keys.
        :exceptions: None.
    '''
    if not source or not keys:
        return {}

    return {key: source[key] for key in keys if key in source}


def has_required_keys[K, V](source: Mapping[K, V], keys: Container[object] | None) -> bool:
    '''
        Checks if all required keys are present in the source dictionary.

        :param source: The source dictionary to check.
        :param keys: The set of mandatory keys.
        :return: True (passed), False (failed).
        :exceptions: None.
    '''
    return keys.issubset(source or {})


def is_present_key[K, V](mapping: Mapping[K, V], key: K) -> bool:
    '''
        Checks if a key is present in a mapping.

        :param mapping: The mapping to check.
        :param key: The key to check.
        :return: True if the key is present in the mapping, False otherwise.
        :exceptions: None.
    '''
    return key in mapping


def is_present_required_key[K, V](
    mapping: Mapping[K, V],
    key: K,
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> None:
    '''
        Raises an exception if a key is not present or is None in a mapping.

        :param mapping: The mapping to check.
        :param key: The key to check.
        :param exc_context: The context representation in string format.
        :param exc_message: The message to include in the exception message.
        :param exc_class: The exception class to raise if the key is not present or is None.
        :exceptions:
            | ATSTypeError: Parameters (mapping and key) types validation failed.
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    istype(mapping, Mapping, exc_context, exc_message)

    if key not in mapping:
        raise_error(
            fallback_context='dicts::is_present_required_key(...)',
            fallback_msg=f'the mapping is missing the required key: {key}',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    if mapping[key] is None:
        raise_error(
            fallback_context='dicts::is_present_required_key(...)',
            fallback_msg=f'the mapping key {key} is None',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )


def require_keys(
    source: Mapping[object, object],
    keys: frozenset[str],
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> None:
    '''
        Requires all keys to be present in the source dictionary.

        :param source: The source dictionary to check.
        :param keys: The set of mandatory keys.
        :param exc_context: The context representation in string format.
        :param exc_message: The message to include in the exception message.
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
            fallback_context='dicts::require_keys(...)',
            fallback_msg=f'the mapping is missing required keys: {missing}',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )


def get_first_available(
    source: Mapping[object, object],
    keys: Sequence[object],
    exc_context: str | None = None,
    exc_message: str | None = None
) -> object | None:
    '''
        Retrieves the first available value from a list of keys in priority order.
        Simulates the logic of: source.get(key1) or source.get(key2) ...

        :param source: The source dictionary/mapping to search.
        :param keys: The sequence of keys to check in order of priority.
        :param exc_context: The context representation in string format.
        :param exc_message: The message to include in the exception message.
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
