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

from typing import Any, List, Tuple, TypeAlias, Optional
from dataclasses import dataclass

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Type alias for parameter metadata: (parameter name, expected type, actual value)
ParamMetadata: TypeAlias = Tuple[str, str, Any]

@dataclass
class ATSCheckerReporterBundle:
    '''
        Parameter Object pattern wrapper encapsulating all core checker domain elements.
        Simplifies dependency passing and signatures for higher-level managers.

        It defines:

            :attributes:
                | context - Message context (default None).
                | parameters_meta - parameter name and parameter type (default None).
                | err_indices - Error set (default None).
                | is_fmt_err - Check for format error type (default False).
            :methods: None
    '''

    context: Optional[str] = None
    parameters_meta: Optional[List[ParamMetadata]] = None
    err_indices: Optional[List[int]] = None
    is_fmt_err: bool = False
