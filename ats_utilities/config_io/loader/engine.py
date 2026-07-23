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
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.setup.bundle import ConfigIOBundle
from ats_utilities.config_io.iconf_file import IConfFile
from ats_utilities.config_io.data import FileData
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Loader(ILoader):
    '''
        Creates an API for loading configuration from file and deploying as object.
        2nd level of configuration loader implementation.

        It defines:

            :attributes:
                | _context - Context bundle.
                | _processor - Processor interface instance.
                | _conf_file - Configuration file interface instance.

            :methods:
                | __init__ - Constructor.
                | get_context - Gets the context.
                | load_configuration - Loads configuration from file.
    '''

    _context: ContextBundle
    _processor: IConfigProcessor
    _conf_file: IConfFile

    @override
    def __init__(self, own: ConfigIOBundle) -> None:
        '''
            Constructor.

            :param own: ConfigIOBundle instance.
            :type own: ConfigIOBundle
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
        not_none(own, context, r'component bundle must be provided')
        istype(own, ConfigIOBundle, context, r'component bundle must be an instance of ConfigIOBundle')
        self._context = own.context_bundle
        self._processor = own.processor
        self._conf_file = ConfFile(
            FileData(
                file_path=own.file_path,
                file_mode=own.READ_MODE,
                context_bundle=self._context
            )
        )

    @override
    def get_context(self) -> ContextBundle:
        '''
            Returns the context.

            :return: Context.
            :rtype: ContextBundle
            :exceptions: None.
        '''
        return self._context

    @override
    def load_configuration(self) -> dict[str, Any]:
        '''
            Loads configuration from file and returns dictionary with configuration content.

            :return: Configuration dictionary.
            :rtype: dict[str, Any]
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
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
