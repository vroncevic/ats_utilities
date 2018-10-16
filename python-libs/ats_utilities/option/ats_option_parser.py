# -*- coding: utf-8 -*-
# ats_option_parser.py
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
from optparse import OptionParser

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n".format(e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSOptionParser(BaseSlots):
    """
        Define class ATSOptionParser with attribute(s) and method(s).
        Create option parser and process arguments from start.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __opt_parser - Options parser
            method:
                __init__ - Initial constructor
                add_operation - Adding option to App/Tool/Script
                parse_args - Process arguments from start
    """

    __slots__ = ('VERBOSE', '__opt_parser')
    VERBOSE = 'ATS_UTILITIES::OPTION::ATS_OPTION_PARSER'

    def __init__(self, version, epilog, description, verbose=False):
        """
            Setting version, epilog and description of App/Tool/Script.
            :param version: App/Tool/Script version and build date
            :type version: <str>
            :param epilog: App/Tool/Script long description
            :type epilog: <str>
            :param description: App/Tool/Script author and license
            :type description: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        version_txt = 'Argument: expected version <str> object'
        version_msg = "{0} {1} {2}".format('def', func, version_txt)
        epilog_txt = 'Argument: expected epilog <str> object'
        epilog_msg = "{0} {1} {2}".format('def', func, epilog_txt)
        description_txt = 'Argument: expected description <str> object'
        description_msg = "{0} {1} {2}".format('def', func, description_txt)
        if version is None or not version:
            raise ATSBadCallError(version_msg)
        if not isinstance(version, str):
            raise ATSTypeError(version_msg)
        if epilog is None or not epilog:
            raise ATSBadCallError(epilog_msg)
        if not isinstance(epilog, str):
            raise ATSTypeError(epilog_msg)
        if description is None or not description:
            raise ATSBadCallError(description_msg)
        if not isinstance(description, str):
            raise ATSTypeError(description_msg)
        verbose_message(
            ATSOptionParser.VERBOSE, verbose, 'Initial ATS option parser'
        )
        self.__opt_parser = OptionParser(
            version=version, epilog=epilog, description=description
        )

    def add_operation(self, *args, **kwargs):
        """
            Adding option to App/Tool/Script.
            :param args: List of arguments (objects)
            :type args: <list>
            :param kwargs: Arguments in shape of dictionary
            :type kwargs: <dict>
            :exceptions: None
        """
        self.__opt_parser.add_option(*args, **kwargs)

    def parse_args(self, argv):
        """
            Process arguments from start.
            :param argv: Arguments
            :type argv: <Python object(s)>
            :return: Options and arguments
            :rtype: <Python object(s)>
            :exceptions: None
        """
        (opts, args) = self.__opt_parser.parse_args(argv)
        return opts, args

