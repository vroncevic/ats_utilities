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
    Factory for creating reporter bundle instance.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.setup.ifactory import IFactory
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.setup.factory import CheckerFactory
from ats_utilities.reporter.theme.engine import ConsoleTheme
from ats_utilities.logger.engine import Logger
from ats_utilities.logger.setup.factory import LoggerFactory
from ats_utilities.reporter.setup.bundle import ReporterBundle
from ats_utilities.reporter.setup.registry import ReporterRegistry
from ats_utilities.reporter.setup.dependencies import ReporterDependencies
from ats_utilities.reporter.setup.options import ReporterOptions
from ats_utilities.reporter.setup.opt_validator import ReporterOptionsValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ReporterFactory(IFactory[ReporterBundle, ReporterOptions]):
    '''
        Factory for creating reporter bundle instance.

        It defines:

            :methods:
                | create_bundle - Creates a reporter bundle with optional pre-configured options.
    '''

    @classmethod
    @override
    def create_bundle(cls, options: ReporterOptions | None = None) -> ReporterBundle:
        '''
            Creates a reporter bundle with optional pre-configured options.

            :param options: Pre-configured options for the bundle (default None).
            :type options: ReporterOptions | None
            :return: Reporter bundle instance.
            :rtype: ReporterBundle
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a Mapping.
                | ATSTypeError: Checker options must be a Mapping.
                | ATSTypeError: Theme options must be a Mapping.
                | ATSTypeError: Logger options must be a Mapping.
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Checker must be provided.
                | ATSValueError: Theme must be provided.
                | ATSValueError: Logger must be provided.
                | ATSTypeError: Bundle must be an instance of ReporterBundle.
                | ATSTypeError: Checker must be an instance of IChecker interface.
                | ATSTypeError: Theme must be an instance of IConsoleTheme interface.
                | ATSTypeError: Logger must be an instance of ILogger interface.
        '''
        if options is not None:
            ReporterOptionsValidator.validate(options)

        checker_opts = options.get('checker') if options else None
        logger_opts = options.get('logger') if options else None
        theme_opts = options.get('theme') if options else None

        checker = Checker(own=CheckerFactory.create_bundle(checker_opts))
        theme = ConsoleTheme(palette=theme_opts)
        logger = Logger(own=LoggerFactory.create_bundle(logger_opts))

        return ReporterRegistry.create_bundle(
            dependencies=ReporterDependencies(
                checker=checker,
                theme=theme,
                logger=logger
            )
        )
