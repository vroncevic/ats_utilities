# -*- coding: UTF-8 -*-
# ats_version.py
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


class ATSVersion(object):
    """
        Define class ATSVersion with attribute(s) and method(s).
        Keep, set, get version number of App/Tool/Script.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __version - Version number of App/Tool/Script
            method:
                __init__ - Initial constructor
                set_ats_version - Setting version number of App/Tool/Script
                get_ats_version - Getting version number of App/Tool/Script
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    __slots__ = (
        'VERBOSE',  # Read-Only
        '__version'
    )
    VERBOSE = 'ATS_UTILITIES::ATS_VERSION'

    def __init__(self, version=None, verbose=False):
        """
            Initial version number of App/Tool/Script.
            :param version: App/Tool/Script version
            :type version: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = ATSVersion
        verbose_message(cls.VERBOSE, verbose, 'Initial ATS version')
        self.__version = version

    def set_ats_version(self, version, verbose=False):
        """
            Setting version number of App/Tool/Script.
            :param version: App/Tool/Script version
            :type version: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func = ATSVersion, stack()[0][3]
        expected_txt = 'Argument: expected version <str> object'
        expected_msg = "{0} {1} {2}".format('def', func, expected_txt)
        if version is None or not version:
            raise ATSBadCallError(expected_msg)
        if not isinstance(version, str):
            raise ATSTypeError(expected_msg)
        verbose_message(cls.VERBOSE, verbose, 'Setting ATS version', version)
        self.__version = version

    def get_ats_version(self, verbose=False):
        """
            Getting version number of App/Tool/Script.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: App/Tool/Script version | None
            :rtype: <str> | <NoneType>
        """
        cls = ATSVersion
        verbose_message(cls.VERBOSE, verbose, 'ATS version', self.__version)
        return self.__version

    def __str__(self):
        """
            Return human readable string (ATSVersion).
            :return: String representation of ATSVersion
            :rtype: <str>
        """
        cls = ATSVersion
        return "{0} version {1}".format(cls.__name__, self.__version)

    def __repr__(self):
        """
            Return unambiguous string (ATSVersion).
            :return: String representation of ATSVersion
            :rtype: <str>
        """
        cls = ATSVersion
        return "{0}(\'{1}\')".format(cls.__name__, self.__version)
