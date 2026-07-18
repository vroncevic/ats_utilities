# -*- coding: UTF-8 -*-

'''
Module
    context_error.py
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
    Utility functions for inspecting call stack and raising contextual exceptions.
'''

from __future__ import annotations

from inspect import currentframe
from types import FrameType

from ats_utilities.exceptions import ATSValueError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def get_caller(depth: int = 1) -> str:
    '''
        Extracts the call context (class_name::method_name or just method_name)
        from the specified stack depth.

        :param depth: Stack depth to inspect (1 for direct caller).
        :type depth: <int>
        :return: Context representation in string format.
        :rtype: <str>
        :exceptions: None.
    '''
    frame: FrameType = currentframe()

    for _ in range(depth):
        if frame is not None:
            frame = frame.f_back

    if frame is None:
        return 'unknown'

    method_name: str = frame.f_code.co_name
    class_name: str | None = None

    if 'self' in frame.f_locals:
        class_name = type(frame.f_locals['self']).__name__.lower()
    elif 'cls' in frame.f_locals:
        class_name = frame.f_locals['cls'].__name__.lower()

    return f'{class_name}::{method_name}' if class_name else method_name


def raise_error(
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

    context: str = get_caller(depth=depth)
    raise exception_class(f'{context} - {exc_message}')
