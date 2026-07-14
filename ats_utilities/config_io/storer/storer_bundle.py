# -*- coding: UTF-8 -*-

'''
Module
    config_storer.py
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
    Defines class ConfigStorer with attribute(s) and method(s).
    Stores the ATS configuration for the ATS.
'''

from __future__ import annotations

from io import StringIO
from json import dumps
from typing import override, Any
from xml.dom.minidom import parseString
from xml.etree.ElementTree import Element, SubElement, tostring, ParseError
from yaml import dump, YAMLError

from ats_utilities.exceptions import ATSValueError
from ats_utilities.config_io.storer.iwrite import IWrite
from ats_utilities.config_io.storer.istorer import IStorer
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.config_io.storer.object2file import Object2File
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import to_str

# Processors and interfaces
from ats_utilities.config_io.processor.xml_processor import XMLProcessor
from ats_utilities.config_io.processor.ixml_processor import IXMLProcessor
from ats_utilities.config_io.processor.json_processor import JSONProcessor
from ats_utilities.config_io.processor.ijson_processor import IJSONProcessor
from ats_utilities.config_io.processor.yaml_processor import YAMLProcessor
from ats_utilities.config_io.processor.iyaml_processor import IYAMLProcessor
from ats_utilities.config_io.processor.ini_processor import INIProcessor
from ats_utilities.config_io.processor.iini_processor import IINIProcessor
from ats_utilities.config_io.processor.cfg_processor import CFGProcessor
from ats_utilities.config_io.processor.icfg_processor import ICFGProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

class ConfigStorer(IStorer):
    '''
        Defines class ConfigStorer with attribute(s) and method(s).
        Stores the ATS configuration for the ATS.
        Unified configuration-based storage support.

        It defines:

            :attributes:
                | _SECTION - Section name for ATS configuration.
                | _XML_INDENT - XML indent for pretty printing.
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger for logging (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _format_type - Format type string (xml, json, yaml, ini, cfg).
                | _processor - Processor for content.
                | _obj2file - Out API for information (default Object2File).
            :methods:
                | __init__ - Initializes ConfigStorer constructor.
                | store_configuration - Stores the ATS configuration.
                | __str__ - Returns the ConfigStorer as string representation.
    '''

    _PROCESSOR_MAPPING: dict[str, tuple[type, type]] = {
        'xml': (XMLProcessor, IXMLProcessor),
        'json': (JSONProcessor, IJSONProcessor),
        'yaml': (YAMLProcessor, IYAMLProcessor),
        'ini': (INIProcessor, IINIProcessor),
        'cfg': (CFGProcessor, ICFGProcessor)
    }
    _SECTION: str = '[ats_info]'
    _XML_INDENT: str = '    '
    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _format_type: str
    _processor: Any
    _obj2file: IWrite

    def __init__(
        self,
        format_type: str,
        info_file: str | None = None,
        object2file: IWrite | None = None,
        config_bundle: ConfigFileBundle | None = None,
        processor: Any = None
    ) -> None:
        '''
            Initializes ConfigStorer constructor.

            :param format_type: Type of format (xml, json, yaml, ini, cfg).
            :type format_type: <str>
            :param info_file: Path to the info file | None.
            :type info_file: <str | None>
            :param object2file: An API for information | None.
            :type object2file: <IWrite | None>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <ConfigFileBundle | None>
            :param processor: Processor for content | None.
            :type processor: <Any>
            :exceptions:
                | ATSTypeError: Invalid type in constructor arguments.
                | ATSValueError: Unsupported format type.
        '''
        self._format_type = str(format_type).lower()
        if self._format_type not in self._PROCESSOR_MAPPING:
            raise ATSValueError(f'Unsupported format type: {self._format_type}')

        config_file_bundle: ConfigFileBundle = config_bundle or ConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)

        proc_cls, proc_interface = self._PROCESSOR_MAPPING[self._format_type]
        self._processor = make_component(processor, proc_cls, None)
        validate_component(self._processor, proc_interface, f'processor must be an {proc_interface.__name__} instance')

        self._obj2file = make_component(object2file, Object2File, {
            'format_type': self._format_type, 'config_file': info_file, 'config_bundle': config_file_bundle
        })
        validate_component(self._obj2file, IWrite, r'obj2file must be an IWrite instance')

    @vcheck([('dict:config', None)])
    @override
    def store_configuration(self, config: dict[str, str]) -> bool:
        '''
            Stores the ATS configuration from dictionary format.

            :param config: Dictionary with information.
            :type config: <dict[str, str]>
            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions:
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        try:
            if self._format_type == 'xml':
                root = Element('configuration')
                for tag_name, tag_value in config.items():
                    child = SubElement(root, tag_name)
                    child.text = str(tag_value)
                raw_xml = tostring(root, encoding='utf-8')
                parsed_xml = parseString(raw_xml)
                xml_content = parsed_xml.toprettyxml(indent=self._XML_INDENT)
                if not self._processor.from_string(xml_content):
                    return False

            elif self._format_type == 'json':
                json_content = dumps(config, indent=4)
                if not self._processor.decode(json_content):
                    return False

            elif self._format_type == 'yaml':
                yaml_content = dump(config, default_flow_style=False)
                if not self._processor.decode(yaml_content):
                    return False

            elif self._format_type == 'ini':
                ini_content = f'{self._SECTION}\n'
                for k, v in config.items():
                    ini_content += f'{k} = {v}\n'
                stream: StringIO = StringIO(ini_content)
                if not self._processor.from_stream(stream):
                    return False

            elif self._format_type == 'cfg':
                lines: list[str] = [f'{k} = {v}\n' for k, v in config.items()]
                self._processor.from_lines(lines)

            return self._obj2file.write_configuration(self._processor)

        except (TypeError, ValueError, YAMLError, ParseError):
            return False

    @override
    def __str__(self) -> str:
        '''
            Returns the ConfigStorer as string representation.

            :return: The ConfigStorer as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
