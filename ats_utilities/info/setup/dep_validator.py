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

from typing import override

from ats_utilities.info.setup.dependencies import InfoDependencies
from ats_utilities.utils.setup.idep_validator import IDependenciesValidator
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
from ats_utilities.info.setup.info_keys import InfoKeys
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none, not_satisfied

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class InfoDependenciesValidator(IDependenciesValidator[InfoDependencies]):
    '''
        Validator for info dependencies.

        It defines:

            :methods:
                | validate - Validates info dependencies instance.
    '''

    @classmethod
    @override
    def validate(cls, dependencies: InfoDependencies) -> None:
        '''
            Validates info dependencies instance.

            :param dependencies: Info dependencies instance to be validated.
            :exceptions:
                | ATSValueError: Dependencies must be provided.
                | ATSValueError: Dependencies attributes must have proper values.
                | ATSTypeError: Dependencies must be an instance of InfoDependencies.
                | ATSTypeError: Dependencies attributes must be instances of their respective interfaces.
        '''
        ctx: str = r'info_dependencies_validator::validate(...)'

        not_none(dependencies, ctx, r'dependencies must be provided')
        istype(dependencies, InfoDependencies, ctx, r'dependencies must be an instance of InfoDependencies')

        attr_to_interface = InfoKeys.get_attr_to_interface()

        for attr_name, expected_interface in attr_to_interface.items():
            not_satisfied(attr_name not in dependencies, ctx, f'Missing required dependency key: {attr_name}')

            value = dependencies[attr_name]
            not_none(value, ctx, f'{attr_name} must be provided')

            err_msg = f'{attr_name.replace("_", " ")} must be an instance of {expected_interface.__name__}'
            istype(value, expected_interface, ctx, err_msg)

        not_satisfied('context_bundle' not in dependencies, ctx, r'context bundle must be provided')

        context_bundle = dependencies['context_bundle']
        not_none(context_bundle, ctx, r'context bundle must be provided')
        istype(context_bundle, ContextBundle, ctx, r'context bundle must be an instance of ContextBundle')
        ContextValidator.validate(context_bundle)
