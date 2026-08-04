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

from ats_utilities.exceptions import ATSValueError

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


def raise_error(
    fallback_context: str,
    fallback_msg: str,
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> None:
    '''
        Raises a contextual exception using caller context.

        :param fallback_context: The fallback prefix for exception.
        :param fallback_msg: The fallback suffix for exception.
        :param exc_context: The contextual prefix for exception.
        :param exc_message: The contextual suffix for exception.
        :param exc_class: The exception class to be raised.
        :exceptions:
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    context: str = exc_context if exc_context is not None else fallback_context
    message: str = exc_message if exc_message is not None else fallback_msg

    raise exc_class(f'{context} - {message}')
