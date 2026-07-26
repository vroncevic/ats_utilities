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
    Validator for option options.
'''

from __future__ import annotations

from collections.abc import Mapping


from ats_utilities.option.setup.options import OptionOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.utils.setup.iopt_validator import IOptionsValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

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
        Validator for option options.

        It defines:

            :methods:
                | validate - Validates option options instance.
    '''

    @classmethod
    def validate(cls, options: OptionOptions) -> None:
        '''
            Validates option options instance.

            :param options: Option options instance to be validated.
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a Mapping.
                | ATSTypeError: Parameters must be a Mapping.
                | ATSTypeError: Context bundle must be a ContextBundle.
                | ATSTypeError: Parser class must be a class type.
        '''
        ctx: str = 'option_options_validator::validate(...)'

        not_none(options, ctx, 'options must be provided')
        istype(options, Mapping, ctx, 'options must be a Mapping')

        parameters = options.get('parameters')
        not_none(parameters, ctx, 'parameters must be provided')
        istype(parameters, Mapping, ctx, 'parameters must be a Mapping')

        context_bundle = options.get('context_bundle')
        not_none(context_bundle, ctx, 'context bundle must be provided')
        istype(context_bundle, ContextBundle, ctx, 'context bundle must be an instance of ContextBundle')

        parser_class = options.get('parser_class')

        if parser_class is not None:
            not_none(parser_class, ctx, 'parser class must be provided')
            istype(parser_class, type, ctx, 'parser class must be a class type')
