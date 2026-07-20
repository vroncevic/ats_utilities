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
    Defines class Loader with attribute(s) and method(s).
    Creates an API for loading configuration from file and deploying as object.
    2nd level of configuration loader implementation.
'''

from __future__ import annotations

from typing import override, Any

from ats_utilities.config_io.loader.iloader import ILoader
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.config_io.config_io_bundle import ConfigIOBundle
from ats_utilities.config_io.iconf_file import IConfFile
from ats_utilities.config_io.conf_file_factory import ConfFileFactory
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


class Loader(ILoader, ContextSupport):
    '''
        Creates an API for loading configuration from file and deploying as object.
        2nd level of configuration loader implementation.

        It defines:

            :attributes:
                | _shared_context - Shared ContextBundle.
                | _processor - Processor interface instance.
                | _conf_file - Configuration file interface instance.

            :methods:
                | __init__ - Constructor.
                | get_shared_context - Gets the shared context.
                | load_configuration - Loads configuration from file.
    '''

    _shared_context: ContextBundle
    _processor: IConfigProcessor
    _conf_file: IConfFile

    @override
    def __init__(self, component_bundle: ConfigIOBundle) -> None:
        '''
            Constructor.

            :param component_bundle: ConfigIOBundle instance.
            :type component_bundle: <ConfigIOBundle>
            :exceptions:
                | ATSValueError: Component bundle must be provided.
                | ATSTypeError: Component bundle must be ConfigIOBundle instance.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
                | ATSValueError: File path must be provided when processor is None.
                | ATSTypeError: File path must be a string.
                | ATSValueError: File does not exist.
                | ATSValueError: Extension must be provided.
                | ATSTypeError: Extension must be a string.
                | ATSValueError: Extension is not supported.
                | ATSTypeError: Validation of processor instance failed.
        '''
        context: str = r'loader::init(...)'
        not_none(component_bundle, context, r'component bundle must be provided')
        istype(component_bundle, ConfigIOBundle, context, r'component bundle must be an instance of ConfigIOBundle')
        self._shared_context = component_bundle.context_bundle
        ContextSupport.__init__(self, self._shared_context)
        self._processor = component_bundle.processor
        self._conf_file = ConfFileFactory.create_conf_file(
            file_path=component_bundle.file_path,
            file_mode=component_bundle.READ_MODE,
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
    def load_configuration(self) -> dict[str, Any]:
        '''
            Loads configuration from file and returns dictionary with configuration content.

            :return: Configuration dictionary.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        content: str | None = None

        try:
            with self._conf_file as config_file:
                if config_file:
                    content = config_file.read()

        except Exception:
            return {}

        if content is None:
            return {}

        if self._processor.deserialize(content):
            return self._processor.to_dict()

        return {}

    @override
    def __str__(self) -> str:
        '''
            Returns the Loader as string representation.

            :return: The Loader as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
