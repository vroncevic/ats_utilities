# -*- coding: UTF-8 -*-

'''
Module
    factory_context_error.py
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
    Defines factory context error utility functions.
'''

from __future__ import annotations

from ats_utilities.exceptions import ATSValueError
from ats_utilities.factory_inspector import get_caller_context

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def raise_context_error(
    fallback_prefix: str,
    fallback_msg: str,
    exc_message: str | None = None,
    exception_class: type[Exception] = ATSValueError,
    depth: int = 2
) -> None:
    '''
        Raises a contextual exception using caller context from the specified stack depth.

        :param fallback_prefix: Fallback prefix to use in the exception message if no message is provided.
        :type fallback_prefix: <str>
        :param fallback_msg: Fallback message to include in the exception message if no message is provided.
        :type fallback_msg: <str>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exception_class: The exception class to raise.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :param depth: Stack depth to inspect.
        :type depth: <int> (default 2)
        :exceptions:
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    if exc_message is None:
        raise exception_class(f'{fallback_prefix} - {fallback_msg}')

    context = get_caller_context(depth=depth)
    raise exception_class(f'{context} - {exc_message}')
