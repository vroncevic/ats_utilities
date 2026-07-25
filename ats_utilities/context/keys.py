# -*- coding: UTF-8 -*-

'''
Module
    keys.py
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
    Runtime components and interface constraints for context bundle.
'''

from __future__ import annotations

from typing import ClassVar, override
from types import MappingProxyType

from ats_utilities.utils.setup.ikeys import IKeys
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.setup.options import CheckerOptions
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.setup.options import ReporterOptions
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.logger.setup.options import LoggerOptions

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ContextKeys(IKeys[str, type]):
    '''
        Runtime components and interface constraints for context bundle.

        It defines:

            :attributes:
                | DEPENDENCY_CHECKER: Checker interface constant.
                | DEPENDENCY_LOGGER: Logger interface constant.
                | DEPENDENCY_REPORTER: Reporter interface constant.
                | DEPENDENCY_VERBOSE: Verbose flag constant.
                | OPTION_CHECKER: Checker options constant.
                | OPTION_LOGGER: Logger options constant.
                | OPTION_REPORTER: Reporter options constant.
                | OPTION_VERBOSE: Verbose flag constant.
            :methods:
                | get_dependency_to_type - Returns mapping of context dependencies to their types.
                | get_option_to_type - Returns mapping of context options to their types.
    '''

    # Dependency Keys
    DEPENDENCY_CHECKER: ClassVar[str] = 'checker'
    DEPENDENCY_LOGGER: ClassVar[str] = 'logger'
    DEPENDENCY_REPORTER: ClassVar[str] = 'reporter'
    DEPENDENCY_VERBOSE: ClassVar[str] = 'verbose'

    # Option Keys
    OPTION_CHECKER: ClassVar[str] = 'checker'
    OPTION_LOGGER: ClassVar[str] = 'logger'
    OPTION_REPORTER: ClassVar[str] = 'reporter'
    OPTION_VERBOSE: ClassVar[str] = 'verbose'

    @classmethod
    @override
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of context dependencies to their types.

            :return: Mapping of context dependencies to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_CHECKER: IChecker,
            cls.DEPENDENCY_LOGGER: ILogger,
            cls.DEPENDENCY_REPORTER: IReporter,
            cls.DEPENDENCY_VERBOSE: bool,
        })

    @classmethod
    @override
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of context options to their types.

            :return: Mapping of context options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_CHECKER: CheckerOptions,
            cls.OPTION_LOGGER: LoggerOptions,
            cls.OPTION_REPORTER: ReporterOptions,
            cls.OPTION_VERBOSE: bool,
        })
