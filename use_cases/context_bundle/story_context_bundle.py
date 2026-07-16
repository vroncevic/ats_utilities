# -*- coding: utf-8 -*-

'''
Module
    story_context_bundle.py
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
    Use cases for ATS context bundle.
'''

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.context.context_registry import ContextRegistry
from ats_utilities.checker.engine import Checker
from ats_utilities.reporter.engine import Reporter
from ats_utilities.reporter.theme.engine import ConsoleTheme 
from ats_utilities.reporter.reporter_bundle import ReporterBundle
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

#
# default [without DI]
# ======================
#
ats_context_bundle: ContextBundle = ContextRegistry.create_default_context_bundle()
print(ats_context_bundle)
print(50 * '=')
print(ats_context_bundle.checker)
print(50 * '=')
print(ats_context_bundle.reporter)
print(50 * '=')
print(ats_context_bundle.verbose)
print(50 * '=')

try:
    object.__setattr__(ats_context_bundle, 'checker', None)
    ats_context_bundle.validate()
except ATSValueError as exc:
    print(f'{exc}')
print(50 * '=')

ats_context_bundle_2: ContextBundle = ContextRegistry.create_default_context_bundle()
print(ats_context_bundle_2)
print(50 * '=')

try:
    object.__setattr__(ats_context_bundle_2, 'reporter', None)
    ats_context_bundle_2.validate()
except ATSValueError as exc:
    print(f'{exc}')
print(50 * '=')

ats_context_bundle_3: ContextBundle = ContextRegistry.create_default_context_bundle()
print(ats_context_bundle_3)
print(50 * '=')

try:
    object.__setattr__(ats_context_bundle_3, 'verbose', 2)
    ats_context_bundle_3.validate()
except ATSTypeError as exc:
    print(f'{exc}')
print(50 * '=')
