# -*- coding: UTF-8 -*-

'''
Module
    ats_splash.py
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
    Defines class Splash with attribute(s) and method(s).
    Loads a splash screen info and adds hyperlinks.
'''

from typing import Any, Dict, Tuple, List, Optional
from time import sleep
from ats_utilities.splash.isplash import ISplash
from ats_utilities.checker.ichecker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.splash.github_infrastructure import GitHubInfrastructure
from ats_utilities.splash.ext_infrastructure import ExtInfrastructure
from ats_utilities.splash.iext_infrastructure import IExtInfrastructure
from ats_utilities.splash.iprogress_bar import IProgressBar
from ats_utilities.splash.progress_bar import ProgressBar
from ats_utilities.splash.iterminal_properties import ITerminalProperties
from ats_utilities.splash.terminal_properties import TerminalProperties
from ats_utilities.splash.isplash_property import ISplashProperty
from ats_utilities.splash.splash_property import SplashProperty

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Splash(ISplash):
    '''
        Defines class Splash with attribute(s) and method(s).
        Loads a splash screen info and adds hyperlinks.
        API splash component.

        It defines:

            :attributes:
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __splash_property - Splash property (default set SplashProperty).
                | __terminal_property - Terminal properties (default set TerminalProperties).
                | __github - GitHub infrastructure for hyperlinks (used if 'ats_use_github_infrastructure' is True).
                | __ext - Generic external infrastructure for hyperlinks (used if 'ats_use_github_infrastructure' is False).
                | __pb - Progress bar (default set ProgressBar).
            :methods:
                | __init__ - Initials Splash constructor.
                | center - Center console line.
    '''

    def __init__(
        self,
        prop: Dict[Any, Any],
        splash_property: Optional[ISplashProperty] = None,
        terminal_property: Optional[ITerminalProperties] = None,
        github: Optional[IExtInfrastructure] = None,
        ext: Optional[IExtInfrastructure] = None,
        pb: Optional[IProgressBar] = None,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials Splash constructor.

            :param prop: Splash property in dict format
            :type prop: <Dict[Any, Any]>
            :param splash_property: Splash property checker | None
            :type splash_property: <Optional[ISplashProperty]>
            :param terminal_property: Terminal properties | None
            :type terminal_property: <Optional[ITerminalProperties]>
            :param github: GitHub infrastructure for hyperlinks | None
            :type github: <Optional[IExtInfrastructure]>
            :param ext: Generic external infrastructure for hyperlinks | None
            :type ext: <Optional[IExtInfrastructure]>
            :param pb: Progress bar | None
            :type pb: <Optional[IProgressBar]>
            :param checker: Error checker | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for outputting messages | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter(self.__checker)
        self.__verbose: bool = verbose
        self.__splash_property: ISplashProperty = splash_property or SplashProperty(
            self.__checker, self.__reporter, self.__verbose
        )
        self.__splash_property.splash_property = prop

        if self.__splash_property.validates():
            self.__terminal_property: ITerminalProperties = terminal_property or TerminalProperties(
                self.__checker, self.__reporter, self.__verbose
            )
            size: Tuple[Any, ...] = self.__terminal_property.size()

            if bool(prop['ats_use_github_infrastructure']):
                print("\n")

                with open(prop['ats_logo_path'], 'r', encoding='utf-8') as scr:
                    for line in scr:
                        processed_line: str = line.rstrip()

                        if bool(processed_line):
                            self.center(int(size[1]), 0, processed_line)

                self.__github: IExtInfrastructure = github or GitHubInfrastructure(
                    self.__checker, self.__reporter, self.__verbose
                )
                self.__github.infrastructure_property = prop
                self.center(int(size[1]), 2, self.__github.get_info_text())
                self.center(int(size[1]), 2, self.__github.get_issue_text())
                self.center(int(size[1]), 2, self.__github.get_author_text())
                print("\n")
            else:
                self.__ext: IExtInfrastructure = ext or ExtInfrastructure(
                    self.__checker, self.__reporter, self.__verbose
                )
                self.__ext.infrastructure_property = prop
                self.center(int(size[1]), 2, self.__ext.get_info_text())
                self.center(int(size[1]), 2, self.__ext.get_issue_text())
                self.center(int(size[1]), 2, self.__ext.get_author_text())
                print("\n")
            self.__pb: IProgressBar = pb or ProgressBar(int(size[1]) - int(int(size[1]) / 2))

            for i in range(0, int(size[1]) - int(int(size[1]) / 2)):
                self.__pb.set_and_plot(i + 1, int(size[1]))
                sleep(0.01)
            del self.__pb

    def center(
        self,
        columns: int,
        additional_shifter: int,
        text: Optional[str]
    ) -> None:
        '''
            Center console line.

            :param columns: Colums for console session
            :type columns: <int>
            :param additional_shifter: Additional shifters
            :type additional_shifter: <int>
            :param text: Text for console session | None
            :type text: <Optional[str]>
            :exceptions: ATSTypeError | ATSValueError
        '''
        start_position: float = (columns / 2) - 30
        number_of_tabs = int((start_position / 8) - 1 + additional_shifter)
        print('{0}{1}'.format('\011' * number_of_tabs, text))
