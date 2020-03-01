# -*- coding: UTF-8 -*-

"""
 Module
     ats_info.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class ATSInfo with attribute(s) and method(s).
     Keep App/Tool/Script information in one container object.
"""

import sys
from datetime import datetime
from inspect import stack

try:
    from ats_utilities.config.check_base_config import CheckBaseConfig
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSInfo(object):
    """
        Define class ATSInfo with attribute(s) and method(s).
        Keep App/Tool/Script information in one container object.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                ATS_VERSION - ATS version key
                ATS_NAME - ATS name key
                ATS_BUILD_DATE - ATS build date key
                ATS_LICENSE - ATS license key
                __name - ATS name
                __version - ATS version
                __license - ATS license
                __build_date - ATS build date
                __ats_info_ok - Initialisation of ATS info is ok/not ok
            method:
                __init__ - Initial constructor
                name - Getting ATS name
                version - Getting ATS version
                license - Getting ATS license
                build_date - Getting ATS build date
                show_base_info - Show ATS info
                is_ats_info_ok - Return ATS info status
    """

    __slots__ = (
        'VERBOSE',
        'ATS_NAME',
        'ATS_VERSION',
        'ATS_BUILD_DATE',
        'ATS_LICENSE',
        '__name',
        '__version',
        '__license',
        '__build_date',
        '__ats_info_ok'
    )
    VERBOSE = 'ATS_UTILITIES::ATS_INFO'
    ATS_NAME = 'ats_name'
    ATS_VERSION = 'ats_version'
    ATS_BUILD_DATE = 'ats_build_date'
    ATS_LICENSE = 'ats_license'

    def __init__(self, info, verbose=False):
        """
            Setting container info for App/Tool/Script.
            :param info: App/Tool/Script basic information
            :type info: <dict>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        info_txt = 'Argument: expected info <dict> object'
        info_msg = "{0} {1} {2}".format('def', func, info_txt)
        if info is None or not info:
            raise ATSBadCallError(info_msg)
        if not isinstance(info, dict):
            raise ATSTypeError(info_msg)
        check_config = CheckBaseConfig.is_correct(info, verbose=verbose)
        if check_config:
            verbose_message(ATSInfo.VERBOSE, verbose, 'Initial ATS info')
            self.__name = info.get(ATSInfo.ATS_NAME)
            self.__version = info.get(ATSInfo.ATS_VERSION)
            self.__license = info.get(ATSInfo.ATS_LICENSE)
            self.__build_date = info.get(ATSInfo.ATS_BUILD_DATE)
            self.__ats_info_ok = True
        else:
            self.__name = None
            self.__version = None
            self.__license = None
            self.__build_date = None
            self.__ats_info_ok = False

    @property
    def name(self):
        """
            Getting ATS name
            :return: App/Tool/Script name
            :rtype: <str>
            :exceptions: None
        """
        return self.__name

    @property
    def version(self):
        """
            Getting ATS version number
            :return: App/Tool/Script version number
            :rtype: <str>
            :exceptions: None
        """
        return self.__version

    @property
    def license(self):
        """
            Getting ATS license text
            :return: App/Tool/Script license text
            :rtype: <str>
            :exceptions: None
        """
        return self.__license

    @property
    def build_date(self):
        """
            Getting ATS build date
            :return: App/Tool/Script build date
            :rtype: <str>
            :exceptions: None
        """
        return self.__build_date

    def show_base_info(self, verbose=False):
        """
            Show ATS info (Ex: [TOOL_NAME] version ver.1.0 05-Apr-2018).
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        if self.__ats_info_ok is True:
            print(
                "\n{0} version {1} {2}".format(
                    "[{0}]".format(self.__name), self.__version,
                    datetime.now().date()
                )
            )

    def is_ats_info_ok(self):
        """
            Return ATS info status.
            :return: Boolean status (initialisation of ATS info is ok)
            :rtype: <bool>
            :exceptions: None
        """
        return self.__ats_info_ok
