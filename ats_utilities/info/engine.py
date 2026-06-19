# -*- coding: utf-8 -*-

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
    Defines class ATSInfoManager with attribute(s) and method(s).
    Creates an API for the ATS information in one container object.
'''

from typing import Dict, List, Optional
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.info.component_bundle import ATSInfoComponentBundle
from ats_utilities.info.iname import IName
from ats_utilities.info.name import ATSName
from ats_utilities.info.iversion import IVersion
from ats_utilities.info.version import ATSVersion
from ats_utilities.info.ilicence import ILicence
from ats_utilities.info.licence import ATSLicence
from ats_utilities.info.ibuild_date import IBuildDate
from ats_utilities.info.build_date import ATSBuildDate
from ats_utilities.info.iinfo_ok import IInfoOk
from ats_utilities.info.info_ok import ATSInfoOk
from ats_utilities.info.info_keys import ATSInfoKeys
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.context_bundle import ContextBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSInfoManager(IInfoManager):
    '''
        Defines class ATSInfoManager with attribute(s) and method(s).
        Creates an API for the ATS information in one container object.
        The ATS information container.

        It defines:

            :attributes:
                | _ATTR_MAP - .
                | _components - The ATS licence (default ATSLicence).
            :methods:
                | __init__ - Initials ATSInfoManager constructor.
                | set_info - Sets the ATS information.
                | info_ok - Checks is ATS information structure ok.
                | __getattr__ - Gets attribute from instance components dinamicly.
                | __setattr__ - Sets attribute to instance components dinamicly and refreshes status.
                | refresh_status - Refresh status for ATS information structure.
                | __str__ - Returns the string representation of ATS info manager.
    '''

    _ATTR_MAP = {
        'name': 'name',
        'version': 'version',
        'licence': 'licence',
        'build_date': 'build_date'
    }

    def __init__(
        self,
        context_bundle: Optional[ContextBundle] = None,
        component_bundle: Optional[ATSInfoComponentBundle] = None
    ) -> None:
        '''
            Initials ATSInfoManager constructor.

            :param context_bundle: Bundle with checker, reporter and verbose | None
            :type context_bundle: <Optional[ContextBundle]>
            :param component_bundle: Bundle with components | None
            :type component_bundle: <Optional[ATSInfoComponentBundle]>
            :exceptions: ATSTypeError
        '''
        bundle: ContextBundle = context_bundle or ContextBundle()
        factory_args = {'info_bundle': bundle}
        components: ATSInfoComponentBundle = component_bundle or ATSInfoComponentBundle()
        name: IName = make_component(components.name, ATSName, factory_args)
        validate_component(name, type(name), type(name).__name__)
        version: IVersion = make_component(components.version, ATSVersion, factory_args)
        validate_component(version, type(version), type(version).__name__)
        licence: ILicence = make_component(components.licence, ATSLicence, factory_args)
        validate_component(licence, type(licence), type(licence).__name__)
        build_date: IBuildDate = make_component(components.build_date, ATSBuildDate, factory_args)
        validate_component(build_date, type(build_date), type(build_date).__name__)
        info_ok: IInfoOk = make_component(components.info_ok, ATSInfoOk, factory_args)
        validate_component(info_ok, type(info_ok), type(info_ok).__name__)
        self._components = ATSInfoComponentBundle(
            name=name, version=version, licence=licence, build_date=build_date, info_ok=info_ok
        )
        self.refresh_status()

    def set_info(self, info: Dict[str, str]) -> None:
        '''
            Sets the ATS information.

            :param info: Dictionary with ATS information
            :type info: <Dict[str, str]>
            :exceptions: ATSTypeError
        '''
        self.name = info.get(ATSInfoKeys.ATS_NAME)
        self.version = info.get(ATSInfoKeys.ATS_VERSION)
        self.build_date = info.get(ATSInfoKeys.ATS_BUILD_DATE)
        self.licence = info.get(ATSInfoKeys.ATS_LICENCE)

    def __getattr__(self, name: str) -> Optional[str]:
        '''
            Gets attribute from instance components dinamicly.

            :param name: Name of the attribute to look up
            :type name: <str>
            :return: The value of the component attribute if found, otherwise None
            :rtype: <Optional[str]>
            :exceptions: AttributeError if attribute is not in map
        '''
        if name in self._ATTR_MAP:
            component = getattr(self._components, name, None)

            return getattr(component, self._ATTR_MAP[name], None) if component else None

        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __setattr__(self, name: str, value: Optional[str]) -> None:
        '''
            Sets attribute to instance components dinamicly and refreshes status.

            :param name: Name of the attribute to set
            :type name: <str>
            :param value: Value to assign to the component attribute
            :type value: <Optional[str]>
            :return: None
            :rtype: <None>
            :exceptions: None
        '''
        if '_components' in self.__dict__ and name in self._ATTR_MAP:
            component = getattr(self._components, name, None)

            if component:
                setattr(component, self._ATTR_MAP[name], value)
                self.refresh_status()

                return

        super().__setattr__(name, value)

    @property
    def info_ok(self) -> bool:
        '''
            Checks is ATS information structure ok.
        
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None
        '''
        return getattr(self._components, 'info_ok', False)

    def refresh_status(self) -> None:
        '''
            Refresh status for ATS information structure.

            :exceptions: None
        '''
        info_ok = getattr(self._components, 'info_ok', False)
        attrs = ['name', 'version', 'licence', 'build_date']
        components = [getattr(self._components, attr, None) for attr in attrs]
        status = all(c and c.not_none() for c in components)
        setattr(info_ok, 'info_ok', status)

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS info manager.

            :return: The ATS info manager string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
