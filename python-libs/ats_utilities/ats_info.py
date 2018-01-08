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

try:
    from ats_utilities.ats_name import ATSName
    from ats_utilities.ats_version import ATSVersion
    from ats_utilities.ats_build_date import ATSBuildDate
    from ats_utilities.ats_license import ATSLicense
    from ats_utilities.config.check_base_config import CheckBaseConfig
    from ats_utilities.error.ats_value_error import ATSValueError
    from ats_utilities.text import COut
    from ats_utilities.text.stdout_text import ATS, ERR, RST
except ImportError as e:
    msg = "\n{0}\n".format(e)
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
            VERBOSE - Verbose prefix console text
        method:
            __init__ - Initial constructor
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    ATS_VERSION = 'ats_version'
    ATS_NAME = 'ats_name'
    ATS_BUILD_DATE = 'ats_build_date'
    ATS_LICENSE = 'ats_license'
    VERBOSE = 'ATS_INFO'

    def __init__(self, info, verbose=False):
        """
        Setting container info for App/Tool/Script.
        :param info: App/Tool/Script basic information
        :type info: <dict>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}".format('Setting info structure')
        COut.print_console_msg(msg, verbose=verbose)
        check_config = CheckBaseConfig.is_correct(info, verbose)
        is_dict = isinstance(info, dict)
        if check_config and is_dict:
            app_name = info.get(cls.ATS_NAME)
            ATSName.__init__(self, app_name, verbose)
            app_version = info.get(cls.ATS_VERSION)
            ATSVersion.__init__(self, app_version, verbose)
            app_build_date = info.get(cls.ATS_BUILD_DATE)
            ATSBuildDate.__init__(self, app_build_date, verbose)
            app_license = info.get(cls.ATS_LICENSE)
            ATSLicense.__init__(self, app_license, verbose)
        else:
            msg = "\n{0} {1}{2} {3} [{4}]{5}\n".format(
                cls.VERBOSE, ERR, ATS, 'wrong info structure', type(info), RST
            )
            raise ATSValueError(msg)

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
        return "{0} info \n{1} \n{2} \n{3} \n{4}".format(
            ATS, ats_name, ats_version, ats_build_date, ats_license
        )

    def __repr__(self):
        """
        Return unambiguous string (ATSInfo).
        :return: String representation of ATSInfo
        :rtype: <str>
        """
        return "{0}(info)".format(type(self).__name__)
