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
    Encapsulates core runtime components for simplification of info bundle creation.
'''

from __future__ import annotations

from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.setup.dependencies import InfoDependencies
from ats_utilities.info.setup.dep_validator import InfoDependenciesValidator
from ats_utilities.info.setup.validator import InfoValidator
from ats_utilities.info.setup.keys import InfoKeys

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class InfoRegistry:
    '''
        Encapsulates core runtime components for simplification of info bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates an info bundle instance.
    '''

    @classmethod
    def create_bundle(cls, dependencies: InfoDependencies) -> InfoBundle:
        '''
            Orchestrates dependency injection and creates an info bundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :return: Info bundle instance.
            :exceptions:
                | ATSValueError: Dependencies must be provided and have proper values.
                | ATSTypeError:  Dependencies must be an instance of InfoDependencies and its
                |                attributes must be instances of their respective types.
        '''
        InfoDependenciesValidator.validate(dependencies)

        bundle: InfoBundle = InfoBundle(
            name=dependencies.get(InfoKeys.DEPENDENCY_NAME) if dependencies else None,
            version=dependencies.get(InfoKeys.DEPENDENCY_VERSION) if dependencies else None,
            licence=dependencies.get(InfoKeys.DEPENDENCY_LICENCE) if dependencies else None,
            build_date=dependencies.get(InfoKeys.DEPENDENCY_BUILD_DATE) if dependencies else None,
            repository=dependencies.get(InfoKeys.DEPENDENCY_REPOSITORY) if dependencies else None,
            organization=dependencies.get(InfoKeys.DEPENDENCY_ORGANIZATION) if dependencies else None,
            use_github=dependencies.get(InfoKeys.DEPENDENCY_USE_GITHUB_INFRASTRUCTURE) if dependencies else None,
            logo=dependencies.get(InfoKeys.DEPENDENCY_LOGO_PATH) if dependencies else None,
            log_file=dependencies.get(InfoKeys.DEPENDENCY_LOG_FILE) if dependencies else None,
            info_ok=dependencies.get(InfoKeys.DEPENDENCY_INFO_OK) if dependencies else None,
            context_bundle=dependencies.get(InfoKeys.OPTION_CONTEXT_BUNDLE) if dependencies else None
        )

        InfoValidator.validate(bundle)

        return bundle
