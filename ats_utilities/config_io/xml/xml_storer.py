# -*- coding: UTF-8 -*-

'''
Module
    xml_storer.py
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
    Defines class XMLStorer with attribute(s) and method(s).
    Stores the ATS configuration for the ATS.
'''

from typing import Dict, List, Optional
from xml.etree.ElementTree import Element, SubElement, tostring, ParseError
from xml.dom.minidom import parseString
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.xml.ixml_storer import IXMLStorer
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.xml.object2xml import Object2Xml
from ats_utilities.config_io.xml.xml_processor import ATSXMLProcessor
from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor
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


class XMLStorer(IXMLStorer):
    '''
        Defines class XMLStorer with attribute(s) and method(s).
        Stores the ATS configuration for the ATS.
        XML configuration-based storage support.

        It defines:

            :attributes:
                | __SECTION - Section name for ATS configuration.
                | __checker - Factoriezed parameters checker (default Checker).
                | __reporter - Factoriezed reporter for messaging (default Reporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __processor - Processor for XML content (default ATSXMLProcessor).
                | __obj2xml - Out API for information (default Object2Xml).
            :methods:
                | __init__ - Initializes XMLStorer constructor.
                | store_configuration - Stores the ATS configuration.
                | __str__ - Returns the XMLStorer as string representation.
    '''

    __SECTION: str = '[ats_info]'

    def __init__(
        self,
        info_file: Optional[str] = None,
        object2xml: Optional[IWrite] = None,
        config_bundle: Optional[ATSConfigFileBundle] = None,
        xml_processor: Optional[IXMLProcessor] = None
    ) -> None:
        '''
            Initializes XMLStorer constructor.

            :param info_file: Path to the info file | None.
            :type info_file: <Optional[str]>
            :param object2xml: An API for information | None.
            :type object2xml: <Optional[IWrite]>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <Optional[ATSConfigFileBundle]>
            :param xml_processor: Processor for XML content | None.
            :type xml_processor: <Optional[IXMLProcessor]>
            :exceptions: ATSTypeError.
        '''
        config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        self.__processor: IXMLProcessor = make_component(xml_processor, ATSXMLProcessor, None)
        validate_component(self.__processor, type(self.__processor), type(self.__processor).__name__)
        self.__obj2xml: IWrite = make_component(object2xml, Object2Xml, {
            'config_file': info_file, 'config_bundle': config_file_bundle
        })
        validate_component(self.__obj2xml, type(self.__obj2xml), type(self.__obj2xml).__name__)

    @validator([('dict:config', None)])
    def store_configuration(self, config: Dict[str, str]) -> bool:
        '''
            Stores the ATS configuration from dictionary format.

            :param config: Dictionary with XML information.
            :type config: <Dict[str, str]>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: ATSTypeError, ATSValueError, RuntimeError, AttributeError.
        '''
        try:
            root = Element('configuration')

            for tag_name, tag_value in config.items():
                child = SubElement(root, tag_name)
                child.text = str(tag_value)

            raw_xml = tostring(root, encoding='utf-8')
            parsed_xml = parseString(raw_xml)
            xml_content = parsed_xml.toprettyxml(indent="    ")

        except (TypeError, ValueError, ParseError):
            return False

        if not self.__processor.from_string(xml_content):
            return False

        return self.__obj2xml.write_configuration(self.__processor)

    def __str__(self) -> str:
        '''
            Returns the XMLStorer as string representation.

            :return: The XMLStorer as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
