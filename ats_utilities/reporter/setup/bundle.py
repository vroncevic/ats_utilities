# -*- coding: UTF-8 -*-

'''
Module
    bundle.py
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
    Encapsulates reporter runtime components for simplification of reporter bundle creation.
'''

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.utils.reflection import instance_to_dict

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class ReporterBundle:
    '''
        Encapsulates reporter runtime components for simplification of reporter bundle creation.

        It defines:

            :attributes:
                | checker - Checker for parameters validation.
                | theme - Theme for console output styling.
                | logger - Logger for messages logging.
            :methods:
                | to_dict - Converts reporter bundle to a dictionary.
    '''

    checker: IChecker
    theme: IConsoleTheme
    logger: ILogger

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts reporter bundle to a dictionary.

            :return: Dictionary representation of the reporter bundle.
            :rtype: dict[str, Any]
            :exceptions:
                | ATSValueError: Instance must be provided.
                | ATSValueError: Instance must be a dataclass instance.
        '''
        return instance_to_dict(self)
