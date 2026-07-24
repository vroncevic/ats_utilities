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
    Validator for logger dependencies.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.logger.setup.dependencies import LoggerDependencies
from ats_utilities.utils.setup.idep_validator import IDependenciesValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none, not_satisfied

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class LoggerDependenciesValidator(IDependenciesValidator[LoggerDependencies]):
    '''
        Validator for logger dependencies.

        It defines:

            :methods:
                | validate - Validates logger dependencies instance.
    '''

    @classmethod
    @override
    def validate(cls, dependencies: LoggerDependencies) -> None:
        '''
            Validates logger dependencies instance.

            :param dependencies: Logger dependencies instance to be validated.
            :type dependencies: LoggerDependencies
            :exceptions:
                | ATSValueError: Dependencies must be provided.
                | ATSTypeError: Dependencies must be a Mapping.
                | ATSTypeError: Log file must be a string.
                | ATSTypeError: Log level must be an integer.
                | ATSTypeError: Logger must be an ILogger or standard logging.Logger instance.
        '''
        ctx: str = r'logger_dependencies_validator::validate(...)'

        not_none(dependencies, ctx, r'dependencies must be provided')
        istype(dependencies, Mapping, ctx, r'dependencies must be a Mapping')

        log_file = dependencies.get('log_file')

        if log_file is not None:
            istype(log_file, str, ctx, r'log file must be a string')

        log_level = dependencies.get('log_level')

        if log_level is not None:
            istype(log_level, int, ctx, r'log level must be an integer')

        logger = dependencies.get('logger')

        if logger is not None:
            not_satisfied(
                not (hasattr(logger, 'info') or hasattr(logger, 'write_log')), ctx,
                r'logger must be an ILogger instance or a standard logging.Logger instance'
            )
