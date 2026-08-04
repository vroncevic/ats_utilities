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
    Encapsulates core runtime components for simplification of the reporter bundle.
'''

from __future__ import annotations

from ats_utilities.reporter.setup.bundle import ReporterBundle
from ats_utilities.reporter.setup.dependencies import ReporterBundleDependencies
from ats_utilities.reporter.setup.keys import ReporterBundleKeys
from ats_utilities.reporter.setup.validator import ReporterBundleValidator
from ats_utilities.reporter.setup.dep_validator import ReporterBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ReporterRegistry:
    '''
        Encapsulates core runtime components for simplification of the reporter bundle.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates the reporter bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: ReporterBundleDependencies) -> ReporterBundle:
        '''
            Orchestrates dependency injection and creates the reporter bundle.

            :param dependencies: The registry-specific orchestration dependencies.
            :return: The reporter bundle.
            :exceptions:
                | ATSValueError: The reporter bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The reporter bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The reporter bundle must be provided and have proper values.
                | ATSTypeError:  The reporter bundle must be an instance of ReporterBundle
                |                and its attributes must be instances of their respective types.
        '''
        ReporterBundleDependenciesValidator.validate(dependencies)

        bundle: ReporterBundle = ReporterBundle(
            checker=dependencies.get(ReporterBundleKeys.DEPENDENCY_CHECKER) if dependencies else None,
            theme=dependencies.get(ReporterBundleKeys.DEPENDENCY_THEME) if dependencies else None,
            logger=dependencies.get(ReporterBundleKeys.DEPENDENCY_LOGGER) if dependencies else None,
        )

        ReporterBundleValidator.validate(bundle)

        return bundle
