# -*- coding: UTF-8 -*-

'''
Module
    ini_storer.py
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
    Defines class INIStorer with attribute(s) and method(s).
    Stores the ATS configuration for the ATS.
'''

from typing import Dict, List, Optional
from io import StringIO
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.ini.iini_storer import IINIStorer
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.ini.object2ini import Object2Ini
from ats_utilities.config_io.ini.ini_processor import ATSINIProcessor
from ats_utilities.config_io.ini.iini_processor import IINIProcessor
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class INIStorer(IINIStorer):
    '''
        Defines class INIStorer with attribute(s) and method(s).
        Stores the ATS configuration for the ATS.
        INI configuration-based storage support.

        It defines:

            :attributes:
                | __SECTION - Section name for ATS configuration.
                | __checker - Factoriezed parameters checker (default ATSChecker).
                | __reporter - Factoriezed reporter for messaging (default ATSReporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __processor - Processor for INI content (default ATSINIProcessor).
                | __obj2ini - Out API for information (default Object2Ini).
            :methods:
                | __init__ - Initials INIStorer constructor.
                | store_configuration - Stores the ATS configuration.
                | __str__ - Returns the string representation of INIStorer.
    '''

    __SECTION: str = '[ats_info]'

    def __init__(
        self,
        info_file: Optional[str] = None,
        object2ini: Optional[IWrite] = None,
        config_bundle: Optional[ATSConfigFileBundle] = None,
        ini_processor: Optional[IINIProcessor] = None
    ) -> None:
        '''
            Initials INIStorer constructor.

            :param info_file: Path to the info file | None
            :type info_file: <Optional[str]>
            :param object2ini: Out API for information | None
            :type object2ini: <Optional[IWrite]>
            :param config_bundle: Configuration bundle | None
            :type config_bundle: <Optional[ATSConfigFileBundle]>
            :param ini_processor: Processor for INI content | None
            :type ini_processor: <Optional[IINIProcessor]>
            :exceptions: ATSTypeError
        '''
        config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        self.__processor: IINIProcessor = make_component(ini_processor, ATSINIProcessor, None)
        validate_component(self.__processor, type(self.__processor), type(self.__processor).__name__)
        self.__obj2ini: IWrite = make_component(object2ini, Object2Ini, {
            'config_file': info_file, 'config_bundle': config_file_bundle
        })
        validate_component(self.__obj2ini, type(self.__obj2ini), type(self.__obj2ini).__name__)

    @validator([('dict:config', None)])
    def store_configuration(self, config: Dict[str, str]) -> bool:
        '''
            Stores the ATS configuration from dictionary format.

            :param config: Dictionary with INI information
            :type config: <Dict[str, str]>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: ATSTypeError, ATSValueError, RuntimeError, AttributeError
        '''
        ini_content = f'{self.__SECTION}\n'

        for k, v in config.items():
            ini_content += f"{k} = {v}\n"

        stream: StringIO = StringIO(ini_content)

        if not self.__processor.from_stream(stream):
            return False

        return self.__obj2ini.write_configuration(self.__processor)

    def __str__(self) -> str:
        '''
            Returns the string representation of INIStorer.

            :return: The INIStorer as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
