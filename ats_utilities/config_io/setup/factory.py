# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating config I/O bundle.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.config_io.setup.bundle import ConfigIOBundle
from ats_utilities.config_io.setup.dependencies import ConfigIODependencies
from ats_utilities.config_io.setup.options import ConfigIOOptions
from ats_utilities.config_io.setup.opt_validator import ConfigIOOptionsValidator
from ats_utilities.config_io.setup.keys import ConfigIOKeys
from ats_utilities.config_io.setup.registry import ConfigIORegistry
from ats_utilities.config_io.processor.factory_processor import ConfigProcessorFactory
from ats_utilities.context.bundle import ContextBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ConfigIOFactory:
    '''
        Factory for creating config I/O bundle.

        It defines:

            :methods:
                | create_bundle - Creates a config I/O bundle using configuration options.
    '''

    @classmethod
    def create_bundle(cls, options: ConfigIOOptions) -> ConfigIOBundle:
        '''
            Creates a config I/O bundle using configuration options.

            :param options: The creation options/parameters for the bundle.
            :return: The config I/O bundle.
            :exceptions:
                | ATSValueError: Options must be provided and have proper values.
                | ATSTypeError:  Options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        ConfigIOOptionsValidator.validate(options)

        file_path: str = options.get(ConfigIOKeys.OPTION_FILE_PATH)
        scheme: Mapping[str, str] = options.get(ConfigIOKeys.OPTION_SCHEME)
        context_bundle: ContextBundle = options.get(ConfigIOKeys.OPTION_CONTEXT_BUNDLE)
        processor = ConfigProcessorFactory.create_from_file_path(
            file_path=file_path,
            scheme=scheme
        )

        return ConfigIORegistry.create_bundle(
            ConfigIODependencies(
                file_path=file_path,
                processor=processor,
                context_bundle=context_bundle
            )
        )
