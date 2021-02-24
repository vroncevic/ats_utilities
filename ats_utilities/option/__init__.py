# -*- coding: utf-8 -*-

"""
 Module
     __init__.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
     ats_utilities is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     ats_utilities is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class ATSOptionParser with attribute(s) and method(s).
     Create option parser and process arguments from start.
"""

import sys
from optparse import OptionParser

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSOptionParser(object):
    """
        Define class ATSOptionParser with attribute(s) and method(s).
        Create option parser and process arguments from start.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __opt_parser - Options parser.
            :methods:
                | __init__ - Initial constructor.
                | add_operation - Add option to App/Tool/Script.
                | parse_args - Process arguments from start.
    """

    __slots__ = ('VERBOSE', '__opt_parser')
    VERBOSE = 'ATS_UTILITIES::OPTION::ATS_OPTION_PARSER'

    def __init__(self, version, epilog, description, verbose=False):
        """
            Initial constructor.

            :param version: App/Tool/Script version and build date.
            :type version: <str>
            :param epilog: App/Tool/Script long description.
            :type epilog: <str>
            :param description: App/Tool/Script author and license.
            :type description: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        """
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:version', version),
            ('str:epilog', epilog),
            ('str:description', description)
        ])
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        verbose_message(
            ATSOptionParser.VERBOSE, verbose, 'init ATS option parser'
        )
        self.__opt_parser = OptionParser(
            version=version, epilog=epilog, description=description
        )

    def add_operation(self, *args, **kwargs):
        """
            Add option to App/Tool/Script.

            :param args: List of arguments (objects).
            :type args: <list>
            :param kwargs: Arguments in shape of dictionary.
            :type kwargs: <dict>
            :exceptions: None
        """
        self.__opt_parser.add_option(*args, **kwargs)

    def parse_args(self, argv):
        """
            Process arguments from start.

            :param argv: Arguments.
            :type argv: <Python object(s)>
            :return: Options and arguments.
            :rtype: <Python object(s)>
            :exceptions: None
        """
        (opts, args) = self.__opt_parser.parse_args(argv)
        return opts, args
