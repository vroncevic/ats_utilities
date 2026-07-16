# -*- coding: UTF-8 -*-

'''
Module
    format_error.py
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
    Error formatting functions.
'''

from __future__ import annotations

from traceback import extract_tb

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def get_debug_info(exc: BaseException) -> str:
    '''
        Get debug information about the exception.

        :param exc: Exception to format.
        :type exc: <BaseException>
        :return: String with debug information.
        :rtype: <str>
        :exceptions: None.
    '''
    summary = extract_tb(exc.__traceback__)[-1]

    return f'{summary.filename}:{summary.lineno}'


def format_error_raw(exc: BaseException, debug: bool = False) -> str:
    '''
        Format exception in a raw format (without prefix and without color codes).

        :param exc: Exception to format.
        :type exc: <BaseException>
        :param debug: Whether to include debug information (location of the error in the code).
        :type debug: <bool> (default False)
        :return: Formatted error message.
        :rtype: <str>
        :exceptions: None.
    '''
    if debug:
        return f'{exc} at ({get_debug_info(exc)})'

    return f'{exc}'


def format_error(exc: BaseException, prefix: str = '', debug: bool = False) -> str:
    '''
        Format exception in a human-readable format.

        :param exc: Exception to format.
        :type exc: <BaseException>
        :param prefix: Prefix to add to the error message (unexpected exception).
        :type prefix: <str>
        :param debug: Whether to include debug information (location of the error in the code).
        :type debug: <bool> (default False)
        :return: Formatted error message.
        :rtype: <str>
        :exceptions: None.
    '''
    msg = f'{prefix} {exc}' if prefix else str(exc)

    if debug:
        return f'\x1b[31m{msg} at ({get_debug_info(exc)})\x1b[0m\n'

    return f'\x1b[31m{msg}\x1b[0m\n'
