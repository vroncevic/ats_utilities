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
    Encapsulates core runtime components for simplification of reporter bundle creation.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.setup.iregistry import IRegistry
from ats_utilities.reporter.setup.bundle import ReporterBundle
from ats_utilities.reporter.setup.dependencies import ReporterDependencies
from ats_utilities.reporter.setup.keys import ReporterKeys
from ats_utilities.reporter.setup.validator import ReporterValidator
from ats_utilities.reporter.setup.dep_validator import ReporterDependenciesValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ReporterRegistry(IRegistry[ReporterBundle, ReporterDependencies]):
    '''
        Encapsulates core runtime components for simplification of reporter bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates a reporter bundle instance.
    '''

    @classmethod
    @override
    def create_bundle(cls, dependencies: ReporterDependencies) -> ReporterBundle:
        '''
            Orchestrates dependency injection and creates a reporter bundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :return: Reporter bundle instance.
            :exceptions:
                | ATSValueError: Dependencies must be provided and have proper values.
                | ATSTypeError:  Dependencies must be an instance of ReporterDependencies
                |                and its attributes must be instances of their
                |                respective types.
        '''
        ReporterDependenciesValidator.validate(dependencies)

        bundle: ReporterBundle = ReporterBundle(
            checker=dependencies.get(ReporterKeys.DEPENDENCY_CHECKER),
            theme=dependencies.get(ReporterKeys.DEPENDENCY_THEME),
            logger=dependencies.get(ReporterKeys.DEPENDENCY_LOGGER),
        )

        ReporterValidator.validate(bundle)

        return bundle
