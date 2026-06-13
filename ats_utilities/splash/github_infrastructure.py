# -*- coding: UTF-8 -*-

'''
Module
    github_infrastructure.py
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
    Defines class GitHubInfrastructure with attribute(s) and method(s).
    Creates an API for processing hyperlinks for splash screen.
'''

from typing import Any, ClassVar, Dict, List, Optional
from ats_utilities.checker.iats_checker import IATSChecker, ErrorChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.splash.iext_infrastructure import IExtInfrastructure

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class GitHubInfrastructure(IExtInfrastructure):
    '''
        Defines class GitHubInfrastructure with attribute(s) and method(s).
        Creates an API for processing hyperlinks for splash screen.
        API for GitHub information.

        It defines:

            :attributes:
                | ERRORS - Error checker.
                | __checker - Error checker.
                | __reporter - ATSReporter for outputting messages.
                | __verbose - Enable/Disable verbose option.
                | __property - Splash property in dict format.
            :methods:
                | __init__ - Initials GitHubInfrastructure constructor.
                | get_info_text - Pre-processes info text.
                | get_issue_text - Pre-processes issue text.
                | get_author_text - Pre-processes author text.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker

    def __init__(
        self,
        prop: Dict[Any, Any],
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials GitHubInfrastructure constructor.

            :param prop: Splash property in dict form
            :type prop: <Dict[Any, Any]>
            :param checker: Error checker | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for outputting messages | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose

        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([('dict:prop', prop)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        if not bool(prop):
            raise ATSValueError(error_msg)

        self.__property: Dict[Any, Any] = prop
        self.__reporter.verbose(self.__verbose, [f'splash property {prop}'])

    def get_info_text(self) -> str:
        '''
            Pre-processes info text for splash.

            :return: Hyperlink with info text
            :rtype: <str>
            :exceptions: None
        '''
        org: str = self.__property['ats_organization']
        repo: str = self.__property['ats_repository']
        url_short: str = f'github.io/{repo}'
        url_long: str = f'https://{org}.github.io/{repo}'
        return f'\x1b]8;;{url_long}\a{url_short}\x1b]8;;\a'

    def get_issue_text(self) -> str:
        '''
            Pre-processes issue text for splash.

            :return: Hyperlink with issue info
            :rtype: <str>
            :exceptions: None
        '''
        org: str = self.__property['ats_organization']
        repo: str = self.__property['ats_repository']
        url: str = f'https://github.com/{org}/{repo}/issues/new/choose'
        return f'\x1b]8;;{url}\agithub.io/issue\x1b]8;;\a'

    def get_author_text(self) -> str:
        '''
            Pre-processes author text for splash.

            :return: Hyperlink with author info
            :rtype: <str>
            :exceptions: None
        '''
        org: str = self.__property['ats_organization']
        org_short: str = f"{org}.github.io"
        org_long: str = f"https://{org}.github.io/bio/"
        return f'\x1b]8;;{org_long}\a{org_short}\x1b]8;;\a'
