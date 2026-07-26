# -*- coding: UTF-8 -*-

'''
Module
    opt_validator.py
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
    Validator for info options.
'''

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from ats_utilities.info.setup.options import InfoOptions
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


class InfoOptionsValidator:
    '''
        Validator for info options.

        It defines:

            :methods:
                | validate - Validates info options instance.
    '''

    @classmethod
    def validate(cls, options: InfoOptions) -> None:
        '''
            Validates info options instance.

            :param options: Info options instance to be validated.
            :exceptions:
                | ATSValueError: Options must be provided and have proper values.
                | ATSTypeError:  Options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'info_options_validator::validate(...)'

        not_none(options, ctx, 'options must be provided and have proper values')
        istype(options, Mapping, ctx, 'options must be a Mapping')

        for opt_name, expected_type in InfoKeys.get_option_to_type().items():
            not_satisfied(opt_name not in options, ctx, f'{opt_name} must be provided')
            value = options.get(opt_name)
            not_none(value, ctx, f'{opt_name} must be provided and have proper value')
            istype(
                value, expected_type, ctx,
                f'{opt_name.replace("_", " ")} must be an instance of {expected_type.__name__}'
            )

            if opt_name is InfoKeys.OPTION_INFO:
                info_structure: Mapping[str, Any] = value
                required_config_keys: Sequence[str] = InfoKeys.get_required_config_keys()
                not_satisfied(
                    not all(key in info_structure for key in required_config_keys),
                    ctx, 'info structure must contain all required keys'
                )

                for key in info_structure.keys():
                    not_satisfied(
                        key not in InfoKeys.get_config_keys(),
                        ctx, f'{key} is not a valid info configuration key'
                    )

                    if InfoKeys.is_optional_config_key(key):
                        continue

                    not_satisfied(
                        info_structure[key] is None, ctx,
                        f'info value for required key {key} must be provided'
                    )
