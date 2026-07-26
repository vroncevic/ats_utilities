# -*- coding: UTF-8 -*-

'''
Module
    component.py
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
from ats_utilities.validation.context_error import raise_error

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


def make_component(
    passed_obj: Any,
    default_class: Any,
    factory_args: Mapping[str, Any] | None = None
) -> Any:
    '''
        Creates a component instance or returns an existing one.

        :param passed_obj: An existing component instance or None.
        :param default_class: The class to instantiate if passed_obj is None.
        :param factory_args: Arguments to ... to the default_class constructor | None.
        :return: An instance of the component.
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
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSTypeError
) -> None:
    '''
        Validates if a component instance is of the expected class type.

        :param instance: The resolved component instance to check.
        :param expected_class: The expected concrete class type.
        :param exc_context: Context representation in string format.
        :param exc_message: Message to include in the exception message.
        :param exc_class: The exception class to raise if value is None.
        :exceptions:
            | Dynamically raises the provided exc_class (e.g., ATSTypeError).
    '''
    if not isinstance(instance, expected_class):
        raise_error(
            fallback_context=r'component::validate_component(...)',
            fallback_msg=f'instance is not of expected type {expected_class}',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )
