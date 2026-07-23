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
    Encapsulates core runtime components for simplification of option bundle creation.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.setup.dependencies import OptionDependencies
from ats_utilities.option.setup.validator import OptionValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class OptionRegistry(IRegistry[OptionBundle, OptionDependencies]):
    '''
        Encapsulates core runtime components for simplification of option bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates an option bundle instance.
    '''

    @classmethod
    @override
    def create_bundle(cls, dependencies: OptionDependencies) -> OptionBundle:
        '''
            Orchestrates dependency injection and creates an option bundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :type dependencies: OptionDependencies
            :return: Option bundle instance.
            :rtype: OptionBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Strategy must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of OptionBundle.
                | ATSTypeError: Parameters must be a Mapping[str, str] instance.
                | ATSTypeError: Strategy must be an IParserStrategy instance.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        bundle: OptionBundle = OptionBundle(
            parameters=dependencies.get('parameters'),
            strategy=dependencies.get('strategy'),
            context_bundle=dependencies.get('context_bundle')
        )

        OptionValidator.validate(bundle)

        return bundle
