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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.info.imanager import IInfoManager
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.info.component_bundle import InfoComponentBundle
from ats_utilities.info.info_keys import InfoKeys
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions import ATSAttributeError, ATSRuntimeError, ATSTypeError, ATSValueError
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import cls_name, to_str
from ats_utilities.factory_value import require_not_satisfied, require_not_none

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
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
                | _components - The ATS info components (default InfoComponentBundle).
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _shared_context - Context bundle with shared context.
                | _is_initialized - Indicates if the info manager component is initialized (default False).
            :methods:
                | __init__ - Initializes InfoManager constructor.
                | get_shared_context - Returns the shared context.
                | set_info - Sets the ATS information.
                | get_info - Gets the ATS information.
                | is_initialized - Checks if the info manager component is initialized.
                | refresh_status - Refresh status for ATS information structure.
                | __str__ - Returns the InfoManager as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _is_initialized: bool
    _components: InfoComponentBundle
    _shared_context: ContextBundle

    def __init__(self, component_bundle: InfoComponentBundle | None = None) -> None:
        '''
            Initializes InfoManager constructor.

            :param component_bundle: Bundle with components | None.
            :type component_bundle: <InfoComponentBundle | None>
            :exceptions: None.
        '''
        self._is_initialized = False

        try:
            # No dependency injection then use default ones.
            self._components = component_bundle or InfoComponentBundle()
            factory_context_bundle(self, self._components.context_bundle)
            self._shared_context = self._components.context_bundle
            self.refresh_status()

            # All components initialized successfully.
            self._is_initialized = True

        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            print(f"\x1b[31m{cls_name(self)} {exc}\x1b[0m")

        except Exception as exc:
            print(f"\x1b[31m{cls_name(self)} unexpected exception: {exc}\x1b[0m")

    @override
    def get_shared_context(self) -> ContextBundle:
        '''
            Returns the shared context.

            :return: Shared context.
            :rtype: <ContextBundle>
            :exceptions: None.
        '''
        return self._shared_context

    @override
    def set_info(self, info: Mapping[str, Any]) -> None:
        '''
            Sets the ATS information (read only data).

            :param info: Mapping with ATS information.
            :type info: <Mapping[str, Any]>
            :exceptions: None.
        '''
        for key in InfoKeys.get_keys():
            if key not in info:
                require_not_none(None, f"info::set_info - missing key: {key}")

            require_not_none(info.get(key), f"info::set_info - null value for key: {key}")

        for key, attr in InfoKeys.get_key_to_attr().items():
            val = info.get(key)

            if key == InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE:
                if isinstance(val, str):
                    val = True if val == 'True' else False

            setattr(self, attr, val)

    @override
    def get_info(self) -> Mapping[str, Any]:
        '''
            Gets the ATS information (read only data).

            :return: Mapping with ATS information.
            :rtype: <Mapping[str, Any]>
            :exceptions: None.
        '''
        return {key: getattr(self, attr) for key, attr in InfoKeys.get_key_to_attr().items()}

    def __getattr__(self, name: str) -> str | bool | None:
        '''
            Gets attribute from instance components dynamically.

            :param name: Name of the attribute to look up.
            :type name: <str>
            :return: The value of the component attribute if found, otherwise None.
            :rtype: <str | bool | None>
            :exceptions:
                | ATSAttributeError: Name of the attribute is not a managed attribute.
        '''
        if name in InfoKeys.get_key_to_attr().values() or name == 'info_ok':
            component = getattr(self._components, name, None)

            return getattr(component, name, None) if component else None

        require_not_satisfied(
            True,
            f"'{type(self).__name__}' object has no attribute '{name}'",
            ATSAttributeError
        )

    def __setattr__(self, name: str, value: str | bool | None) -> None:
        '''
            Sets attribute to instance components dynamically and refreshes status.

            :param name: Name of the attribute to set.
            :type name: <str>
            :param value: Value to assign to the component attribute.
            :type value: <str | bool | None>
            :exceptions: None.
        '''
        if '_components' in self.__dict__ and (name in InfoKeys.get_key_to_attr().values() or name == 'info_ok'):
            component = getattr(self._components, name, None)

            if component:
                setattr(component, name, value)
                self.refresh_status()

                return

        super().__setattr__(name, value)

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the info manager component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        component = getattr(self._components, 'info_ok', None) if self._is_initialized else None

        return self._is_initialized and (component.info_ok if component else False)

    @override
    def refresh_status(self) -> None:
        '''
            Refresh status for ATS information structure.

            :exceptions: None.
        '''
        info_ok = getattr(self._components, 'info_ok', False)
        info_ok.info_ok = all(
            getattr(self._components, attr, None).not_none()
            for attr in InfoKeys.get_key_to_attr().values()
        )

    @override
    def __str__(self) -> str:
        '''
            Returns the InfoManager as string representation.

            :return: The InfoManager as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
