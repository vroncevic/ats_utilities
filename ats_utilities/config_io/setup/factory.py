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
from ats_utilities.config_io.setup.dependencies import ConfigIOBundleDependencies
from ats_utilities.config_io.setup.options import ConfigIOBundleOptions
from ats_utilities.config_io.setup.opt_validator import ConfigIOBundleOptionsValidator
from ats_utilities.config_io.setup.keys import ConfigIOBundleKeys
from ats_utilities.config_io.setup.registry import ConfigIOBundleRegistry
from ats_utilities.config_io.processor.factory_processor import ConfigProcessorFactory
from ats_utilities.context.bundle import ContextBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ConfigIOBundleFactory:
    '''
        Factory for creating config I/O bundle.

        It defines:

            :methods:
                | create_bundle - Creates a config I/O bundle using configuration options.
    '''

    @classmethod
    def create_bundle(cls, options: ConfigIOBundleOptions) -> ConfigIOBundle:
        '''
            Creates a config I/O bundle using configuration options.

            :param options: The creation options/parameters for the bundle.
            :return: The config I/O bundle.
            :exceptions:
                | ATSValueError: The config I/O bundle options must be provided and have proper attributes.
                | ATSTypeError:  The config I/O bundle options must be an instance of Mapping and its attributes
                |                must be instances of their respective types.
                | ATSValueError: The config I/O bundle dependencies must be provided and have proper attributes.
                | ATSTypeError:  The config I/O bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The config I/O bundle must be provided and have proper values.
                | ATSTypeError:  The config I/O bundle must be an instance of ConfigIOBundle and its
                |                attributes must be instances of their respective types.
        '''
        ConfigIOBundleOptionsValidator.validate(options)

        file_path: str = options.get(ConfigIOBundleKeys.OPTION_FILE_PATH)
        scheme: Mapping[str, str] = options.get(ConfigIOBundleKeys.OPTION_SCHEME)
        context_bundle: ContextBundle = options.get(ConfigIOBundleKeys.OPTION_CONTEXT_BUNDLE)
        processor = ConfigProcessorFactory.create_from_file_path(
            file_path=file_path,
            scheme=scheme
        )

        return ConfigIOBundleRegistry.create_bundle(
            ConfigIOBundleDependencies(
                file_path=file_path,
                processor=processor,
                context_bundle=context_bundle
            )
        )
