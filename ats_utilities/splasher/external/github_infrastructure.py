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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.splasher.external.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.context.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.context.context_bundle_inject import inject_context_bundle
from ats_utilities.utils.reflection import has_attrs, to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.utils.dicts import require_keys, cherry_pick_dict
from ats_utilities.validation.check_value import not_empty

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class GitHubInfrastructure(IExtInfrastructure):
    '''
        Defines class GitHubInfrastructure with attribute(s) and method(s).
        Creates an API for processing hyperlinks for splash screen.
        Note: Splash screen infrastructure comes from info configuration file as read only data.

        It defines:

            :attributes:
                | _REQUIRED_KEYS - Required keys for infrastructure property (default frozenset).
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger (default Logger).
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

    _REQUIRED_KEYS: frozenset[str] = frozenset([SplashKeys.ATS_ORGANIZATION, SplashKeys.ATS_REPOSITORY])
    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _infrastructure_property: Mapping[str, Any] | None

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initials GitHubInfrastructure constructor.

            :param context_bundle: Context bundle for GitHub infrastructure.
            :type context_bundle: <ContextBundle>
            :exceptions:
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        inject_context_bundle(self, context_bundle)
        self._infrastructure_property = None

    @property
    @vreport('getting infrastructure property {infrastructure_property}')
    @override
    def infrastructure_property(self) -> Mapping[str, Any]:
        '''
            Property method for getting infrastructure property.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Formatted infrastructure property in Mapping format (read only data).
            :rtype: <Mapping[str, Any]>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._infrastructure_property or {}

    @infrastructure_property.setter
    @mcheck([('Mapping:setup', None)])
    @vreport('setting infrastructure property {infrastructure_property}')
    @override
    def infrastructure_property(self, setup: Mapping[str, Any]) -> None:
        '''
            Property method for setting project infrastructure property.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :param setup: Project infrastructure property in Mapping format (read only data).
            :type setup: <Mapping[str, Any]>
            :exceptions:
                | ATSTypeError: infrastructure property setup is not a Mapping.
                | ATSValueError: infrastructure property setup is missing required keys.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        require_keys(setup, self._REQUIRED_KEYS)
        self._infrastructure_property = cherry_pick_dict(setup, self._REQUIRED_KEYS)

    @vreport('getting info text {infrastructure_property}')
    @has_attrs('_infrastructure_property')
    @override
    def get_info_text(self) -> str:
        '''
            Pre-processes info text for splash.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Hyperlink with info text.
            :rtype: <str>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_infrastructure_property'.
                | ATSValueError: Target property name value is missing or empty.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        org: str = self._infrastructure_property.get(SplashKeys.ATS_ORGANIZATION)
        not_empty(org, r'missing organization')
        repo: str = self._infrastructure_property.get(SplashKeys.ATS_REPOSITORY)
        not_empty(repo, r'missing repository')

        url_short: str = f'github.io/{repo}'
        url_long: str = f'https://{org}.github.io/{repo}'

        return f'\x1b]8;;{url_long}\a{url_short}\x1b]8;;\a'

    @vreport('getting info text {infrastructure_property}')
    @has_attrs('_infrastructure_property')
    @override
    def get_issue_text(self) -> str:
        '''
            Pre-processes issue text for splash.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Hyperlink with issue info.
            :rtype: <str>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_infrastructure_property'.
                | ATSValueError: Target property name value is missing or empty.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        org: str = self._infrastructure_property.get(SplashKeys.ATS_ORGANIZATION)
        not_empty(org, r'missing organization')
        repo: str = self._infrastructure_property.get(SplashKeys.ATS_REPOSITORY)
        not_empty(repo, r'missing repository')

        url: str = f'https://github.com/{org}/{repo}/issues/new/choose'

        return f'\x1b]8;;{url}\agithub.io/issue\x1b]8;;\a'

    @vreport('getting info text {infrastructure_property}')
    @has_attrs('_infrastructure_property')
    @override
    def get_author_text(self) -> str:
        '''
            Pre-processes author text for splash.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Hyperlink with author info.
            :rtype: <str>
            :exceptions:
                | ATSValueError: Missing or empty attribute: '_infrastructure_property'.
                | ATSValueError: Target property name value is missing or empty.
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        org: str = self._infrastructure_property.get(SplashKeys.ATS_ORGANIZATION)
        not_empty(org, r'missing organization')

        org_short: str = f'{org}.github.io'
        org_long: str = f'https://{org}.github.io/bio/'

        return f'\x1b]8;;{org_long}\a{org_short}\x1b]8;;\a'

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of GitHubInfrastructure.

            :return: The GitHubInfrastructure as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
