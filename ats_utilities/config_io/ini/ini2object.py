# -*- coding: UTF-8 -*-

'''
Module
    ini2object.py
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
    Defines class Ini2Object with attribute(s) and method(s).
    Creates an API for reading configuration from an INI file.
'''

from typing import List, Optional
from ats_utilities.config_io.iread import IRead
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.file_bundle import ATSFileBundle
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.ini.iini_processor import IINIProcessor
from ats_utilities.config_io.ini.ini_processor import ATSINIProcessor
from ats_utilities.reporter.proxy_reporter import vreporter
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


class Ini2Object(IRead):
    '''
        Defines class Ini2Object with attribute(s) and method(s).
        Creates an API for reading configuration from an INI file.
        Conversion of INI config to Python object.

        It defines:

            :attributes:
                | __EXT - File extension of the configuration file.
                | __MODE - File open mode.
                | __config_file_bundle - Configuration file bundle parameters (default None).
                | __checker - Factoriezed parameters checker (default ATSChecker).
                | __reporter - Factoriezed reporter for messaging (default ATSReporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __file_checker - FileCheck for checking file (default FileCheck).
                | __ini_processor - Processor for INI content (default ATSINIProcessor).
                | __file_path - Configuration file path (default None).
                | __file_bundle_shared - File bundle parameters (default None).
            :methods:
                | __init__ - Initials Ini2Object constructor.
                | read_configuration - reads configuration from an INI file.
                | __str__ - Returns the string representation of INI object.
    '''

    __EXT: str = 'ini'
    __MODE: str = 'r'

    def __init__(
        self,
        config_file: Optional[str],
        config_bundle: Optional[ATSConfigFileBundle] = None,
        ini_processor: Optional[IINIProcessor] = None,
    ) -> None:
        '''
            Initials Ini2Object constructor.

            :param config_file: Configuration file path in string format | None
            :type config_file: <Optional[str]>
            :param config_bundle: Configuration file bundle parameters | None
            :type config_bundle: <Optional[ATSConfigFileBundle]>
            :param ini_processor: Processor for INI content | None
            :type ini_processor: <Optional[IINIProcessor]>
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
        self.__ini_processor: IINIProcessor = make_component(ini_processor, ATSINIProcessor, None)
        validate_component(self.__ini_processor, type(self.__ini_processor), type(self.__ini_processor).__name__)
        self.__file_path: str = str(config_file)
        self.__file_bundle_shared: ATSFileBundle = ATSFileBundle()
        self.__file_bundle_shared.file_path = self.__file_path
        self.__file_bundle_shared.file_mode = self.__MODE
        self.__file_bundle_shared.file_format = self.__EXT

    @vreporter('read configuration from file {file_path}')
    def read_configuration(self) -> Optional[IINIProcessor]:
        '''
            Reads a configuration from an INI file.

            :return: Configuration object | None
            :rtype: <Optional[IINIProcessor]>
            :exceptions: None
        '''
        with ConfFile(self.__file_bundle_shared, self.__config_file_bundle) as ini:
            if bool(ini):
                if self.__ini_processor.from_stream(ini):
                    return self.__ini_processor

        return None

    def __str__(self) -> str:
        '''
            Returns the string representation of INI object.

            :return: The INI object as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
