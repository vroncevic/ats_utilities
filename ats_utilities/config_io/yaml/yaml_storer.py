# -*- coding: UTF-8 -*-

'''
Module
    yaml_storer.py
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
    Defines class YAMLStorer with attribute(s) and method(s).
    Stores the ATS configuration for the ATS.
'''

from typing import Dict, List, Optional
from yaml import dump, YAMLError
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.istorer import IStorer
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.yaml.object2yaml import Object2Yaml
from ats_utilities.config_io.yaml.yaml_processor import YAMLProcessor
from ats_utilities.config_io.yaml.iyaml_processor import IYAMLProcessor
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class YAMLStorer(IStorer):
    '''
        Defines class YAMLStorer with attribute(s) and method(s).
        Stores the ATS configuration for the ATS.
        YAML configuration-based storage support.

        It defines:

            :attributes:
                | __checker - Factoriezed parameters checker (default Checker).
                | __reporter - Factoriezed reporter for messaging (default Reporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __processor - Processor for YAML content (default YAMLProcessor).
                | __obj2yaml - Out API for information (default Object2Yaml).
            :methods:
                | __init__ - Initializes YAMLStorer constructor.
                | store_configuration - Stores the ATS configuration.
                | __str__ - Returns the YAMLStorer as string representation.
    '''

    def __init__(
        self,
        info_file: Optional[str] = None,
        object2yaml: Optional[IWrite] = None,
        config_bundle: Optional[ATSConfigFileBundle] = None,
        yaml_processor: Optional[IYAMLProcessor] = None
    ) -> None:
        '''
            Initializes YAMLStorer constructor.

            :param info_file: Path to the info file | None.
            :type info_file: <Optional[str]>
            :param object2yaml: An API for information | None.
            :type object2yaml: <Optional[IWrite]>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <Optional[ATSConfigFileBundle]>
            :param yaml_processor: Processor for YAML content | None.
            :type yaml_processor: <Optional[IYAMLProcessor]>
            :exceptions: ATSTypeError.
        '''
        config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        self.__processor: IYAMLProcessor = make_component(yaml_processor, YAMLProcessor, None)
        validate_component(self.__processor, type(self.__processor), type(self.__processor).__name__)
        self.__obj2yaml: IWrite = make_component(object2yaml, Object2Yaml, {
            'config_file': info_file, 'config_bundle': config_file_bundle
        })
        validate_component(self.__obj2yaml, type(self.__obj2yaml), type(self.__obj2yaml).__name__)

    @validator([('dict:config', None)])
    def store_configuration(self, config: Dict[str, str]) -> bool:
        '''
            Stores the ATS configuration from dictionary format.

            :param config: Dictionary with YAML information.
            :type config: <Dict[str, str]>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: ATSTypeError, ATSValueError, RuntimeError, AttributeError.
        '''
        try:
            yaml_content = dump(config, default_flow_style=False)

            if not self.__processor.decode(yaml_content):
                return False

            return self.__obj2yaml.write_configuration(self.__processor)
        except (TypeError, ValueError, YAMLError):
            return False

    def __str__(self) -> str:
        '''
            Returns the YAMLStorer as string representation.

            :return: The YAMLStorer as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
