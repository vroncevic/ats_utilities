# -*- coding: UTF-8 -*-

'''
Module
    checker_registry.py
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
    Encapsulates core runtime components for simplification of CheckerBundle creation.
'''

from __future__ import annotations

from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.checker.checker_bundle import CheckerBundle
from ats_utilities.checker.checker_params import CheckerParams

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CheckerRegistry(IRegistry[CheckerBundle, CheckerParams | None]):
    '''
        Encapsulates core runtime components for simplification of CheckerBundle creation.

        It defines:

            :methods:
                | create_bundle - Creates a CheckerBundle instance using provided components.
    '''

    @classmethod
    @override
    def create_bundle(cls, params: CheckerParams | None = None) -> CheckerBundle:
        '''
            Creates a CheckerBundle instance using provided components.

            :param params: Registry-specific orchestration parameters.
            :type params: CheckerParams | None
            :return: CheckerBundle instance.
            :rtype: <CheckerBundle>
            :exceptions:
                | ATSValueError: Context provider must be provided.
                | ATSValueError: Check reporter must be provided.
                | ATSValueError: Format validator must be provided.
                | ATSValueError: Type validator must be provided.
                | ATSTypeError: Context provider must be an instance of IContextProvider.
                | ATSTypeError: Check reporter must be an instance of ICheckReporter.
                | ATSTypeError: Format validator must be an instance of IFormatValidator.
                | ATSTypeError: Type validator must be an instance of ITypeValidator.
        '''
        return CheckerBundle(
            format_validator=params.get('format_validator') if params else None,
            type_validator=params.get('type_validator') if params else None,
            context_provider=params.get('context_provider') if params else None,
            check_reporter=params.get('check_reporter') if params else None
        )
