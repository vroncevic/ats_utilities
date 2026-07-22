# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating context bundle instance.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.ifactory import IFactory
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.setup.factory import CheckerFactory
from ats_utilities.logger.engine import Logger
from ats_utilities.logger.setup.factory import LoggerFactory
from ats_utilities.reporter.engine import Reporter
from ats_utilities.reporter.setup.registry import ReporterRegistry
from ats_utilities.reporter.theme.engine import ConsoleTheme
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ContextFactory(IFactory[ContextBundle, bool]):
    '''
        Factory for creating context bundle instance.

        It defines:

            :methods:
                | create_default_bundle - Creates a default context bundle with pre-configured options.
    '''

    @classmethod
    @override
    def create_default_bundle(cls, options: bool = False) -> ContextBundle:
        '''
            Creates a default context bundle with pre-configured options.

            :param options: Pre-configured options for the bundle (default False).
            :type options: bool
            :return: Default context bundle instance.
            :rtype: ContextBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Checker must be provided.
                | ATSValueError: Logger must be provided.
                | ATSValueError: Reporter must be provided.
                | ATSValueError: Verbose must be provided.
                | ATSTypeError: Bundle must be an instance of ContextBundle.
                | ATSTypeError: Checker must be an instance of IChecker.
                | ATSTypeError: Logger must be an instance of ILogger.
                | ATSTypeError: Reporter must be an instance of IReporter.
                | ATSTypeError: Verbose must be a boolean.
        '''
        checker: Checker = Checker(own=CheckerFactory.create_default_bundle())
        logger: Logger = Logger(own=LoggerFactory.create_default_bundle())
        theme: ConsoleTheme = ConsoleTheme()
        reporter: Reporter = Reporter(
            own=ReporterRegistry.create_bundle({
                'checker': checker, 'theme': theme, 'logger': logger
            })
        )

        bundle: ContextBundle = ContextBundle(
            checker=checker,
            logger=logger,
            reporter=reporter,
            verbose=options
        )

        ContextValidator.validate(bundle)

        return bundle
