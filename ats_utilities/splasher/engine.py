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
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.splasher.setup.bundle import SplashBundle
from ats_utilities.splasher.setup.validator import SplashValidator
from ats_utilities.splasher.data import CenterData
from ats_utilities.splasher.data_validator import CenterDataValidator
from ats_utilities.splasher.setup.splash_keys import SplashKeys
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_value import not_satisfied

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Splasher(ISplasher[ContextBundle, CenterData]):
    '''
        Defines class Splasher with attribute(s) and method(s).
        Implements a splash screen with hyperlinks.

        It defines:

            :attributes:
                | _is_initialized - Indicates if splasher component is initialized.
                | _show_splash - Indicates if splasher should be shown.
                | _context - Context bundle with core components.
            :methods:
                | __init__ - Initializes Splasher.
                | get_context - Returns context bundle.
                | center - Centers console line and places text.
                | is_initialized - Checks if splasher is initialized.
                | __str__ - Returns splasher as string representation.
    '''

    _is_initialized: bool
    _show_splash: bool
    _context: ContextBundle

    def __init__(self, own: SplashBundle) -> None:
        '''
            Initializes Splasher.

            :param own: Splash screen component bundle.
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Properties dictionary must be provided.
                | ATSValueError: Splash property must be provided.
                | ATSValueError: Property validated flag must be provided.
                | ATSValueError: Terminal properties must be provided.
                | ATSValueError: External infrastructure must be provided.
                | ATSValueError: Progress bar must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Bundle must be an instance of SplashBundle.
                | ATSTypeError: Properties dictionary must be an instance of Mapping.
                | ATSTypeError: Splash property must be an instance of ISplashProperty.
                | ATSTypeError: Property validated flag must be an instance of bool.
                | ATSTypeError: Terminal properties must be an instance of ITerminalProperties.
                | ATSTypeError: External infrastructure must be an instance of IExtInfrastructure.
                | ATSTypeError: Progress bar must be an instance of IProgressBar.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
                | ATSValueError: Checker must be provided.
                | ATSValueError: Logger must be provided.
                | ATSValueError: Reporter must be provided.
                | ATSValueError: Verbose must be provided.
                | ATSTypeError: Checker must be an instance of IChecker.
                | ATSTypeError: Logger must be an instance of ILogger.
                | ATSTypeError: Reporter must be an instance of IReporter.
                | ATSTypeError: Verbose must be a boolean.
                | ATSValueError: App/Tool/Script logo file path not correct.
                | ATSValueError: Logo file content is invalid.
        '''
        SplashValidator.validate(own)
        self._is_initialized = False
        self._show_splash = False
        self._context = own.context_bundle

        if own.property_validated:
            splash_keys = own.splash_property.splash_keys or {}

            if not splash_keys.get('enabled', True):
                self._is_initialized = True

                return

            else:
                self._show_splash = True

            size: tuple[Any, ...] = own.terminal_property.size()
            stdout.write('\n\n')

            try:
                with open(own.prop[SplashKeys.ATS_LOGO_PATH], 'r', encoding='utf-8') as scr:
                    for line in scr:
                        processed_line: str = line.rstrip()

                        if bool(processed_line):
                            position: CenterData = CenterData(columns=int(size[1]), additional_shifter=0)
                            self.center(position, processed_line)

            except (OSError, UnicodeDecodeError) as exc:
                ctx: str = r'splasher::init(...)'
                not_satisfied(True, ctx, f'logo file content is invalid {exc}')

            position: CenterData = CenterData(columns=int(size[1]), additional_shifter=2)
            self.center(position, own.ext.get_info_text())
            self.center(position, own.ext.get_issue_text())
            self.center(position, own.ext.get_author_text())
            stdout.write('\n\n')

            for i in range(0, int(size[1]) - int(int(size[1]) / 2)):
                own.pb.set_and_plot(i + 1, int(size[1]))
                sleep(0.01)

            stdout.write('\n')

        self._is_initialized = True

    @override
    def get_context(self) -> ContextBundle:
        '''
            Returns context bundle.

            :return: Context bundle.
            :rtype: ContextBundle
            :exceptions: None.
        '''
        return self._context

    @override
    def center(self, position: CenterData, text: str) -> None:
        '''
            Centers console line and places text.

            :param position: Position data for console output.
            :param text: Text to be centered.
            :exceptions:
                | ATSValueError: Columns count must be provided.
                | ATSTypeError: Columns count is not an integer.
                | ATSValueError: Columns count cannot be negative.
                | ATSValueError: Additional shifter must be provided.
                | ATSTypeError: Additional shifter is not an integer.
                | ATSValueError: Additional shifter cannot be negative.
        '''
        if not self._show_splash:
            return

        CenterDataValidator.validate(position)
        start_position: float = (position.columns / 2) - 30
        number_of_tabs = int((start_position / 8) - 1 + position.additional_shifter)
        stdout.write('{0}{1}\n'.format('\011' * number_of_tabs, text))

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if splasher component is initialized.

            :return: True if successfully, otherwise False.
            :exceptions: None.
        '''
        return self._is_initialized

    @override
    def __str__(self) -> str:
        '''
            Returns splasher as string representation.

            :return: Splasher as string representation.
            :exceptions: None.
        '''
        return to_str(self)
