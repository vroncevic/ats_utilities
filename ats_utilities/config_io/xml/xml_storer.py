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

from xml.etree.ElementTree import Element, SubElement, tostring, ParseError
from xml.dom.minidom import parseString
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.istorer import IStorer
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.xml.object2xml import Object2Xml
from ats_utilities.config_io.xml.xml_processor import XMLProcessor
from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor
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


class XMLStorer(IStorer):
    '''
        Defines class XMLStorer with attribute(s) and method(s).
        Stores the ATS configuration for the ATS.
        XML configuration-based storage support.

        It defines:

            :attributes:
                | _SECTION - Section name for ATS configuration.
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _processor - Processor for XML content (default XMLProcessor).
                | _obj2xml - Out API for information (default Object2Xml).
            :methods:
                | __init__ - Initializes XMLStorer constructor.
                | store_configuration - Stores the ATS configuration.
                | __str__ - Returns the XMLStorer as string representation.
    '''

    _SECTION: str = '[ats_info]'

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(
        self,
        info_file: str | None = None,
        object2xml: IWrite | None = None,
        config_bundle: ATSConfigFileBundle | None = None,
        xml_processor: IXMLProcessor | None = None
    ) -> None:
        '''
            Initializes XMLStorer constructor.

            :param info_file: Path to the info file | None.
            :type info_file: <str | None>
            :param object2xml: An API for information | None.
            :type object2xml: <IWrite | None>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <ATSConfigFileBundle | None>
            :param xml_processor: Processor for XML content | None.
            :type xml_processor: <IXMLProcessor | None>
            :exceptions: ATSTypeError.
        '''
        config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        self._processor: IXMLProcessor = make_component(xml_processor, XMLProcessor, None)
        validate_component(self._processor, XMLProcessor)
        self._obj2xml: IWrite = make_component(object2xml, Object2Xml, {
            'config_file': info_file, 'config_bundle': config_file_bundle
        })
        validate_component(self._obj2xml, Object2Xml)

    @validator([('dict:config', None)])
    def store_configuration(self, config: dict[str, str]) -> bool:
        '''
            Stores the ATS configuration from dictionary format.

            :param config: Dictionary with XML information.
            :type config: <dict[str, str]>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError..
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

        if not self._processor.from_string(xml_content):
            return False

        return self._obj2xml.write_configuration(self._processor)

    def __str__(self) -> str:
        '''
            Returns the XMLStorer as string representation.

            :return: The XMLStorer as string representation.
            :rtype: <str>
            :exceptions: None..
        '''
        return format_instance_to_string(self)
