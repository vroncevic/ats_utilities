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
    Defines class SplashManager with attribute(s) and method(s).
    Provides an API for splash screen with hyperlinks.
'''

from __future__ import annotations

from time import sleep
from sys import stdout

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.splash.setup.bundle import SplashBundle
from ats_utilities.splash.setup.validator import SplashValidator
from ats_utilities.splash.property.isplash_property import ISplashProperty
from ats_utilities.splash.terminal.iterminal_properties import ITerminalProperties
from ats_utilities.splash.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splash.progressbar.iprogress_bar import IProgressBar
from ats_utilities.splash.data import CenterData
from ats_utilities.splash.data_validator import CenterDataValidator
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_value import not_satisfied

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class SplashManager:
    '''
        Defines class SplashManager with attribute(s) and method(s).
        Provides an API for splash screen with hyperlinks.

        It defines:

            :attributes:
                | _is_initialized - Indicates if splasher component is initialized.
                | _show_splash - Indicates if splasher should be shown.
                | _splash_property - Splash screen property component.
                | _terminal_property - Terminal properties component.
                | _ext - External infrastructure component.
                | _pb - Progress bar component.
                | _context - Context bundle with core components.
            :methods:
                | __init__ - Initializes splash manager.
                | get_bundle - Returns current splash manager configuration bundle.
                | update_bundle - Updates splash manager configuration bundle.
                | _apply_bundle - Applies bundle configuration to instance attributes.
                | get_context - Returns context bundle.
                | show - Shows the splash screen.
                | center - Centers console line and places text.
                | is_initialized - Checks if splash manager is initialized.
                | __str__ - Returns splash manager as string representation.
    '''

    _is_initialized: bool
    _show_splash: bool
    _splash_property: ISplashProperty
    _terminal_property: ITerminalProperties
    _ext: IExtInfrastructure
    _pb: IProgressBar
    _context: ContextBundle

    def __init__(self, own: SplashBundle) -> None:
        '''
            Initializes splash manager.

            :param own: Splash manager bundle.
            :exceptions:
                | ATSValueError: Splash bundle must be provided and have proper values.
                | ATSTypeError:  Splash bundle must be an instance of SplashBundle
                |                and its attributes must be instances of their
                |                respective interfaces and types.
        '''
        self._is_initialized = False
        self._show_splash = False
        self._apply_bundle(own)
        self._is_initialized = True

    def get_bundle(self) -> SplashBundle:
        '''
            Gets current splash manager configuration bundle.

            :return: Splash manager bundle.
            :exceptions: None.
        '''
        return SplashBundle(
            splash_property=self._splash_property,
            terminal_property=self._terminal_property,
            ext=self._ext,
            pb=self._pb,
            context_bundle=self._context
        )

    def update_bundle(self, bundle: SplashBundle) -> bool:
        '''
            Updates splash manager configuration bundle.

            :param bundle: Splash manager bundle.
            :return: True if configuration was successfully updated, False otherwise.
            :exceptions: None.
        '''
        try:
            self._is_initialized = False
            self._show_splash = False
            self._apply_bundle(bundle)
            self._is_initialized = True

            return True

        except (ATSValueError, ATSTypeError):
            return False

    def _apply_bundle(self, bundle: SplashBundle) -> None:
        '''
            Applies bundle to instance attributes.

            :param bundle: Splash manager bundle.
            :exceptions: None.
        '''
        SplashValidator.validate(bundle)
        self._splash_property = bundle.splash_property
        self._terminal_property = bundle.terminal_property
        self._ext = bundle.ext
        self._pb = bundle.pb
        self._context = bundle.context_bundle

        if self._splash_property.is_settings_enabled():
            self._show_splash = True

    def get_context(self) -> ContextBundle:
        '''
            Returns context bundle.

            :return: Context bundle.
            :exceptions: None.
        '''
        return self._context

    def show(self) -> None:
        '''
            Shows the splash screen.

            :exceptions:
                | ATSValueError: Logo file is invalid.
        '''
        if not self._show_splash:
            return

        size: tuple[object, ...] = self._terminal_property.size()
        stdout.write('\n\n')

        try:
            logo_path: str | None = self._splash_property.get_logo()

            if logo_path is not None:
                with open(logo_path, 'r', encoding='utf-8') as scr:
                    for line in scr:
                        processed_line: str = line.rstrip()

                        if bool(processed_line):
                            position: CenterData = CenterData(columns=int(size[1]), additional_shifter=0)
                            self.center(position, processed_line)

        except (OSError, UnicodeDecodeError) as exc:
            ctx: str = 'splasher::show(...)'
            msg: str = f'logo file content is invalid {exc}'
            not_satisfied(True, ctx, msg)

        position: CenterData = CenterData(columns=int(size[1]), additional_shifter=2)
        self.center(position, self._ext.get_info_text())
        self.center(position, self._ext.get_issue_text())
        self.center(position, self._ext.get_author_text())
        stdout.write('\n\n')

        for i in range(0, int(size[1]) - int(int(size[1]) / 2)):
            self._pb.set_and_plot(i + 1, int(size[1]))
            sleep(0.01)

        stdout.write('\n')

    def center(self, position: CenterData, text: str | None) -> None:
        '''
            Centers console line and places text.

            :param position: Position data for console output.
            :param text: Text to be centered | None.
            :exceptions: None.
        '''
        if not self._show_splash:
            return

        if not bool(text):
            return

        try:
            CenterDataValidator.validate(position)

        except (ATSValueError, ATSTypeError):
            return

        start_position: float = (position.columns / 2) - 30
        number_of_tabs = int((start_position / 8) - 1 + position.additional_shifter)
        stdout.write('{0}{1}\n'.format('\011' * number_of_tabs, text))

    def is_initialized(self) -> bool:
        '''
            Checks if splash manager is initialized.

            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        return self._is_initialized

    def __str__(self) -> str:
        '''
            Returns splash manager as string representation.

            :return: Splash manager as string representation.
            :exceptions: None.
        '''
        return to_str(self)
