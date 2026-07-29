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
    Encapsulates core runtime components for simplification of base bundle creation.
'''

from __future__ import annotations

from ats_utilities.utils.setup.iregistry import IRegistry
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.dependencies import BaseDependencies
from ats_utilities.base.setup.validator import BaseValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class BaseRegistry(IRegistry[BaseBundle, BaseDependencies]):
    '''
        Encapsulates core runtime components for simplification of base bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates a base bundle instance.
    '''

    @classmethod
    def create_bundle(cls, dependencies: BaseDependencies) -> BaseBundle:
        '''
            Orchestrates dependency injection and creates a base bundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :return: Base bundle instance.
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Information file must be provided.
                | ATSValueError: Config loader must be provided.
                | ATSValueError: Info manager must be provided.
                | ATSValueError: Options parser must be provided.
                | ATSValueError: SplashManager must be provided.
                | ATSValueError: Use generator flag must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of BaseBundle.
                | ATSTypeError: Information file must be an instance of str.
                | ATSTypeError: Config loader must be an instance of ILoader.
                | ATSTypeError: Info manager must be an instance of IInfoManager.
                | ATSTypeError: Options parser must be an instance of IOptionManager.
                | ATSTypeError: SplashManager must be an instance of ISplashManager.
                | ATSTypeError: Use generator flag must be an instance of bool.
                | ATSTypeError: Generator must be an instance of IGenerator or None.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        bundle: BaseBundle = BaseBundle(
            info_file=dependencies.get('info_file') if dependencies else None,
            config_loader=dependencies.get('config_loader') if dependencies else None,
            info_manager=dependencies.get('info_manager') if dependencies else None,
            options_parser=dependencies.get('options_parser') if dependencies else None,
            splasher=dependencies.get('splasher') if dependencies else None,
            generator=dependencies.get('generator') if dependencies else None,
            use_generator=dependencies.get('use_generator') if dependencies else None,
            context_bundle=dependencies.get('context_bundle') if dependencies else None
        )

        BaseValidator.validate(bundle)

        return bundle
