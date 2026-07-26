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
from typing import Any, override

from ats_utilities.info.iinfo_manager import IInfoManager
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.setup.validator import InfoValidator
from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.exceptions import ATSAttributeError
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_value import not_satisfied, not_none

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class InfoManager(IInfoManager[Mapping[str, Any], ContextBundle]):
    '''
        Defines class InfoManager with attribute(s) and method(s).
        Provides an API for the information in one container object.
        The information container for App/Tool/Script.
        Note: The information is read-only data (it is provided by
        configuraiton file which is loaded by config loader).

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
        self.refresh_status()
        self._is_initialized = True

    @override
    def get_context(self) -> ContextBundle:
        '''
            Returns the context.

            :return: Context.
            :exceptions: None.
        '''
        return self._context

    def is_attribute(self, name: str | bool | None) -> bool:
        '''
            Checks if attribute name is a manageable attribute.

            :param name: Name of the attribute to check.
            :return: True if attribute name is a manageable attribute, otherwise False.
            :exceptions: None.
        '''
        has_components: bool = '_components' in self.__dict__
        is_registered_attribute: bool = (
            name in InfoKeys.get_dependency_to_type().keys() or name == InfoKeys.ATS_INFO_OK
        )

        return has_components and is_registered_attribute

    @override
    def set_info(self, info: Mapping[str, Any]) -> None:
        '''
            Sets the information structure.

            :param info: Mapping with information.
            :exceptions: None.
        '''
        for key in InfoKeys.get_config_keys():
            if key == InfoKeys.ATS_LOG_FILE:
                continue

            ctx: str = r'info_manager::set_info(...)'

            if key not in info:
                not_none(None, ctx, f'missing key: {key}')

            not_none(info.get(key), ctx, f'null value for key: {key}')

        for key, attr in InfoKeys.get_dependency_to_type().items():
            val = info.get(key)

            if key == InfoKeys.ATS_LOG_FILE and val is None:
                continue

            if key == InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE:
                if isinstance(val, str):
                    val = True if val == 'True' else False

            setattr(self, attr, val)

    @override
    def get_info(self) -> Mapping[str, Any]:
        '''
            Gets the information structure.

            :return: Mapping with information.
            :exceptions: None.
        '''
        return {
            key: getattr(self, attr)
            for key, attr in InfoKeys.get_dependency_to_type().items()
            if key != InfoKeys.ATS_LOG_FILE or getattr(self, attr) is not None
        }

    def __getattr__(self, name: str) -> str | bool | None:
        '''
            Gets attribute from instance components dynamically.

            :param name: Name of the attribute to look up.
            :return: The value of the component attribute if found, otherwise None.
            :exceptions:
                | ATSAttributeError: Name of the attribute is not a managed attribute.
        '''
        if self.is_attribute(name):
            component = getattr(self._components, name, None)

            return getattr(component, name, None) if component else None

        ctx: str = r'info_manager::getattr(...)'
        not_satisfied(True, ctx, f'{type(self).__name__} object has no attribute {name}', ATSAttributeError)

    def __setattr__(self, name: str, value: str | bool | None) -> None:
        '''
            Sets attribute to instance components dynamically and refreshes status.

            :param name: Name of the attribute to set.
            :param value: Value to assign to the component attribute.
            :exceptions: None.
        '''
        if self.is_attribute(name):
            component = getattr(self._components, name, None)

            if component:
                setattr(component, name, value)
                self.refresh_status()

                return

        super().__setattr__(name, value)

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if info manager is initialized.

            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        component = getattr(self._components, InfoKeys.ATS_INFO_OK, None) if self._is_initialized else None

        return self._is_initialized and (component.info_ok if component else False)

    @override
    def refresh_status(self) -> None:
        '''
            Refresh status for information structure.

            :exceptions: None.
        '''
        info_ok = getattr(self._components, InfoKeys.ATS_INFO_OK, False)
        info_ok.info_ok = all(
            getattr(self._components, attr, None).not_none()
            for attr in InfoKeys.get_dependency_to_type().values()
            if attr != InfoKeys.ATS_LOG_FILE
        )

    @override
    def __str__(self) -> str:
        '''
            Returns info manager as string representation.

            :return: Info manager as string representation.
            :exceptions: None.
        '''
        return to_str(self)
