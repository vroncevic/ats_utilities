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

from yaml import dump, YAMLError
from typing import override
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.istorer import IStorer
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
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
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
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
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _processor - Processor for YAML content (default YAMLProcessor).
                | _obj2yaml - Out API for information (default Object2Yaml).
            :methods:
                | __init__ - Initializes YAMLStorer constructor.
                | store_configuration - Stores the ATS configuration.
                | __str__ - Returns the YAMLStorer as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(
        self,
        info_file: str | None = None,
        object2yaml: IWrite | None = None,
        config_bundle: ATSConfigFileBundle | None = None,
        yaml_processor: IYAMLProcessor | None = None
    ) -> None:
        '''
            Initializes YAMLStorer constructor.

            :param info_file: Path to the info file | None.
            :type info_file: <str | None>
            :param object2yaml: An API for information | None.
            :type object2yaml: <IWrite | None>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <ATSConfigFileBundle | None>
            :param yaml_processor: Processor for YAML content | None.
            :type yaml_processor: <IYAMLProcessor | None>
            :exceptions:
                | ATSTypeError: Invalid type in constructor arguments.
        '''
        config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        self._processor: IYAMLProcessor = make_component(yaml_processor, YAMLProcessor, None)
        validate_component(self._processor, YAMLProcessor)
        self._obj2yaml: IWrite = make_component(object2yaml, Object2Yaml, {
            'config_file': info_file, 'config_bundle': config_file_bundle
        })
        validate_component(self._obj2yaml, Object2Yaml)

    @validator([('dict:config', None)])
    @override
    def store_configuration(self, config: dict[str, str]) -> bool:
        '''
            Stores the ATS configuration from dictionary format.

            :param config: Dictionary with YAML information.
            :type config: <dict[str, str]>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        try:
            yaml_content = dump(config, default_flow_style=False)

            if not self._processor.decode(yaml_content):
                return False

            return self._obj2yaml.write_configuration(self._processor)
        except (TypeError, ValueError, YAMLError):
            return False

    @override
    def __str__(self) -> str:
        '''
            Returns the YAMLStorer as string representation.

            :return: The YAMLStorer as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
