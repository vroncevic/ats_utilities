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
    Validator for info dependencies.
'''

from __future__ import annotations

from collections.abc import Mapping, Sequence

from ats_utilities.info.setup.dependencies import InfoDependencies
from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none, not_satisfied

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class InfoDependenciesValidator:
    '''
        Validator for info dependencies.

        It defines:

            :methods:
                | validate - Validates info dependencies instance.
    '''

    @classmethod
    def validate(cls, dependencies: InfoDependencies) -> None:
        '''
            Validates info dependencies instance.

            :param dependencies: Info dependencies instance to be validated.
            :exceptions:
                | ATSValueError: Dependencies must be provided and have proper values.
                | ATSTypeError:  Dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'info_dependencies_validator::validate(...)'
        msg_dependencies_none: str = 'dependencies must be provided'
        msg_dependencies_not_mapping: str = 'dependencies must be an instance of Mapping'

        not_none(dependencies, ctx, msg_dependencies_none)
        istype(dependencies, Mapping, ctx, msg_dependencies_not_mapping)

        required_dependency_keys: Sequence[str] = [
            InfoKeys.get_name_of_config_key(key) for key in InfoKeys.get_required_config_keys()
        ]
        optional_dependency_keys: Sequence[str] = [
            InfoKeys.get_name_of_config_key(key) for key in InfoKeys.get_optional_config_keys()
        ]

        for key in required_dependency_keys:
            not_satisfied(key not in dependencies, ctx, f'{key} must be provided in dependencies')

        for attr_name, expected_type in InfoKeys.get_dependency_to_type().items():
            msg_attr_required_none: str = f'{attr_name} must be provided and have proper attribute'
            msg_attr_optional_not_instance: str = f'{attr_name} must be an instance of {expected_type.__name__}'

            attribute = dependencies.get(attr_name)

            if attr_name in required_dependency_keys:
                not_satisfied(attribute is None, ctx, msg_attr_required_none)
                istype(attribute, expected_type, ctx, msg_attr_optional_not_instance)
                continue

            if attr_name in optional_dependency_keys and attribute is not None:
                istype(attribute, expected_type, ctx, msg_attr_optional_not_instance)
