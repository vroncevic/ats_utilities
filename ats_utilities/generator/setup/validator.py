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
    Validator for generator bundle instance.
'''

from __future__ import annotations

from typing import override

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generator.setup.bundle import GeneratorBundle
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.utils.ivalidator import IValidator
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class GeneratorValidator(IValidator[GeneratorBundle]):
    '''
        Validator for generator bundle instance.

        It defines:

            :methods:
                | validate - Validates generator bundle instance.
    '''

    @classmethod
    @override
    def validate(cls, bundle: GeneratorBundle) -> None:
        '''
            Validates generator bundle instance.

            :param bundle: Generator bundle instance to be validated.
            :type bundle: GeneratorBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSValueError: Scheme loader must be provided.
                | ATSValueError: Tar processor must be provided.
                | ATSValueError: Template processor must be provided.
                | ATSTypeError: Bundle must be an instance of GeneratorBundle.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Scheme loader must be an ISchemeLoader instance.
                | ATSTypeError: Tar processor must be an ITarProcessor instance.
                | ATSTypeError: Template processor must be an ITemplateProcessor instance.
        '''
        ctx: str = r'generator_validator::validate(...)'

        not_none(bundle, ctx, r'bundle must be provided')
        istype(bundle, GeneratorBundle, ctx, r'bundle must be an instance of GeneratorBundle')

        not_none(bundle.scheme_loader, ctx, r'scheme loader must be provided')
        not_none(bundle.tar_processor, ctx, r'tar processor must be provided')
        not_none(bundle.template_processor, ctx, r'template processor must be provided')
        not_none(bundle.context_bundle, ctx, r'context bundle must be provided')

        istype(bundle.scheme_loader, ISchemeLoader, ctx, r'scheme loader must be an ISchemeLoader instance')
        istype(bundle.tar_processor, ITarProcessor, ctx, r'tar processor must be an ITarProcessor instance')
        istype(bundle.template_processor, ITemplateProcessor, ctx, r'template processor must be an ITemplateProcessor instance')
        istype(bundle.context_bundle, ContextBundle, ctx, r'context bundle must be a ContextBundle instance')
