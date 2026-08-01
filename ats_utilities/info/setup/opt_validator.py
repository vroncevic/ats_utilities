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
    A validator for the info options instance.
'''

from __future__ import annotations

from collections.abc import Mapping, Sequence

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
        A validator for the info options instance.

        It defines:

            :methods:
                | validate - Validates the info options instance.
    '''

    @classmethod
    def validate(cls, options: InfoOptions) -> None:
        '''
            Validates the info options instance.

            :param options: The info options instance to be validated.
            :exceptions:
                | ATSValueError: Options must be provided and have proper values.
                | ATSTypeError:  Options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'info_options_validator::validate(...)'
        msg_options_none: str = 'options must be provided and have proper values'
        msg_options_not_mapping: str = 'options must be a Mapping'

        not_none(options, ctx, msg_options_none)
        istype(options, Mapping, ctx, msg_options_not_mapping)

        for attr_name, expected_type in InfoKeys.get_option_to_type().items():
            msg_opt_not_provided: str = f'{attr_name} must be provided'
            msg_opt_none: str = f'{attr_name} must be provided and have proper attribute'
            msg_opt_not_instance: str = f'{attr_name} must be an instance of {expected_type.__name__}'

            not_satisfied(attr_name not in options, ctx, msg_opt_not_provided)

            attribute = options.get(attr_name)

            not_none(attribute, ctx, msg_opt_none)
            istype(attribute, expected_type, ctx, msg_opt_not_instance)

            if attr_name is InfoKeys.OPTION_INFO:
                info_structure: Mapping[str, object] = attribute
                required_config_keys: Sequence[str] = InfoKeys.get_required_config_keys()
                msg_required_keys_missing: str = 'info structure must contain all required keys'
                msg_invalid_key: str = 'is not a valid info configuration key'
                msg_optional_none: str = 'info attribute for required key must be provided'

                not_satisfied(not all(key in info_structure for key in required_config_keys), ctx, msg_required_keys_missing)

                for key in info_structure.keys():
                    not_satisfied(key not in InfoKeys.get_config_keys(), ctx, msg_invalid_key)

                    if InfoKeys.is_optional_config_key(key):
                        continue

                    not_satisfied(info_structure[key] is None, ctx, msg_optional_none)
