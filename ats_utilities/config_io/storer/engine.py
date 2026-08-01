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
    Defines the Storer class with attribute(s) and method(s).
    Provides an API for storing the configuration from mapping format to configuration file.
    2nd level of configuration storer implementation.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.config_io.setup.bundle import ConfigIOBundle
from ats_utilities.config_io.setup.validator import ConfigIOValidator
from ats_utilities.config_io.iconf_file import IConfFile
from ats_utilities.config_io.data import FileData
from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class Storer:
    '''
        Defines the Storer class with attribute(s) and method(s).
        Provides an API for storing the configuration from mapping format to configuration file.
        2nd level of configuration storer implementation.

        It defines:

            :attributes:
                | _context - The ContextBundle.
                | _processor - The processor interface instance.
                | _conf_file - The configuration file interface instance.

            :methods:
                | __init__ - Initializes storer.
                | get_context - Gets context.
                | store_configuration - Stores configuration to file.
                | __str__ - Returns the storer as a string representation.
    '''

    _context: ContextBundle
    _processor: IConfigProcessor
    _conf_file: IConfFile

    def __init__(self, own: ConfigIOBundle) -> None:
        '''
            Initializes storer.

            :param own: The ConfigIOBundle instance.
            :exceptions:
                | ATSValueError: ConfigIOBundle must be provided and have proper values.
                | ATSTypeError:  ConfigIOBundle must be an instance of ConfigIOBundle and its
                |                attributes must be instances of their respective types.
        '''
        ConfigIOValidator.validate(own)
        self._context = own.context_bundle
        self._processor = own.processor
        self._conf_file = ConfFile(
            FileData(
                file_path=own.file_path,
                file_mode=own.WRITE_MODE,
                context_bundle=self._context
            )
        )

    def get_context(self) -> ContextBundle:
        '''
            Returns context.

            :return: The context.
            :exceptions: None.
        '''
        return self._context

    def store_configuration(self, config: Mapping[str, str]) -> bool:
        '''
            Writes configuration to file.

            :param config: The configuration object.
            :return: True if successful, otherwise False.
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

    def __str__(self) -> str:
        '''
            Returns the storer as a string representation.

            :return: The Storer as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
