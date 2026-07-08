# -*- coding: UTF-8 -*-

'''
Module
    factory_inspector.py
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
    Factory inspector utility functions.
'''

from __future__ import annotations

from inspect import currentframe
from types import FrameType

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


def get_caller_context(depth: int = 1) -> str:
    '''
        Extracts the call context (class_name::method_name or just method_name)
        from the specified stack depth.

        :param depth: Stack depth to inspect (1 for direct caller).
        :type depth: <int>
        :return: Context representation.
        :rtype: <str>
        :exceptions: None.
    '''
    frame: FrameType = currentframe()

    for _ in range(depth):
        if frame is not None:
            frame = frame.f_back

    if frame is None:
        return r'unknown'

    method_name: str = frame.f_code.co_name
    class_name: str | None = None

    if r'self' in frame.f_locals:
        class_name = type(frame.f_locals[r'self']).__name__.lower()
    elif r'cls' in frame.f_locals:
        class_name = frame.f_locals[r'cls'].__name__.lower()

    return f'{class_name}::{method_name}' if class_name else method_name
