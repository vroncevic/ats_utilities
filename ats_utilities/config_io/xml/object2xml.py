# -*- coding: UTF-8 -*-

'''
Module
    object2xml.py
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
    Defines class Object2Xml with attribute(s) and method(s).
    Creates an API for writing a configuration to a XML file.
'''
from typing import List, Optional
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.file_bundle import ATSFileBundle
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor
from ats_utilities.reporter.proxy_reporter import vreporter
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import get_private_attr, format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Object2Xml(IWrite):
    '''
        Defines class Object2Xml with attribute(s) and method(s).
        Creates an API for writing a configuration to a XML file.
        Conversion of Python object to XML content.

        It defines:

            :attributes:
                | __EXT - File extension of the configuration file.
                | __MODE - File open mode.
                | __config_file_bundle - Configuration file bundle parameters (default None).
                | __checker - Factoriezed parameters checker (default ATSChecker).
                | __reporter - Factoriezed reporter for messaging (default ATSReporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __file_checker - FileCheck for checking file (default FileCheck).
                | __file_path - Configuration file path (default None).
                | __file_bundle_shared - File bundle parameters (default None).
            :methods:
                | __init__ - Initials Object2Xml constructor.
                | write_configuration - Writes configuration to a XML file.
                | __str__ - Returns the string representation of object2xml.
    '''

    __EXT: str = 'xml'
    __MODE: str = 'w'

    def __init__(
        self,
        config_file: Optional[str],
        config_bundle: Optional[ATSConfigFileBundle] = None
    ) -> None:
        '''
            Initials Object2Xml constructor.

            :param config_file: Configuration file path in string format | None
            :type config_file: <Optional[str]>
            :param config_bundle: Configuration file bundle parameters | None
            :type config_bundle: <Optional[ATSConfigFileBundle]>
            :exceptions: ATSTypeError
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
        self.__file_path: str = str(config_file)
        self.__file_bundle_shared: ATSFileBundle = ATSFileBundle()
        self.__file_bundle_shared.file_path = self.__file_path
        self.__file_bundle_shared.file_mode = self.__MODE
        self.__file_bundle_shared.file_format = self.__EXT

    @validator([('Optional[IXMLProcessor]:config', None)])
    @vreporter('write configuration to file {file_path}')
    def write_configuration(self, config: Optional[IXMLProcessor]) -> bool:
        '''
            Writes configuration to a XML file.

            :param config: Configuration object | None
            :type config: <Optional[IXMLProcessor]>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions:
                | ATSTypeError, ATSValueError, RuntimeError, AttributeError
                | RuntimeError, AttributeError
        '''
        status: bool = False

        if not bool(config):
            return status

        xml_content: str = config.to_string()

        if not bool(xml_content):
            return status

        with ConfFile(self.__file_bundle_shared, self.__config_file_bundle) as xml:
            if bool(xml):
                if xml.write(xml_content):
                    status = True

        return status

    def __str__(self) -> str:
        '''
            Returns the string representation of object2xml.

            :return: The object2xml as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
