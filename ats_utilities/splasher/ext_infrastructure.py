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
from ats_utilities.splasher.iext_infrastructure import IExtInfrastructure
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import get_private_attr, format_instance_to_string
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter

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
                | __checker - Factoriezed parameters checker (default ATSChecker).
                | __reporter - Factoriezed reporter for messaging (default ATSReporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __infrastructure_property - Infrastructure property in dict format (default None).
            :methods:
                | __init__ - Initials ExtInfrastructure constructor.
                | infrastructure_property - Property method for get/set infrastructure property.
                | get_info_text - Pre-processes info text.
                | get_issue_text - Pre-processes issue text.
                | get_author_text - Pre-processes author text.
                | _reporter - Property method for getting the internal reporter instance.
                | __str__ - Returns the string representation of external infrastructure.
    '''

    def __init__(self, splash_bundle: Optional[ContextBundle] = None) -> None:
        '''
            Initials ExtInfrastructure constructor.

            :param splash_bundle: Bundle with checker, reporter and verbose | None
            :type splash_bundle: <Optional[ContextBundle]>
            :exceptions: None
        '''
        factory_context_bundle(self, splash_bundle)
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
            self._reporter.error(['missing infrastructure property'])
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
            self._reporter.error(['missing infrastructure property'])
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
            self._reporter.error(['missing infrastructure property'])
            return ''

        org: str = self.__infrastructure_property['ats_organization']

        return f'\x1b]8;;{org}\a{org}\x1b]8;;\a'

    @property
    def _reporter(self) -> IReporter:
        '''
            Property method for getting the internal reporter instance.

            :return: The reporter instance in IReporter format
            :rtype: <IReporter>
            :exceptions: None
        '''
        return get_private_attr(self, 'reporter')

    def __str__(self) -> str:
        '''
            Returns the string representation of external infrastructure.

            :return: The external infrastructure as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
