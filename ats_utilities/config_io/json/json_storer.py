# -*- coding: UTF-8 -*-

'''
Module
    json_storer.py
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
    Defines class JSONStorer with attribute(s) and method(s).
    Stores the ATS configuration for the ATS.
'''

from json import dumps
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.istorer import IStorer
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.json.object2json import Object2Json
from ats_utilities.config_io.json.json_processor import JSONProcessor
from ats_utilities.config_io.json.ijson_processor import IJSONProcessor
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


class JSONStorer(IStorer):
    '''
        Defines class JSONStorer with attribute(s) and method(s).
        Stores the ATS configuration for the ATS.
        JSON configuration-based storage support.

        It defines:

            :attributes:
                | _checker - Factoriezed parameters checker (default Checker).
                | _reporter - Factoriezed reporter for messaging (default Reporter).
                | _verbose - Factoriezed Enable/Disable verbose option (default False).
                | _processor - Processor for JSON content (default JSONProcessor).
                | _obj2json - Out API for information (default Object2Json).
            :methods:
                | __init__ - Initializes JSONStorer constructor.
                | store_configuration - Stores the ATS configuration.
                | __str__ - Returns the JSONStorer as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(
        self,
        info_file: str | None = None,
        object2json: IWrite | None = None,
        config_bundle: ATSConfigFileBundle | None = None,
        json_processor: IJSONProcessor | None = None
    ) -> None:
        '''
            Initializes JSONStorer constructor.

            :param info_file: Path to the info file | None.
            :type info_file: <str | None>
            :param object2json: An API for information | None.
            :type object2json: <IWrite | None>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <ATSConfigFileBundle | None>
            :param json_processor: Processor for JSON content | None.
            :type json_processor: <IJSONProcessor | None>
            :exceptions: ATSTypeError.
        '''
        config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        self._processor: IJSONProcessor = make_component(json_processor, JSONProcessor, None)
        validate_component(self._processor, type(self._processor), type(self._processor).__name__)
        self._obj2json: IWrite = make_component(object2json, Object2Json, {
            'config_file': info_file, 'config_bundle': config_file_bundle
        })
        validate_component(self._obj2json, type(self._obj2json), type(self._obj2json).__name__)

    @validator([('dict:config', None)])
    def store_configuration(self, config: dict[str, str]) -> bool:
        '''
            Stores the ATS configuration from dictionary format.

            :param config: Dictionary with JSON information.
            :type config: <dict[str, str]>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError..
        '''
        try:
            configuration = dumps(config, indent=4)
            if not self._processor.decode(configuration):
                return False

            return self._obj2json.write_configuration(self._processor)

        except (TypeError, ValueError):
            return False

    def __str__(self) -> str:
        '''
            Returns the JSONStorer as string representation.

            :return: The JSONStorer as string representation.
            :rtype: <str>
            :exceptions: None..
        '''
        return format_instance_to_string(self)
