# -*- coding: UTF-8 -*-

'''
Module
    project_setup_registry.py
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

from collections.abc import Mapping
from typing import Any

from ats_utilities.project_setup.project_setup_bundle import ProjectSetupBundle
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.project_setup.pro_name import ProName
from ats_utilities.project_setup.pro_config import ProConfig
from ats_utilities.project_setup.template_dir import TemplateDir

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ProjectSetupRegistry:
    '''
        Encapsulates core runtime components for simplification of ProjectSetupBundle creation.

        It defines:

            :methods:
                | create_default_project_setup_bundle - Creates a default ProjectSetupBundle.
    '''

    @classmethod
    def create_default_project_setup_bundle(
        cls,
        setup: Mapping[str, Any],
        context_bundle: ContextBundle
    ) -> ProjectSetupBundle:
        '''
            Creates a default ProjectSetupBundle with pre-configured components.

            :param setup: The project setup dictionary.
            :type setup: <Mapping[str, Any]>
            :param context_bundle: The context bundle.
            :type context_bundle: <ContextBundle>
            :return: Default ProjectSetupBundle instance.
            :rtype: <ProjectSetupBundle>
            :exceptions: None.
        '''
        pro_name: ProName = ProName(context_bundle=context_bundle)
        pro_name.pro_name = setup.get('pro_name')
        pro_config: ProConfig = ProConfig(context_bundle=context_bundle)
        pro_config.config = setup.get('pro_config')
        template_dir: TemplateDir = TemplateDir(context_bundle=context_bundle)
        template_dir.template_dir = setup.get('template_dir')

        return ProjectSetupBundle(
            pro_name=pro_name,
            pro_config=pro_config,
            template_dir=template_dir,
            context_bundle=context_bundle
        )
