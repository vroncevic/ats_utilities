# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines class Storer with attribute(s) and method(s).
    Creates an API for storing the configuration from mapping format to configuration file.
    2nd level of configuration storer implementation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override
from sys import stderr

from ats_utilities.config_io.storer.istorer import IStorer
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.config_io.config_io_bundle import ConfigIOBundle
from ats_utilities.config_io.iconf_file import IConfFile
from ats_utilities.config_io.conf_file_registry import ConfFileRegistry
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.context.context_support import ContextSupport
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Storer(ContextSupport, IStorer):
    '''
        Defines class Storer with attribute(s) and method(s).
        Creates an API for storing the configuration from mapping format to configuration file.
        2nd level of configuration storer implementation.

        It defines:

            :attributes:
                | _shared_context - Shared context bundle.
                | _processor - Processor instance.
                | _conf_file_bundle - Configuration file bundle parameters.
            :methods:
                | __init__ - Initializes Storer constructor.
                | get_shared_context - Returns the shared context.
                | store_configuration - Stores configuration content from mapping to configuration file.
                | __str__ - Returns the Storer as string representation.
    '''

    _shared_context: ContextBundle
    _processor: IConfigProcessor
    _conf_file: IConfFile

    def __init__(self, component_bundle: ConfigIOBundle) -> None:
        '''
            Initializes Storer constructor.

            :param component_bundle: Component bundle parameters.
            :type component_bundle: <ConfigIOBundle>
            :exceptions:
                | ATSValueError: Component bundle must be provided.
                | ATSTypeError: Component bundle must be of type ConfigIOBundle.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be of type ContextBundle.
                | ATSValueError: File path must be provided when processor is None.
                | ATSTypeError: File path must be a string.
                | ATSValueError: File does not exist.
                | ATSValueError: Extension must be provided.
                | ATSTypeError: Extension must be a string.
                | ATSValueError: Extension is not supported.
                | ATSTypeError: Validation of processor instance failed.
        '''
        not_none(
            component_bundle,
            r'storer::init(...)',
            r'component bundle must be provided'
        )
        istype(
            component_bundle, ConfigIOBundle,
            r'storer::init(...)',
            r'component bundle must be of type ConfigIOBundle'
        )
        self._shared_context = component_bundle.context_bundle
        ContextSupport.__init__(self, self._shared_context)
        self._processor = component_bundle.processor
        self._conf_file = ConfFileRegistry.create_conf_file(
            file_path=component_bundle.file_path,
            file_mode=component_bundle.WRITE_MODE,
            context_bundle=self._shared_context
        )

    @override
    def get_shared_context(self) -> ContextBundle:
        '''
            Returns the shared context.

            :return: Shared context.
            :rtype: <ContextBundle>
            :exceptions: None.
        '''
        return self._shared_context

    @override
    def store_configuration(self, config: Mapping[str, str]) -> bool:
        '''
            Writes configuration to a file.

            :param config: Configuration object.
            :type config: <Mapping[str, str]>
            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        if not config:
            return False

        if not self._processor.update_data(config):
            return False

        content = self._processor.serialize()

        try:
            with self._conf_file as config_file:
                if config_file:
                    config_file.write(content)
                    return True

        except Exception:
            return False

        return False

    @override
    def __str__(self) -> str:
        '''
            Returns the Storer instance as string representation.

            :return: The Storer instance as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
