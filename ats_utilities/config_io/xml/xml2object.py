# -*- coding: UTF-8 -*-

'''
Module
    xml2object.py
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
    Defines class Xml2Object with attribute(s) and method(s).
    Creates an API for reading a configuration from an XML file.
'''

from typing import List, Optional
from ats_utilities.config_io.iread import IRead
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.file_bundle import ATSFileBundle
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor
from ats_utilities.config_io.xml.xml_processor import ATSXMLProcessor
from ats_utilities.reporter.proxy_reporter import vreporter
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


class Xml2Object(IRead):
    '''
        Defines class Xml2Object with attribute(s) and method(s).
        Creates an API for reading a configuration from an XML file.
        Conversion of XML content to Python object.

        It defines:

            :attributes:
                | __EXT - File extension of the configuration file.
                | __MODE - File open mode.
                | __config_file_bundle - Configuration file bundle parameters (default None).
                | __checker - Factoriezed parameters checker (default Checker).
                | __reporter - Factoriezed reporter for messaging (default Reporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __file_checker - FileCheck for checking file (default FileCheck).
                | __xml_processor - Processor for XML content (default ATSXMLProcessor).
                | __file_path - Configuration file path (default None).
                | __file_bundle_shared - File bundle parameters (default None).
            :methods:
                | __init__ - Initializes Xml2Object constructor.
                | read_configuration - Reads a configuration from an XML file.
                | __str__ - Returns the Xml2Object as string representation.
    '''

    __EXT: str = 'xml'
    __MODE: str = 'r'

    def __init__(
        self,
        config_file: Optional[str],
        config_bundle: Optional[ATSConfigFileBundle] = None,
        xml_processor: Optional[IXMLProcessor] = None
    ) -> None:
        '''
            Initializes Xml2Object constructor.

            :param config_file: Configuration file path in string format | None.
            :type config_file: <Optional[str]>
            :param config_bundle: Configuration file bundle parameters | None.
            :type config_bundle: <Optional[ATSConfigFileBundle]>
            :param xml_processor: Processor for XML content | None.
            :type xml_processor: <Optional[IXMLProcessor]>
            :exceptions: ATSTypeError.
        '''
        self.__config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, self.__config_file_bundle.context)
        context_bundle_shared: ContextBundle = ContextBundle(
            checker=get_private_attr(self, 'checker'),
            reporter=get_private_attr(self, 'reporter'),
            verbose=get_private_attr(self, 'verbose')
        )
        self.__file_checker: IFileCheck = make_component(
            self.__config_file_bundle.file_checker, FileCheck, {'config_bundle': context_bundle_shared}
        )
        validate_component(self.__file_checker, type(self.__file_checker), type(self.__file_checker).__name__)
        self.__xml_processor: IXMLProcessor = make_component(xml_processor, ATSXMLProcessor, None)
        validate_component(self.__xml_processor, type(self.__xml_processor), type(self.__xml_processor).__name__)
        self.__file_path: str = str(config_file)
        self.__file_bundle_shared: ATSFileBundle = ATSFileBundle()
        self.__file_bundle_shared.file_path = self.__file_path
        self.__file_bundle_shared.file_mode = self.__MODE
        self.__file_bundle_shared.file_format = self.__EXT

    @vreporter('read configuration from file {file_path}')
    def read_configuration(self) -> Optional[IXMLProcessor]:
        '''
            Reads a configuration from an XML file.

            :return: Configuration object | None.
            :rtype: <Optional[IXMLProcessor]>
            :exceptions: None.
        '''
        content: Optional[str] = None
        config: Optional[IXMLProcessor] = None

        with ConfFile(self.__file_bundle_shared, self.__config_file_bundle) as xml:
            if bool(xml):
                content = xml.read()

                if bool(content):
                    if self.__xml_processor.from_string(str(content)):
                        config = self.__xml_processor

        return config

    def __str__(self) -> str:
        '''
            Returns the Xml2Object as string representation.

            :return: The Xml2Object as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
