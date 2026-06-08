# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
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
    Defines ats_utilities.exceptions package.
'''

from typing import List
from ats_utilities.exceptions.ats_error import ATSError
from ats_utilities.exceptions.ats_attribute_error import ATSAttributeError
from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
from ats_utilities.exceptions.ats_file_error import ATSFileError
from ats_utilities.exceptions.ats_key_error import ATSKeyError
from ats_utilities.exceptions.ats_lookup_error import ATSLookupError
from ats_utilities.exceptions.ats_parameter_error import ATSParameterError
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

__all__ = [
    'ATSError',
    'ATSAttributeError',
    'ATSBadCallError',
    'ATSFileError',
    'ATSKeyError',
    'ATSLookupError',
    'ATSParameterError',
    'ATSTypeError',
    'ATSValueError'
]