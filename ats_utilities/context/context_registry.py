# -*- coding: UTF-8 -*-

'''
Module
    context_registry.py
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
    Encapsulates core runtime components for simplification of ContextBundle creation.
'''

from __future__ import annotations

from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.checker_registry import CheckerRegistry
from ats_utilities.logger.engine import Logger
from ats_utilities.logger.logger_registry import LoggerRegistry
from ats_utilities.reporter.engine import Reporter
from ats_utilities.reporter.reporter_bundle import ReporterBundle
from ats_utilities.reporter.theme.engine import ConsoleTheme
from ats_utilities.context.context_bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ContextRegistry(IRegistry[ContextBundle]):
    '''
        Encapsulates core runtime components for simplification of ContextBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a ContextBundle instance.
                | create_default_context_bundle - Creates a default ContextBundle.
    '''

    @classmethod
    @override
    def create_bundle(cls, **kwargs: Any) -> ContextBundle:
        '''
            Creates a ContextBundle instance using optional verbose parameter.

            :param kwargs: Additional registry-specific orchestration parameters.
            :return: ContextBundle instance.
            :rtype: <ContextBundle>
            :exceptions:
                | ATSValueError: Verbose must be provided.
                | ATSTypeError: Verbose must be a boolean.
        '''
        verbose: bool = kwargs.get('verbose')

        return cls.create_default_context_bundle(
            verbose=verbose
        )

    @classmethod
    def create_default_context_bundle(cls, verbose: bool = False) -> ContextBundle:
        '''
            Creates a default ContextBundle with pre-configured components.

            :param verbose: Enables verbose output (default False).
            :type verbose: <bool>
            :return: Default ContextBundle instance.
            :rtype: <ContextBundle>
            :exceptions: None.
        '''
        checker: Checker = Checker(component_bundle=CheckerRegistry.create_default_checker_bundle())
        theme: ConsoleTheme = ConsoleTheme()
        logger: Logger = Logger(component_bundle=LoggerRegistry.create_default_logger_bundle())
        reporter_bundle: ReporterBundle = ReporterBundle(checker=checker, theme=theme, logger=logger)
        reporter: Reporter = Reporter(component_bundle=reporter_bundle)

        return ContextBundle(
            checker=checker,
            logger=logger,
            reporter=reporter,
            verbose=verbose
        )
