# -*- coding: utf-8 -*-

'''
Module
    ats_info.py
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
    Defines class ATSInfo with attribute(s) and method(s).
    Creates an API for the ATS information in one container object.
'''

from typing import Any, ClassVar, List, Dict, Optional
from datetime import datetime
from ats_utilities.checker import IATSChecker, ATSChecker, ErrorChecker
from ats_utilities.console_io import IATSReporter, ATSReporter
from ats_utilities.exceptions import ATSTypeError
from ats_utilities.info import ATSName, ATSVersion, ATSLicence, ATSBuildDate, ATSInfoOk

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSInfo(ATSName, ATSVersion, ATSLicence, ATSBuildDate, ATSInfoOk):
    '''
        Defines class ATSInfo with attribute(s) and method(s).
        Creates an API for the ATS information in one container object.
        The ATS information container.

        It defines:

            :attributes:
                | ERRORS - Error checker mapping.
                | ATS_NAME - The ATS name key.
                | ATS_VERSION - The ATS version key.
                | ATS_LICENCE - The ATS licence key.
                | ATS_BUILD_DATE - The ATS build date key.
                | ATS_BASE_INFO - The ATS base information dict.
                | __checker - Error checker.
                | __reporter - ATSReporter for messaging.
                | __verbose - Enable/Disable verbose option.
            :methods:
                | __init__ - Initials ATSInfo constructor.
                | show_base_info - Shows ATS information.
                | is_correct - Checks information structure.
    '''

    ERRORS: ClassVar[type[ErrorChecker]] = ErrorChecker
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
        info: Dict[Any, Any],
        checker: Optional[IATSChecker] = None,
        reporter: Optional[IATSReporter] = None,
        verbose: bool = False
    ) -> None:
        '''
            Initials ATSInfo constructor.

            :param info: The ATS basic information
            :type info: <Dict[Any, Any]>
            :param checker: Error checker | None
            :type checker: <Optional[IATSChecker]>
            :param reporter: ATSReporter for check operations | None
            :type reporter: <Optional[IATSReporter]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        ATSName.__init__(self, checker, reporter, verbose)
        ATSVersion.__init__(self, checker, reporter, verbose)
        ATSLicence.__init__(self, checker, reporter, verbose)
        ATSBuildDate.__init__(self, checker, reporter, verbose)
        ATSInfoOk.__init__(self, checker, reporter, verbose)
        self.__checker: IATSChecker = checker or ATSChecker()
        self.__reporter: IATSReporter = reporter or ATSReporter()
        self.__verbose: bool = verbose
        if self.is_correct(info, self.__verbose):
            self.__reporter.verbose(self.__verbose, ['load ATS information'])
            self.name = str(info.get(self.ATS_NAME))
            self.version = str(info.get(self.ATS_VERSION))
            self.licence = str(info.get(self.ATS_LICENCE))
            self.build_date = str(info.get(self.ATS_BUILD_DATE))
            self.ats_info_ok = True

    def show_base_info(self) -> None:
        '''
            Shows ATS information.

            :exceptions: None
        '''
        if self.ats_info_ok:
            print(f'\n[{self.name}] ver {self.version} {datetime.now().date()}')

    def is_correct(self, info: Dict[Any, Any], verbose: bool = False) -> bool:
        '''
            Checks information structure.

            :param info: The ATS base information
            :type info: <Dict[Any, Any]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (all info params are ok) | False
            :rtype: <bool>
            :exceptions: ATSTypeError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.__checker.validate_parameters([('dict:info', info)])

        if error_id == self.ERRORS.TYPE_ERROR:
            raise ATSTypeError(error_msg)

        self.__reporter.verbose(self.__verbose or verbose, [f'info structure {str(info)}'])
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
