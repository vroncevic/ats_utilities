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

from __future__ import annotations

from yaml import dump, YAMLError
from typing import override

from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.istorer import IStorer
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.config_io.yaml.object2yaml import Object2Yaml
from ats_utilities.config_io.yaml.yaml_processor import YAMLProcessor
from ats_utilities.config_io.yaml.iyaml_processor import IYAMLProcessor
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class YAMLStorer(IStorer):
    '''
        Defines class YAMLStorer with attribute(s) and method(s).
        Stores the ATS configuration for the ATS.
        YAML configuration-based storage support.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger for logging (default Logger).
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
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _processor: IYAMLProcessor
    _obj2yaml: IWrite

    def __init__(
        self,
        info_file: str | None = None,
        object2yaml: IWrite | None = None,
        config_bundle: ConfigFileBundle | None = None,
        yaml_processor: IYAMLProcessor | None = None
    ) -> None:
        '''
            Initializes YAMLStorer constructor.

            :param info_file: Path to the info file | None.
            :type info_file: <str | None>
            :param object2yaml: An API for information | None.
            :type object2yaml: <IWrite | None>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <ConfigFileBundle | None>
            :param yaml_processor: Processor for YAML content | None.
            :type yaml_processor: <IYAMLProcessor | None>
            :exceptions:
                | ATSTypeError: Invalid type in constructor arguments.
        '''
        config_file_bundle: ConfigFileBundle = config_bundle or ConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        self._processor = make_component(yaml_processor, YAMLProcessor, None)
        validate_component(self._processor, IYAMLProcessor, r'processor must be an IYAMLProcessor instance')
        self._obj2yaml = make_component(object2yaml, Object2Yaml, {
            'config_file': info_file, 'config_bundle': config_file_bundle
        })
        validate_component(self._obj2yaml, IWrite, r'obj2yaml must be an IWrite instance')

    @vcheck([('dict:config', None)])
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
        return to_str(self)
