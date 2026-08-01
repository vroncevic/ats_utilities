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
    Defines the InfoManager class with attribute(s) and method(s).
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
from ats_utilities.exceptions import ATSAttributeError, ATSValueError, ATSTypeError
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
        Defines the InfoManager class with attribute(s) and method(s).
        Provides an API for the information in one container object.
        The information container for the App/Tool/Script.
        Note: The information is read-only data (it is provided by
        configuration file which is loaded by config loader).

        It defines:

            :attributes:
                | _components - The info components (default InfoBundle).
                | _context - The context bundle with context.
                | _is_initialized - The indicates if the info manager component is initialized (default: False).
            :methods:
                | __init__ - Initializes the InfoManager.
                | get_bundle - Gets current info bundle.
                | update_bundle - Updates info bundle.
                | _apply_bundle - Applies bundle configuration to instance attributes.
                | get_context - Returns the context.
                | set_info - Sets the information structure.
                | get_info - Gets the information structure.
                | is_registered_attribute - Checks if the attribute name is a registered dependency attribute name.
                | __getattr__ - Gets attribute by name.
                | __setattr__ - Sets attribute by name.
                | is_initialized - Checks if the info manager is initialized.
                | refresh_status - Refreshes the status for the information structure.
                | __str__ - Returns the info manager as a string representation.
    '''

    _is_initialized: bool
    _components: InfoBundle
    _context: ContextBundle

    def __init__(self, own: InfoBundle) -> None:
        '''
            Initializes the InfoManager.

            :param own: The bundle with components.
            :exceptions:
                | ATSValueError: Info bundle must be provided and have proper values.
                | ATSTypeError:  Info bundle must be an instance of InfoBundle and its
                |                attributes must be instances of their respective types.
        '''
        self._is_initialized = False
        InfoValidator.validate(own)
        self._apply_bundle(own)
        self._is_initialized = True

    def get_bundle(self) -> InfoBundle:
        '''
            Gets current info bundle.

            :return: The info bundle.
            :exceptions: None.
        '''
        return self._components

    def update_bundle(self, bundle: InfoBundle) -> bool:
        '''
            Updates info configuration bundle.

            :param bundle: The info bundle with info components.
            :return: True if the configuration was successfully updated, False otherwise.
            :exceptions: None.
        '''
        try:
            self._is_initialized = False
            InfoValidator.validate(bundle)
            self._apply_bundle(bundle)
            self._is_initialized = True

            return True

        except (ATSValueError, ATSTypeError):
            return False

    def _apply_bundle(self, bundle: InfoBundle) -> None:
        '''
            Applies bundle configuration to instance attributes.

            :param bundle: The info bundle with info components.
            :exceptions: None.
        '''
        self._components = bundle
        self._context = bundle.context_bundle
        self.refresh_status()

    def get_context(self) -> ContextBundle:
        '''
            Returns the context.

            :return: The context.
            :exceptions: None.
        '''
        return self._context

    def set_info(self, info: Mapping[str, object]) -> None:
        '''
            Sets the information structure by re-creating the info bundle.

            :param info: The mapping with configuration information.
            :exceptions:
                | ATSValueError: Info mapping must be provided and contain required keys.
                | ATSTypeError:  Info mapping must be an instance of Mapping.
        '''
        ctx: str = 'info_manager::set_info(...)'
        msg_info_none: str = 'info mapping must be provided'
        msg_info_istype: str = 'info must be a Mapping'

        not_none(info, ctx, msg_info_none)
        istype(info, Mapping, ctx, msg_info_istype)

        self._components = InfoFactory.create_bundle({
            InfoKeys.OPTION_INFO: info,
            InfoKeys.OPTION_CONTEXT_BUNDLE: self._context
        })
        self.refresh_status()

    def get_info(self) -> Mapping[str, object]:
        '''
            Gets the information structure.

            :return: The mapping representation of current info configuration.
            :exceptions: None.
        '''
        info_dict: dict[str, object] = {}
        config_key_to_dep = InfoKeys.get_config_keys_to_dependency_keys()

        for config_key, dep_attr in config_key_to_dep.items():
            component = getattr(self._components, dep_attr, None)

            if component is not None:
                val = getattr(component, dep_attr, None)

                if val is not None:
                    info_dict[config_key] = val

        return MappingProxyType(info_dict)

    def is_registered_attribute(self, name: str) -> bool:
        '''
            Checks if the attribute name is a registered dependency attribute name.

            :param name: The name of the attribute to check.
            :return: True if attribute name is a registered attribute, otherwise False.
            :exceptions: None.
        '''
        has_components: bool = '_components' in self.__dict__
        is_registered: bool = name in InfoKeys.get_all_names_config_keys()

        return has_components and is_registered

    def __getattr__(self, name: str) -> str | bool | None:
        '''
            Gets attribute from instance components dynamically.

            :param name: The name of the attribute to look up.
            :return: The value of the component attribute if found, otherwise None.
            :exceptions:
                | ATSAttributeError: Name of the attribute is not a registered attribute.
        '''
        if self.is_registered_attribute(name):
            component = getattr(self._components, name, None)

            return getattr(component, name, None) if component else None

        ctx: str = 'info_manager::getattr(...)'
        msg_attr_not_registered: str = f'{type(self).__name__} has no attribute {name}'

        not_satisfied(True, ctx, msg_attr_not_registered, ATSAttributeError)

    def __setattr__(self, name: str, value: str | bool | None) -> None:
        '''
            Sets attribute to instance components dynamically and refreshes status.

            :param name: The name of the attribute to set.
            :param value: The value to assign to the component attribute.
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
        msg_attr_not_registered: str = f'{type(self).__name__} has no registered attribute {name}'

        not_satisfied(True, ctx, msg_attr_not_registered, ATSAttributeError)

    def is_initialized(self) -> bool:
        '''
            Checks if the info manager is successfully initialized and has a valid status.

            :return: True if successfully initialized, otherwise False.
            :exceptions: None.
        '''
        if not self._is_initialized or self._components is None:
            return False

        info_ok_component = getattr(self._components, InfoKeys.DEPENDENCY_INFO_OK, None)

        return bool(info_ok_component and getattr(info_ok_component, InfoKeys.DEPENDENCY_INFO_OK, False))

    def refresh_status(self) -> None:
        '''
            Refreshes the status for the information structure based on the validity of required components.

            :exceptions: None.
        '''
        if not hasattr(self, '_components') or self._components is None:
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
            Returns the info manager as a string representation.

            :return: The Info manager as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
