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
    A validator for the option options instance.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.option.setup.options import OptionOptions
from ats_utilities.option.setup.keys import OptionKeys
from ats_utilities.context.validator import ContextValidator 
from ats_utilities.utils.setup.iopt_validator import IOptionsValidator
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


class OptionOptionsValidator(IOptionsValidator[OptionOptions]):
    '''
        A validator for the option options instance.

        It defines:

            :methods:
                | validate - Validates the option options instance.
    '''

    @classmethod
    def validate(cls, options: OptionOptions) -> None:
        '''
            Validates the option options instance.

            :param options: The option options instance to be validated.
            :exceptions:
                | ATSValueError: Options must be provided and have proper values.
                | ATSTypeError:  Options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'option_options_validator::validate(...)'

        not_none(options, ctx, 'options must be provided')
        istype(options, Mapping, ctx, 'options must be a Mapping')

        for opt_name, expected_type in OptionKeys.get_option_to_type().items():
            opt_attribute: object = options.get(opt_name)
            not_none(opt_attribute, ctx, f'{opt_name.replace("_", " ")} must be provided')
            istype(
                opt_attribute, expected_type, ctx,
                f'{opt_name.replace("_", " ")} must be an instance of {expected_type.__name__}'
            )

            if opt_name == OptionKeys.OPTION_PARAMETERS:
                missing_keys: set[str] = OptionKeys.REQUIRED_CONFIG_KEYS_SET - opt_attribute.keys()
                msg: str | None = f'missing configuration keys: {', '.join(sorted(missing_keys))}' if missing_keys else None
                not_satisfied(bool(missing_keys), ctx, msg)

            if opt_name == OptionKeys.OPTION_CONTEXT_BUNDLE:
                ContextValidator.validate(opt_attribute)
