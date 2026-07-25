# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core runtime components for simplification of logger bundle creation.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.setup.iregistry import IRegistry
from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.setup.dependencies import LoggerDependencies
from ats_utilities.logger.setup.keys import LoggerKeys
from ats_utilities.logger.setup.validator import LoggerValidator
from ats_utilities.logger.setup.dep_validator import LoggerDependenciesValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class LoggerRegistry(IRegistry[LoggerBundle, LoggerDependencies]):
    '''
        Encapsulates core runtime components for simplification of logger bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates a logger bundle instance.
    '''

    @classmethod
    @override
    def create_bundle(cls, dependencies: LoggerDependencies) -> LoggerBundle:
        '''
            Orchestrates dependency injection and creates a logger bundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :return: Logger bundle instance.
            :exceptions:
                | ATSValueError: Dependencies must be provided and have proper values.
                | ATSTypeError:  Dependencies must be an instance of LoggerDependencies
                |                and its attributes must be instances of their
                |                respective types.
        '''
        LoggerDependenciesValidator.validate(dependencies)

        bundle: LoggerBundle = LoggerBundle(
            logger=dependencies.get(LoggerKeys.DEPENDENCY_LOGGER),
            has_file_handler=dependencies.get(LoggerKeys.DEPENDENCY_HAS_FILE_HANDLER),
            formatter=dependencies.get(LoggerKeys.DEPENDENCY_FORMATTER),
            buffer=dependencies.get(LoggerKeys.DEPENDENCY_BUFFER),
            handler_manager=dependencies.get(LoggerKeys.DEPENDENCY_HANDLER_MANAGER)
        )

        LoggerValidator.validate(bundle)

        return bundle
