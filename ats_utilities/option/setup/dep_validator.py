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
    Validator for the option bundle dependencies.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.option.setup.dependencies import OptionBundleDependencies
from ats_utilities.option.setup.keys import OptionBundleKeys
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


class OptionBundleDependenciesValidator:
    '''
        Validator for the option bundle dependencies.

        It defines:

            :methods:
                | validate - Validates the option bundle dependencies.
    '''

    @classmethod
    def validate(cls, dependencies: OptionBundleDependencies) -> None:
        '''
            Validates the option bundle dependencies.

            :param dependencies: The option bundle dependencies to be validated.
            :exceptions:
                | ATSValueError: The option bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The option bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'option_bundle_dependencies_validator::validate(...)'
        msg_dependencies_none: str = 'the option bundle dependencies must be provided'
        msg_dependencies_istype: str = 'the option bundle dependencies must be a Mapping'

        not_none(dependencies, ctx, msg_dependencies_none)
        istype(dependencies, Mapping, ctx, msg_dependencies_istype)

        for attr_name, expected_type in OptionBundleKeys.get_dependency_to_type().items():
            msg_attr_none: str = f'the {attr_name.replace("_", " ")} must be provided'
            msg_attr_istype: str = f'the {attr_name.replace("_", " ")} must be an instance of {expected_type.__name__}'

            attribute: object = dependencies.get(attr_name)

            not_none(attribute, ctx, msg_attr_none)
            istype(attribute, expected_type, ctx, msg_attr_istype)

            if attr_name == OptionBundleKeys.DEPENDENCY_CONTEXT_BUNDLE:
                ContextBundleValidator.validate(attribute)
