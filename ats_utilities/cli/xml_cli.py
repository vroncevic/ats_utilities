# -*- coding: UTF-8 -*-

'''
 Module
     xml_cli.py
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
     Defined class XmlCLI with attribute(s) and method(s).
     Created API for check and load informations, setup argument parser.
'''

import sys

try:
    from six import add_metaclass
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.xml import XmlBase
    from ats_utilities.abstract import AbstractMethod
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(VerboseRoot)
class XmlCLI(XmlBase):
    '''
        Defined class XmlCLI with attribute(s) and method(s).
        Created API for check and load informations, setup argument parser.
        It defines:

            :attributes:
                | __verbose - enable/disable verbose option.
            :methods:
                | __init__ - initial constructor.
                | add_new_option - adding new option for CL interface.
                | parse_args - parse arguments.
                | process - process and run tool operation (Abstract method).
                | __str__ - str dunder method for XmlCLI.
    '''

    def __init__(self, informations_file, verbose=False):
        '''
            Initial constructor.

            :param informations_file: informations file path.
            :type informations_file: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:informations_file', informations_file)
        ])
        if status == ATSChecker.type_error:
            raise ATSTypeError(error)
        if status == ATSChecker.value_error:
            raise ATSBadCallError(error)
        XmlBase.__init__(self, informations_file, verbose=verbose)
        self.__verbose = verbose
        verbose_message(XmlCLI.verbose, verbose, 'init ATS xml cli')

    def add_new_option(self, *args, **kwargs):
        '''
            Adding new option for CL interface.

            :param args: list of arguments (objects).
            :type args: <list>
            :param kwargs: arguments in shape of dictionary.
            :type kwargs: <dict>
            :exceptions: None
        '''
        self.option_parser.add_operation(*args, **kwargs)

    def parse_args(self, argv):
        '''
            Process arguments from start.

            :param argv: arguments.
            :type argv: <list>
            :return: options and arguments.
            :rtype: <Python object(s)>
            :exceptions: None
        '''
        args = self.option_parser.parse_args(argv)
        return args

    @AbstractMethod
    def process(self, verbose=False):
        '''
            Process and run tool operation (Abstract method).

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exception: NotImplementedError
        '''

    def __str__(self):
        '''
            Dunder str method for XmlCLI.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0}({1}, {2})'.format(
            self.__class__.__name__, XmlBase.__str__(self), str(self.__verbose)
        )
