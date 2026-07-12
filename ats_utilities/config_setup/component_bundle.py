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
    Defines component bundle dataclass for dependency grouping and management.
    Encapsulates config setup components to minimize constructor overhead.
'''

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

from ats_utilities.config_setup.ipro_config import IProConfig
from ats_utilities.config_setup.ipro_name import IProName
from ats_utilities.config_setup.itemplate_dir import ITemplateDir
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


@dataclass(slots=True, kw_only=True)
class ConfigSetupComponentBundle:
    '''
        Defines component bundle dataclass for dependency grouping and management.
        Encapsulates config setup components to minimize constructor overhead.

        It defines:

            :attributes:
                | pro_config - Project configuration mechanism (default None).
                | pro_name - Project name mechanism (default None).
                | template_dir - Project template directory mechanism (default None).
                | context_bundle - Context bundle for configuration utilities (default None).
            :methods:
                | validate - Validates that ConfigSetupComponentBundle is valid (can be called after merge).
                | merge - Merges non-None values from another ConfigSetupComponentBundle instance into this one.
                | to_dict - Converts the ConfigSetupComponentBundle instance to a dictionary.
    '''

    pro_config: IProConfig | None = None
    pro_name: IProName | None = None
    template_dir: ITemplateDir | None = None
    context_bundle: ContextBundle | None = None

    def validate(self) -> None:
        '''
            Validates that ConfigSetupComponentBundle is valid (can be called after merge).
            Performs validation of pro_config, pro_name, template_dir and context_bundle attributes.
            Pro config must be non-None and an instance of IProConfig interface.
            Pro name must be non-None and an instance of IProName interface.
            Template directory must be non-None and an instance of ITemplateDir interface.
            Context bundle must be non-None and an instance of ContextBundle.

            :exceptions:
                | ATSValueError: Project configuration must be provided.
                | ATSValueError: Project name must be provided.
                | ATSValueError: Template directory must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Project configuration must be an instance of IProConfig interface.
                | ATSTypeError: Project name must be an instance of IProName interface.
                | ATSTypeError: Template directory must be an instance of ITemplateDir interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        require_not_none(self.pro_config, 'project configuration must be provided')
        require_not_none(self.pro_name, 'project name must be provided')
        require_not_none(self.template_dir, 'template directory must be provided')
        require_not_none(self.context_bundle, 'context bundle must be provided')
        check_type(self.pro_config, IProConfig, 'project configuration must be an instance of IProConfig interface')
        check_type(self.pro_name, IProName, 'project name must be an instance of IProName interface')
        check_type(self.template_dir, ITemplateDir, 'template directory must be an instance of ITemplateDir interface')
        check_type(self.context_bundle, ContextBundle, 'context bundle must be an instance of ContextBundle')

    def merge(self, other: ConfigSetupComponentBundle) -> None:
        '''
            Merges non-None values from another ConfigSetupComponentBundle instance into this one.

            :param other: Another ConfigSetupComponentBundle instance to merge into this one.
            :type other: <ConfigSetupComponentBundle>
            :exceptions:
                | ATSTypeError: Other must be ConfigSetupComponentBundle instance.
        '''
        check_type(other, ConfigSetupComponentBundle, 'other must be ConfigSetupComponentBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict:
        '''
            Converts the ConfigSetupComponentBundle instance to a dictionary.

            :return: Dictionary representation of the ConfigSetupComponentBundle instance.
            :rtype: <dict>
            :exceptions: None.
        '''
        return asdict(self)
