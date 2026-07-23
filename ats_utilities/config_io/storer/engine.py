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
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Storer(IStorer):
    '''
        Creates an API for storing the configuration from mapping format to configuration file.
        2nd level of configuration storer implementation.

        It defines:

            :attributes:
                | _context - ContextBundle.
                | _processor - Processor interface instance.
                | _conf_file - Configuration file interface instance.

            :methods:
                | __init__ - Constructor.
                | get_context - Gets the context.
                | store_configuration - Stores configuration to file.
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
        context: str = r'storer::init(...)'
        not_none(own, context, r'component bundle must be provided')
        istype(own, ConfigIOBundle, context, r'component bundle must be of type ConfigIOBundle')
        self._context = own.context_bundle
        self._processor = own.processor
        self._conf_file = ConfFile(
            FileData(
                file_path=own.file_path,
                file_mode=own.WRITE_MODE,
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
    def store_configuration(self, config: Mapping[str, str]) -> bool:
        '''
            Writes configuration to a file.

            :param config: Configuration object.
            :type config: Mapping[str, str]
            :return: True if successful, otherwise False.
            :rtype: bool
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
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
