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

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def raise_error(
    fallback_context: str,
    fallback_msg: str,
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> None:
    '''
        Raises a contextual exception using caller context.

        :param fallback_context: Fallback prefix to use in the exception message if no message is provided.
        :type fallback_context: <str>
        :param fallback_msg: Fallback message to include in the exception message if no message is provided.
        :type fallback_msg: <str>
        :param exc_context: Context representation in string format.
        :type exc_context: <str | None>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exc_class: The exception class to raise.
        :type exc_class: <type[BaseException]> (default ATSValueError)
        :exceptions:
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    if exc_message is None or exc_context is None:
        raise exc_class(f'{fallback_context} - {fallback_msg}')

    raise exc_class(f'{exc_context} - {exc_message}')
