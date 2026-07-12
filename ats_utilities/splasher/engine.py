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
from sys import stdout, stderr

from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.splasher.component_bundle import SplashComponentBundle
from ats_utilities.splasher.splash_center_bundle import SplashCenterBundle
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions import ATSAttributeError, ATSRuntimeError, ATSTypeError, ATSValueError
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import cls_name, to_str
from ats_utilities.factory_file_utils import check_file_exists

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Splasher(ISplasher):
    '''
        Defines class Splasher with method(s).
        Implements a splash screen with hyperlinks.

        It defines:

            :attributes:
                | _is_initialized - Indicates if the splasher component is initialized (default False).
                | _show_splash - Indicates if the splasher should be shown (default False).
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _shared_context - Context bundle with shared context.
            :methods:
                | __init__ - Initials Splasher constructor.
                | get_shared_context - Returns the shared context.
                | center - Centers console line.
                | is_initialized - Checks if splasher is initialized.
                | __str__ - Returns the string representation of Splasher.
    '''

    _is_initialized: bool = False
    _show_splash: bool = False
    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _shared_context: ContextBundle

    def __init__(self, component_bundle: SplashComponentBundle | None = None) -> None:
        '''
            Initials Splasher constructor.

            :param component_bundle: Splash screen component bundle | None.
            :type component_bundle: <SplashComponentBundle | None>
            :exceptions: None.
        '''
        try:
            bundle: SplashComponentBundle = component_bundle or SplashComponentBundle()
            factory_context_bundle(self, bundle.context_bundle)
            self._shared_context = bundle.context_bundle

            if bundle.property_validated:
                splash_keys = bundle.splash_property.splash_keys or {}

                if not splash_keys.get('enabled', True):
                    self._is_initialized = True

                    return

                else:
                    self._show_splash = True

                size: tuple[Any, ...] = bundle.terminal_property.size()
                splash_center_bundle: SplashCenterBundle = SplashCenterBundle()

                if bool(bundle.prop[SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE]):
                    check_file_exists(
                        bundle.prop[SplashKeys.ATS_LOGO_PATH],
                        r'application/tool/script logo file path is missing or empty'
                    )
                    stdout.write("\n\n")

                    with open(bundle.prop[SplashKeys.ATS_LOGO_PATH], 'r', encoding='utf-8') as scr:
                        for line in scr:
                            processed_line: str = line.rstrip()

                            if bool(processed_line):
                                splash_center_bundle.columns = int(size[1])
                                splash_center_bundle.additional_shifter = 0
                                splash_center_bundle.text = processed_line
                                self.center(splash_center_bundle)

                    splash_center_bundle.columns = int(size[1])
                    splash_center_bundle.additional_shifter = 2
                    splash_center_bundle.text = bundle.github.get_info_text()
                    self.center(splash_center_bundle)
                    splash_center_bundle.text = bundle.github.get_issue_text()
                    self.center(splash_center_bundle)
                    splash_center_bundle.text = bundle.github.get_author_text()
                    self.center(splash_center_bundle)
                    stdout.write("\n\n")
                else:
                    splash_center_bundle.columns = int(size[1])
                    splash_center_bundle.additional_shifter = 2
                    splash_center_bundle.text = bundle.ext.get_info_text()
                    self.center(splash_center_bundle)
                    splash_center_bundle.text = bundle.ext.get_issue_text()
                    self.center(splash_center_bundle)
                    splash_center_bundle.text = bundle.ext.get_author_text()
                    self.center(splash_center_bundle)
                    stdout.write("\n\n")

                for i in range(0, int(size[1]) - int(int(size[1]) / 2)):
                    bundle.pb.set_and_plot(i + 1, int(size[1]))
                    sleep(0.01)
                stdout.write("\n")

                # All components initialized successfully.
                self._is_initialized = True

        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            stderr.write(f"\x1b[31m{cls_name(self)} {exc}\x1b[0m\n")

        except Exception as exc:
            stderr.write(f"\x1b[31m{cls_name(self)} unexpected exception: {exc}\x1b[0m\n")

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
    def center(self, splash_center_bundle: SplashCenterBundle | None = None) -> None:
        '''
            Centers console line.

            :param splash_center_bundle: Splash center bundle for centering console output | None.
            :type splash_center_bundle: <SplashCenterBundle | None>
            :exceptions:
                | ATSTypeError: columns count 'columns' is not an integer.
                | ATSValueError: columns count 'columns' is less than 0.
                | ATSTypeError: additional shifter 'additional_shifter' is not an integer.
                | ATSValueError: additional shifter 'additional_shifter' is less than 0.
                | ATSTypeError: text 'text' is not a string or None.
                | ATSValueError: text 'text' is empty.
        '''
        if not self._show_splash:
            return

        bundle: SplashCenterBundle = splash_center_bundle or SplashCenterBundle()
        bundle.validate()
        start_position: float = (bundle.columns / 2) - 30
        number_of_tabs = int((start_position / 8) - 1 + bundle.additional_shifter)
        stdout.write('{0}{1}\n'.format('\011' * number_of_tabs, bundle.text))

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if splasher component is initialized.

            :return: <True> If splasher is initialized | <False> if it is not initialized.
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
