# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating project bundle instance.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.utils.ifactory import IFactory
from ats_utilities.generator.project.setup.bundle import ProjectBundle
from ats_utilities.generator.project.setup.dependencies import (
    ProjectOptions, ProjectDependencies
)
from ats_utilities.generator.project.setup.registry import ProjectRegistry
from ats_utilities.generator.project.pro_name import ProName
from ats_utilities.generator.project.pro_config import ProConfig
from ats_utilities.generator.project.template_dir import TemplateDir
from ats_utilities.context.bundle import ContextBundle
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


class ProjectFactory(IFactory[ProjectBundle, ProjectOptions]):
    '''
        Factory for creating project bundle instance.

        It defines:

            :methods:
                | create_default_bundle - Creates a default project bundle using configuration options.
                | create_default_project_bundle - Creates a default project bundle using configuration options.
    '''

    @classmethod
    @override
    def create_default_bundle(cls, options: ProjectOptions) -> ProjectBundle:
        '''
            Creates a default project bundle using configuration options.

            :param options: Creation options/parameters for the bundle.
            :type options: ProjectOptions
            :return: Project bundle instance.
            :rtype: ProjectBundle
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a dictionary.
                | ATSValueError: Setup must be provided.
                | ATSTypeError: Setup must be a Mapping instance.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Project name must be provided.
                | ATSValueError: Project configuration must be provided.
                | ATSValueError: Template directory must be provided.
                | ATSTypeError: Bundle must be an instance of ProjectBundle.
                | ATSTypeError: Project name must be an IProName instance.
                | ATSTypeError: Project configuration must be an IProConfig instance.
                | ATSTypeError: Template directory must be an ITemplateDir instance.
        '''
        ctx: str = r'project_factory::create_default_bundle(...)'
        not_none(options, ctx, r'options must be provided')
        istype(options, dict, ctx, r'options must be a dictionary')

        setup: Mapping[str, Any] = options.get('setup')
        context_bundle: ContextBundle = options.get('context_bundle')

        not_none(setup, ctx, r'setup must be provided')
        istype(setup, Mapping, ctx, r'setup must be a Mapping instance')
        not_none(context_bundle, ctx, r'context_bundle must be provided')
        istype(context_bundle, ContextBundle, ctx, r'context_bundle must be ContextBundle instance')

        pro_name = ProName(context_bundle=context_bundle)
        pro_name.pro_name = setup.get('pro_name')
        pro_config = ProConfig(context_bundle=context_bundle)
        pro_config.config = setup.get('pro_config')
        template_dir = TemplateDir(context_bundle=context_bundle)
        template_dir.template_dir = setup.get('template_dir')

        return ProjectRegistry.create_bundle(
            ProjectDependencies(
                pro_name=pro_name,
                pro_config=pro_config,
                template_dir=template_dir,
                context_bundle=context_bundle
            )
        )

    @classmethod
    def create_default_project_bundle(
        cls,
        setup: Mapping[str, Any],
        context_bundle: ContextBundle
    ) -> ProjectBundle:
        '''
            Creates a default project bundle.

            :param setup: The project setup dictionary.
            :type setup: Mapping[str, Any]
            :param context_bundle: The context bundle.
            :type context_bundle: ContextBundle
            :return: Project bundle instance.
            :rtype: ProjectBundle
            :exceptions:
                | ATSValueError: Options must be provided.
                | ATSTypeError: Options must be a dictionary.
                | ATSValueError: Setup must be provided.
                | ATSTypeError: Setup must be a Mapping instance.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Project name must be provided.
                | ATSValueError: Project configuration must be provided.
                | ATSValueError: Template directory must be provided.
                | ATSTypeError: Bundle must be an instance of ProjectBundle.
                | ATSTypeError: Project name must be an IProName instance.
                | ATSTypeError: Project configuration must be an IProConfig instance.
                | ATSTypeError: Template directory must be an ITemplateDir instance.
        '''
        return cls.create_default_bundle(
            ProjectOptions(setup=setup, context_bundle=context_bundle)
        )
