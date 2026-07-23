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

from typing import override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.setup.dependencies import InfoDependencies
from ats_utilities.info.setup.validator import InfoValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class InfoRegistry(IRegistry[InfoBundle, InfoDependencies]):
    '''
        Encapsulates core runtime components for simplification of info bundle creation.

        It defines:

            :methods:
                | create_bundle - Orchestrates dependency injection and creates an info bundle instance.
    '''

    @classmethod
    @override
    def create_bundle(cls, dependencies: InfoDependencies) -> InfoBundle:
        '''
            Orchestrates dependency injection and creates an info bundle instance.

            :param dependencies: Registry-specific orchestration dependencies.
            :type dependencies: InfoDependencies
            :return: Info bundle instance.
            :rtype: InfoBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Name must be provided.
                | ATSValueError: Version must be provided.
                | ATSValueError: Licence must be provided.
                | ATSValueError: Build date must be provided.
                | ATSValueError: Repository must be provided.
                | ATSValueError: Organization must be provided.
                | ATSValueError: Use GitHub must be provided.
                | ATSValueError: Logo must be provided.
                | ATSValueError: Log file must be provided.
                | ATSValueError: Info ok must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of InfoBundle.
                | ATSTypeError: Name must be an instance of IName interface.
                | ATSTypeError: Version must be an instance of IVersion interface.
                | ATSTypeError: Licence must be an instance of ILicence interface.
                | ATSTypeError: Build date must be an instance of IBuildDate interface.
                | ATSTypeError: Repository must be an instance of IRepository interface.
                | ATSTypeError: Organization must be an instance of IOrganization interface.
                | ATSTypeError: Use GitHub must be an instance of IUseGitHub interface.
                | ATSTypeError: Logo must be an instance of ILogo interface.
                | ATSTypeError: Log file must be an instance of ILogFile interface.
                | ATSTypeError: Info ok must be an instance of IInfoOk interface.
                | ATSTypeError: Context bundle must be an instance of ContextBundle class.
        '''
        bundle = InfoBundle(
            name=dependencies.get('name'),
            version=dependencies.get('version'),
            licence=dependencies.get('licence'),
            build_date=dependencies.get('build_date'),
            repository=dependencies.get('repository'),
            organization=dependencies.get('organization'),
            use_github=dependencies.get('use_github'),
            logo=dependencies.get('logo'),
            log_file=dependencies.get('log_file'),
            info_ok=dependencies.get('info_ok'),
            context_bundle=dependencies.get('context_bundle')
        )

        InfoValidator.validate(bundle)

        return bundle
