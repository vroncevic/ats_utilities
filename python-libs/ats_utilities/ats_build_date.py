# -*- coding: UTF-8 -*-
# ats_build_date.py
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
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSBuildDate(object):
    """
        Define class ATSBuildDate with attribute(s) and method(s).
        Keep, set, get build date of App/Tool/Script.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __build_date - Build date of App/Tool/Script
            method:
                __init__ - Initial constructor
                build_date - Getting/Setting build date of App/Tool/Script
    """

    __slots__ = ('VERBOSE', '__build_date')
    VERBOSE = 'ATS_UTILITIES::ATS_BUILD_DATE'

    def __init__(self, build_date=None, verbose=False):
        """
            Initial build date of App/Tool/Script.
            :param build_date: Build date of App/Tool/Script
            :type build_date: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            ATSBuildDate.VERBOSE, verbose, 'Initial ATS build date'
        )
        self.__build_date = build_date

    @property
    def build_date(self):
        """
            Getting build date of App/Tool/Script.
            :return: Build date of App/Tool/Script | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        """
        return self.__build_date

    @build_date.setter
    def build_date(self, build_date):
        """
            Setting build date of App/Tool/Script.
            :param build_date: Build date of App/Tool/Script
            :type build_date: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        expected_txt = 'Argument: expected build_date <str> object'
        expected_msg = "{0} {1} {2}".format('def', func, expected_txt)
        if build_date is None or not build_date:
            raise ATSBadCallError(expected_msg)
        if not isinstance(build_date, str):
            raise ATSTypeError(expected_msg)
        self.__build_date = build_date

