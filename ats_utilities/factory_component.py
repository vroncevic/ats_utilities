# -*- coding: UTF-8 -*-

'''
Module
    factory_component.py
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
    Factory universally create and validate component instantiation.
    Encapsulates core utilities to minimize constructor overhead.
    Provides a simple factory mechanism for dependency injection.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ats_utilities.exceptions import ATSTypeError
from ats_utilities.factory_context_error import raise_context_error

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


def make_component(
    passed_obj: Any,
    default_class: Any,
    factory_args: Mapping[str, Any] | None = None
) -> Any:
    '''
        Creates a component instance or returns an existing one.

        :param passed_obj: An existing component instance or None.
        :type passed_obj: <Any>
        :param default_class: The class to instantiate if passed_obj is None.
        :type default_class: <Any>
        :param factory_args: Arguments to pass to the default_class constructor | None.
        :type factory_args: <Mapping[str, Any] | None>
        :return: An instance of the component.
        :rtype: <Any>
        :exceptions: None.
    '''
    if passed_obj is not None:
        return passed_obj

    kwargs = dict(factory_args) if factory_args is not None else {}

    # No dependency injection then create using default ones.
    return default_class(**kwargs)


def validate_component(
    instance: Any,
    expected_class: type[Any],
    exc_message_path: str | None = None,
    exception_class: type[Exception] = ATSTypeError
) -> None:
    '''
        Validates if a component instance is of the expected class type.

        :param instance: The resolved component instance to check.
        :type instance: <Any>
        :param expected_class: The expected concrete class type.
        :type expected_class: <type[Any]>
        :param exc_message_path: Path and details to include in the exception message.
        :type exc_message_path: <str | None>
        :param exception_class: The exception class to raise if value is None.
        :type exception_class: <type[Exception]> (default ATSTypeError)
        :exceptions:
            | Dynamically raises the provided exception_class (e.g., ATSTypeError).
    '''
    if not isinstance(instance, expected_class):
        raise_context_error(
            fallback_prefix=r'factory_component::validate_component',
            fallback_msg=f'instance is not of expected type {expected_class}',
            exc_message_path=exc_message_path,
            exception_class=exception_class,
            depth=3
        )
