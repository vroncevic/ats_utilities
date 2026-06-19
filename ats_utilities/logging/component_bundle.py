# -*- coding: utf-8 -*-

'''
Module
    component_bundle.py
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
    Defines component bundle data classe for dependency group simplification.
    Encapsulates core utilities to minimize constructor overhead.
'''

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from ats_utilities.logging.ilogger import ILogger
from ats_utilities.logging.logger_bundle import LoggerBundle
from ats_utilities.context_bundle import ContextBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class ATSLoggingComponentBundle:
    '''
        Parameter Object pattern wrapper encapsulating all core logging domain elements.
        Simplifies dependency passing and signatures for higher-level managers.

        It defines:

            :attributes:
                | logger - Logger instance (default None)
                | logger_bundle - Bundle with logger parameters (default LoggerBundle)
                | logging_bundle - Bundle with context (default ContextBundle)
    '''

    logger: Optional[ILogger] = None
    logger_bundle: Optional[LoggerBundle] = field(default_factory=LoggerBundle)
    logging_bundle: Optional[ContextBundle] = field(default_factory=ContextBundle)
