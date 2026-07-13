# -*- coding: UTF-8 -*-

'''
Module
    config_loader.py
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
    Defines class ConfigLoader with attribute(s) and method(s).
    Default implementation of IConfigLoadManager and ILoader.
'''

from __future__ import annotations

from typing import override
from os.path import basename

from ats_utilities.config_io.loader.iconfig_manager import IConfigLoadManager, IConfigProcessor
from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.config_io.loader.config_loader_bundle import ConfigLoaderBundle
from ats_utilities.config_io.loader.iread import IRead
from ats_utilities.config_io.loader.file2object import File2Object
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import to_str
from ats_utilities.logger.ilogger import ILogger

from ats_utilities.config_io.processor.icfg_processor import ICFGProcessor
from ats_utilities.config_io.processor.iini_processor import IINIProcessor
from ats_utilities.config_io.processor.ijson_processor import IJSONProcessor
from ats_utilities.config_io.processor.ixml_processor import IXMLProcessor
from ats_utilities.config_io.processor.iyaml_processor import IYAMLProcessor

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

# Optional configuration interface type
IConfigProcessor = ICFGProcessor | IINIProcessor | IJSONProcessor | IXMLProcessor | IYAMLProcessor | None


class ConfigLoader(IConfigLoadManager, ILoader):
    '''
        Defines class ConfigLoader with attribute(s) and method(s).
        Default implementation of IConfigLoadManager and ILoader.

        It defines:

            :attributes:
                | _info_file - Configuration file for loading process (default None).
                | _config2object - Convertor configuration to object (default None).
                | _config_bundle - ATS configuration file bundle (default None).
                | _processor - Interface for configuration processor (default None).
                | _logger - Injected logger for logging.
            :methods:
                | setup_loader - Setup config loader based on configuration file type.
                | load_configuration - Loads the ATS configuration in dictionary format.
                | __str__ - Returns the ConfigLoader as string representation.
    '''

    _info_file: str | None
    _config2object: IRead | None
    _config_bundle: ConfigFileBundle | None
    _processor: IConfigProcessor | None
    _logger: ILogger

    def __init__(
        self,
        config_loader_bundle: ConfigLoaderBundle | None = None,
        info_file: str | None = None,
        config2object: IRead | None = None,
        config_bundle: ConfigFileBundle | None = None,
        processor: IConfigProcessor | None = None
    ) -> None:
        '''
            Initializes ConfigLoader constructor.

            :param config_loader_bundle: Configuration file for loading process | None.
            :type config_loader_bundle: <ConfigLoaderBundle | None>
            :param info_file: Path to the info file | None.
            :type info_file: <str | None>
            :param config2object: An API for information | None.
            :type config2object: <IRead | None>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <ConfigFileBundle | None>
            :param processor: Processor for configuration content | None.
            :type processor: <IConfigProcessor | None>
            :exceptions: None.
        '''
        if config_loader_bundle is not None:
            self._info_file = config_loader_bundle.info_file
            self._config2object = config_loader_bundle.config2object
            self._config_bundle = config_loader_bundle.config_bundle
            self._processor = config_loader_bundle.processor
        else:
            self._info_file = info_file
            self._config2object = config2object
            self._config_bundle = config_bundle
            self._processor = processor

        self._configuration = None
        if self._info_file:
            file_format: str = basename(self._info_file).split('.')[1]
            reader = make_component(self._config2object, File2Object, {
                'format_type': file_format,
                'config_file': self._info_file,
                'config_bundle': self._config_bundle,
                'processor': self._processor
            })
            validate_component(reader, IRead, r'reader must be an IRead instance')
            if bool(reader):
                self._configuration = reader.read_configuration()

    @override
    def setup_loader(self) -> ILoader:
        '''
            Setup configuration loader based on configuration file type.

            :return: Configuration loader interface.
            :rtype: <ILoader>
            :exceptions: None.
        '''
        if not self._info_file:
            return None

        file_format: str = basename(self._info_file).split('.')[1]
        if file_format not in ('cfg', 'ini', 'json', 'xml', 'yaml'):
            return None
        return self

    @override
    def load_configuration(self) -> dict[str, str]:
        '''
            Loads the ATS configuration in dictionary format.

            :return: Dictionary with configuration information.
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        if not self._configuration:
            return {}

        return self._configuration.to_dict()

    @override
    def __str__(self) -> str:
        '''
            Returns the ConfigLoader as string representation.

            :return: The ConfigLoader as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
