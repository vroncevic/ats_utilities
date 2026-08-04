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
    Validator for the option bundle.
'''

from __future__ import annotations

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextBundleValidator
from ats_utilities.option.setup.bundle import OptionBundle
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
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


class OptionBundleValidator:
    '''
        Validator for the option bundle.

        It defines:

            :methods:
                | validate - Validates the option bundle.
    '''

    @classmethod
    def validate(cls, bundle: OptionBundle) -> None:
        '''
            Validates the option bundle.

            :param bundle: The option bundle instance to be validated.
            :exceptions:
                | ATSValueError: The option bundle must be provided and have proper values.
                | ATSTypeError:  The option bundle must be an instance of OptionBundle and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'option_bundle_validator::validate(...)'
        msg_bundle_none: str = 'the option bundle must be provided'
        msg_bundle_istype: str = 'the option bundle must be an instance of OptionBundle'
        msg_strategy_none: str = 'the strategy must be provided'
        msg_strategy_istype: str = 'the strategy must be an IParserStrategy instance'
        msg_context_bundle_none: str = 'the context bundle must be provided'
        msg_context_bundle_istype: str = 'the context bundle must be a ContextBundle instance'

        not_none(bundle, ctx, msg_bundle_none)
        istype(bundle, OptionBundle, ctx, msg_bundle_istype)

        not_none(bundle.strategy, ctx, msg_strategy_none)
        not_none(bundle.context_bundle, ctx, msg_context_bundle_none)

        istype(bundle.strategy, IParserStrategy, ctx, msg_strategy_istype)
        istype(bundle.context_bundle, ContextBundle, ctx, msg_context_bundle_istype)

        ContextBundleValidator.validate(bundle.context_bundle)
