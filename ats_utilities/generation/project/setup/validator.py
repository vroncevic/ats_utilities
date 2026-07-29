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
    Validator for project bundle instance.
'''

from __future__ import annotations

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generation.project.setup.bundle import ProjectBundle
from ats_utilities.generation.project.ipro_config import IProConfig
from ats_utilities.generation.project.ipro_name import IProName
from ats_utilities.generation.project.itemplate_dir import ITemplateDir
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


class ProjectValidator:
    '''
        Validator for project bundle instance.

        It defines:

            :methods:
                | validate - Validates project bundle instance.
    '''

    @classmethod
    def validate(cls, bundle: ProjectBundle) -> None:
        '''
            Validates project bundle instance.

            :param bundle: Project bundle instance to be validated.
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Project name must be provided.
                | ATSValueError: Project configuration must be provided.
                | ATSValueError: Template directory must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of ProjectBundle.
                | ATSTypeError: Project name must be an instance of IProName.
                | ATSTypeError: Project configuration must be an instance of IProConfig.
                | ATSTypeError: Template directory must be an instance of ITemplateDir.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        ctx: str = 'project_validator::validate(...)'

        not_none(bundle, ctx, 'bundle must be provided')
        istype(bundle, ProjectBundle, ctx, 'bundle must be an instance of ProjectBundle')

        not_none(bundle.pro_name, ctx, 'project name must be provided')
        not_none(bundle.pro_config, ctx, 'project configuration must be provided')
        not_none(bundle.template_dir, ctx, 'template directory must be provided')
        not_none(bundle.context_bundle, ctx, 'context bundle must be provided')

        istype(bundle.pro_name, IProName, ctx, 'project name must be an IProName instance')
        istype(bundle.pro_config, IProConfig, ctx, 'project configuration must be an IProConfig instance')
        istype(bundle.template_dir, ITemplateDir, ctx, 'template directory must be an ITemplateDir instance')
        istype(bundle.context_bundle, ContextBundle, ctx, 'context bundle must be a ContextBundle instance')
