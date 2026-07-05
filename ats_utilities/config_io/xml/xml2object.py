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

from __future__ import annotations

from typing import override

from ats_utilities.config_io.iread import IRead
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.file_bundle import FileBundle
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.config_io.xml.ixml_processor import IXMLProcessor
from ats_utilities.config_io.xml.xml_processor import XMLProcessor
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import to_str

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
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
                | _EXT - File extension of the configuration file.
                | _MODE - File open mode.
                | _config_file_bundle - Configuration file bundle parameters (default None).
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _file_checker - FileCheck for checking file (default FileCheck).
                | _xml_processor - Processor for XML content (default XMLProcessor).
                | _file_path - Configuration file path (default None).
                | _file_bundle_shared - File bundle parameters (default None).
            :methods:
                | __init__ - Initializes Xml2Object constructor.
                | read_configuration - Reads a configuration from an XML file.
                | __str__ - Returns the Xml2Object as string representation.
    '''

    _EXT: str = 'xml'
    _MODE: str = 'r'

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(
        self,
        config_file: str | None,
        config_bundle: ConfigFileBundle | None = None,
        xml_processor: IXMLProcessor | None = None
    ) -> None:
        '''
            Initializes Xml2Object constructor.

            :param config_file: Configuration file path in string format | None.
            :type config_file: <str | None>
            :param config_bundle: Configuration file bundle parameters | None.
            :type config_bundle: <ConfigFileBundle | None>
            :param xml_processor: Processor for XML content | None.
            :type xml_processor: <IXMLProcessor | None>
            :exceptions:
                | ATSTypeError: Invalid type in constructor arguments.
        '''
        self._config_file_bundle: ConfigFileBundle = config_bundle or ConfigFileBundle()
        factory_context_bundle(self, self._config_file_bundle.context)
        context_bundle_shared: ContextBundle = ContextBundle(
            checker=self._checker, reporter=self._reporter, verbose=self._verbose
        )
        self._file_checker: IFileCheck = make_component(
            self._config_file_bundle.file_checker, FileCheck, {'config_bundle': context_bundle_shared}
        )
        validate_component(self._file_checker, FileCheck)
        self._xml_processor: IXMLProcessor = make_component(xml_processor, XMLProcessor, None)
        validate_component(self._xml_processor, XMLProcessor)
        self._file_path: str = str(config_file)
        self._file_bundle_shared: FileBundle = FileBundle()
        self._file_bundle_shared.file_path = self._file_path
        self._file_bundle_shared.file_mode = self._MODE
        self._file_bundle_shared.file_format = self._EXT

    @vreport('read configuration from file {file_path}')
    @override
    def read_configuration(self) -> IXMLProcessor | None:
        '''
            Reads a configuration from an XML file.

            :return: Configuration object | None.
            :rtype: <IXMLProcessor | None>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        content: str | None = None
        config: IXMLProcessor | None = None

        with ConfFile(self._file_bundle_shared, self._config_file_bundle) as xml:
            if bool(xml):
                content = xml.read()

                if bool(content):
                    if self._xml_processor.from_string(str(content)):
                        config = self._xml_processor

        return config

    @override
    def __str__(self) -> str:
        '''
            Returns the Xml2Object as string representation.

            :return: The Xml2Object as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
