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
    Defines vreport decorator for automatic console logging via templates.
    Utility for proxy reporting that borrows IReporter from class instances
    and supports multiple message templates and variables.
'''

from __future__ import annotations

from collections.abc import Callable
from re import findall
from functools import wraps
from typing import Any, cast

from ats_utilities.factory_context_error import raise_context_error
from ats_utilities.exceptions import ATSAttributeError, ATSRuntimeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'

def vreport[F: Callable[..., Any]](templates: str | list[str]) -> Callable[[F], F]:
    '''
        Decorator supporting class methods and property operations.
        Borrows the reporter object and verbose flag dynamically from the 
        class instance to automatically format and report status messages.
        Supports single or multiple message templates with multiple variables.

        :param templates: Single template string or a list of template strings.
        :type templates: <str | list[str]>
        :return: Wrapped function.
        :rtype: <Callable[[F], F]>
        :exceptions:
            | ATSRuntimeError: Decorator cannot be used on a standalone function.
            | ATSAttributeError: Class is required to provide a '_reporter' object to
            |                    use the @vreport decorator.
    '''
    message_templates: list[str] = [templates] if isinstance(templates, str) else templates

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            self_instance = args[0] if args else None

            if self_instance is None:
                raise_context_error(
                    fallback_prefix='vreport::decorator',
                    fallback_msg=f'Decorator @vreport on {func.__name__} can only be used on class methods.',
                    exc_message_path=None,
                    exception_class=ATSRuntimeError,
                depth=3
            )

            class_name = self_instance.__class__.__name__

            # BORROWING: Extracting reporter from the instance
            reporter = getattr(
                self_instance, '_reporter',
                getattr(self_instance, f'_{class_name}_reporter', None)
            )

            # BORROWING: Extracting verbose flag from the instance
            is_verbose = getattr(
                self_instance, '_verbose',
                getattr(self_instance, f'_{class_name}_verbose', False)
            )

            if reporter is None:
                raise_context_error(
                    fallback_prefix='vreport::decorator',
                    fallback_msg=f"Class '{class_name}' is required to provide a '_reporter' object to use the @vreport decorator.",
                    exc_message_path=None,
                    exception_class=ATSAttributeError,
                    depth=3
                )

            # Executing the original method first to get updated state (critical for setters)
            result = func(*args, **kwargs)

            final_messages: list[str] = []

            for template in message_templates:
                placeholders = findall('\{([^}]+)\}', template)
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
