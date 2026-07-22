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
    Encapsulates core runtime components for simplification of ContextBundle creation.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.dependencies import ContextDependencies
from ats_utilities.context.validator import ContextValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ContextRegistry(IRegistry[ContextBundle, ContextDependencies | None]):
    '''
        Encapsulates core runtime components for simplification of ContextBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a ContextBundle instance.
    '''

    @classmethod
    @override
    def create_bundle(cls, dependencies: ContextDependencies | None) -> ContextBundle:
        '''
            Orchestrates dependency injection and creates a context bundle instance.

            :param dependencies: Dependencies required to construct the context bundle.
            :type dependencies: ContextDependencies
            :return: Context bundle instance.
            :rtype: ContextBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Checker must be provided.
                | ATSValueError: Logger must be provided.
                | ATSValueError: Reporter must be provided.
                | ATSValueError: Verbose must be provided.
                | ATSTypeError: Bundle must be an instance of ContextBundle.
                | ATSTypeError: Checker must be an instance of IChecker.
                | ATSTypeError: Logger must be an instance of ILogger.
                | ATSTypeError: Reporter must be an instance of IReporter.
                | ATSTypeError: Verbose must be a boolean.
        '''
        bundle: ContextBundle = ContextBundle(
            checker=dependencies.get('checker') if dependencies else None,
            logger=dependencies.get('logger') if dependencies else None,
            reporter=dependencies.get('reporter') if dependencies else None,
            verbose=dependencies.get('verbose') if dependencies else False
        )

        ContextValidator.validate(bundle)

        return bundle

