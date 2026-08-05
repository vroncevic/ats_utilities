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
    Defines the ExtInfrastructure class with attribute(s) and method(s).
    Provides an API for processing hyperlinks for splash screen.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextBundleValidator
from ats_utilities.splash.property.splash_property import SplashProperty
from ats_utilities.utils.dicts import cherry_pick_dict, require_keys
from ats_utilities.utils.reflection import has_attrs, to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ExtInfrastructure:
    '''
        Defines the ExtInfrastructure class with attribute(s) and method(s).
        Provides an API for processing hyperlinks for splash screen.
        Note: Splash screen infrastructure comes from info configuration file as read only data.

        It defines:

            :attributes:
                | _REQUESTED_KEYS - The requested keys from infrastructure property.
                | _infrastructure_property - The external infrastructure settings.
                | _context - The context bundle.
            :methods:
                | __init__ - Initializes the external infrastructure.
                | infrastructure_property - Property method for get/set external infrastructure.
                | get_info_text - Pre-processes info text.
                | get_issue_text - Pre-processes issue text.
                | get_author_text - Pre-processes author text.
                | __str__ - Returns the external infrastructure as a string representation.
    '''

    _REQUESTED_KEYS: frozenset[str] = frozenset([
        SplashProperty.NAME_SETTING,
        SplashProperty.ORGANIZATION_SETTING,
        SplashProperty.REPOSITORY_SETTING
    ])
    _infrastructure_property: Mapping[str, object] | None
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes the external infrastructure.

            :param context_bundle: The context bundle for external infrastructure.
            :exceptions:
                | ATSValueError: The context bundle must be provided and have proper values.
                | ATSTypeError:  The context bundle must be an instance of ContextBundle
                |                and its attributes must be instances of their respective types.
        '''
        ContextBundleValidator.validate(context_bundle)
        self._context = context_bundle
        self._infrastructure_property = None

    @property
    @vreport('getting infrastructure property {infrastructure_property}')
    def infrastructure_property(self) -> Mapping[str, object]:
        '''
            Property method for getting the infrastructure property.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: The formatted infrastructure property in Mapping format (read only data).
            :exceptions:
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._infrastructure_property or {}

    @infrastructure_property.setter
    @mcheck([('Mapping:settings', None)])
    @vreport('setting infrastructure property {infrastructure_property}')
    def infrastructure_property(self, settings: Mapping[str, object]) -> None:
        '''
            Property method for setting the project infrastructure property.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :param settings: The project infrastructure property in Mapping format (read only data).
            :exceptions:
                | ATSValueError:     Infrastructure property settings is missing required keys.
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError:      Parameter type validation failed.
                | ATSValueError:     Parameter format validation failed.
                | ATSRuntimeError:   The decorator is used on a non-class method.
                | ATSAttributeError: The class does not provide a '_checker' object.
        '''
        ctx: str = 'ext_infrastructure::infrastructure_property(...)'
        msg: str = 'the infrastructure property settings is missing required keys'

        require_keys(settings, self._REQUESTED_KEYS, ctx, msg)

        self._infrastructure_property = cherry_pick_dict(settings, self._REQUESTED_KEYS)

    @vreport('getting info text {infrastructure_property}')
    @has_attrs('_infrastructure_property')
    def get_info_text(self) -> str | None:
        '''
            Pre-processes info text for splash.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Hyperlink with info text | None.
            :exceptions:
                | ATSValueError:     Missing or empty attribute: '_infrastructure_property'.
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        name: str = self._infrastructure_property.get(SplashProperty.NAME_SETTING)

        if not name:
            return None

        return f'\x1b]8;;{name}\a{name}\x1b]8;;\a'

    @vreport('getting issue text {infrastructure_property}')
    @has_attrs('_infrastructure_property')
    def get_issue_text(self) -> str | None:
        '''
            Pre-processes issue text for splash.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Hyperlink with issue info | None.
            :exceptions:
                | ATSValueError:     Missing or empty attribute: '_infrastructure_property'.
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        repo: str = self._infrastructure_property.get(SplashProperty.REPOSITORY_SETTING)

        if not repo:
            return None

        return f'\x1b]8;;{repo}\a{repo}\x1b]8;;\a'

    @vreport('getting author text {infrastructure_property}')
    @has_attrs('_infrastructure_property')
    def get_author_text(self) -> str | None:
        '''
            Pre-processes author text for splash.
            Note: Splash screen infrastructure comes from info configuration file as read only data.

            :return: Hyperlink with author info | None.
            :exceptions:
                | ATSValueError:     Missing or empty attribute: '_infrastructure_property'.
                | ATSRuntimeError:   The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        organization: str = self._infrastructure_property.get(SplashProperty.ORGANIZATION_SETTING)

        if not organization:
            return None

        return f'\x1b]8;;{organization}\a{organization}\x1b]8;;\a'

    def __str__(self) -> str:
        '''
            Returns the external infrastructure as a string representation.

            :return: The External infrastructure as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
