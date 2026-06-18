# -*- coding: utf-8 -*-

'''
Module
    base_bundle.py
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
    Defines parameter bundle data classes for dependency group simplification.
    Encapsulates core utilities to minimize constructor overhead.
'''

from dataclasses import dataclass
from typing import List, Optional
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.iparser_strategy import IArgParserStrategy
from ats_utilities.option.ioption_parser import IOptionManager

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class ATSBaseBundle:
    '''
        Encapsulates the core metadata management, parsing strategies, and option parsing components.
        Acts as a Parameter Object to simplify constructors for tool-related infrastructure.

        It defines:

            :attributes:
                | info_manager - Metadata and tool information manager implementation (default None)
                | strategy - Argument parsing strategy implementation (default None)
                | options_parser - Command line option parser implementation (default None)
    '''

    info_manager: Optional[IInfoManager] = None
    strategy: Optional[IArgParserStrategy] = None
    options_parser: Optional[IOptionManager] = None
