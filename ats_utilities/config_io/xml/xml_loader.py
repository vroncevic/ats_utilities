# -*- coding: UTF-8 -*-

'''
Module
    xml_loader.py
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
    Defines class XMLLoader with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

from typing import Dict, List, Optional
from ats_utilities.config_io.iread import IRead
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.config_io.iloader import ILoader
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.xml.xml2object import Xml2Object
from ats_utilities.config_io.xml.xml_processor import XMLProcessor
from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import get_private_attr, format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class XMLLoader(ILoader):
    '''
        Defines class XMLLoader with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        XML configuration-based API support.

        It defines:

            :attributes:
                | __checker - Factoriezed parameters checker (default Checker).
                | __reporter - Factoriezed reporter for messaging (default Reporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __configuration - XML processor configuration (default None).
            :methods:
                | __init__ - Initializes XMLLoader constructor.
                | load_configuration - Loads the ATS configuration in dictionary format.
                | __str__ - Returns the XMLLoader as string representation.
    '''

    def __init__(
        self,
        info_file: Optional[str] = None,
        xml2object: Optional[IRead] = None,
        config_bundle: Optional[ATSConfigFileBundle] = None,
        xml_processor: Optional[IXMLProcessor] = None
    ) -> None:
        '''
            Initializes XMLLoader constructor.

            :param info_file: Path to the info file | None.
            :type info_file: <Optional[str]>
            :param xml2object: An API for information | None.
            :type xml2object: <Optional[IRead]>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <Optional[ATSConfigFileBundle]>
            :param xml_processor: Processor for XML content | None.
            :type xml_processor: <Optional[IXMLProcessor]>
            :exceptions: ATSTypeError.
        '''
        config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        context_bundle_shared: ContextBundle = ContextBundle(
            checker=get_private_attr(self, 'checker'),
            reporter=get_private_attr(self, 'reporter'),
            verbose=get_private_attr(self, 'verbose')
        )
        file_checker: IFileCheck = make_component(
            config_file_bundle.file_checker, FileCheck, {'config_bundle': context_bundle_shared}
        )
        validate_component(file_checker, type(file_checker), type(file_checker).__name__)
        processor: IXMLProcessor = make_component(xml_processor, XMLProcessor, None)
        validate_component(processor, type(processor), type(processor).__name__)
        xml2obj: IRead = make_component(xml2object, Xml2Object, {
            'config_file': info_file, 'config_bundle': config_file_bundle, 'xml_processor': processor
        })
        validate_component(xml2obj, type(xml2obj), type(xml2obj).__name__)
        self.__configuration: Optional[IXMLProcessor] = None

        if bool(xml2obj):
            self.__configuration = xml2obj.read_configuration()

    def load_configuration(self) -> Dict[str, str]:
        '''
            Loads the ATS configuration in dictionary format.

            :return: Dictionary with XML information.
            :rtype: <Dict[str, str]>
            :exceptions: None.
        '''
        if not self.__configuration:
            return {}

        return self.__configuration.to_dict()

    def __str__(self) -> str:
        '''
            Returns the XMLLoader as string representation.

            :return: The XMLLoader as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
