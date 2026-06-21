# -*- coding: UTF-8 -*-

'''
Module
    json_loader.py
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
    Defines class JSONLoader with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

from ats_utilities.config_io.iread import IRead
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.iloader import ILoader
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.json.json2object import Json2Object
from ats_utilities.config_io.json.json_processor import JSONProcessor
from ats_utilities.config_io.json.ijson_processor import IJSONProcessor
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import get_private_attr, format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class JSONLoader(ILoader):
    '''
        Defines class JSONLoader with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        JSON configuration-based API support.

        It defines:

            :attributes:
                | _checker - Factoriezed parameters checker (default Checker).
                | _reporter - Factoriezed reporter for messaging (default Reporter).
                | _verbose - Factoriezed Enable/Disable verbose option (default False).
                | _configuration - JSON processor configuration (default None).
            :methods:
                | __init__ - Initializes JSONLoader constructor.
                | load_configuration - Loads the ATS configuration in dictionary format.
                | __str__ - Returns the JSONLoader as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(
        self,
        info_file: str | None = None,
        json2object: IRead | None = None,
        config_bundle: ATSConfigFileBundle | None = None,
        json_processor: IJSONProcessor | None = None
    ) -> None:
        '''
            Initializes JSONLoader constructor.

            :param info_file: Path to the info file | None.
            :type info_file: <str | None>
            :param json2object: An API for information | None.
            :type json2object: <IRead | None>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <ATSConfigFileBundle | None>
            :param json_processor: Processor for JSON content | None.
            :type json_processor: <IJSONProcessor | None>
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
        processor: IJSONProcessor = make_component(json_processor, JSONProcessor, None)
        validate_component(processor, type(processor), type(processor).__name__)
        json2obj: IRead = make_component(json2object, Json2Object, {
            'config_file': info_file, 'config_bundle': config_file_bundle, 'json_processor': processor
        })
        validate_component(json2obj, type(json2obj), type(json2obj).__name__)
        self._configuration: IJSONProcessor | None = None

        if bool(json2obj):
            self._configuration = json2obj.read_configuration()

    def load_configuration(self) -> dict[str, str]:
        '''
            Loads the ATS configuration in dictionary format.

            :return: Dictionary with JSON information.
            :rtype: <dict[str, str]>
            :exceptions: None..
        '''
        if not self._configuration:
            return {}

        return self._configuration.to_dict()

    def __str__(self) -> str:
        '''
            Returns the JSONLoader as string representation.

            :return: The JSONLoader as string representation.
            :rtype: <str>
            :exceptions: None..
        '''
        return format_instance_to_string(self)
