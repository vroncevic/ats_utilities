# -*- coding: utf-8 -*-

'''
Module
    ats_info_manager.py
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
    Defines class ATSInfoManager with attribute(s) and method(s).
    Creates an API for the ATS information in one container object.
'''

from typing import Any, List, Dict, Optional
from datetime import datetime
from ats_utilities.info.iinfo_manager import IATSInfoManager
from ats_utilities.info.iname import IATSName
from ats_utilities.info.name import ATSName
from ats_utilities.info.iversion import IATSVersion
from ats_utilities.info.version import ATSVersion
from ats_utilities.info.ilicence import IATSLicence
from ats_utilities.info.licence import ATSLicence
from ats_utilities.info.ibuild_date import IATSBuildDate
from ats_utilities.info.build_date import ATSBuildDate
from ats_utilities.info.iinfo_ok import IATSInfoOk
from ats_utilities.info.info_ok import ATSInfoOk
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


class ATSInfoManager(IATSInfoManager):
    '''
        Defines class ATSInfoManager with attribute(s) and method(s).
        Creates an API for the ATS information in one container object.
        The ATS information container.

        It defines:

            :attributes:
                | ATS_NAME - The ATS name key.
                | ATS_VERSION - The ATS version key.
                | ATS_LICENCE - The ATS licence key.
                | ATS_BUILD_DATE - The ATS build date key.
                | ATS_BASE_INFO - The ATS base information dict.
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
                | __name - The ATS name (default None).
                | __version - The ATS version (default set ATSName).
                | __licence - The ATS licence (default set ATSLicence).
                | __build_date - The ATS build date (default set ATSBuildDate).
                | __info_ok - The ATS information status (default set ATSInfoOk).
                | __pre_setup - Pre-setup flag for preparing ATS information (default False).
            :methods:
                | __init__ - Initials ATSInfoManager constructor.
                | _pre_setup_check - Performs a pre-setup check for ATS information.
                | pre_setup - Property method for getting ATS pre-setup status.
                | show_base_info - Shows ATS information.
                | base_info_is_ok - Checks base information structure.
                | __str__ - Returns the string representation of ATS info manager.
    '''

    ATS_NAME: str = 'ats_name'
    ATS_VERSION: str = 'ats_version'
    ATS_LICENCE: str = 'ats_licence'
    ATS_BUILD_DATE: str = 'ats_build_date'
    ATS_BASE_INFO: dict[int, str] = {
        1: ATS_NAME,
        2: ATS_VERSION,
        3: ATS_LICENCE,
        4: ATS_BUILD_DATE,
    }

    def __init__(
        self,
        info: Optional[Dict[Any, Any]] = None,
        name: Optional[IATSName] = None,
        version: Optional[IATSVersion] = None,
        licence: Optional[IATSLicence] = None,
        build_date: Optional[IATSBuildDate] = None,
        info_ok: Optional[IATSInfoOk] = None,
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSInfoManager constructor.

            :info: The ATS base information in dict format | None
            :type info: <Optional[Dict[Any, Any]]]>
            :param name: The ATS name (default set ATSName) | None
            :type name: <Optional[IATSName]>
            :param version: The ATS version (default set ATSVersion) | None
            :type version: <Optional[IATSVersion]>
            :param licence: The ATS licence (default set ATSLicence) | None
            :type licence: <Optional[IATSLicence]>
            :param build_date: The ATS build date (default set ATSBuildDate) | None
            :type build_date: <Optional[IATSBuildDate]>
            :param info_ok: The ATS information status (default set ATSInfoOk) | None
            :type info_ok: <Optional[IATSInfoOk]>
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
        self.__name: Optional[IATSName] = name or ATSName(
            checker=self.__checker, reporter=self.__reporter, verbose=self.__verbose
        )
        self.__version: Optional[IATSVersion] = version or ATSVersion(
            checker=self.__checker, reporter=self.__reporter, verbose=self.__verbose
        )
        self.__licence: Optional[IATSLicence] = licence or ATSLicence(
            checker=self.__checker, reporter=self.__reporter, verbose=self.__verbose
        )
        self.__build_date: Optional[IATSBuildDate] = build_date or ATSBuildDate(
            checker=self.__checker, reporter=self.__reporter, verbose=self.__verbose
        )
        self.__info_ok: Optional[IATSInfoOk] = info_ok or ATSInfoOk(
            checker=self.__checker, reporter=self.__reporter, verbose=self.__verbose
        )
        self.__pre_setup: bool = False

        if info is not None and self._pre_setup_check(info, name, version, licence, build_date, info_ok):
            self.__name.name = info.get(self.ATS_NAME)
            self.__version.version = info.get(self.ATS_VERSION)
            self.__licence.licence = info.get(self.ATS_LICENCE)
            self.__build_date.build_date = info.get(self.ATS_BUILD_DATE)
            self.__info_ok.info_ok = True

        self.__pre_setup = all([
            self.__name.is_name_not_none(),
            self.__version.is_version_not_none(),
            self.__licence.is_licence_not_none(),
            self.__build_date.is_build_date_not_none(),
            self.__info_ok.info_ok
        ])

    def _pre_setup_check(
        self,
        info: Optional[Dict[Any, Any]] = None,
        name: Optional[IATSName] = None,
        version: Optional[IATSVersion] = None,
        licence: Optional[IATSLicence] = None,
        build_date: Optional[IATSBuildDate] = None,
        info_ok: Optional[IATSInfoOk] = None,
    ) -> bool:
        '''
            Performs a pre-setup check for ATS information.
            This method is called during initialization if an 'info' dictionary is provided.
            It validates the 'info' dictionary and issues warnings if individual info objects
            (name, version, licence, build_date, info_ok) are also provided, as the values
            from the 'info' dictionary will take precedence.

            :param info: The ATS base information in dict format.
            :type info: <Optional[Dict[Any, Any]]>
            :param name: The ATS name object.
            :type name: <Optional[IATSName]>
            :param version: The ATS version object.
            :type version: <Optional[IATSVersion]>
            :param licence: The ATS licence object.
            :type licence: <Optional[IATSLicence]>
            :param build_date: The ATS build date object.
            :type build_date: <Optional[IATSBuildDate]>
            :param info_ok: The ATS information status object.
            :type info_ok: <Optional[IATSInfoOk]>
            :return: True if the 'info' dictionary is valid, False otherwise.
            :rtype: <bool>
            :exceptions: ATSTypeError, ATSValueError (potentially from base_info_is_ok via validator)
        '''
        if info and self.base_info_is_ok(info):
            if name:
                self.__reporter.warning(['ATS base info (dict) will overwrite ATS name'])

            if version:
                self.__reporter.warning(['ATS base info (dict) will overwrite ATS version'])

            if licence:
                self.__reporter.warning(['ATS base info (dict) will overwrite ATS licence'])

            if build_date:
                self.__reporter.warning(['ATS base info (dict) will overwrite ATS build date'])

            if info_ok:
                self.__reporter.warning(['ATS base info (dict) will overwrite ATS info_ok'])
        else:
            return False

        return True

    @property
    @vreporter('get pre_setup {pre_setup}')
    def pre_setup(self) -> bool:
        '''
            Property method for getting ATS pre-setup status.

            :return: The ATS pre-setup status in bool format
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__pre_setup

    @pre_setup.setter
    @vreporter('set pre_setup {pre_setup}')
    def pre_setup(self, pre_setup: bool) -> None:
        '''
            Property method for getting ATS pre-setup status.

            :param pre_setup: The ATS pre-setup status in bool format
            :type pre_setup: <bool>
            :return: The ATS pre-setup status in bool format
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        self.__pre_setup = pre_setup

    @vreporter('show base pre_setup {pre_setup}')
    def show_base_info(self) -> None:
        '''
            Shows ATS information.

            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        if self.__pre_setup and self.__info_ok and self.__name and self.__version:
            print(f'\n[{self.__name.name}] ver {self.__version.version} {datetime.now().date()}')

    @validator([('dict:info', None)])
    @vreporter('base info ok pre_setup {pre_setup}')
    def base_info_is_ok(self, info: Dict[Any, Any]) -> bool:
        '''
            Checks base information structure.

            :param info: The ATS base information in dict format
            :type info: <Dict[Any, Any]>
            :return: True (all info params are ok) | False (info params are not ok)
            :rtype: <bool>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        all_state: List[bool] = []

        for info_key in info.keys():
            if info_key not in self.ATS_BASE_INFO.values():
                self.__reporter.error([f'key not expected [{info_key}]'])
                all_state.append(False)
            else:
                if info[info_key] is None:
                    self.__reporter.error([f'parameter [{info_key}] is None'])
                    all_state.append(False)
                else:
                    all_state.append(True)

        return all(all_state)

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS info manager.

            :return: The ATS info manager string representation
            :rtype: <str>
            :exceptions: None
        '''
        name = str(self.__name).replace('\n', '\n    ')
        version = str(self.__version).replace('\n', '\n    ')
        licence = str(self.__licence).replace('\n', '\n    ')
        build_date = str(self.__build_date).replace('\n', '\n    ')
        info_ok = str(self.__info_ok).replace('\n', '\n    ')
        pre_setup = str(self.__pre_setup).replace('\n', '\n    ')
        checker = str(self.__checker).replace('\n', '\n    ')
        reporter = str(self.__reporter).replace('\n', '\n    ')
        verbose = str(self.__verbose).replace('\n', '\n    ')

        return (
            f'<{self.__class__.__name__}(\n'
            f'    name={name},\n'
            f'    version={version},\n'
            f'    licence={licence},\n'
            f'    build_date={build_date},\n'
            f'    info_ok={info_ok},\n'
            f'    pre_setup={pre_setup},\n'
            f'    checker={checker},\n'
            f'    reporter={reporter},\n'
            f'    verbose={verbose}\n)> at 0x{id(self):x}'
        )
