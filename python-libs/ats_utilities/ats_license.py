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
    sys.exit(msg)  # Force close python ATS ###################################

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
        Keep, set, get console_io license of App/Tool/Script.
        It defines:
            attribute:
                VERBOSE - Console text indicator for current process-phase
                __license - Text with license
            method:
                __init__ - Initial constructor
                set_ats_license - Setting App/Tool/Script console_io license
                get_ats_license - Getting App/Tool/Script console_io license
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_UTILITIES::ATS_LICENSE]'

    def __init__(self, txt_license=None, verbose=False):
        """
            Initial console_io license of App/Tool/Script.
            :param txt_license: App/Tool/Script console_io license | None
            :type txt_license: <str> | <NoneType>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = self.__class__
        verbose_message(cls.VERBOSE, verbose, 'Initial license')
        self.__license = txt_license

    def set_ats_license(self, txt_license, verbose=False):
        """
            Setting console_io license of App/Tool/Script.
            :param txt_license: App/Tool/Script console_io license
            :type txt_license: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func, status = self.__class__, stack()[0][3], False
        expected_txt = 'Argument: expected txt_license <str> object'
        expected_msg = "{0} {1} {2}".format(cls.VERBOSE, func, expected_txt)
        if txt_license is None or not txt_license:
            raise ATSBadCallError(expected_msg)
        if not isinstance(txt_license, str):
            raise ATSTypeError(expected_msg)
        verbose_message(cls.VERBOSE, verbose, 'Setting license', txt_license)
        self.__license = txt_license

    def get_ats_license(self, verbose=False):
        """
            Getting console_io license of App/Tool/Script.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: App/Tool/Script license text | None
            :rtype: <str> | <NoneType>
        """
        cls = self.__class__
        verbose_message(cls.VERBOSE, verbose, 'License', self.__license)
        return self.__license

    def __str__(self):
        """
            Return human readable string (ATSLicense).
            :return: String representation of ATSLicense
            :rtype: <str>
        """
        return "{0} license {1}".format(self.__class__, self.__license)

    def __repr__(self):
        """
            Return unambiguous string (ATSLicense).
            :return: String representation of ATSLicense
            :rtype: <str>
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__license)
