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
    Validator for config I/O bundle instance.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
from ats_utilities.config_io.setup.bundle import ConfigIOBundle
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
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


class ConfigIOValidator:
    '''
        Validator for config I/O bundle instance.

        It defines:

            :methods:
                | validate - Validates config I/O bundle instance.
    '''

    @classmethod
    def validate(cls, bundle: ConfigIOBundle) -> None:
        '''
            Validates config I/O bundle instance.

            :param bundle: Config I/O bundle instance to be validated.
            :exceptions:
                | ATSValueError: ConfigIOBundle must be provided and have proper values.
                | ATSTypeError:  ConfigIOBundle must be an instance of ConfigIOBundle and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'config_io_validator::validate(...)'
        msg_bundle_none: str = 'ConfigIOBundle must be provided'
        msg_bundle_istype: str = 'ConfigIOBundle must be an instance of ConfigIOBundle'
        msg_file_path_none: str = 'File path must be provided'
        msg_scheme_none: str = 'Scheme must be provided'
        msg_processor_none: str = 'Processor must be provided'
        msg_context_bundle_none: str = 'Context bundle must be provided'
        msg_file_path_istype: str = 'File path must be a string'
        msg_scheme_istype: str = 'Scheme must be an instance of Mapping interface'
        msg_processor_istype: str = 'Processor must be an instance of IConfigProcessor interface'
        msg_context_bundle_istype: str = 'Context bundle must be an instance of ContextBundle interface'

        not_none(bundle, ctx, msg_bundle_none)
        istype(bundle, ConfigIOBundle, ctx, msg_bundle_istype)

        not_none(bundle.file_path, ctx, msg_file_path_none)
        not_none(bundle.scheme, ctx, msg_scheme_none)
        not_none(bundle.processor, ctx, msg_processor_none)
        not_none(bundle.context_bundle, ctx, msg_context_bundle_none)

        istype(bundle.file_path, str, ctx, msg_file_path_istype)
        istype(bundle.scheme, Mapping, ctx, msg_scheme_istype)
        istype(bundle.processor, IConfigProcessor, ctx, msg_processor_istype)
        istype(bundle.context_bundle, ContextBundle, ctx, msg_context_bundle_istype)

        ContextValidator.validate(bundle.context_bundle)
