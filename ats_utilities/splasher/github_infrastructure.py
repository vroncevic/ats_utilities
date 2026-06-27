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

from typing import Any, override
from ats_utilities.splasher.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import require_attributes, format_instance_to_string
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter
from ats_utilities.factory_dict_utils import require_keys, cherry_pick_dict

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class GitHubInfrastructure(IExtInfrastructure):
    '''
        Defines class GitHubInfrastructure with attribute(s) and method(s).
        Creates an API for processing hyperlinks for splash screen.

        It defines:

            :attributes:
                | _required_keys - Required keys for infrastructure property (default frozenset).
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _infrastructure_property - Splasher GitHub hyperlinks property (default None).
            :methods:
                | __init__ - Initials GitHubInfrastructure constructor.
                | get_info_text - Pre-processes info text.
                | get_issue_text - Pre-processes issue text.
                | get_author_text - Pre-processes author text.
                | __str__ - Returns the string representation of GitHubInfrastructure.
    '''

    _required_keys: frozenset[str] = frozenset([SplashKeys.ATS_ORGANIZATION, SplashKeys.ATS_REPOSITORY])

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initials GitHubInfrastructure constructor.

            :param context_bundle: Context bundle for GitHub infrastructure | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._infrastructure_property: dict[Any, Any] | None = None

    @property
    @vreporter('get infrastructure property {infrastructure_property}')
    @override
    def infrastructure_property(self) -> dict[Any, Any] | None:
        '''
            Property method for getting infrastructure property.

            :return: Formatted infrastructure property in dict format | None.
            :rtype: <dict[Any, Any] | None>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
        '''
        return self._infrastructure_property

    @infrastructure_property.setter
    @validator([('dict:infrastructure_property_setup', None)])
    @vreporter('set infrastructure property {infrastructure_property}')
    @override
    def infrastructure_property(self, infrastructure_property_setup: dict[Any, Any] | None) -> None:
        '''
            Property method for setting project infrastructure property.

            :param infrastructure_property_setup: Project infrastructure property in dict format | None.
            :type infrastructure_property_setup: <dict[Any, Any] | None>
            :exceptions:
                | ATSTypeError: infrastructure property setup is not a dict | None.
                | ATSValueError: infrastructure property setup is missing required keys.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        require_keys(infrastructure_property_setup, self._required_keys)
        self._infrastructure_property = cherry_pick_dict(infrastructure_property_setup, self._required_keys)

    @vreporter('get info text {infrastructure_property}')
    @require_attributes('_infrastructure_property')
    @override
    def get_info_text(self) -> str:
        '''
            Pre-processes info text for splash.

            :return: Hyperlink with info text.
            :rtype: <str>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_infrastructure_property'.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
        '''
        org: str = self._infrastructure_property.get(SplashKeys.ATS_ORGANIZATION)
        repo: str = self._infrastructure_property.get(SplashKeys.ATS_REPOSITORY)
        url_short: str = f'github.io/{repo}'
        url_long: str = f'https://{org}.github.io/{repo}'

        return f'\x1b]8;;{url_long}\a{url_short}\x1b]8;;\a'

    @vreporter('get info text {infrastructure_property}')
    @require_attributes('_infrastructure_property')
    @override
    def get_issue_text(self) -> str:
        '''
            Pre-processes issue text for splash.

            :return: Hyperlink with issue info.
            :rtype: <str>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_infrastructure_property'.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
        '''
        org: str = self._infrastructure_property.get(SplashKeys.ATS_ORGANIZATION)
        repo: str = self._infrastructure_property.get(SplashKeys.ATS_REPOSITORY)
        url: str = f'https://github.com/{org}/{repo}/issues/new/choose'

        return f'\x1b]8;;{url}\agithub.io/issue\x1b]8;;\a'

    @vreporter('get info text {infrastructure_property}')
    @require_attributes('_infrastructure_property')
    @override
    def get_author_text(self) -> str:
        '''
            Pre-processes author text for splash.

            :return: Hyperlink with author info.
            :rtype: <str>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_infrastructure_property'.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
        '''
        org: str = self._infrastructure_property.get(SplashKeys.ATS_ORGANIZATION)
        org_short: str = f"{org}.github.io"
        org_long: str = f"https://{org}.github.io/bio/"

        return f'\x1b]8;;{org_long}\a{org_short}\x1b]8;;\a'

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of GitHubInfrastructure.

            :return: The GitHubInfrastructure as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
