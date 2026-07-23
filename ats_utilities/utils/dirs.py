# -*- coding: UTF-8 -*-

'''
Module
    dirs.py
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
    Defines factory directory utility functions.
'''

from __future__ import annotations

from pathlib import Path

from ats_utilities.exceptions import ATSValueError
from ats_utilities.validation.context_error import raise_error
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def check_dir_exists(
    dir_path: str,
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> None:
    '''
        Checks if a directory exists.

        :param dir_path: Path to the directory.
        :type dir_path: str
        :param exc_context: Context representation in string format.
        :type exc_context: str | None
        :param exc_message: Message to include in the exception message.
        :type exc_message: str | None
        :param exc_class: The exception class to raise if value is None.
        :type exc_class: type[BaseException] (default ATSValueError)
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    istype(dir_path, str, exc_context, exc_message)

    if not dir_path:
        raise_error(
            fallback_context=r'dirs::check_dir_exists(...)',
            fallback_msg=r'directory path must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    if not Path(dir_path).is_dir():
        raise_error(
            fallback_context=r'dirs::check_dir_exists(...)',
            fallback_msg=f'directory at the provided path does not exist: {dir_path}',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )
