# -*- coding: UTF-8 -*-

'''
Module
    validator.py
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
    A validator for the option bundle instance.
'''

from __future__ import annotations

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
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


class OptionValidator:
    '''
        A validator for the option bundle instance.

        It defines:

            :methods:
                | validate - Validates the option bundle instance.
    '''

    @classmethod
    def validate(cls, bundle: OptionBundle) -> None:
        '''
            Validates the option bundle instance.

            :param bundle: The option bundle instance to be validated.
            :exceptions:
                | ATSValueError: Option bundle must be provided and have proper values.
                | ATSTypeError:  Option bundle must be an instance of OptionBundle and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'option_validator::validate(...)'

        not_none(bundle, ctx, 'option bundle must be provided')
        istype(bundle, OptionBundle, ctx, 'option bundle must be an instance of OptionBundle')

        not_none(bundle.strategy, ctx, 'strategy must be provided')
        not_none(bundle.context_bundle, ctx, 'context bundle must be provided')

        istype(bundle.strategy, IParserStrategy, ctx, 'strategy must be an IParserStrategy instance')
        istype(bundle.context_bundle, ContextBundle, ctx, 'context bundle must be a ContextBundle instance')

        ContextValidator.validate(bundle.context_bundle)
