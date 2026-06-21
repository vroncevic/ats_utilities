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

from typing import Any
from ats_utilities.splasher.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import require_attributes, format_instance_to_string
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter
from ats_utilities.factory_utils import require_keys, cherry_pick_dict

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ExtInfrastructure(IExtInfrastructure):
    '''
        Defines class ExtInfrastructure with attribute(s) and method(s).
        Creates an API for processing hyperlinks for splash screen.

        It defines:

            :attributes:
                | _required_keys - Required keys for infrastructure property (default frozenset).
                | _checker - Factoriezed parameters checker (default Checker).
                | _reporter - Factoriezed reporter for messaging (default Reporter).
                | _verbose - Factoriezed Enable/Disable verbose option (default False).
                | _infrastructure_property - Splasher hyperlinks property (default None).
            :methods:
                | __init__ - Initials ExtInfrastructure constructor.
                | infrastructure_property - Property method for get/set infrastructure property.
                | get_info_text - Pre-processes info text.
                | get_issue_text - Pre-processes issue text.
                | get_author_text - Pre-processes author text.
                | __str__ - Returns the string representation of ExtInfrastructure.
    '''

    _required_keys: frozenset[str] = frozenset([
        SplashKeys.ATS_NAME, SplashKeys.ATS_ORGANIZATION, SplashKeys.ATS_REPOSITORY
    ])

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initials ExtInfrastructure constructor.

            :param context_bundle: Context bundle for external infrastructure | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._infrastructure_property: dict[Any, Any] | None = None

    @property
    @vreporter('get infrastructure property {infrastructure_property}')
    def infrastructure_property(self) -> dict[Any, Any] | None:
        '''
            Property method for getting infrastructure property.

            :return: Formatted infrastructure property in dict format | None.
            :rtype: <dict[Any, Any] | None>
            :exceptions: ATSRuntimeError, ATSAttributeError
        '''
        return self._infrastructure_property

    @infrastructure_property.setter
    @validator([('dict:infrastructure_property_setup', None)])
    @vreporter('set infrastructure property {infrastructure_property}')
    def infrastructure_property(self, infrastructure_property_setup: dict[Any, Any] | None) -> None:
        '''
            Property method for setting project infrastructure property.

            :param infrastructure_property_setup: Project infrastructure property in dict format | None.
            :type infrastructure_property_setup: <dict[Any, Any] | None>
            :exceptions: ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError.
        '''
        require_keys(infrastructure_property_setup, self._required_keys)
        self._infrastructure_property = cherry_pick_dict(infrastructure_property_setup, self._required_keys)

    @vreporter('get info text {infrastructure_property}')
    @require_attributes('_infrastructure_property')
    def get_info_text(self) -> str:
        '''
            Pre-processes info text for splash.

            :return: Hyperlink with info text.
            :rtype: <str>
            :exceptions: ATSValueError, ATSRuntimeError, ATSAttributeError.
        '''
        name: str = self._infrastructure_property.get(SplashKeys.ATS_NAME)

        return f'\x1b]8;;{name}\a{name}\x1b]8;;\a'

    @vreporter('get issue text {infrastructure_property}')
    @require_attributes('_infrastructure_property')
    def get_issue_text(self) -> str:
        '''
            Pre-processes issue text for splash.

            :return: Hyperlink with issue info.
            :rtype: <str>
            :exceptions: ATSValueError, ATSRuntimeError, ATSAttributeError.
        '''
        repo: str = self._infrastructure_property.get(SplashKeys.ATS_REPOSITORY)

        return f'\x1b]8;;{repo}\a{repo}\x1b]8;;\a'

    @vreporter('get author text {infrastructure_property}')
    @require_attributes('_infrastructure_property')
    def get_author_text(self) -> str:
        '''
            Pre-processes author text for splash.

            :return: Hyperlink with author info.
            :rtype: <str>
            :exceptions: ATSValueError, ATSRuntimeError, ATSAttributeError.
        '''
        org: str = self._infrastructure_property.get(SplashKeys.ATS_ORGANIZATION)

        return f'\x1b]8;;{org}\a{org}\x1b]8;;\a'

    def __str__(self) -> str:
        '''
            Returns the string representation of ExtInfrastructure.

            :return: The ExtInfrastructure as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
