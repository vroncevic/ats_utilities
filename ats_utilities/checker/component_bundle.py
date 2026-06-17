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

from typing import List, Optional
from dataclasses import dataclass
from ats_utilities.checker.itype_validator import IATSTypeValidator
from ats_utilities.checker.iformat_validator import IATSFormatValidator
from ats_utilities.checker.icontext_provider import IATSContextProvider
from ats_utilities.checker.icheck_reporter import IATSCheckReporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
class ATSCheckerComponentBundle:
    '''
        Parameter Object pattern wrapper encapsulating all core checker domain elements.
        Simplifies dependency passing and signatures for higher-level managers.

        It defines:

            :attributes:
                | format_validator - Validator for parameters format (default None).
                | type_validator - Validator for parameters type (default None).
                | context_provider - Provider for call context (default None).
                | check_reporter - Formatter for message reports (default None).
            :methods: None
    '''

    format_validator: Optional[IATSFormatValidator] = None
    type_validator: Optional[IATSTypeValidator] = None
    context_provider: Optional[IATSContextProvider] = None
    check_reporter: Optional[IATSCheckReporter] = None
