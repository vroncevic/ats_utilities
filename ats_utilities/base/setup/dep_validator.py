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
    Validator for the base bundle dependencies.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.base.setup.dependencies import BaseBundleDependencies
from ats_utilities.base.setup.keys import BaseBundleKeys
from ats_utilities.context.validator import ContextBundleValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class BaseBundleDependenciesValidator:
    '''
        Validator for the base bundle dependencies.

        It defines:

            :methods:
                | validate - Validates the base bundle dependencies.
    '''

    @classmethod
    def validate(cls, dependencies: BaseBundleDependencies) -> None:
        '''
            Validates the base bundle dependencies.

            :param dependencies: The base bundle dependencies.
            :exceptions:
                | ATSValueError: The base bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The base bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'base_bundle_dependencies_validator::validate(...)'
        msg_dependencies_none: str = 'the dependencies must be provided'
        msg_dependencies_istype: str = 'the dependencies must be a Mapping'

        not_none(dependencies, ctx, msg_dependencies_none)
        istype(dependencies, Mapping, ctx, msg_dependencies_istype)

        for attr_name, expected_type in BaseBundleKeys.get_dependency_to_type().items():
            attribute = dependencies.get(attr_name)

            if attr_name == BaseBundleKeys.DEPENDENCY_GENERATION_MANAGER and attribute is None:
                continue

            msg_attr_name_none: str = f'the {attr_name.replace("_", " ")} must be provided'
            msg_attr_name_istype: str = f'the {attr_name.replace("_", " ")} must be an instance of {expected_type.__name__}'

            not_none(attribute, ctx, msg_attr_name_none)
            istype(attribute, expected_type, ctx, msg_attr_name_istype)

            if attr_name == BaseBundleKeys.DEPENDENCY_CONTEXT_BUNDLE:
                ContextBundleValidator.validate(attribute)
