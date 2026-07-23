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

from ats_utilities.utils.ifactory import IFactory
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.setup.factory import CheckerFactory
from ats_utilities.reporter.theme.engine import ConsoleTheme
from ats_utilities.logger.engine import Logger
from ats_utilities.logger.setup.factory import LoggerFactory
from ats_utilities.reporter.setup.bundle import ReporterBundle
from ats_utilities.reporter.setup.registry import ReporterRegistry

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ReporterFactory(IFactory[ReporterBundle, None]):
    '''
        Factory for creating reporter bundle instance.

        It defines:

            :methods:
                | create_default_bundle - Creates a default reporter bundle with pre-configured options.
    '''

    @classmethod
    @override
    def create_default_bundle(cls, options: None = None) -> ReporterBundle:
        '''
            Creates a default reporter bundle with pre-configured options.

            :param options: Pre-configured options for the bundle (default None).
            :type options: None
            :return: Default reporter bundle instance.
            :rtype: ReporterBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Checker must be provided.
                | ATSValueError: Theme must be provided.
                | ATSValueError: Logger must be provided.
                | ATSTypeError: Bundle must be an instance of ReporterBundle.
                | ATSTypeError: Checker must be an instance of IChecker interface.
                | ATSTypeError: Theme must be an instance of IConsoleTheme interface.
                | ATSTypeError: Logger must be an instance of ILogger interface.
        '''
        checker: Checker = Checker(own=CheckerFactory.create_default_bundle())
        theme: ConsoleTheme = ConsoleTheme()
        logger: Logger = Logger(own=LoggerFactory.create_default_bundle())

        return ReporterRegistry.create_bundle({'checker': checker, 'theme': theme, 'logger': logger})
