# -*- coding: UTF-8 -*-

'''
Module
    reporter_registry.py
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
    Encapsulates core runtime components for simplification of ReporterBundle creation.
'''

from __future__ import annotations

from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.reporter.bundle import ReporterBundle
from ats_utilities.reporter.params import ReporterParams

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ReporterRegistry(IRegistry[ReporterBundle, ReporterParams | None]):
    '''
        Encapsulates core runtime components for simplification of ReporterBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a ReporterBundle.
    '''

    @classmethod
    @override
    def create_bundle(cls, params: ReporterParams | None = None) -> ReporterBundle:
        '''
            Creates a ReporterBundle instance.

            :param params: Registry-specific orchestration parameters.
            :type params: ReporterParams | None
            :return: ReporterBundle instance.
            :rtype: <ReporterBundle>
            :exceptions:
                | ATSValueError: Checker bundle must be provided.
                | ATSValueError: Theme must be provided.
                | ATSValueError: Logger bundle must be provided.
                | ATSTypeError: Checker bundle must be a CheckerBundle instance.
                | ATSTypeError: Theme must be a Theme instance.
                | ATSTypeError: Logger bundle must be a LoggerBundle instance.
        '''
        return ReporterBundle(
            checker=params.get('checker') if params else None,
            theme=params.get('theme') if params else None,
            logger=params.get('logger') if params else None,
        )

