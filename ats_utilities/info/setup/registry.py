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
    Encapsulates the core runtime components for the simplification of the info bundle.
'''

from __future__ import annotations

from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.setup.dependencies import InfoBundleDependencies
from ats_utilities.info.setup.dep_validator import InfoBundleDependenciesValidator
from ats_utilities.info.setup.validator import InfoBundleValidator
from ats_utilities.info.setup.keys import InfoBundleKeys

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class InfoBundleRegistry:
    '''
        Encapsulates the core runtime components for the simplification of the info bundle.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates the info bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: InfoBundleDependencies) -> InfoBundle:
        '''
            Orchestrates dependency injection and creates the info bundle.

            :param dependencies: The registry-specific orchestration dependencies.
            :return: The info bundle.
            :exceptions:
                | ATSValueError: The info bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The info bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The info bundle must be provided and have proper values.
                | ATSTypeError:  The info bundle must be an instance of InfoBundle and its
                |                attributes must be instances of their respective types.
        '''
        InfoBundleDependenciesValidator.validate(dependencies)

        bundle: InfoBundle = InfoBundle(
            name=dependencies.get(InfoBundleKeys.DEPENDENCY_NAME) if dependencies else None,
            version=dependencies.get(InfoBundleKeys.DEPENDENCY_VERSION) if dependencies else None,
            licence=dependencies.get(InfoBundleKeys.DEPENDENCY_LICENCE) if dependencies else None,
            build_date=dependencies.get(InfoBundleKeys.DEPENDENCY_BUILD_DATE) if dependencies else None,
            repository=dependencies.get(InfoBundleKeys.DEPENDENCY_REPOSITORY) if dependencies else None,
            organization=dependencies.get(InfoBundleKeys.DEPENDENCY_ORGANIZATION) if dependencies else None,
            use_github=dependencies.get(InfoBundleKeys.DEPENDENCY_USE_GITHUB_INFRASTRUCTURE) if dependencies else None,
            logo=dependencies.get(InfoBundleKeys.DEPENDENCY_LOGO_PATH) if dependencies else None,
            log_file=dependencies.get(InfoBundleKeys.DEPENDENCY_LOG_FILE) if dependencies else None,
            info_ok=dependencies.get(InfoBundleKeys.DEPENDENCY_INFO_OK) if dependencies else None,
            context_bundle=dependencies.get(InfoBundleKeys.OPTION_CONTEXT_BUNDLE) if dependencies else None
        )

        InfoBundleValidator.validate(bundle)

        return bundle
