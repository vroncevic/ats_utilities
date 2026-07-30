# -*- coding: UTF-8 -*-

'''
Module
    splash_property.py
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
    Defines class SplashProperty with attribute(s) and method(s).
    Provides an API for checking splash screen property.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
from ats_utilities.info.setup.keys import InfoKeys
from ats_utilities.utils.dicts import is_present_key
from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class SplashProperty:
    '''
        Defines class SplashProperty with attribute(s) and method(s).
        Provides an API for checking splash screen property.
        Note: Splash screen property comes from info configuration file as read only data.

        It defines:

            :attributes:
                | _settings - Splash keys for App/Tool/Script splash screen (default None).
            :methods:
                | __init__ - Initials SplashProperty constructor.
                | settings - Property method for get/set splash keys.  
                | __str__ - Returns splash property as string representation.
    '''

    _settings: Mapping[str, object]
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initials SplashProperty constructor.

            :param context_bundle: Context bundle for splash screen property.
            :exceptions:
                | ATSValueError:  Context bundle must be provided and have proper values.
                | ATSTypeError:   Context bundle must be an instance of ContextBundle
                |                 and its attributes must be instances of their
                |                 respective types.
        '''
        ContextValidator.validate(context_bundle)
        self._context = context_bundle
        self._settings = {
            'enabled' : False,
            'name' : None,
            'repository' : None,
            'organization' : None,
            'logo' : None,
            'use_github_infrastructure' : False
        }

    @property
    @vreport('getting splash property {settings}')
    def settings(self) -> Mapping[str, object]:
        '''
            Property method for getting splash screen property.
            Note: Splash screen property comes from info configuration file as read only data.

            :return: Formatted splash screen property in Mapping format (read only data).
            :exceptions:
                | ATSRuntimeError:   Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._settings

    @settings.setter
    @mcheck([('Mapping:settings', None)])
    @vreport('setting splash property {settings}')
    def settings(self, settings: Mapping[str, object]) -> None:
        '''
            Property method for setting project splash screen property.
            Note: Splash screen property comes from info configuration file as read only data.

            :param settings: Project splash property in Mapping format (read only data).
            :exceptions:
                | ATSTypeError:      Infrastructure property settings is not a Mapping.
                | ATSRuntimeError:   Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError:      Parameter type validation failed.
                | ATSValueError:     Parameter format validation failed.
                | ATSRuntimeError:   Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        is_name_present: bool = is_present_key(settings, InfoKeys.ATS_NAME)
        is_repository_present: bool = is_present_key(settings, InfoKeys.ATS_REPOSITORY)
        is_organization_present: bool = is_present_key(settings, InfoKeys.ATS_ORGANIZATION)
        is_logo_present: bool = is_present_key(settings, InfoKeys.ATS_LOGO_PATH)
        is_github_present: bool = is_present_key(settings, InfoKeys.ATS_USE_GITHUB_INFRASTRUCTURE)

        self._settings['name'] = InfoKeys.get_name(settings) if is_name_present else None
        self._settings['repository'] = InfoKeys.get_repository(settings) if is_repository_present else None
        self._settings['organization'] = InfoKeys.get_organization(settings) if is_organization_present else None
        self._settings['logo'] = InfoKeys.get_logo(settings) if is_logo_present else None
        self._settings['github'] = InfoKeys.get_use_github_infrastructure(settings) if is_github_present else None

    def __str__(self) -> str:
        '''
            Returns splash property as string representation.

            :return: Splash property as string representation.
            :exceptions: None.
        '''
        return to_str(self)
