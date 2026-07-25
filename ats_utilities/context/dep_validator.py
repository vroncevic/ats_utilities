# -*- coding: UTF-8 -*-

'''
Module
    dep_validator.py
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
    Validator for context dependencies.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from ats_utilities.context.dependencies import ContextDependencies
from ats_utilities.context.keys import ContextKeys
from ats_utilities.utils.setup.idep_validator import IDependenciesValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ContextDependenciesValidator(IDependenciesValidator[ContextDependencies]):
    '''
        Validator for context dependencies.

        It defines:

            :methods:
                | validate - Validates context dependencies instance.
    '''

    @classmethod
    @override
    def validate(cls, dependencies: ContextDependencies) -> None:
        '''
            Validates context dependencies instance.

            :param dependencies: Context dependencies instance to be validated.
            :exceptions:
                | ATSValueError: Context dependencies must be provided and have proper values.
                | ATSTypeError:  Context dependencies must be an instance of ContextDependencies
                |                and its attributes must be instances of their
                |                respective types.
        '''
        ctx: str = r'context_dependencies_validator::validate(...)'

        not_none(dependencies, ctx, r'dependencies must be provided')
        istype(dependencies, Mapping, ctx, r'dependencies must be a Mapping')

        for attr_name, expected_type in ContextKeys.get_dependency_to_type().items():
            value = dependencies.get(attr_name)

            if value is not None:
                err_msg = f'{attr_name.replace("_", " ")} must be an instance of {expected_type.__name__}'
                istype(value, expected_type, ctx, err_msg)
