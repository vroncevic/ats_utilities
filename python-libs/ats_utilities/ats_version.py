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
    from ats_utilities.console_io.verbose import ATSVerbose
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
                VERBOSE - Console text indicator for current process-phase
                __version - Version number of App/Tool/Script
            method:
                __init__ - Initial constructor
                set_ats_version - Setting version number of App/Tool/Script
                get_ats_version - Getting version number of App/Tool/Script
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_UTILITIES::ATS_VERSION]'

    def __init__(self, version=None, verbose=False):
        """
            Initial version number of App/Tool/Script.
            :param version: App/Tool/Script version | None
            :type version: <str> | <NoneType>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        if verbose:
            cls, ver = self.__class__, ATSVerbose()
            ver.message = "{0} {1}".format('Initial version', version)
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        self.__version = version

    def set_ats_version(self, version, verbose=False):
        """
            Setting version number of App/Tool/Script.
            :param version: App/Tool/Script version
            :type version: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls, func, status = self.__class__, stack()[0][3], False
        if version is None:
            txt = 'Argument: missing version <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSBadCallError(msg)
        if not isinstance(version, str):
            txt = 'Argument: expected version <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSTypeError(msg)
        if verbose:
            ver = ATSVerbose()
            ver.message = "{0} {1}".format('Setting version', version)
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        self.__version = version

    def get_ats_version(self, verbose=False):
        """
            Getting version number of App/Tool/Script.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: App/Tool/Script version | None
            :rtype: <str> | <NoneType>
        """
        if verbose:
            cls, ver = self.__class__, ATSVerbose()
            ver.message = "{0} {1}".format('Version', self.__version)
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        return self.__version

    def __str__(self):
        """
            Return human readable string (ATSVersion).
            :return: String representation of ATSVersion
            :rtype: <str>
        """
        return "{0} version {1}".format(self.__class__, self.__version)

    def __repr__(self):
        """
            Return unambiguous string (ATSVersion).
            :return: String representation of ATSVersion
            :rtype: <str>
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__version)
