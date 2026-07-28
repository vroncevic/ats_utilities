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
    Provides an API for the information in one container object.
'''

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.setup.factory import InfoFactory
from ats_utilities.info.setup.validator import InfoValidator
from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.exceptions import ATSAttributeError
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_satisfied, not_none

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class InfoManager:
    '''
        Defines class InfoManager with attribute(s) and method(s).
        Provides an API for the information in one container object.
        The information container for App/Tool/Script.
        Note: The information is read-only data (it is provided by
        configuration file which is loaded by config loader).

        It defines:

            :attributes:
                | _components - The info components (default InfoBundle).
                | _context - Context bundle with context.
                | _is_initialized - Indicates if the info manager component is initialized (default False).
            :methods:
                | __init__ - Initializes InfoManager constructor.
                | get_context - Returns the context.
                | set_info - Sets the information structure.
                | get_info - Gets the information structure.
                | is_initialized - Checks if info manager is initialized.
                | refresh_status - Refreshes status for information structure.
                | __str__ - Returns info manager as string representation.
    '''

    _is_initialized: bool
    _components: InfoBundle
    _context: ContextBundle

    def __init__(self, own: InfoBundle) -> None:
        '''
            Initializes InfoManager constructor.

            :param own: Bundle with components.
            :exceptions:
                | ATSValueError: Info bundle must be provided and have proper values.
                | ATSTypeError:  Info bundle must be an instance of InfoBundle and its
                |                attributes must be instances of their respective types.
        '''
        InfoValidator.validate(own)
        self._components = own
        self._context = own.context_bundle
        self._is_initialized = False
        self.refresh_status()
        self._is_initialized = True

    def get_context(self) -> ContextBundle:
        '''
            Returns the context.

            :return: Context.
            :exceptions: None.
        '''
        return self._context

    def set_info(self, info: Mapping[str, object]) -> None:
        '''
            Sets the information structure by re-creating the info bundle.

            :param info: Mapping with configuration information.
            :exceptions:
                | ATSValueError: Info mapping must be provided and contain required keys.
                | ATSTypeError:  Info mapping must be an instance of Mapping.
        '''
        ctx: str = 'info_manager::set_info(...)'
        not_none(info, ctx, 'info mapping must be provided')
        istype(info, Mapping, ctx, 'info must be a Mapping')

        self._components = InfoFactory.create_bundle({
            InfoKeys.OPTION_INFO: info,
            InfoKeys.OPTION_CONTEXT_BUNDLE: self._context
        })
        self.refresh_status()

    def get_info(self) -> Mapping[str, object]:
        '''
            Gets the information structure.

            :return: Mapping representation of current info configuration.
            :exceptions: None.
        '''
        info_dict: dict[str, object] = {}
        config_key_to_dep = InfoKeys.get_config_keys()

        for config_key, dep_attr in config_key_to_dep.items():
            component = getattr(self._components, dep_attr, None)

            if component is not None:
                val = getattr(component, dep_attr, None)

                if val is not None:
                    info_dict[config_key] = val

        return MappingProxyType(info_dict)

    def is_registered_attribute(self, name: str) -> bool:
        '''
            Checks if attribute name is a registered dependency attribute name.

            :param name: Name of the attribute to check.
            :return: True if attribute name is a registered attribute, otherwise False.
            :exceptions: None.
        '''
        has_components: bool = '_components' in self.__dict__
        is_registered: bool = name in InfoKeys.get_all_names_config_keys()

        return has_components and is_registered

    def __getattr__(self, name: str) -> str | bool | None:
        '''
            Gets attribute from instance components dynamically.

            :param name: Name of the attribute to look up.
            :return: The value of the component attribute if found, otherwise None.
            :exceptions:
                | ATSAttributeError: Name of the attribute is not a registered attribute.
        '''
        if self.is_registered_attribute(name):
            component = getattr(self._components, name, None)

            return getattr(component, name, None) if component else None

        ctx: str = 'info_manager::getattr(...)'
        not_satisfied(True, ctx, f'{type(self).__name__} has no attribute {name}', ATSAttributeError)

    def __setattr__(self, name: str, value: str | bool | None) -> None:
        '''
            Sets attribute to instance components dynamically and refreshes status.

            :param name: Name of the attribute to set.
            :param value: Value to assign to the component attribute.
            :exceptions:
                | ATSAttributeError: Name of the attribute is not a registered attribute.
        '''
        if name.startswith('_'):
            super().__setattr__(name, value)

            return

        if self.is_registered_attribute(name):
            component = getattr(self._components, name, None)

            if component is not None:
                setattr(component, name, value)
                self.refresh_status()

                return

        ctx: str = 'info_manager::setattr(...)'
        not_satisfied(True, ctx, f'{type(self).__name__} has no registered attribute {name}', ATSAttributeError)

    def is_initialized(self) -> bool:
        '''
            Checks if info manager is successfully initialized and has valid status.

            :return: True if successfully initialized, otherwise False.
            :exceptions: None.
        '''
        if not self._is_initialized or self._components is None:
            return False

        info_ok_component = getattr(self._components, InfoKeys.DEPENDENCY_INFO_OK, None)
        return bool(info_ok_component and getattr(info_ok_component, InfoKeys.DEPENDENCY_INFO_OK, False))

    def refresh_status(self) -> None:
        '''
            Refreshes status for information structure based on required components validity.

            :exceptions: None.
        '''
        if not hasattr(self, r'_components') or self._components is None:
            return

        required_dep_names = InfoKeys.get_names_of_required_config_keys()
        is_all_ok: bool = True

        for dep_name in required_dep_names:
            if dep_name == InfoKeys.DEPENDENCY_INFO_OK:
                continue

            component = getattr(self._components, dep_name, None)

            if component is None:
                is_all_ok = False
                break

            val = getattr(component, dep_name, None)

            if val is None or val == '':
                is_all_ok = False
                break

        info_ok_component = getattr(self._components, InfoKeys.DEPENDENCY_INFO_OK, None)

        if info_ok_component is not None:
            setattr(info_ok_component, InfoKeys.DEPENDENCY_INFO_OK, is_all_ok)

    def __str__(self) -> str:
        '''
            Returns info manager as string representation.

            :return: Info manager as string representation.
            :exceptions: None.
        '''
        return to_str(self)
