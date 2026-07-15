# -*- coding: UTF-8 -*-

'''
Module
    factory_format_error.py
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
    Factory error formatting function.
'''

from __future__ import annotations

from traceback import extract_tb
from typing import Any

from ats_utilities.factory_class import cls_name

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def format_error_raw(instance: Any, exc: Exception, debug: bool = False) -> str:
    '''
        Format exception in a raw format (without prefix and without color codes).

        :param instance: Instance of the class.
        :type instance: <Any>
        :param exc: Exception to format.
        :type exc: <Exception>
        :param debug: Whether to include debug information (location of the error in the code).
        :type debug: <bool> (default False)
        :return: Formatted error message.
        :rtype: <str>
        :exceptions: None.
    '''
    if debug:
        tb = exc.__traceback__
        summary = extract_tb(tb)[-1]
        filename = summary.filename
        lineno = summary.lineno

        return f'{cls_name(instance)} {exc} (at {filename}:{lineno})'

    return f'{cls_name(instance)} {exc}'


def format_error(instance: Any, exc: Exception, prefix: str = '', debug: bool = False) -> str:
    '''
        Format exception in a human-readable format.

        :param instance: Instance of the class.
        :type instance: <Any>
        :param exc: Exception to format.
        :type exc: <Exception>
        :param prefix: Prefix to add to the error message.
        :type prefix: <str>
        :param debug: Whether to include debug information (location of the error in the code).
        :type debug: <bool> (default False)
        :return: Formatted error message.
        :rtype: <str>
        :exceptions: None.
    '''
    msg = f'{prefix}: {exc}' if prefix else str(exc)

    if debug:
        tb = exc.__traceback__
        summary = extract_tb(tb)[-1]
        filename = summary.filename
        lineno = summary.lineno

        return f'\x1b[31m{cls_name(instance)} {msg} (at {filename}:{lineno})\x1b[0m\n'

    return f'\x1b[31m{cls_name(instance)} {msg}\x1b[0m\n'
