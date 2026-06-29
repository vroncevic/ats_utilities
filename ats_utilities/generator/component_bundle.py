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

from typing import Any
from dataclasses import dataclass
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.generator.ischeme_loader import ISchemeLoader
from ats_utilities.generator.itar_processor import ITarProcessor
from ats_utilities.generator.itemplate_processor import ITemplateProcessor
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


@dataclass
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
                | validate - Validates that essential components are set.
                | merge - Merges non-None values from another bundle into this one.
                | to_dict - Converts the bundle attributes to a dictionary.
    '''

    scheme_loader: ISchemeLoader | None = None
    tar_processor: ITarProcessor | None = None
    template_processor: ITemplateProcessor | None = None
    context_bundle: ContextBundle | None = None


    def validate(self) -> None:
        '''
            Validates that essential components are set.

            :exceptions:
                | ATSValueError: Context bundle must be set.
                | ATSValueError: Scheme loader must be set.
                | ATSValueError: Tar processor must be set.
                | ATSValueError: Template processor must be set.
        '''
        if not self.context_bundle:
            raise ATSValueError("context bundle must be set.")

        if not self.scheme_loader:
            raise ATSValueError("scheme loader must be set.")

        if not self.tar_processor:
            raise ATSValueError("tar processor must be set.")

        if not self.template_processor:
            raise ATSValueError("template processor must be set.")

    def merge(self, other: 'GeneratorComponentBundle') -> None:
        '''
            Merges non-None values from another bundle into this one.

            :param other: Another bundle to merge into this one.
            :type other: <GeneratorComponentBundle>
            :exceptions: None.
        '''
        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the bundle attributes to a dictionary.

            :return: Dictionary representation of the bundle attributes.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_')
        }
