# -*- coding: UTF-8 -*-

'''
Module
    generator_bundle.py
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
    Defines parameter bundle dataclass for template generation.
    Encapsulates template generation parameters for simplifcation.
'''

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, frozen=True, kw_only=True)
class GeneratorBundle:
    '''
        Defines class GeneratorBundle with method(s).
        Encapsulates template generation parameters for simplifcation.

        It defines:

            :attributes:
                | scheme_loader - Loader/resolver for scheme configuration.
                | tar_processor - Processor for archive extraction and template rendering.
                | template_processor - Processor for template rendering.
                | context_bundle - Context bundle for generator.
            :methods:
                | __post_init__ - Post-initialization hook to validate generator bundle.
                | validate - Validates generator bundle.
                | to_dict - Converts the generator bundle to a dictionary.
    '''

    scheme_loader: ISchemeLoader
    tar_processor: ITarProcessor
    template_processor: ITemplateProcessor
    context_bundle: ContextBundle

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate generator bundle.

            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSValueError: Scheme loader must be provided.
                | ATSValueError: Tar processor must be provided.
                | ATSValueError: Template processor must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Scheme loader must be an ISchemeLoader instance.
                | ATSTypeError: Tar processor must be an ITarProcessor instance.
                | ATSTypeError: Template processor must be an ITemplateProcessor instance.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates generator bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSValueError: Scheme loader must be provided.
                | ATSValueError: Tar processor must be provided.
                | ATSValueError: Template processor must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSTypeError: Scheme loader must be an ISchemeLoader instance.
                | ATSTypeError: Tar processor must be an ITarProcessor instance.
                | ATSTypeError: Template processor must be an ITemplateProcessor instance.
        '''
        context: str = r'generator_bundle::validate(...)'
        not_none(self.context_bundle, context, r'context bundle must be provided')
        not_none(self.scheme_loader, context, r'scheme loader must be provided')
        not_none(self.tar_processor, context, r'tar processor must be provided')
        not_none(self.template_processor, context, r'template processor must be provided')
        istype(self.context_bundle, ContextBundle, context, r'context bundle must be a ContextBundle instance')
        istype(self.scheme_loader, ISchemeLoader, context, r'scheme loader must be an ISchemeLoader instance')
        istype(self.tar_processor, ITarProcessor, context, r'tar processor must be an ITarProcessor instance')
        istype(self.template_processor, ITemplateProcessor, context, r'template processor must be an ITemplateProcessor instance')

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the generator bundle to a dictionary.

            :return: Dictionary representation of the generator bundle.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            field: getattr(self, field)
            for field in self.__dataclass_fields__
        }
