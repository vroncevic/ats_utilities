# -*- coding: utf-8 -*-

'''
Module
    story_context_bundle_simple_di.py
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
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.checker_registry import CheckerRegistry
from ats_utilities.logger.engine import Logger
from ats_utilities.logger.logger_registry import LoggerRegistry
from ats_utilities.reporter.engine import Reporter
from ats_utilities.reporter.reporter_registry import ReporterRegistry
from ats_utilities.reporter.theme.engine import ConsoleTheme 
from ats_utilities.reporter.reporter_bundle import ReporterBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

#
# [with simple  DI]
# ==================
#
mychecker: Checker = Checker(component_bundle=CheckerRegistry.create_default_checker_bundle())
mylogger: Logger = Logger(component_bundle=LoggerRegistry.create_default_logger_bundle())
myreporter: Reporter = Reporter(component_bundle=ReporterRegistry.create_default_reporter_bundle())

ats_context_bundle_di: ContextBundle = ContextBundle(
    checker=mychecker,
    logger=mylogger,
    reporter=myreporter,
    verbose=True
)
print(ats_context_bundle_di)
print(ats_context_bundle_di.checker)
print(ats_context_bundle_di.reporter)
print(ats_context_bundle_di.verbose)
print(50 * '=')
