# -*- coding: UTF-8 -*-
# ats_license.py
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


class ATSLicense(object):
    """
        Define class ATSLicense with attribute(s) and method(s).
        Keep, set, get license of App/Tool/Script.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __license - Text with license for App/Tool/Script
            method:
                __init__ - Initial constructor
                license - Getting/Setting App/Tool/Script license
    """

    __slots__ = ('VERBOSE', '__license')
    VERBOSE = 'ATS_UTILITIES::ATS_LICENSE'

    def __init__(self, txt_license=None, verbose=False):
        """
            Initial console_io license of App/Tool/Script.
            :param txt_license: App/Tool/Script license
            :type txt_license: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(ATSLicense.VERBOSE, verbose, 'Initial ATS license')
        self.__license = txt_license

    @property
    def license(self):
        """
            Getting console_io license of App/Tool/Script.
            :return: App/Tool/Script license text | None
            :rtype: <str> | <NoneType>
            :exceptions: None
        """
        return self.__license

    @license.setter
    def license(self, txt_license):
        """
            Setting console_io license of App/Tool/Script.
            :param txt_license: App/Tool/Script license
            :type txt_license: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        expected_txt = 'Argument: expected txt_license <str> object'
        expected_msg = "{0} {1} {2}".format('def', func, expected_txt)
        if txt_license is None or not txt_license:
            raise ATSBadCallError(expected_msg)
        if not isinstance(txt_license, str):
            raise ATSTypeError(expected_msg)
        self.__license = txt_license

