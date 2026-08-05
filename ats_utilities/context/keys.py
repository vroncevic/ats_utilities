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
    Runtime components and interface constraints for the context bundle.
'''

from __future__ import annotations

from typing import ClassVar
from types import MappingProxyType

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.setup.options import CheckerBundleOptions
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.setup.options import ReporterBundleOptions
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.logger.setup.options import LoggerBundleOptions

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ContextBundleKeys:
    '''
        Runtime components and interface constraints for the context bundle.

        It defines:

            :attributes:
                | DEPENDENCY_CHECKER - The checker interface constant for the context bundle.
                | DEPENDENCY_LOGGER - The logger interface constant for the context bundle.
                | DEPENDENCY_REPORTER - The reporter interface constant for the context bundle.
                | DEPENDENCY_VERBOSE - The verbose flag constant for the context bundle.
                | OPTION_CHECKER - The checker options constant for the context bundle.
                | OPTION_LOGGER - The logger options constant for the context bundle.
                | OPTION_REPORTER - The reporter options constant for the context bundle.
                | OPTION_VERBOSE - The verbose flag constant for the context bundle.
            :methods:
                | get_dependency_to_type - Returns the mapping of the context bundle dependencies to their types.
                | get_option_to_type - Returns the mapping of the context bundle options to their types.
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
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of the context bundle dependencies to their types.

            :return: The mapping of the context bundle dependencies to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_CHECKER: IChecker,
            cls.DEPENDENCY_LOGGER: ILogger,
            cls.DEPENDENCY_REPORTER: IReporter,
            cls.DEPENDENCY_VERBOSE: bool,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns the mapping of the context bundle options to their types.

            :return: The mapping of the context bundle options to their types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_CHECKER: CheckerBundleOptions,
            cls.OPTION_LOGGER: LoggerBundleOptions,
            cls.OPTION_REPORTER: ReporterBundleOptions,
            cls.OPTION_VERBOSE: bool,
        })
