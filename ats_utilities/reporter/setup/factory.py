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
    Factory for creating the reporter bundle.
'''

from __future__ import annotations

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
from ats_utilities.reporter.setup.keys import ReporterKeys

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ReporterFactory:
    '''
        Factory for creating the reporter bundle.

        It defines:

            :methods:
                | create_bundle - Creates the reporter bundle with optional pre-configured options.
    '''

    @classmethod
    def create_bundle(cls, options: ReporterOptions | None = None) -> ReporterBundle:
        '''
            Creates the reporter bundle with optional pre-configured options.

            :param options: The pre-configured options for the bundle (default: None).
            :return: The reporter bundle.
            :exceptions:
                | ATSValueError: The options must be provided and have proper values.
                | ATSTypeError:  The options must be an instance of Mapping and its attributes
                |                must be instances of their respective types.
        '''
        if options is not None:
            ReporterOptionsValidator.validate(options)

        checker_opts = options.get(ReporterKeys.OPTION_CHECKER) if options else None
        logger_opts = options.get(ReporterKeys.OPTION_LOGGER) if options else None
        theme_opts = options.get(ReporterKeys.OPTION_THEME) if options else None

        checker = Checker(own=CheckerFactory.create_bundle(options=checker_opts))
        theme = ConsoleTheme(palette=theme_opts)
        logger = Logger(own=LoggerFactory.create_bundle(options=logger_opts))

        return ReporterRegistry.create_bundle(
            dependencies=ReporterDependencies(
                checker=checker,
                theme=theme,
                logger=logger
            )
        )
