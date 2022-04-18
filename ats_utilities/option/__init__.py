# -*- coding: utf-8 -*-

'''
 Module
     __init__.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class ATSOptionParser with attribute(s) and method(s).
     Created option parser and argument processor.
'''

import sys
from argparse import ArgumentParser

try:
    from six import add_metaclass
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(VerboseRoot)
class ATSOptionParser:
    '''
        Defined class ATSOptionParser with attribute(s) and method(s).
        Created option parser and argument processor.

        It defines:

            :attributes:
                | __verbose - enable/disable verbose option.
                | __opt_parser - options parser.
            :methods:
                | __init__ - initial constructor.
                | add_operation - add option to ATS.
                | parse_args - process arguments from start.
                | __str__ - str dunder method for ATSOptionParser.
    '''

    def __init__(self, version, epilog, description, verbose=False):
        '''
            Initial constructor.

            :param version: ATS version and build date.
            :type version: <str>
            :param epilog: ATS long description.
            :type epilog: <str>
            :param description: ATS author and license.
            :type description: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:version', version), ('str:epilog', epilog),
            ('str:description', description)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__verbose = verbose
        self.__opt_parser = ArgumentParser(version, epilog, description)
        verbose_message(
            ATSOptionParser.VERBOSE, self.__verbose or verbose,
            version, epilog, description
        )

    def add_operation(self, *args, **kwargs):
        '''
            Add option to ATS.

            :param args: list of arguments (objects).
            :type args: <list>
            :param kwargs: arguments in shape of dictionary.
            :type kwargs: <dict>
            :exceptions: None
        '''
        self.__opt_parser.add_argument(*args, **kwargs)

    def parse_args(self, arguments, verbose=False):
        '''
            Process arguments from start.

            :param arguments: arguments.
            :type arguments: <list>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: namespace object.
            :rtype: <argparse.Namespace>
            :exceptions: None
        '''
        args = self.__opt_parser.parse_args(arguments)
        verbose_message(
            ATSOptionParser.VERBOSE, self.__verbose or verbose, arguments
        )
        return args

    def __str__(self):
        '''
            Dunder str method for ATSOptionParser.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__verbose),
            str(self.__opt_parser)
        )
