# -*- coding: UTF-8 -*-
# atf_info.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# ats_utilities is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ats_utilities is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from datetime import datetime
from inspect import stack

try:
    from ats_utilities.ats_name import ATSName
    from ats_utilities.ats_version import ATSVersion
    from ats_utilities.ats_build_date import ATSBuildDate
    from ats_utilities.ats_license import ATSLicense
    from ats_utilities.config.check_base_config import CheckBaseConfig
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSInfo(ATSName, ATSVersion, ATSBuildDate, ATSLicense):
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
                __ats_info_ok - Initialisation of ATS info is ok/not ok
            method:
                __init__ - Initial constructor
                show_base_info - Show ATS info
                get_ats_info - Return ATS info status
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    __slots__ = (
        'VERBOSE',  # Read-Only
        'ATS_NAME',  # Read-Only
        'ATS_VERSION',  # Read-Only
        'ATS_BUILD_DATE',  # Read-Only
        'ATS_LICENSE',  # Read-Only
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
        cls, func = ATSInfo, stack()[0][3]
        info_txt = 'Argument: expected info <dict> object'
        info_msg = "{0} {1} {2}".format('def', func, info_txt)
        if info is None or not info:
            raise ATSBadCallError(info_msg)
        if not isinstance(info, dict):
            raise ATSTypeError(info_msg)
        verbose_message(cls.VERBOSE, verbose, 'Initial ATS info')
        check_config = CheckBaseConfig.is_correct(info, verbose=verbose)
        if check_config:
            app_name = info.get(cls.ATS_NAME)
            ATSName.__init__(self, app_name, verbose=verbose)
            app_version = info.get(cls.ATS_VERSION)
            ATSVersion.__init__(self, app_version, verbose=verbose)
            app_build_date = info.get(cls.ATS_BUILD_DATE)
            ATSBuildDate.__init__(self, app_build_date, verbose=verbose)
            app_license = info.get(cls.ATS_LICENSE)
            ATSLicense.__init__(self, app_license, verbose=verbose)
            self.__ats_info_ok = True
        else:
            self.__ats_info_ok = False

    def show_base_info(self, verbose=False):
        """
            Show ATS info (Ex: [TOOL_NAME] version ver.1.0 05-Apr-2018).
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        if self.__ats_info_ok is True:
            info_msg = "\n{0} version {1} {2}".format(
                "[{0}]".format(self.get_ats_name(verbose=verbose)),
                self.get_ats_version(verbose=verbose),
                datetime.now().date()
            )
            print(info_msg)

    def get_ats_info(self):
        """
            Return ATS info status.
            :return: Boolean status (initialisation of ATS info is ok)
            :rtype: <bool>
        """
        return self.__ats_info_ok

    def __str__(self):
        """
            Return human readable string (ATSInfo).
            :return: String representation of ATSInfo
            :rtype: <str>
        """
        ats_name = self.get_ats_name()
        ats_version = self.get_ats_version()
        ats_build_date = self.get_ats_build_date()
        ats_license = self.get_ats_license()
        return "Info \n{0} \n{1} \n{2} \n{3}".format(
            ats_name, ats_version, ats_build_date, ats_license
        )

    def __repr__(self):
        """
            Return unambiguous string (ATSInfo).
            :return: String representation of ATSInfo
            :rtype: <str>
        """
        cls = ATSInfo
        return "{0}(info)".format(cls.__name__)
