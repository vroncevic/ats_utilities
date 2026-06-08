# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
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

from typing import Any, ClassVar, Dict, Tuple, List, Optional
from time import sleep
from ats_utilities.checker import IATSChecker, ATSChecker, ErrorChecker
from ats_utilities.console_io import IATSReporter, ATSReporter
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from .isplash import ISplash
from .github_infrastructure import GitHubInfrastructure
from .ext_infrastructure import ExtInfrastructure
from .iext_infrastructure import IExtInfrastructure
from .iprogress_bar import IProgressBar
from .progress_bar import ProgressBar
from .iterminal_properties import ITerminalProperties
from .terminal_properties import TerminalProperties
from .isplash_screen import ISplashProperty
from .splash_property import SplashProperty

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
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
                | ERRORS - Error checker.
                | __checker - Error checker.
                | __reporter - ATSReporter for outputting messages.
                | __verbose - Enable/Disable verbose option.
                | __splash_property - Splash property checker.
                | __terminal_property - Terminal properties.
                | __github - GitHub infrastructure for hyperlinks (used if 'ats_use_github_infrastructure' is True).
                | __ext - Generic external infrastructure for hyperlinks (used if 'ats_use_github_infrastructure' is False).
                | __pb - Progress bar.
            :methods:
                | __init__ - Initials Splash constructor.
                | center - Center console line.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

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

            :param prop: Splash property in dict form
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
            :type checker: :class:`~ats_utilities.checker.IATSChecker`
            :param reporter: ATSReporter for outputting messages | None
            :type reporter: :class:`~ats_utilities.console_io.iats_reporter.IATSReporter`
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        self.__splash_property: ISplashProperty = splash_property or SplashProperty(
            prop, self.__checker, self.__reporter, self.__verbose
        )

        if self.__splash_property.validate(self.__verbose):
            self.__terminal_property: ITerminalProperties = terminal_property or TerminalProperties(
                self.__checker, self.__reporter, self.__verbose
            )
            size: Tuple[Any, ...] = self.__terminal_property.size(self.__verbose)

            if bool(prop['ats_use_github_infrastructure']):
                print("\n")

                with open(prop['ats_logo_path'], 'r', encoding='utf-8') as scr:
                    for line in scr:
                        processed_line: str = line.rstrip()

                        if bool(processed_line):
                            self.center(int(size[1]), 0, processed_line)
                self.__github: IExtInfrastructure = github or GitHubInfrastructure(
                    prop, self.__checker, self.__reporter, self.__verbose
                )
                self.center(int(size[1]), 2, self.__github.get_info_text())
                self.center(int(size[1]), 2, self.__github.get_issue_text())
                self.center(int(size[1]), 2, self.__github.get_author_text())
                print("\n")
            else:
                self.__ext: IExtInfrastructure = ext or ExtInfrastructure(
                    prop, self.__checker, self.__reporter, self.__verbose
                )
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
        error_msg, error_id = self.__checker.validate_parameters([
            ('int:columns', columns),
            ('int:additional_shifter', additional_shifter),
            ('str:text', text)
        ])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        if not bool(text):
            raise ATSValueError('missing text')

        self.__reporter.verbose(self.__verbose or verbose, [f'{columns} {additional_shifter} {text}'])
        start_position: float = (columns / 2) - 30
        number_of_tabs = int((start_position / 8) - 1 + additional_shifter)
        print('{0}{1}'.format('\011' * number_of_tabs, text))
