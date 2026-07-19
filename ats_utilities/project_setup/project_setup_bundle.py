# -*- coding: UTF-8 -*-

'''
Module
    project_setup_bundle.py
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
    Encapsulates core runtime components for simplification of ProjectSetupBundle creation.
'''

from __future__ import annotations

from dataclasses import dataclass

from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.project_setup.ipro_config import IProConfig
from ats_utilities.project_setup.ipro_name import IProName
from ats_utilities.project_setup.itemplate_dir import ITemplateDir
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
class ProjectSetupBundle:
    '''
        Encapsulates core runtime components for simplification of ProjectSetupBundle creation.
        Enables passing dependencies to other objects.

        It defines:

            :attributes:
                | pro_name - Project name mechanism.
                | pro_config - Project configuration mechanism.
                | template_dir - Project template directory mechanism.
                | context_bundle - The context bundle.
            :methods:
                | __post_init__ - Post-initialization hook to validate project setup bundle.
                | validate - Validates that project setup bundle is valid.
                | to_dict - Converts the project setup bundle instance to a dictionary.
    '''

    pro_name: IProName
    pro_config: IProConfig
    template_dir: ITemplateDir
    context_bundle: ContextBundle

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to validate project setup bundle.

            :exceptions:
                | ATSValueError: Project name must be provided.
                | ATSValueError: Project configuration must be provided.
                | ATSValueError: Template directory must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Project name must be an instance of IProName interface.
                | ATSTypeError: Project configuration must be an instance of IProConfig interface.
                | ATSTypeError: Template directory must be an instance of ITemplateDir interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle class.
        '''
        self.validate()

    def validate(self) -> None:
        '''
            Validates project setup bundle.
            Performs validation of all bundle attributes.
            All attributes must be non-None and instances of their respective interfaces.

            :exceptions:
                | ATSValueError: Project name must be provided.
                | ATSValueError: Project configuration must be provided.
                | ATSValueError: Template directory must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Project name must be an instance of IProName interface.
                | ATSTypeError: Project configuration must be an instance of IProConfig interface.
                | ATSTypeError: Template directory must be an instance of ITemplateDir interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle class.
        '''
        not_none(
            self.pro_name,
            r'project_setup_bundle::validate(...)',
            r'project name must be provided'
        )
        not_none(
            self.pro_config,
            r'project_setup_bundle::validate(...)',
            r'project configuration must be provided'
        )
        not_none(
            self.template_dir,
            r'project_setup_bundle::validate(...)',
            r'template directory must be provided'
        )
        not_none(
            self.context_bundle,
            r'project_setup_bundle::validate(...)',
            r'context bundle must be provided'
        )
        istype(
            self.pro_name, IProName,
            r'project_setup_bundle::validate(...)',
            r'project name must be an instance of IProName interface'
        )
        istype(
            self.pro_config, IProConfig,
            r'project_setup_bundle::validate(...)',
            r'project configuration must be an instance of IProConfig interface'
        )
        istype(
            self.template_dir, ITemplateDir,
            r'project_setup_bundle::validate(...)',
            r'template directory must be an instance of ITemplateDir interface'
        )
        istype(
            self.context_bundle, ContextBundle,
            r'project_setup_bundle::validate(...)',
            r'context bundle must be an instance of ContextBundle class'
        )

    def to_dict(self) -> dict:
        '''
            Converts the project setup bundle instance to a dictionary.

            :return: Dictionary representation of the project setup bundle instance.
            :rtype: <dict>
            :exceptions: None.
        '''
        return {name: getattr(self, name) for name in self.__slots__}
