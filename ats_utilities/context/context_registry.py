# -*- coding: UTF-8 -*-

'''
Module
    context_registry.py
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

from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.context.context_params import ContextParams

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ContextRegistry(IRegistry[ContextBundle, ContextParams | None]):
    '''
        Encapsulates core runtime components for simplification of ContextBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a ContextBundle instance.
    '''

    @classmethod
    @override
    def create_bundle(cls, params: ContextParams | None = None) -> ContextBundle:
        '''
            Creates a ContextBundle instance using optional verbose parameter.

            :param params: Registry-specific orchestration parameters.
            :type params: ContextParams | None
            :return: ContextBundle instance.
            :rtype: <ContextBundle>
            :exceptions:
                | ATSValueError: Verbose must be provided.
                | ATSTypeError: Verbose must be a boolean.
        '''
        verbose: bool = params.get('verbose', False) if params else False
        return ContextBundle(
            checker=params.get('checker') if params else None,
            logger=params.get('logger') if params else None,
            reporter=params.get('reporter') if params else None,
            verbose=verbose
        )

