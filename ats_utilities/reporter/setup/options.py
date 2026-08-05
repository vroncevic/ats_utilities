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
    Reporter bundle options for the reporter bundle.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import TypedDict, NotRequired

from ats_utilities.checker.setup.options import CheckerBundleOptions
from ats_utilities.logger.setup.options import LoggerBundleOptions

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ReporterBundleOptions(TypedDict):
    '''
        Reporter bundle options for the reporter bundle.

        It defines:

            :attributes:
                | checker - The checker bundle options for parameters validation.
                | theme - The theme for console output styling.
                | logger - The logger bundle options for messages logging.
    '''

    checker: NotRequired[CheckerBundleOptions]
    theme: NotRequired[Mapping[str, str]]
    logger: NotRequired[LoggerBundleOptions]
