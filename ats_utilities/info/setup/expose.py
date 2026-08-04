# -*- coding: UTF-8 -*-

'''
Module
    expose.py
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
    Defines the InfoExpose class with method(s).
    Exposes helper methods to safely extract configuration properties.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.info.setup.keys import InfoBundleKeys
from ats_utilities.utils.dicts import is_present_required_key

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class InfoExpose:
    '''
        Defines the InfoExpose class with method(s).
        Exposes helper methods to safely extract configuration properties.

        It defines:

            :methods:
                | get_name - Returns the name of the application from the config.
                | get_version - Returns the version of the application from the config.
                | get_build_date - Returns the build date of the application from the config.
                | get_licence - Returns the licence of the application from the config.
                | get_repository - Returns the repository of the application from the config.
                | get_organization - Returns the organization of the application from the config.
                | get_use_github_infrastructure - Returns the use github infrastructure of the application from the config.
                | get_logo_path - Returns the logo path of the application from the config.
                | get_log_file - Returns the log file of the application from the config.
                | get_info_ok - Returns the info ok of the application from the config.
    '''

    @classmethod
    def get_name(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the name of the application from the config.

            :param config: The configuration mapping.
            :return: The name of the application if defined.
            :exceptions:
                | ATSValueError: The key ATS_NAME is not present in config.
        '''
        ctx: str = 'info_expose::get_name(...)'
        msg: str = f'the {InfoBundleKeys.ATS_NAME} key is not present in config'
        is_present_required_key(config, InfoBundleKeys.ATS_NAME, ctx, msg)

        return config.get(InfoBundleKeys.ATS_NAME)

    @classmethod
    def get_version(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the version of the application from the config.

            :param config: The configuration mapping.
            :return: The version of the application if defined.
            :exceptions:
                | ATSValueError: The key ATS_VERSION is not present in config.
        '''
        ctx: str = 'info_expose::get_version(...)'
        msg: str = f'the {InfoBundleKeys.ATS_VERSION} key is not present in config'
        is_present_required_key(config, InfoBundleKeys.ATS_VERSION, ctx, msg)

        return config.get(InfoBundleKeys.ATS_VERSION)

    @classmethod
    def get_build_date(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the build date of the application from the config.

            :param config: The configuration mapping.
            :return: The build date of the application if defined.
            :exceptions:
                | ATSValueError: The key ATS_BUILD_DATE is not present in config.
        '''
        ctx: str = 'info_expose::get_build_date(...)'
        msg: str = f'the {InfoBundleKeys.ATS_BUILD_DATE} key is not present in config'
        is_present_required_key(config, InfoBundleKeys.ATS_BUILD_DATE, ctx, msg)

        return config.get(InfoBundleKeys.ATS_BUILD_DATE)

    @classmethod
    def get_licence(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the licence of the application from the config.

            :param config: The configuration mapping.
            :return: The licence of the application if defined.
            :exceptions:
                | ATSValueError: The key ATS_LICENCE is not present in config.
        '''
        ctx: str = 'info_expose::get_licence(...)'
        msg: str = f'the {InfoBundleKeys.ATS_LICENCE} key is not present in config'
        is_present_required_key(config, InfoBundleKeys.ATS_LICENCE, ctx, msg)

        return config.get(InfoBundleKeys.ATS_LICENCE)

    @classmethod
    def get_repository(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the repository of the application from the config.

            :param config: The configuration mapping.
            :return: The repository of the application if defined.
            :exceptions:
                | ATSValueError: The key ATS_REPOSITORY is not present in config.
        '''
        ctx: str = 'info_expose::get_repository(...)'
        msg: str = f'the {InfoBundleKeys.ATS_REPOSITORY} key is not present in config'
        is_present_required_key(config, InfoBundleKeys.ATS_REPOSITORY, ctx, msg)

        return config.get(InfoBundleKeys.ATS_REPOSITORY)

    @classmethod
    def get_organization(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the organization of the application from the config.

            :param config: The configuration mapping.
            :return: The organization of the application if defined.
            :exceptions:
                | ATSValueError: The key ATS_ORGANIZATION is not present in config.
        '''
        ctx: str = 'info_expose::get_organization(...)'
        msg: str = f'the {InfoBundleKeys.ATS_ORGANIZATION} key is not present in config'
        is_present_required_key(config, InfoBundleKeys.ATS_ORGANIZATION, ctx, msg)

        return config.get(InfoBundleKeys.ATS_ORGANIZATION)

    @classmethod
    def get_use_github_infrastructure(cls, config: Mapping[str, str]) -> bool:
        '''
            Returns the use github infrastructure of the application from the config.

            :param config: The configuration mapping.
            :return: The use github infrastructure of the application if defined.
            :exceptions:
                | ATSValueError: The key ATS_USE_GITHUB_INFRASTRUCTURE is not present in config.
        '''
        ctx: str = 'info_expose::get_use_github_infrastructure(...)'
        msg: str = f'the {InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE} key is not present in config'
        is_present_required_key(config, InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE, ctx, msg)

        return config.get(InfoBundleKeys.ATS_USE_GITHUB_INFRASTRUCTURE)

    @classmethod
    def get_logo_path(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the logo path of the application from the config.

            :param config: The configuration mapping.
            :return: The logo path of the application if defined.
            :exceptions:
                | ATSValueError: The key ATS_LOGO_PATH is not present in config.
        '''
        ctx: str = 'info_expose::get_logo_path(...)'
        msg: str = f'the {InfoBundleKeys.ATS_LOGO_PATH} key is not present in config'
        is_present_required_key(config, InfoBundleKeys.ATS_LOGO_PATH, ctx, msg)

        return config.get(InfoBundleKeys.ATS_LOGO_PATH)

    @classmethod
    def get_log_file(cls, config: Mapping[str, str]) -> str:
        '''
            Returns the log file of the application from the config.

            :param config: The configuration mapping.
            :return: The log file of the application if defined.
            :exceptions:
                | ATSValueError: The key ATS_LOG_FILE is not present in config.
        '''
        ctx: str = 'info_expose::get_log_file(...)'
        msg: str = f'the {InfoBundleKeys.ATS_LOG_FILE} key is not present in config'
        is_present_required_key(config, InfoBundleKeys.ATS_LOG_FILE, ctx, msg)

        return config.get(InfoBundleKeys.ATS_LOG_FILE)

    @classmethod
    def get_info_ok(cls, config: Mapping[str, str]) -> bool:
        '''
            Returns the info ok of the application from the config.

            :param config: The configuration mapping.
            :return: The info ok of the application if defined.
            :exceptions:
                | ATSValueError: The key ATS_INFO_OK is not present in config.
        '''
        ctx: str = 'info_expose::get_info_ok(...)'
        msg: str = f'the {InfoBundleKeys.ATS_INFO_OK} key is not present in config'
        is_present_required_key(config, InfoBundleKeys.ATS_INFO_OK, ctx, msg)

        return config.get(InfoBundleKeys.ATS_INFO_OK)
