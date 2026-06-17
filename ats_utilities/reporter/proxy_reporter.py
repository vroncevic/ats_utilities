# -*- coding: UTF-8 -*-

'''
Module
    proxy_reporter.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
    Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines vreporter decorator for automatic console logging via templates.
    Utility for proxy reporting that borrows IReporter from class instances
    and supports multiple message templates and variables.
'''

import re
from functools import wraps
from typing import Any, Callable, List, Union, TypeVar, cast

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Allows decorator to remember signature wrapped method
F = TypeVar('F', bound=Callable[..., Any])


def vreporter(templates: Union[str, List[str]]) -> Callable[[F], F]:
    '''
        Decorator supporting class methods and property operations.
        Borrows the reporter object and verbose flag dynamically from the 
        class instance to automatically format and report status messages.
        Supports single or multiple message templates with multiple variables.

        :param templates: Single template string or a list of template strings
        :type templates: <Union[str, List[str]]>
        :return: Wrapped function
        :rtype: <Callable[[F], F]>
        :exceptions: RuntimeError, AttributeError
    '''
    message_templates: List[str] = [templates] if isinstance(templates, str) else templates

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            self_instance = args[0] if args else None

            if not self_instance:
                raise RuntimeError(
                    f"Decorator @verboser on '{func.__name__}' "
                    f"can only be used on class methods."
                )

            class_name = self_instance.__class__.__name__

            # BORROWING: Extracting reporter and verbose flag from the instance
            reporter = getattr(
                self_instance, '_reporter',
                getattr(self_instance, f'_{class_name}__reporter', None)
            )

            is_verbose = getattr(
                self_instance, '_verbose',
                getattr(self_instance, f'_{class_name}__verbose', False)
            )

            if reporter is None:
                raise AttributeError(
                    f"Class '{class_name}' is required to provide "
                    f"a '_reporter' object to use the @verboser decorator."
                )

            # Executing the original method first to get updated state (critical for setters)
            result = func(*args, **kwargs)

            final_messages: List[str] = []

            for template in message_templates:
                placeholders = re.findall(r'\{([^}]+)\}', template)
                format_context = {}

                for placeholder in placeholders:
                    # To prevent infinite recursion via public property getters,
                    # we explicitly check the internal object's __dict__ for 
                    # mangled private, protected, or local attributes first.
                    private_mangled = f'_{class_name}__{placeholder}'
                    protected_name = f'_{placeholder}'

                    if private_mangled in self_instance.__dict__:
                        val = self_instance.__dict__[private_mangled]
                    elif protected_name in self_instance.__dict__:
                        val = self_instance.__dict__[protected_name]
                    elif placeholder in self_instance.__dict__:
                        val = self_instance.__dict__[placeholder]
                    else:
                        # If the attribute isn't directly inside __dict__, we look up via getattr
                        # while avoiding calling properties named identically to the active function.
                        if placeholder != func.__name__:
                            val = getattr(self_instance, placeholder, 'None')
                        else:
                            val = result if result is not None else 'None'

                    format_context[placeholder] = val if val is not None else 'None'

                try:
                    formatted_msg = template.format(**format_context)  # type: ignore
                    final_messages.append(formatted_msg)
                except (KeyError, IndexError, ValueError, TypeError):
                    final_messages.append(template)

            # Forwarding the processed list of messages to the borrowed reporter
            if final_messages:
                reporter.verbose(is_verbose, final_messages)

            return result
        return cast(F, wrapper)
    return decorator
