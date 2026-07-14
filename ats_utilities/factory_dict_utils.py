# -*- coding: UTF-8 -*-

'''
Module
    factory_dict_utils.py
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

from typing import Any
from collections.abc import Mapping

from ats_utilities.exceptions import ATSValueError
from ats_utilities.factory_context_error import raise_context_error
from ats_utilities.factory_type import check_type

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def cherry_pick_dict(source: Mapping[Any, Any], keys: frozenset[str]) -> dict[Any, Any]:
    '''
        Cherry picks keys from a source dictionary.

        :param source: Source dictionary from which to pick keys.
        :type source: <Mapping[Any, Any]>
        :param keys: Set of keys to pick from the source dictionary.
        :type keys: <frozenset[str]>
        :return: Dictionary with cherry picked keys.
        :rtype: <dict[Any, Any]>
        :exceptions: None.
    '''
    if not source or not keys:
        return {}

    return {key: source[key] for key in keys if key in source}


def has_required_keys(source: Mapping[Any, Any], keys: frozenset[str]) -> bool:
    '''
        Checks if all required keys are present in the source dictionary.

        :param source: Source dictionary to check.
        :type source: <dict[Any, Any]>
        :param keys: Set of mandatory keys.
        :type keys: <frozenset[str]>
        :return: True (passed), False (failed).
        :rtype: <bool>
        :exceptions: None.
    '''
    return keys.issubset(source or {})


def require_keys(
    source: Mapping[Any, Any],
    keys: frozenset[str],
    exc_message: str | None = None,
    exception_class: type[BaseException] = ATSValueError
) -> None:
    '''
        Requires all keys to be present in the source dictionary.

        :param source: Source dictionary to check.
        :type source: <Mapping[Any, Any]>
        :param keys: Set of mandatory keys.
        :type keys: <frozenset[str]>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exception_class: The exception class to raise if value is None.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :exceptions:
            | ATSTypeError: Parameters (source and keys) types validation failed.
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    check_type(source, Mapping, exc_message)
    check_type(keys, frozenset, exc_message)

    if not has_required_keys(source, keys):
        missing = list(keys - frozenset(source.keys() if source else []))

        raise_context_error(
            fallback_prefix=r'factory_dict_utils::require_keys',
            fallback_msg=f'mapping is missing required keys: {missing}',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )
