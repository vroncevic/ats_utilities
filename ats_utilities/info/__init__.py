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
    Creates API for ATS informations in one container object.
'''

import sys
from typing import Any, List, Dict
from datetime import datetime

try:
    from ats_utilities import auto_str
    from ats_utilities.checker import ATSChecker
    from ats_utilities.info.ats_name import ATSName
    from ats_utilities.info.ats_info_ok import ATSInfoOk
    from ats_utilities.info.ats_version import ATSVersion
    from ats_utilities.info.ats_licence import ATSLicence
    from ats_utilities.info.ats_info_meta import ATSInfoMeta
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
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@auto_str
class ATSInfo(
        ATSName,
        ATSVersion,
        ATSLicence,
        ATSBuildDate,
        ATSInfoOk,
        metaclass=ATSInfoMeta
):
    '''
        Defines class ATSInfo with attribute(s) and method(s).
        Creates API for ATS informations in one container object.
        ATS info container.

        It defines:

            :attributes:
                | ats_name - ATS name key.
                | ats_version - ATS version key.
                | ats_licence - ATS licence key.
                | ats_build_date - ATS build date key.
                | ats_base_info - ATS base information dict.
                | _verbose - Enable/Disable verbose option.
                | _statuses - List of check statuses.
            :methods:
                | __init__ - Initial ATSInfo constructor.
                | show_base_info - Show ATS informations.
                | is_correct - Check information structure.
    '''

    ats_name: str = 'ats_name'
    ats_version: str = 'ats_version'
    ats_licence: str = 'ats_licence'
    ats_build_date: str = 'ats_build_date'
    ats_base_info: dict[int, str] = {
        1: ats_name,
        2: ats_version,
        3: ats_licence,
        4: ats_build_date,
    }

    _verbose: bool
    _statuses: List[bool]

    def __init__(
        self, info: Dict[Any, Any], verbose: bool = False
    ) -> None:
        '''
            Initial ATSInfo constructor.

            :param info: ATS basic informations
            :type info: <Dict[Any, Any]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('dict:info', info)
        ])
        if error_id == ATSChecker.type_error:
            raise ATSTypeError(error_msg)
        if error_id == ATSChecker.value_error:
            raise ATSBadCallError(error_msg)
        ATSName.__init__(self)
        ATSVersion.__init__(self)
        ATSLicence.__init__(self)
        ATSBuildDate.__init__(self)
        ATSInfoOk.__init__(self)
        self._verbose = verbose
        self._statuses = []
        self.is_correct(info, verbose=verbose)
        if all(self._statuses):
            verbose_message(
                ATSInfo.verbose,  # pylint: disable=no-member
                verbose,
                tuple('load ATS informations')
            )
            self.name = str(info.get(ATSInfo.ats_name))
            self.version = str(info.get(ATSInfo.ats_version))
            self.licence = str(info.get(ATSInfo.ats_licence))
            self.build_date = str(info.get(ATSInfo.ats_build_date))
            self.ats_info_ok = True

    def show_base_info(self) -> None:
        '''
            Show ATS informations.

            :exceptions: None
        '''
        if self.ats_info_ok:
            print(
                f'\n[{self.name}] ver {self.version} {datetime.now().date()}'
            )

    def is_correct(
        self, informations: Dict[Any, Any], verbose: bool = False
    ) -> None:
        '''
            Check information structure.

            :param informations: ATS base informations
            :type informations: <Dict[Any, Any]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker: ATSChecker = ATSChecker()
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = checker.check_params([
            ('dict:informations', informations)
        ])
        if error_id == ATSChecker.type_error:
            raise ATSTypeError(error_msg)
        if error_id == ATSChecker.value_error:
            raise ATSBadCallError(error_msg)
        verbose_message(
            ATSInfo.verbose,  # pylint: disable=no-member
            verbose,
            tuple(str(informations))
        )
        for info_key in informations.keys():
            if info_key not in ATSInfo.ats_base_info.values():
                error_message(
                    ATSInfo.verbose,  # pylint: disable=no-member
                    tuple(f'key not expected [{info_key}]')
                )
                self._statuses.append(False)
            else:
                self._statuses.append(True)
