# -*- coding: UTF-8 -*-

'''
Module
    dependencies.py
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
    Project dependencies and options for project bundle creation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypedDict

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.generator.project.ipro_config import IProConfig
from ats_utilities.generator.project.ipro_name import IProName
from ats_utilities.generator.project.itemplate_dir import ITemplateDir

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ProjectDependencies(TypedDict):
    '''
        Project dependencies for project bundle creation.

        It defines:

            :attributes:
                | pro_name: Project name mechanism.
                | pro_config: Project configuration mechanism.
                | template_dir: Project template directory mechanism.
                | context_bundle: The context bundle.
    '''
    pro_name: IProName
    pro_config: IProConfig
    template_dir: ITemplateDir
    context_bundle: ContextBundle


class ProjectOptions(TypedDict):
    '''
        Project options for project bundle creation.

        It defines:

            :attributes:
                | setup: The project setup dictionary.
                | context_bundle: The context bundle.
    '''
    setup: Mapping[str, Any]
    context_bundle: ContextBundle
