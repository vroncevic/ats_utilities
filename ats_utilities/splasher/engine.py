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
    Defines class Splasher with method(s).
    Implements a splash screen with hyperlinks.
'''

from __future__ import annotations

from typing import Any, override
from time import sleep
from sys import stdout

from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.splasher.splash_bundle import SplashBundle
from ats_utilities.splasher.splash_center_bundle import SplashCenterBundle
from ats_utilities.splasher.splash_center_registry import SplashCenterRegistry
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.context.context_support import ContextSupport
from ats_utilities.utils.reflection import to_str
from ats_utilities.utils.files import check_file_exists
from ats_utilities.validation.check_value import not_satisfied, not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Splasher(ContextSupport, ISplasher):
    '''
        Defines class Splasher with attribute(s) and method(s).
        Implements a splash screen with hyperlinks.

        It defines:

            :attributes:
                | _is_initialized - Indicates if the splasher component is initialized (default False).
                | _show_splash - Indicates if the splasher should be shown (default False).
                | _shared_context - Context bundle with shared context.
            :methods:
                | __init__ - Initials Splasher constructor.
                | get_shared_context - Returns the shared context.
                | center - Centers console line.
                | is_initialized - Checks if splasher is initialized.
                | __str__ - Returns the string representation of Splasher.
    '''

    _is_initialized: bool
    _show_splash: bool
    _shared_context: ContextBundle

    def __init__(self, component_bundle: SplashBundle) -> None:
        '''
            Initials Splasher constructor.

            :param component_bundle: Splash screen component bundle.
            :type component_bundle: <SplashBundle>
            :exceptions:
                | ATSValueError: Component bundle must be provided.
                | ATSTypeError: Component bundle must be a SplashBundle instance.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        self._is_initialized = False
        self._show_splash = False
        context: str = r'splasher::init(...)'
        not_none(component_bundle, context, r'component_bundle must be provided')
        istype(component_bundle, SplashBundle, context, r'component_bundle must be a SplashBundle instance')
        self._shared_context = component_bundle.context_bundle
        ContextSupport.__init__(self, self._shared_context)

        if component_bundle.property_validated:
            splash_keys = component_bundle.splash_property.splash_keys or {}

            if not splash_keys.get('enabled', True):
                self._is_initialized = True

                return

            else:
                self._show_splash = True

            size: tuple[Any, ...] = component_bundle.terminal_property.size()

            check_file_exists(
                component_bundle.prop[SplashKeys.ATS_LOGO_PATH], context,
                r'App/Tool/Script logo file path not correct'
            )
            stdout.write('\n\n')

            try:
                with open(component_bundle.prop[SplashKeys.ATS_LOGO_PATH], 'r', encoding='utf-8') as scr:
                    for line in scr:
                        processed_line: str = line.rstrip()

                        if bool(processed_line):
                            splash_center_bundle: SplashCenterBundle = SplashCenterRegistry.create_bundle(
                                columns=int(size[1]), additional_shifter=0
                            )

                            self.center(splash_center_bundle, processed_line)

            except (OSError, UnicodeDecodeError) as exc:
                not_satisfied(True, context, f'logo file content is invalid {exc}')

            splash_center_bundle: SplashCenterBundle = SplashCenterRegistry.create_bundle(
                columns=int(size[1]), additional_shifter=2
            )

            self.center(splash_center_bundle, component_bundle.ext.get_info_text())
            self.center(splash_center_bundle, component_bundle.ext.get_issue_text())
            self.center(splash_center_bundle, component_bundle.ext.get_author_text())
            stdout.write('\n\n')

            for i in range(0, int(size[1]) - int(int(size[1]) / 2)):
                component_bundle.pb.set_and_plot(i + 1, int(size[1]))
                sleep(0.01)

            stdout.write('\n')

        self._is_initialized = True

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
    def center(self, splash_center_bundle: SplashCenterBundle, text: str = '') -> None:
        '''
            Centers console line with given text.

            :param splash_center_bundle: Splash center bundle for centering console output.
            :type splash_center_bundle: <SplashCenterBundle>
            :param text: Text to center.
            :type text: <str>
            :exceptions: None.
        '''
        if not self._show_splash:
            return

        start_position: float = (splash_center_bundle.columns / 2) - 30
        number_of_tabs = int((start_position / 8) - 1 + splash_center_bundle.additional_shifter)
        stdout.write('{0}{1}\n'.format('\011' * number_of_tabs, text))

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if splasher component is initialized.

            :return: <True> if successful, <False> otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._is_initialized

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of Splasher.

            :return: The Splasher as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
