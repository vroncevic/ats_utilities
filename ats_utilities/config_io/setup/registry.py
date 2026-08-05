# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core config I/O bundle for the config I/O bundle.
'''

from __future__ import annotations

from ats_utilities.config_io.setup.bundle import ConfigIOBundle
from ats_utilities.config_io.setup.dependencies import ConfigIOBundleDependencies
from ats_utilities.config_io.setup.dep_validator import ConfigIOBundleDependenciesValidator
from ats_utilities.config_io.setup.keys import ConfigIOBundleKeys
from ats_utilities.config_io.setup.validator import ConfigIOBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ConfigIOBundleRegistry:
    '''
        Encapsulates core config I/O bundle for the config I/O bundle.

        It defines:

            :methods:
                | create_bundle - Orchestrates the dependency injection and creates a config I/O bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: ConfigIOBundleDependencies) -> ConfigIOBundle:
        '''
            Orchestrates the dependency injection and creates a config I/O bundle.

            :param dependencies: The registry-specific orchestration dependencies.
            :return: The ConfigIOBundle.
            :exceptions:
                | ATSValueError: The config I/O bundle dependencies must be provided and have proper attributes.
                | ATSTypeError:  The config I/O bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The config I/O bundle must be provided and have proper values.
                | ATSTypeError:  The config I/O bundle must be an instance of ConfigIOBundle and its
                |                attributes must be instances of their respective types.
        '''
        ConfigIOBundleDependenciesValidator.validate(dependencies)

        bundle: ConfigIOBundle = ConfigIOBundle(
            file_path=dependencies.get(ConfigIOBundleKeys.DEPENDENCY_FILE_PATH) if dependencies else None,
            processor=dependencies.get(ConfigIOBundleKeys.DEPENDENCY_PROCESSOR) if dependencies else None,
            context_bundle=dependencies.get(ConfigIOBundleKeys.DEPENDENCY_CONTEXT_BUNDLE) if dependencies else None
        )

        ConfigIOBundleValidator.validate(bundle)

        return bundle
