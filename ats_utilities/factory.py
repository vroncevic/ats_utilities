# -*- coding: utf-8 -*-

'''
Module
    factory.py
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
    Defines a helper function for component instantiation.
    Provides a simple factory mechanism for dependency injection.
'''

from typing import Any, List, Dict, Tuple, Type, Optional, Union
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

def inject(instance: Any, *dependencies: Tuple[str, Any, Any, Optional[Union[str, List[str], Tuple[str, ...]]]]) -> None:
    '''
        Universally injects system or domain components into a class instance.
        Adheres to SOLID principles by avoiding hardcoded component names or classes.
        Dynamically handles multi-dependency relationship chains between sequence steps.

        :param instance: The object instance (self) to inject attributes into.
        :type instance: <Any>
        :param dependencies: Variadic sequence of tuples containing injection rules.
                             Format: ('attr_name', value, fallback, 'depends_on_attr')
                             The 'depends_on_attr' can be a string, list, or tuple.
        :type dependencies: <Tuple[str, Any, Any, Optional[Union[str, List[str], Tuple[str, ...]]]]>
        :exceptions: None
    '''
    class_name = instance.__class__.__name__
    prefix = f'_{class_name}__'

    for tuple_data in dependencies:
        attr_name: str = tuple_data[0]
        passed_val: Any = tuple_data[1]
        fallback: Any = tuple_data[2]
        depends_on: Optional[Union[str, List[str], Tuple[str, ...]]] = tuple_data[3] if len(tuple_data) > 3 else None

        full_attr_name = f'{prefix}{attr_name}'

        if passed_val is not None:
            resolved_val = passed_val
        else:
            if isinstance(fallback, type):
                if depends_on:

                    if isinstance(depends_on, str):
                        dep_list = [depends_on]
                    else:
                        dep_list = list(depends_on)

                    factory_kwargs = {}
                    for dep in dep_list:
                        target_dep_name = f'{prefix}{dep}'
                        dependency_obj = instance.__dict__.get(target_dep_name)

                        if dependency_obj is not None:
                            factory_kwargs[dep] = dependency_obj

                    resolved_val = fallback(**factory_kwargs)
                else:
                    resolved_val = fallback()
            else:
                resolved_val = fallback

        setattr(instance, full_attr_name, resolved_val)

def get_private_attr(instance: Any, attr_name: str) -> Any:
    '''
        Dynamically retrieves a name-mangled private attribute from an instance.

        :param instance: The class instance (self) containing the attribute
        :type instance: <Any>
        :param attr_name: The target private attribute name (e.g., '__checker')
        :type attr_name: <str>
        :return: The resolved attribute value
        :rtype: <Any>
        :exceptions: AttributeError
    '''
    class_name = instance.__class__.__name__
    clean_attr = attr_name.lstrip('_')
    return getattr(instance, f'_{class_name}__{clean_attr}')

def make_component(passed_obj: Any, default_class: Any, factory_args: Optional[Dict[str, Any]] = None) -> Any:
    '''
        Creates a component instance or returns an existing one.

        :param passed_obj: An existing component instance or None
        :type passed_obj: <Any>
        :param default_class: The class to instantiate if passed_obj is None
        :type default_class: <Any>
        :param factory_args: Arguments to pass to the default_class constructor | None
        :type factory_args: <Optional[Dict[str, Any]]>
        :return: An instance of the component
        :rtype: <Any>
        :exceptions: None
    '''
    if passed_obj is not None:
        return passed_obj

    if factory_args is None:
        factory_args = {}

    return default_class(**factory_args)

def validate_component(instance: Any, expected_class: Type[Any], component_name: str) -> None:
    '''
        Validates if a component instance is of the expected class type.
        Raises an ATSTypeError if the validation fails.

        :param instance: The resolved component instance to check
        :type instance: <Any>
        :param expected_class: The expected concrete class type
        :type expected_class: <Type[Any]>
        :param component_name: Name of the component for the error message
        :type component_name: <str>
        :exceptions: ATSTypeError
    '''
    if not isinstance(instance, expected_class):
        raise ATSTypeError(f"Failed to initialize default {component_name} component.")

def format_instance_to_string(instance: Any) -> str:
    '''
        Generates a standardized string representation for any class instance.
        Cleans name-mangled private attributes and appends memory addresses in hex.

        :param instance: The class instance to format.
        :type instance: <Any>
        :return: String representation of the instance.
        :rtype: <str>
        :exceptions: None
    '''
    class_name = instance.__class__.__name__
    prefix = f'_{class_name}__'

    formatted_lines: List[str] = []
    for k, v in instance.__dict__.items():
        clean_key = k[len(prefix):] if k.startswith(prefix) else k
        val_str = str(v).replace('\n', '\n    ')

        v_id_hex = f'0x{id(v):x}'
        if f'at {v_id_hex}' not in val_str:
            if isinstance(v, (str, int, float, bool)):
                val_str = f"'{val_str}' at {v_id_hex}" if isinstance(v, str) else f"{val_str} at {v_id_hex}"
            else:
                val_str = f"{val_str} at {v_id_hex}"

        formatted_lines.append(f'    {clean_key}={val_str}')

    formatted_attrs = ',\n'.join(formatted_lines)

    if not formatted_attrs:
        return f'{class_name} at 0x{id(instance):x}'

    return f'{class_name}(\n{formatted_attrs}\n) at 0x{id(instance):x}'
