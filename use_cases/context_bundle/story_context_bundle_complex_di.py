# -*- coding: utf-8 -*-

'''
Module
    story_context_bundle_complex_di.py
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

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.engine import Checker
from ats_utilities.reporter.engine import Reporter
from ats_utilities.reporter.theme.engine import ConsoleTheme 
from ats_utilities.reporter.component_bundle import ReporterComponentBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'

#
# [with complex DI]
# ==================
#
mychecker: Checker = Checker()
mytheme: ConsoleTheme = ConsoleTheme()
component_bundle: ReporterComponentBundle = ReporterComponentBundle(
    checker=mychecker,
    theme=mytheme
)

myreporter: Reporter = Reporter(component_bundle=component_bundle)

ats_context_bundle_di: ContextBundle = ContextBundle(
    checker=mychecker,
    reporter=myreporter,
    verbose=True
)
print(ats_context_bundle_di)
print(ats_context_bundle_di.checker)
print(ats_context_bundle_di.reporter)
print(ats_context_bundle_di.verbose)
print(50 * '=')
