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
    Provides an API for processing hyperlinks for splash screen.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
from ats_utilities.splash.setup.keys import SplashKeys
from ats_utilities.utils.reflection import has_attrs, to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.utils.dicts import require_keys, cherry_pick_dict
from ats_utilities.validation.check_value import not_empty

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class GitHubInfrastructure:
    '''
        Defines class GitHubInfrastructure with attribute(s) and method(s).
        Provides an API for processing hyperlinks for splash screen.
        Note: Splash screen infrastructure comes from info configuration file as read only data.

        It defines:

            :attributes:
                | _REQUIRED_KEYS - Required keys for infrastructure property (default frozenset).
                | _infrastructure_property - SplashManager GitHub hyperlinks property (default None).
            :methods:
                | __init__ - Initials git hub infrastructure.
                | get_info_text - Pre-processes info text.
                | get_issue_text - Pre-processes issue text.
                | get_author_text - Pre-processes author text.
                | __str__ - Returns git hub infrastructure as string representation.
    '''

    _REQUIRED_KEYS: frozenset[str] = frozenset([SplashKeys.ATS_ORGANIZATION, SplashKeys.ATS_REPOSITORY])
    _infrastructure_property: Mapping[str, object] | None
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initials git hub infrastructure.

            :param context_bundle: Context bundle for git hub infrastructure.
            :exceptions:
                | ATSValueError:  Context bundle must be provided and have proper values.
                | ATSTypeError:   Context bundle must be an instance of ContextBundle
                |                 and its attributes must be instances of their
                |                 respective types.
        '''
        ContextValidator.validate(context_bundle)
        self._context = context_bundle
        self._infrastructure_property = None

    @property
    @vreport('getting infrastructure property {infrastructure_property}')
    def infrastructure_property(self) -> Mapping[str, object]:
        '''
            Property method for getting infrastructure property.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Formatted infrastructure property in Mapping format (read only data).
            :exceptions:
                | ATSRuntimeError:   Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._infrastructure_property or {}

    @infrastructure_property.setter
    @mcheck([('Mapping:setup', None)])
    @vreport('setting infrastructure property {infrastructure_property}')
    def infrastructure_property(self, setup: Mapping[str, object]) -> None:
        '''
            Property method for setting project infrastructure property.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :param setup: Project infrastructure property in Mapping format (read only data).
            :exceptions:
                | ATSTypeError:      Infrastructure property setup is not a Mapping.
                | ATSValueError:     Infrastructure property setup is missing required keys.
                | ATSRuntimeError:   Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError:      Parameter type validation failed.
                | ATSValueError:     Parameter format validation failed.
                | ATSRuntimeError:   Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        context: str = 'github_infrastructure::infrastructure_property(...)'
        require_keys(setup, self._REQUIRED_KEYS, context, 'infrastructure property setup is missing required keys')
        self._infrastructure_property = cherry_pick_dict(setup, self._REQUIRED_KEYS)

    @vreport('getting info text {infrastructure_property}')
    @has_attrs('_infrastructure_property')
    def get_info_text(self) -> str:
        '''
            Pre-processes info text for splash.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Hyperlink with info text.
            :exceptions:
                | ATSValueError:     Missing or empty attribute: '_infrastructure_property'.
                | ATSValueError:     Target property name value is missing or empty.
                | ATSRuntimeError:   Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        context: str = 'github_infrastructure::get_info_text(...)'
        org: str = self._infrastructure_property.get(SplashKeys.ATS_ORGANIZATION)
        not_empty(org, context, 'info property organization is missing or empty')
        repo: str = self._infrastructure_property.get(SplashKeys.ATS_REPOSITORY)
        not_empty(repo, context, 'info property repository is missing or empty')
        url_short: str = f'github.io/{repo}'
        url_long: str = f'https://{org}.github.io/{repo}'

        return f'\x1b]8;;{url_long}\a{url_short}\x1b]8;;\a'

    @vreport('getting info text {infrastructure_property}')
    @has_attrs('_infrastructure_property')
    def get_issue_text(self) -> str:
        '''
            Pre-processes issue text for splash.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Hyperlink with issue info.
            :exceptions:
                | ATSValueError:     Missing or empty attribute: '_infrastructure_property'.
                | ATSValueError:     Target property name value is missing or empty.
                | ATSRuntimeError:   Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        context: str = 'github_infrastructure::get_issue_text(...)'
        org: str = self._infrastructure_property.get(SplashKeys.ATS_ORGANIZATION)
        not_empty(org, context, 'issue property organization is missing or empty')
        repo: str = self._infrastructure_property.get(SplashKeys.ATS_REPOSITORY)
        not_empty(repo, context, 'issue property repository is missing or empty')
        url: str = f'https://github.com/{org}/{repo}/issues/new/choose'

        return f'\x1b]8;;{url}\agithub.io/issue\x1b]8;;\a'

    @vreport('getting info text {infrastructure_property}')
    @has_attrs('_infrastructure_property')
    def get_author_text(self) -> str:
        '''
            Pre-processes author text for splash.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Hyperlink with author info.
            :exceptions:
                | ATSValueError:     Missing or empty attribute: '_infrastructure_property'.
                | ATSValueError:     Target property name value is missing or empty.
                | ATSRuntimeError:   Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        context: str = 'github_infrastructure::get_author_text(...)'
        org: str = self._infrastructure_property.get(SplashKeys.ATS_ORGANIZATION)
        not_empty(org, context, 'author property organization is missing or empty')
        org_short: str = f'{org}.github.io'
        org_long: str = f'https://{org}.github.io/bio/'

        return f'\x1b]8;;{org_long}\a{org_short}\x1b]8;;\a'

    def __str__(self) -> str:
        '''
            Returns git hub infrastructure as string representation.

            :return: Git hub infrastructure as string representation.
            :exceptions: None.
        '''
        return to_str(self)
