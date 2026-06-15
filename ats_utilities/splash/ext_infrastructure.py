# -*- coding: UTF-8 -*-

'''
Module
    ext_infrastructure.py
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
    Defines class ExtInfrastructure with attribute(s) and method(s).
    Creates an API for processing hyperlinks for splash screen.
'''

from typing import Any, Dict, List, Optional
from ats_utilities.splash.iext_infrastructure import IExtInfrastructure
from ats_utilities.checker.ichecker import IATSChecker
from ats_utilities.checker.ats_checker import ATSChecker
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.console_io.ireporter import IATSReporter
from ats_utilities.console_io.reporter import ATSReporter
from ats_utilities.console_io.proxy_reporter import vreporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ExtInfrastructure(IExtInfrastructure):
    '''
        Defines class ExtInfrastructure with attribute(s) and method(s).
        Creates an API for processing hyperlinks for splash screen.
        API for GitHub information.

        It defines:

            :attributes:
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __infrastructure_property - Infrastructure property in dict format (default None).
            :methods:
                | __init__ - Initials ExtInfrastructure constructor.
                | infrastructure_property - Property method for get/set infrastructure property.
                | get_info_text - Pre-processes info text.
                | get_issue_text - Pre-processes issue text.
                | get_author_text - Pre-processes author text.
                | __str__ - Returns the string representation of external infrastructure.
    '''

    def __init__(
        self,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ExtInfrastructure constructor.

            :param checker: Parameters checker (default set ATSChecker) | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: Reporter for messaging (default set ATSReporter) | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        # No dependency injection then use default ones.
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter(checker=self.__checker)
        self.__verbose: bool = verbose
        self.__infrastructure_property: Optional[Dict[Any, Any]] = None

    @property
    @vreporter('get infrastructure property {infrastructure_property}')
    def infrastructure_property(self) -> Optional[Dict[Any, Any]]:
        '''
            Property method for getting infrastructure property.

            :return: Formatted infrastructure property in dict format | None
            :rtype: <Optional[str]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__infrastructure_property

    @infrastructure_property.setter
    @validator([('dict:infrastructure_property_setup', None)])
    @vreporter('set infrastructure property {infrastructure_property}')
    def infrastructure_property(self, infrastructure_property_setup: Optional[Dict[Any, Any]]) -> None:
        '''
            Property method for setting project infrastructure property.

            :param infrastructure_property_setup: Project infrastructure property in dict format | None
            :type infrastructure_property_setup: <Optional[Dict[Any, Any]]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__infrastructure_property = infrastructure_property_setup

    @vreporter('get info text {infrastructure_property}')
    def get_info_text(self) -> str:
        '''
            Pre-processes info text for splash.

            :return: Hyperlink with info text
            :rtype: <str>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        if not self.__infrastructure_property:
            self.__reporter.error(['missing infrastructure property'])
            return ''

        name: str = self.__infrastructure_property['ats_name']

        return f'\x1b]8;;{name}\a{name}\x1b]8;;\a'

    @vreporter('get issue text {infrastructure_property}')
    def get_issue_text(self) -> str:
        '''
            Pre-processes issue text for splash.

            :return: Hyperlink with issue info
            :rtype: <str>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        if not self.__infrastructure_property:
            self.__reporter.error(['missing infrastructure property'])
            return ''

        repo: str = self.__infrastructure_property['ats_repository']

        return f'\x1b]8;;{repo}\a{repo}\x1b]8;;\a'

    @vreporter('get author text {infrastructure_property}')
    def get_author_text(self) -> str:
        '''
            Pre-processes author text for splash.

            :return: Hyperlink with author info
            :rtype: <str>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        if not self.__infrastructure_property:
            self.__reporter.error(['missing infrastructure property'])
            return ''

        org: str = self.__infrastructure_property['ats_organization']

        return f'\x1b]8;;{org}\a{org}\x1b]8;;\a'

    def __str__(self) -> str:
        '''
            Returns the string representation of external infrastructure.

            :return: The external infrastructure as string
            :rtype: <str>
            :exceptions: None
        '''
        infrastructure_property = str(self.__infrastructure_property).replace('\n', '\n    ')
        checker = str(self.__checker).replace('\n', '\n    ')
        reporter = str(self.__reporter).replace('\n', '\n    ')
        verbose = str(self.__verbose).replace('\n', '\n    ')

        return (
            f'<{self.__class__.__name__}(\n'
            f'    infrastructure_property={infrastructure_property},\n'
            f'    checker={checker},\n'
            f'    reporter={reporter},\n'
            f'    verbose={verbose}\n)> at 0x{id(self):x}'
        )
