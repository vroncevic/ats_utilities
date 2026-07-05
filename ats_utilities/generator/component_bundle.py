# -*- coding: UTF-8 -*-

'''
Module
    component_bundle.py
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

from dataclasses import asdict, dataclass
from typing import Any

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.generator.ischeme_loader import ISchemeLoader
from ats_utilities.generator.itar_processor import ITarProcessor
from ats_utilities.generator.itemplate_processor import ITemplateProcessor
from ats_utilities.generator.scheme_loader import SchemeLoader
from ats_utilities.generator.tar_processor import TarProcessor
from ats_utilities.generator.template_processor import TemplateProcessor
from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass(slots=True, kw_only=True)
class GeneratorComponentBundle:
    '''
        Defines class GeneratorComponentBundle with method(s).
        Encapsulates template generation parameters for simplifcation.

        It defines:

            :attributes:
                | scheme_loader - Loader/resolver for scheme configuration.
                | tar_processor - Processor for archive extraction and template rendering.
                | template_processor - Processor for template rendering.
                | context_bundle - Context bundle for generator.
            :methods:
                | __post_init__ - Post-initialization hook for automatic component creation.
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another GeneratorComponentBundle instance into this one.
                | to_dict - Converts the GeneratorComponentBundle instance to a dictionary.
    '''

    scheme_loader: ISchemeLoader | None = None
    tar_processor: ITarProcessor | None = None
    template_processor: ITemplateProcessor | None = None
    context_bundle: ContextBundle | None = None

    def __post_init__(self) -> None:
        '''
            Post-initialization hook for automatic component creation.
        '''
        if self.context_bundle is None:
            self.context_bundle = ContextBundle()

        self.template_processor = make_component(
            self.template_processor, TemplateProcessor, {'context_bundle': self.context_bundle}
        )
        validate_component(self.template_processor, ITemplateProcessor)

        self.scheme_loader = make_component(
            self.scheme_loader, SchemeLoader, {'context_bundle': self.context_bundle}
        )
        validate_component(self.scheme_loader, ISchemeLoader)

        self.tar_processor = make_component(
            self.tar_processor, TarProcessor, {
                'context_bundle': self.context_bundle,
                'template_processor': self.template_processor
            }
        )
        validate_component(self.tar_processor, ITarProcessor)


    def validate(self) -> None:
        '''
            Validates that GeneratorComponentBundle is valid (can be called after merge).
            Performs validation of context bundle, scheme loader, tar processor and template processor attributes.
            Context bundle must be non-None.
            Scheme loader must be non-None and an instance of ISchemeLoader interface.
            Tar processor must be non-None and an instance of ITarProcessor interface.
            Template processor must be non-None and an instance of ITemplateProcessor interface.

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
        require_not_none(self.context_bundle, "context bundle must be provided")
        require_not_none(self.scheme_loader, "scheme loader must be provided")
        require_not_none(self.tar_processor, "tar processor must be provided")
        require_not_none(self.template_processor, "template processor must be provided")
        check_type(self.context_bundle, ContextBundle, "context bundle must be a ContextBundle instance")
        check_type(self.scheme_loader, ISchemeLoader, "scheme loader must be an ISchemeLoader instance")
        check_type(self.tar_processor, ITarProcessor, "tar processor must be an ITarProcessor instance")
        check_type(self.template_processor, ITemplateProcessor, "template processor must be an ITemplateProcessor instance")

    def merge(self, other: GeneratorComponentBundle) -> None:
        '''
            Merges non-None values from another GeneratorComponentBundle into this one.

            :param other: Another GeneratorComponentBundle to merge into this one.
            :type other: <GeneratorComponentBundle>
            :exceptions:
                | ATSTypeError: Other must be a GeneratorComponentBundle instance.
        '''
        check_type(other, GeneratorComponentBundle, "other must be a GeneratorComponentBundle instance")

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the GeneratorComponentBundle instance to a dictionary.

            :return: Dictionary representation of the GeneratorComponentBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return asdict(self)
