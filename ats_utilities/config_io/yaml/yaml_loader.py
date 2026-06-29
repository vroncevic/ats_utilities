# -*- coding: UTF-8 -*-

'''
Module
    yaml_loader.py
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
    Defines class YAMLLoader with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

from typing import override
from ats_utilities.config_io.iread import IRead
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.iloader import ILoader
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
from ats_utilities.config_io.yaml.yaml_processor import YAMLProcessor
from ats_utilities.config_io.yaml.iyaml_processor import IYAMLProcessor
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class YAMLLoader(ILoader):
    '''
        Defines class YAMLLoader with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        YAML configuration-based API support.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _configuration - YAML processor configuration (default None).
            :methods:
                | __init__ - Initializes YAMLLoader constructor.
                | load_configuration - Loads the ATS configuration in dictionary format.
                | __str__ - Returns the YAMLLoader as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(
        self,
        info_file: str | None = None,
        yaml2object: IRead | None = None,
        config_bundle: ATSConfigFileBundle | None = None,
        yaml_processor: IYAMLProcessor | None = None
    ) -> None:
        '''
            Initializes YAMLLoader constructor.

            :param info_file: Path to the info file | None.
            :type info_file: <str | None>
            :param yaml2object: An API for information | None.
            :type yaml2object: <IRead | None>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <ATSConfigFileBundle | None>
            :param yaml_processor: Configuration processor for YAML | None.
            :type yaml_processor: <IYAMLProcessor | None>
            :exceptions:
                | ATSTypeError: Invalid type in constructor arguments.
        '''
        config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        context_bundle_shared: ContextBundle = ContextBundle(
            checker=self._checker, reporter=self._reporter, verbose=self._verbose
        )
        file_checker: IFileCheck = make_component(
            config_file_bundle.file_checker, FileCheck, {'config_bundle': context_bundle_shared}
        )
        validate_component(file_checker, FileCheck)
        processor: IYAMLProcessor = make_component(yaml_processor, YAMLProcessor, None)
        validate_component(processor, YAMLProcessor)
        yaml2obj: IRead = make_component(yaml2object, Yaml2Object, {
            'config_file': info_file, 'config_bundle': config_file_bundle, 'yaml_processor': processor
        })
        validate_component(yaml2obj, Yaml2Object)
        self._configuration: IYAMLProcessor | None = None

        if bool(yaml2obj):
            self._configuration = yaml2obj.read_configuration()

    @override
    def load_configuration(self) -> dict[str, str]:
        '''
            Loads the ATS configuration in dictionary format.

            :return: Dictionary with YAML information.
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        if not self._configuration:
            return {}

        return self._configuration.to_dict()

    @override
    def __str__(self) -> str:
        '''
            Returns the YAMLLoader as string representation.

            :return: The YAMLLoader as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
