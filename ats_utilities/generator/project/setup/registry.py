# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core runtime components for simplification of project bundle creation.
'''

from __future__ import annotations

from typing import override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.generator.project.setup.bundle import ProjectBundle
from ats_utilities.generator.project.setup.dependencies import ProjectDependencies
from ats_utilities.generator.project.setup.validator import ProjectValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ProjectRegistry(IRegistry[ProjectBundle, ProjectDependencies]):
    '''
        Encapsulates core runtime components for simplification of project bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates a project bundle instance.
    '''

    @classmethod
    @override
    def create_bundle(cls, dependencies: ProjectDependencies) -> ProjectBundle:
        '''
            Orchestrates dependency injection and creates a project bundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :type dependencies: ProjectDependencies
            :return: Project bundle instance.
            :rtype: ProjectBundle
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
        bundle = ProjectBundle(
            pro_name=dependencies.get('pro_name'),
            pro_config=dependencies.get('pro_config'),
            template_dir=dependencies.get('template_dir'),
            context_bundle=dependencies.get('context_bundle')
        )

        ProjectValidator.validate(bundle)

        return bundle
