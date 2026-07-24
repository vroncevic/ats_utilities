# -*- coding: UTF-8 -*-

'''
Module
    dep_validator.py
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
    Validator for reporter dependencies.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.reporter.setup.dependencies import ReporterDependencies
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.theme.iconsole_theme import IConsoleTheme
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.utils.setup.idep_validator import IDependenciesValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ReporterDependenciesValidator(IDependenciesValidator[ReporterDependencies]):
    '''
        Validator for reporter dependencies.

        It defines:

            :methods:
                | validate - Validates reporter dependencies instance.
    '''

    @classmethod
    @override
    def validate(cls, dependencies: ReporterDependencies) -> None:
        '''
            Validates reporter dependencies instance.

            :param dependencies: Reporter dependencies instance to be validated.
            :type dependencies: ReporterDependencies
            :exceptions:
                | ATSValueError: Dependencies must be provided.
                | ATSTypeError: Dependencies must be a Mapping.
                | ATSTypeError: Checker must be an instance of IChecker interface.
                | ATSTypeError: Theme must be an instance of IConsoleTheme interface.
                | ATSTypeError: Logger must be an instance of ILogger interface.
        '''
        ctx: str = r'reporter_dependencies_validator::validate(...)'

        not_none(dependencies, ctx, r'dependencies must be provided')
        istype(dependencies, Mapping, ctx, r'dependencies must be a Mapping')

        checker = dependencies.get('checker')

        if checker is not None:
            istype(checker, IChecker, ctx, r'checker must be an IChecker instance')

        theme = dependencies.get('theme')

        if theme is not None:
            istype(theme, IConsoleTheme, ctx, r'theme must be an IConsoleTheme instance')

        logger = dependencies.get('logger')

        if logger is not None:
            istype(logger, ILogger, ctx, r'logger must be an ILogger instance')
