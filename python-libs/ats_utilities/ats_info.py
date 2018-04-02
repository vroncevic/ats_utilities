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
                ATS_VERSION - ATS version key
                ATS_NAME - ATS name key
                ATS_BUILD_DATE - ATS build date key
                ATS_LICENSE - ATS license key
                VERBOSE - Console text indicator for current process-phase
            method:
                __init__ - Initial constructor
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    ATS_VERSION = 'ats_version'
    ATS_NAME = 'ats_name'
    ATS_BUILD_DATE = 'ats_build_date'
    ATS_LICENSE = 'ats_license'
    VERBOSE = '[ATS_UTILITIES::ATS_INFO]'

    def __init__(self, info, verbose=False):
        """
            Setting container info for App/Tool/Script.
            :param info: App/Tool/Script basic information
            :type info: <dict>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func = self.__class__, stack()[0][3]
        info_txt = 'Argument: expected info <dict> object'
        info_msg = "{0} {1} {2}".format(cls.VERBOSE, func, info_txt)
        if info is None:
            raise ATSBadCallError(info_msg)
        if not isinstance(info, dict):
            raise ATSTypeError(info_msg)
        verbose_message(cls.VERBOSE, verbose, 'Initial tool info')
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
        return "{0}(info)".format(type(self).__name__)
