# -*- coding: utf-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Creates API for ATS information in one container object.
'''

import sys
from typing import Any, List, Dict
from datetime import datetime

try:
    from ats_utilities.info.ats_name import ATSName
    from ats_utilities.info.ats_info_ok import ATSInfoOk
    from ats_utilities.info.ats_version import ATSVersion
    from ats_utilities.info.ats_licence import ATSLicence
    from ats_utilities.console_io.error import error_message
    from ats_utilities.info.ats_build_date import ATSBuildDate
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.9.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSInfo(ATSName, ATSVersion, ATSLicence, ATSBuildDate, ATSInfoOk):
    '''
        Defines class ATSInfo with attribute(s) and method(s).
        Creates API for ATS information in one container object.
        ATS info container.

        It defines:

            :attributes:
                | ATS_NAME - ATS name key.
                | ATS_VERSION - ATS version key.
                | ATS_LICENCE - ATS licence key.
                | ATS_BUILD_DATE - ATS build date key.
                | ATS_BASE_INFO - ATS base information dict.
                | _verbose - Enable/Disable verbose option.
                | _statuses - List of check statuses.
            :methods:
                | __init__ - Initial ATSInfo constructor.
                | show_base_info - Show ATS information.
                | is_correct - Check information structure.
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

    def __init__(self, info: Dict[Any, Any], verbose: bool = False) -> None:
        '''
            Initial ATSInfo constructor.

            :param info: ATS basic information
            :type info: <Dict[Any, Any]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        ATSName.__init__(self, verbose)
        ATSVersion.__init__(self, verbose)
        ATSLicence.__init__(self, verbose)
        ATSBuildDate.__init__(self, verbose)
        ATSInfoOk.__init__(self, verbose)
        self._verbose = verbose
        self._statuses: List[bool] = []
        self.is_correct(info, self._verbose)
        if all(self._statuses):
            verbose_message(self._verbose, ['load ATS information'])
            self.name = str(info.get(self.ATS_NAME))
            self.version = str(info.get(self.ATS_VERSION))
            self.licence = str(info.get(self.ATS_LICENCE))
            self.build_date = str(info.get(self.ATS_BUILD_DATE))
            self.ats_info_ok = True

    def show_base_info(self) -> None:
        '''
            Show ATS information.

            :exceptions: None
        '''
        if self.ats_info_ok:
            print(
                f'\n[{self.name}] ver {self.version} {datetime.now().date()}'
            )

    def is_correct(
        self, information: Dict[Any, Any], verbose: bool = False
    ) -> None:
        '''
            Check information structure.

            :param information: ATS base information
            :type information: <Dict[Any, Any]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('dict:information', information)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if error_id == self.VALUE_ERROR:
            raise ATSBadCallError(error_msg)
        verbose_message(
            self._verbose or verbose, [f'info structure {str(information)}']
        )
        for info_key in information.keys():
            if info_key not in self.ATS_BASE_INFO.values():
                error_message([f'key not expected [{info_key}]'])
                self._statuses.append(False)
            else:
                self._statuses.append(True)
