# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class Splash with attribute(s) and method(s).
    Loads a splash screen info and adds hyperlinks.
'''

import sys
from typing import Any, Dict, Tuple, List, Optional
from time import sleep

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.splash.progress_bar import ProgressBar
    from ats_utilities.splash.terminal_properties import TerminalProperties
    from ats_utilities.splash.splash_property import SplashProperty
    from ats_utilities.splash.github_infrastructure import GitHubInfrastructure
    from ats_utilities.splash.ext_infrastructure import ExtInfrastructure
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Splash(SplashProperty):
    '''
        Defines class Splash with attribute(s) and method(s).
        Loads a splash screen info and adds hyperlinks.
        API splash component.

        It defines:

            :attributes:
                | _verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials Splash constructor.
                | center - Center console line.
    '''

    def __init__(self, prop: Dict[Any, Any], verbose: bool = False) -> None:
        '''
            Initials Splash constructor.

            :param prop: Splash property in dict form
            :type prop: <: Dict[Any, Any]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__(prop, verbose)
        self._verbose: bool = verbose
        if self.validate(self._verbose):
            terminal: TerminalProperties = TerminalProperties(self._verbose)
            size: Tuple[Any, ...] = terminal.size(self._verbose)
            if bool(prop['ats_use_github_infrastructure']):
                print("\n")
                with open(prop['ats_logo_path'], 'r', encoding='utf-8') as scr:
                    for line in scr:
                        processed_line: str = line.rstrip()
                        if bool(processed_line):
                            self.center(int(size[1]), 0, processed_line)
                infrastruct = GitHubInfrastructure(prop, self._verbose)
                self.center(int(size[1]), 2, infrastruct.get_info_text())
                self.center(int(size[1]), 2, infrastruct.get_issue_text())
                self.center(int(size[1]), 2, infrastruct.get_author_text())
                print("\n")
            else:
                infrastruct = ExtInfrastructure(prop, self._verbose)
                self.center(int(size[1]), 2, infrastruct.get_info_text())
                self.center(int(size[1]), 2, infrastruct.get_issue_text())
                self.center(int(size[1]), 2, infrastruct.get_author_text())
                print("\n")
            pb: ProgressBar = ProgressBar(int(size[1]) - int(int(size[1]) / 2))
            for i in range(0, int(size[1]) - int(int(size[1]) / 2)):
                pb.set_and_plot(i + 1, int(size[1]))
                sleep(0.01)
            del pb

    def center(
        self,
        columns: int,
        additional_shifter: int,
        text: Optional[str],
        verbose: bool = False
    ) -> None:
        '''
            Center console line.

            :param columns: Colums for console session
            :type columns: <int>
            :param additional_shifter: Additional shifters
            :type additional_shifter: <int>
            :param text: Text for console session | None
            :type text: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('int:columns', columns),
            ('int:additional_shifter', additional_shifter),
            ('str:text', text)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(text):
            raise ATSValueError('missing text')
        verbose_message(
            self._verbose or verbose,
            [f'{columns} {additional_shifter} {text}']
        )
        start_position: float = (columns / 2) - 30
        number_of_tabs = int((start_position / 8) - 1 + additional_shifter)
        print('{0}{1}'.format('\011' * number_of_tabs, text))
