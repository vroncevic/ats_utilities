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
    Defines class InfoManager with attribute(s) and method(s).
    Creates an API for the ATS information in one container object.
'''

from typing import Any
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.info.component_bundle import InfoComponentBundle
from ats_utilities.info.iname import IName
from ats_utilities.info.name import Name
from ats_utilities.info.iversion import IVersion
from ats_utilities.info.version import Version
from ats_utilities.info.ilicence import ILicence
from ats_utilities.info.licence import Licence
from ats_utilities.info.ibuild_date import IBuildDate
from ats_utilities.info.build_date import BuildDate
from ats_utilities.info.irepository import IRepository
from ats_utilities.info.repository import Repository
from ats_utilities.info.iorganization import IOrganization
from ats_utilities.info.organization import Organization
from ats_utilities.info.iuse_github import IUseGitHub
from ats_utilities.info.use_github import UseGitHub
from ats_utilities.info.ilogo_path import ILogoPath
from ats_utilities.info.logo import Logo
from ats_utilities.info.iinfo_ok import IInfoOk
from ats_utilities.info.info_ok import InfoOk
from ats_utilities.info.info_keys import InfoKeys
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import get_class_name, format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_runtime_error import ATSRuntimeError
from ats_utilities.exceptions.ats_attribute_error import ATSAttributeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class InfoManager(IInfoManager):
    '''
        Defines class InfoManager with attribute(s) and method(s).
        Creates an API for the ATS information in one container object.
        The ATS information container.

        It defines:

            :attributes:
                | _ATTR_MAP - Map attributes to dynamic component properties.
                | _components - The ATS info components (default InfoComponentBundle).
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _is_initialized - Indicates if the info manager component is initialized (default False).
            :methods:
                | __init__ - Initializes InfoManager constructor.
                | set_info - Sets the ATS information.
                | get_info - Gets the ATS information.
                | is_initialized - Checks if the info manager component is initialized.
                | refresh_status - Refresh status for ATS information structure.
                | __str__ - Returns the string representation of InfoManager.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    _ATTR_MAP = {
        'name': 'name',
        'version': 'version',
        'licence': 'licence',
        'build_date': 'build_date',
        'repository': 'repository',
        'organization': 'organization',
        'use_github': 'use_github',
        'logo_path': 'logo_path',
        'info_ok': 'info_ok'
    }

    def __init__(self, component_bundle: InfoComponentBundle | None = None) -> None:
        '''
            Initializes InfoManager constructor.

            :param component_bundle: Bundle with components | None.
            :type component_bundle: <InfoComponentBundle | None>
            :exceptions: None.
        '''
        # No dependency injection then use default ones.
        bundle: InfoComponentBundle = component_bundle or InfoComponentBundle()
        factory_context_bundle(self, bundle.context_bundle)
        self._is_initialized: bool = False

        try:
            factory_args = {'context_bundle': bundle.context_bundle}
            name: IName = make_component(bundle.name, Name, factory_args)
            validate_component(name, Name)
            version: IVersion = make_component(bundle.version, Version, factory_args)
            validate_component(version, Version)
            licence: ILicence = make_component(bundle.licence, Licence, factory_args)
            validate_component(licence, Licence)
            build_date: IBuildDate = make_component(bundle.build_date, BuildDate, factory_args)
            validate_component(build_date, BuildDate)
            repository: IRepository = make_component(bundle.repository, Repository, factory_args)
            validate_component(repository, Repository)
            organization: IOrganization = make_component(bundle.organization, Organization, factory_args)
            validate_component(organization, Organization)
            use_github: IUseGitHub = make_component(bundle.use_github, UseGitHub, factory_args)
            validate_component(use_github, UseGitHub)
            logo_path: ILogoPath = make_component(bundle.logo_path, Logo, factory_args)
            validate_component(logo_path, Logo)
            info_ok: IInfoOk = make_component(bundle.info_ok, InfoOk, factory_args)
            validate_component(info_ok, InfoOk)
            self._components = InfoComponentBundle(
                name=name, version=version, licence=licence, build_date=build_date,
                repository=repository, organization=organization, use_github=use_github,
                logo_path=logo_path, info_ok=info_ok
            )
            self.refresh_status()
            self._is_initialized = True

        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            self._reporter.error([f'{get_class_name(self)} {exc}'])

    def set_info(self, info: dict[str, Any]) -> None:
        '''
            Sets the ATS information.

            :param info: Dictionary with ATS information.
            :type info: <dict[str, Any]>
            :exceptions: ATSTypeError.
        '''
        self.name = info.get(InfoKeys.ATS_NAME)
        self.version = info.get(InfoKeys.ATS_VERSION)
        self.build_date = info.get(InfoKeys.ATS_BUILD_DATE)
        self.licence = info.get(InfoKeys.ATS_LICENCE)
        self.repository = info.get(InfoKeys.ATS_REPOSITORY)
        self.organization = info.get(InfoKeys.ATS_ORGANIZATION)
        use_github = info.get(InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE)
        if isinstance(use_github, str):
            use_github = True if use_github == 'True' else False
        self.use_github = use_github
        self.logo_path = info.get(InfoKeys.ATS_LOGO_PATH)

    def get_info(self) -> dict[str, Any]:
        '''
            Gets the ATS information.

            :return: Dictionary with ATS information.
            :rtype: <dict[str, Any]>
            :exceptions: None..
        '''
        return {
            InfoKeys.ATS_NAME: self.name,
            InfoKeys.ATS_VERSION: self.version,
            InfoKeys.ATS_BUILD_DATE: self.build_date,
            InfoKeys.ATS_LICENCE: self.licence,
            InfoKeys.ATS_REPOSITORY: self.repository,
            InfoKeys.ATS_ORGANIZATION: self.organization,
            InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE: self.use_github,
            InfoKeys.ATS_LOGO_PATH: self.logo_path
        }

    def __getattr__(self, name: str) -> str | bool | None:
        '''
            Gets attribute from instance components dynamically.

            :param name: Name of the attribute to look up.
            :type name: <str>
            :return: The value of the component attribute if found, otherwise None.
            :rtype: <str | bool | None>
            :exceptions: AttributeError if attribute is not in map.
        '''
        if name in self._ATTR_MAP:
            component = getattr(self._components, name, None)

            return getattr(component, self._ATTR_MAP[name], None) if component else None

        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __setattr__(self, name: str, value: str | bool | None) -> None:
        '''
            Sets attribute to instance components dynamically and refreshes status.

            :param name: Name of the attribute to set.
            :type name: <str>
            :param value: Value to assign to the component attribute.
            :type value: <str | bool | None>
            :exceptions: None..
        '''
        if '_components' in self.__dict__ and name in self._ATTR_MAP:
            component = getattr(self._components, name, None)

            if component:
                setattr(component, self._ATTR_MAP[name], value)
                self.refresh_status()

                return

        super().__setattr__(name, value)

    def is_initialized(self) -> bool:
        '''
            Checks if the info manager component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        component = getattr(self._components, 'info_ok', None) if self._is_initialized else None
        return self._is_initialized and (component.info_ok if component else False)

    def refresh_status(self) -> None:
        '''
            Refresh status for ATS information structure.

            :exceptions: None..
        '''
        info_ok = getattr(self._components, 'info_ok', False)
        attrs = ['name', 'version', 'licence', 'build_date']
        components = [getattr(self._components, attr, None) for attr in attrs]
        status = all(c and c.not_none() for c in components)
        setattr(info_ok, 'info_ok', status)

    def __str__(self) -> str:
        '''
            Returns the ATS info manager as string representation.

            :return: The ATS info manager as string representation.
            :rtype: <str>
            :exceptions: None..
        '''
        return format_instance_to_string(self)


