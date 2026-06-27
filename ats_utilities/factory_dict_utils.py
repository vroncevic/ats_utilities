# -*- coding: utf-8 -*-

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

from typing import Any
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


def cherry_pick_dict(source: dict[Any, Any] | None, keys: frozenset[str]) -> dict[Any, Any]:
    '''
        Cherry picks keys from a source dictionary.

        :param source: Source dictionary from which to pick keys | None.
        :type source: <dict[Any, Any] | None>
        :param keys: Set of keys to pick from the source dictionary.
        :type keys: <frozenset[str]>
        :return: Dictionary with cherry picked keys.
        :rtype: <dict[Any, Any]>
        :exceptions: None.
    '''
    if not source or not keys:
        return {}

    return {key: source[key] for key in keys if key in source}


def has_required_keys(source: dict[Any, Any] | None, keys: frozenset[str]) -> bool:
    '''
        Checks if all required keys are present in the source dictionary.

        :param source: Source dictionary to check | None.
        :type source: <dict[Any, Any] | None>
        :param keys: Set of mandatory keys.
        :type keys: <frozenset[str]>
        :return: True (passed), False (failed).
        :rtype: <bool>
        :exceptions: None.
    '''
    return keys.issubset(source or {})


def require_keys(source: dict[Any, Any] | None, keys: frozenset[str]) -> None:
    '''
        Requires all keys to be present in the source dictionary.

        :param source: Source dictionary to check | None.
        :type source: <dict[Any, Any] | None>
        :param keys: Set of mandatory keys.
        :type keys: <frozenset[str]>
        :exceptions:
            | ATSTypeError: Expected dict or None for 'source', got <type>.
            | ATSTypeError: Expected frozenset for 'keys', got <type>.
            | ATSValueError: Missing required keys.
    '''
    if source is not None and not isinstance(source, dict):
        raise ATSTypeError(f"expected dict or None for 'source', got {type(source).__name__}")

    if not isinstance(keys, frozenset):
        raise ATSTypeError(f"expected frozenset for 'keys', got {type(keys).__name__}")

    missing_keys: frozenset[str] = keys.difference(source or {})

    if missing_keys:
        raise ATSValueError(f'missing required keys {missing_keys}')
