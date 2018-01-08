# -*- coding: UTF-8 -*-
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
from optparse import OptionParser

try:
    from ats_utilities.text import COut
    from ats_utilities.text.stdout_text import DBG, ERR, RST
    from ats_utilities.error.ats_value_error import ATSValueError
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


class ATSOptionParser(object):
    """
    Define class ATSOptionParser with attribute(s) and method(s).
    Create option parser and process arguments from start.
    It defines:
        attribute:
            VERBOSE - Verbose prefix console text
            __opt_parser - Options parser
        method:
            __init__ - Initial constructor
            add_operation - Adding option to App/Tool/Script
            parese_args - Process arguments from start
    """

    VERBOSE = 'ATS_OPTION_PARSER'

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
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}".format('Setting option parser')
        COut.print_console_msg(msg, verbose=verbose)
        if version and epilog and description:
            self.__opt_parser = OptionParser(
                version=version, epilog=epilog, description=description
            )
        else:
            msg = "\n{0} {1}{2} {3}{4}\n".format(
                cls.VERBOSE, ERR, 'Missing option parser argument(s)',
                'version/epilog/description', RST
            )
            raise ATSValueError(msg)

    def add_operation(self, *args, **kwargs):
        """
        Adding option to App/Tool/Script.
        :param args: List of arguments (objects)
        :type args: <list>
        :param kwargs: Arguments in shape of dictionary
        :type kwargs: <dict>
        """
        self.__opt_parser.add_option(*args, **kwargs)

    def parse_args(self, argv):
        """
        Process arguments from start.
        :param argv: Arguments
        :type argv: <Python object(s)>
        :return: Options and arguments
        :rtype: <Python object(s)>
        """
        (opts, args) = self.__opt_parser.parse_args(argv)
        return opts, args
