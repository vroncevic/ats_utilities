# -*- coding: UTF-8 -*-
# ats_name.py
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


class ATSName(object):
    """
        Define class ATSName with attribute(s) and method(s).
        Keep, set, get App/Tool/Script name.
        It defines:
            attribute:
                VERBOSE - Console text indicator for current process-phase
                __program_name - Name of App/Tool/Script
            method:
                __init__ - Initial constructor
                set_ats_name - Setting name of App/Tool/Script
                get_ats_name - Getting name of App/Tool/Script
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    VERBOSE = '[ATS_UTILITIES::ATS_NAME]'

    def __init__(self, program_name=None, verbose=False):
        """
            Initial name of App/Tool/Script.
            :param program_name: App/Tool/Script name | None
            :type program_name: <str> | <NoneType>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = self.__class__
        verbose_message(cls.VERBOSE, verbose, 'Initial name')
        self.__program_name = program_name

    def set_ats_name(self, program_name, verbose=False):
        """
            Setting name of App/Tool/Script.
            :param program_name: App/Tool/Script name
            :type program_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func, status = self.__class__, stack()[0][3], False
        expected_txt = 'Argument: expected program_name <str> object'
        expected_msg = "{0} {1} {2}".format(cls.VERBOSE, func, expected_txt)
        if program_name is None:
            raise ATSBadCallError(expected_msg)
        if not isinstance(program_name, str):
            raise ATSTypeError(expected_msg)
        verbose_message(cls.VERBOSE, verbose, 'Setting name', program_name)
        self.__program_name = program_name

    def get_ats_name(self, verbose=False):
        """
            Getting name of App/Tool/Script.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: App/Tool/Script name | None
            :rtype: <str> | <NoneType>
        """
        cls = self.__class__
        verbose_message(cls.VERBOSE, verbose, 'Name', self.__program_name)
        return self.__program_name

    def __str__(self):
        """
            Return human readable string (ATSName).
            :return: String representation of ATSName
            :rtype: <str>
        """
        return "{0} name {1}".format(self.__class__, self.__program_name)

    def __repr__(self):
        """
            Return unambiguous string (ATSName).
            :return: String representation of ATSName
            :rtype: <str>
        """
        return "{0}(\'{1}\')".format(type(self).__name__, self.__program_name)
