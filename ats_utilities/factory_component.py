# -*- coding: utf-8 -*-

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

from typing import Any
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

def make_component(passed_obj: Any, default_class: Any, factory_args: dict[str, Any] | None = None) -> Any:
    '''
        Creates a component instance or returns an existing one.

        :param passed_obj: An existing component instance or None.
        :type passed_obj: <Any>
        :param default_class: The class to instantiate if passed_obj is None.
        :type default_class: <Any>
        :param factory_args: Arguments to pass to the default_class constructor | None.
        :type factory_args: <dict[str, Any] | None>
        :return: An instance of the component.
        :rtype: <Any>
        :exceptions: None.
    '''
    if passed_obj is not None:
        return passed_obj

    if factory_args is None:
        factory_args = {}

    # No dependency injection then use default ones.
    return default_class(**factory_args)

def validate_component(instance: Any, expected_class: type[Any]) -> None:
    '''
        Validates if a component instance is of the expected class type.

        :param instance: The resolved component instance to check.
        :type instance: <Any>
        :param expected_class: The expected concrete class type.
        :type expected_class: <type[Any]>
        :exceptions:
            | ATSTypeError - instance is not of expected class type.
    '''
    if not isinstance(instance, expected_class):
        raise ATSTypeError(f"instance [{type(instance).__name__}] is not of expected type {expected_class.__name__}.")
