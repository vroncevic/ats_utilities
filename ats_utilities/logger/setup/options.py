# -*- coding: UTF-8 -*-

'''
Module
    options.py
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
    Logger options for the logger factory bundle.
'''

from __future__ import annotations

from typing import TypedDict, NotRequired

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class LoggerBundleOptions(TypedDict):
    '''
        Logger options for the logger factory bundle.

        It defines:

            :attributes:
                | log_file - The path to the log file for the logger bundle.
                | log_level - The log level for the logger bundle.
                | log_format - The format string for the log messages for the logger bundle.
                | log_datefmt - The date format string for the log messages for the logger bundle.
    '''

    log_file: NotRequired[str | None]
    log_level: NotRequired[int | None]
    log_format: NotRequired[str | None]
    log_datefmt: NotRequired[str | None]
