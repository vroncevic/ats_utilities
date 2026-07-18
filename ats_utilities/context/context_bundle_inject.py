# -*- coding: UTF-8 -*-

'''
Module
    inject_context_bundle.py
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
    Factory universally injects components (checker, reporter, verbose).
    Encapsulates core utilities to minimize constructor overhead.
    Provides a simple factory mechanism for dependency injection.
'''

from __future__ import annotations

from typing import Any

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.checker.engine import Checker
from ats_utilities.logger.engine import Logger
from ats_utilities.reporter.engine import Reporter
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def inject(instance: Any, *dependencies: tuple[str, Any, Any, str | list[str] | tuple[str, ...] | None]) -> None:
    '''
        Universally injects system or domain components into a class instance.
        Adheres to SOLID principles by avoiding hardcoded component names or classes.
        Dynamically handles multi-dependency relationship chains between sequence steps.

        :param instance: The object instance (self) to inject attributes into.
        :type instance: <Any>
        :param dependencies: Variadic sequence of tuples containing injection rules.
                             Format: ('attr_name', value, fallback, 'depends_on_attr')
                             The 'depends_on_attr' can be a string, list, or tuple.
        :type dependencies: <tuple[str, Any, Any, str | list[str] | tuple[str, ...] | None]>
        :exceptions: None.
    '''
    prefix: str = '_'

    for tuple_data in dependencies:
        attr_name: str = tuple_data[0]
        passed_val: Any = tuple_data[1]
        fallback: Any = tuple_data[2]
        depends_on: str | list[str] | tuple[str, ...] | None = tuple_data[3] if len(tuple_data) > 3 else None

        full_attr_name: str = f'{prefix}{attr_name}'

        if passed_val is not None:
            resolved_val: Any = passed_val
        else:
            if isinstance(fallback, type):
                if depends_on:

                    if isinstance(depends_on, str):
                        dep_list: list[str] = [depends_on]
                    else:
                        dep_list = list(depends_on)

                    factory_kwargs: dict[str, Any] = {}

                    for dep in dep_list:
                        target_dep_name: str = f'{prefix}{dep}'
                        dependency_obj: Any = instance.__dict__.get(target_dep_name)

                        if dependency_obj is not None:
                            factory_kwargs[dep] = dependency_obj

                    resolved_val = fallback(**factory_kwargs)
                else:
                    resolved_val = fallback()
            else:
                resolved_val = fallback

        setattr(instance, full_attr_name, resolved_val)


def inject_context_bundle(instance: Any, ctx: ContextBundle) -> None:
    '''
        Factory universally injects components (checker, reporter, verbose).

        :param instance: The object instance (self) to inject attributes into.
        :type instance: <Any>
        :param ctx: Context bundle (checker, logger, reporter and verbose).
        :type ctx: <ContextBundle>
        :exceptions:
            | ATSValueError: Context bundle must be provided.
            | ATSTypeError: Context bundle must be an instance of ContextBundle.
    '''
    not_none(ctx, f'context must be provided for {instance.__class__.__name__}')
    istype(ctx, ContextBundle, f'context must be an instance of ContextBundle for {instance.__class__.__name__}')

    inject(
        instance,
        ('checker', ctx.checker, Checker, None),
        ('logger', ctx.logger, Logger, None),
        ('reporter', ctx.reporter, Reporter, ['checker', 'logger']),
        ('verbose', ctx.verbose, False, None)
    )
