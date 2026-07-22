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

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.reporter.setup.bundle import ReporterBundle
from ats_utilities.reporter.setup.dependencies import ReporterDependencies
from ats_utilities.reporter.setup.validator import ReporterValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ReporterRegistry(IRegistry[ReporterBundle, ReporterDependencies | None]):
    '''
        Encapsulates core runtime components for simplification of reporter bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates a reporter bundle instance.
    '''

    @classmethod
    @override
    def create_bundle(cls, dependencies: ReporterDependencies | None = None) -> ReporterBundle:
        '''
            Orchestrates dependency injection and creates a reporter bundle instance.

            :param dependencies: Registry-specific orchestration dependencies (default None).
            :type dependencies: ReporterDependencies | None
            :return: Reporter bundle instance.
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
        bundle: ReporterBundle = ReporterBundle(
            checker=dependencies.get('checker') if dependencies else None,
            theme=dependencies.get('theme') if dependencies else None,
            logger=dependencies.get('logger') if dependencies else None,
        )

        ReporterValidator.validate(bundle)

        return bundle
