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
    A validator for the generator bundle.
'''

from __future__ import annotations

from ats_utilities.generation.setup.bundle import GeneratorBundle
from ats_utilities.generation.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generation.tar.itar_processor import ITarProcessor
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
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


class GeneratorValidator:
    '''
        A validator for the generator bundle.

        It defines:

            :methods:
                | validate - Validates the generator bundle.
    '''

    @classmethod
    def validate(cls, bundle: GeneratorBundle) -> None:
        '''
            Validates the generator bundle.

            :param bundle: The generator bundle instance to be validated.
            :exceptions:
                | ATSValueError: Generator bundle must be provided and have proper values.
                | ATSTypeError:  Generator bundle must be an instance of GeneratorBundle and its attributes
                |                must be instances of their respective types.
        '''
        ctx: str = 'generator_validator::validate(...)'
        msg_bundle_none: str = 'bundle must be provided'
        msg_bundle_istype: str = 'bundle must be an instance of GeneratorBundle'
        msg_scheme_loader_none: str = 'scheme loader must be provided'
        msg_tar_processor_none: str = 'tar processor must be provided'
        msg_context_bundle_none: str = 'context bundle must be provided'
        msg_scheme_loader_istype: str = 'scheme loader must be an ISchemeLoader instance'
        msg_tar_processor_istype: str = 'tar processor must be an ITarProcessor instance'
        msg_context_bundle_istype: str = 'context bundle must be a ContextBundle instance'

        not_none(bundle, ctx, msg_bundle_none)
        istype(bundle, GeneratorBundle, ctx, msg_bundle_istype)

        not_none(bundle.scheme_loader, ctx, msg_scheme_loader_none)
        not_none(bundle.tar_processor, ctx, msg_tar_processor_none)
        not_none(bundle.context_bundle, ctx, msg_context_bundle_none)

        istype(bundle.scheme_loader, ISchemeLoader, ctx, msg_scheme_loader_istype)
        istype(bundle.tar_processor, ITarProcessor, ctx, msg_tar_processor_istype)
        istype(bundle.context_bundle, ContextBundle, ctx, msg_context_bundle_istype)

        ContextValidator.validate(bundle.context_bundle)