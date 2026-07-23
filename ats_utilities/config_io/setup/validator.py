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
from typing import override

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.setup.bundle import ConfigIOBundle
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.utils.ivalidator import IValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ConfigIOValidator(IValidator[ConfigIOBundle]):
    '''
        Validator for config I/O bundle instance.

        It defines:

            :methods:
                | validate - Validates config I/O bundle instance.
    '''

    @classmethod
    @override
    def validate(cls, bundle: ConfigIOBundle) -> None:
        '''
            Validates config I/O bundle instance.

            :param bundle: Config I/O bundle instance to be validated.
            :type bundle: ConfigIOBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: File path must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Processor must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of ConfigIOBundle.
                | ATSTypeError: File path must be a string.
                | ATSTypeError: Scheme must be an instance of Mapping interface.
                | ATSTypeError: Processor must be an instance of IConfigProcessor interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle interface.
        '''
        ctx: str = r'config_io_validator::validate(...)'

        not_none(bundle, ctx, r'bundle must be provided')
        istype(bundle, ConfigIOBundle, ctx, r'bundle must be an instance of ConfigIOBundle')

        not_none(bundle.file_path, ctx, r'file path must be provided')
        not_none(bundle.scheme, ctx, r'scheme must be provided')
        not_none(bundle.processor, ctx, r'processor must be provided')
        not_none(bundle.context_bundle, ctx, r'context bundle must be provided')

        istype(bundle.file_path, str, ctx, r'file path must be a string')
        istype(bundle.scheme, Mapping, ctx, r'scheme must be an instance of Mapping interface')
        istype(bundle.processor, IConfigProcessor, ctx, r'processor must be an instance of IConfigProcessor interface')
        istype(bundle.context_bundle, ContextBundle, ctx, r'context bundle must be an instance of ContextBundle interface')
