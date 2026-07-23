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
from ats_utilities.splasher.data import CenterData
from ats_utilities.splasher.data_validator import CenterDataValidator
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.utils.reflection import to_str
from ats_utilities.utils.files import check_file_exists
from ats_utilities.validation.check_value import not_satisfied, not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class Splasher(ISplasher):
    '''
        Defines class Splasher with attribute(s) and method(s).
        Implements a splash screen with hyperlinks.

        It defines:

            :attributes:
                | _is_initialized - Indicates if the splasher component is initialized (default False).
                | _show_splash - Indicates if the splasher should be shown (default False).
                | _context - Context bundle with context.
            :methods:
                | __init__ - Initials Splasher constructor.
                | get_context - Returns the context.
                | center - Centers console line.
                | is_initialized - Checks if splasher is initialized.
                | __str__ - Returns the string representation of Splasher.
    '''

    _is_initialized: bool
    _show_splash: bool
    _context: ContextBundle

    def __init__(self, own: SplashBundle) -> None:
        '''
            Initials Splasher constructor.

            :param own: Splash screen component bundle.
            :type own: SplashBundle
            :exceptions:
                | ATSValueError: Component bundle must be provided.
                | ATSTypeError: Component bundle must be a SplashBundle instance.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        self._is_initialized = False
        self._show_splash = False
        context: str = r'splasher::init(...)'
        not_none(own, context, r'own must be provided')
        istype(own, SplashBundle, context, r'own must be a SplashBundle instance')
        self._context = own.context_bundle

        if own.property_validated:
            splash_keys = own.splash_property.splash_keys or {}

            if not splash_keys.get('enabled', True):
                self._is_initialized = True

                return

            else:
                self._show_splash = True

            size: tuple[Any, ...] = own.terminal_property.size()

            check_file_exists(
                own.prop[SplashKeys.ATS_LOGO_PATH], context,
                r'App/Tool/Script logo file path not correct'
            )
            stdout.write('\n\n')

            try:
                with open(own.prop[SplashKeys.ATS_LOGO_PATH], 'r', encoding='utf-8') as scr:
                    for line in scr:
                        processed_line: str = line.rstrip()

                        if bool(processed_line):
                            center_data = CenterData(
                                columns=int(size[1]), additional_shifter=0
                            )

                            self.center(center_data, processed_line)

            except (OSError, UnicodeDecodeError) as exc:
                not_satisfied(True, context, f'logo file content is invalid {exc}')

            center_data = CenterData(
                columns=int(size[1]), additional_shifter=2
            )

            self.center(center_data, own.ext.get_info_text())
            self.center(center_data, own.ext.get_issue_text())
            self.center(center_data, own.ext.get_author_text())
            stdout.write('\n\n')

            for i in range(0, int(size[1]) - int(int(size[1]) / 2)):
                own.pb.set_and_plot(i + 1, int(size[1]))
                sleep(0.01)

            stdout.write('\n')

        self._is_initialized = True

    @override
    def get_context(self) -> ContextBundle:
        '''
            Returns the context.

            :return: Context.
            :rtype: ContextBundle
            :exceptions: None.
        '''
        return self._context

    @override
    def center(self, center_data: CenterData, text: str = '') -> None:
        '''
            Centers console line with given text.

            :param center_data: Center data for centering console output.
            :type center_data: <CenterData>
            :param text: Text to center.
            :type text: str
            :exceptions:
                | ATSValueError: Columns count must be provided.
                | ATSTypeError: Columns count is not an integer.
                | ATSValueError: Columns count cannot be negative.
                | ATSValueError: Additional shifter must be provided.
                | ATSTypeError: Additional shifter is not an integer.
                | ATSValueError: Additional shifter cannot be negative.
        '''
        CenterDataValidator.validate(center_data)
        if not self._show_splash:
            return

        start_position: float = (center_data.columns / 2) - 30
        number_of_tabs = int((start_position / 8) - 1 + center_data.additional_shifter)
        stdout.write('{0}{1}\n'.format('\011' * number_of_tabs, text))

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if splasher component is initialized.

            :return: True if successfully, otherwise False.
            :rtype: bool
            :exceptions: None.
        '''
        return self._is_initialized

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of Splasher.

            :return: The Splasher as string representation.
            :rtype: str
            :exceptions: None.
        '''
        return to_str(self)
