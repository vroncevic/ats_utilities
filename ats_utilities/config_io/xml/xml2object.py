# -*- coding: UTF-8 -*-

'''
 Module
     xml2object.py
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
     Defined class Xml2Object with attribute(s) and method(s).
     Created API for reading a configuration/information from a xml file.
'''

import sys

try:
    from six import add_metaclass
    from bs4 import BeautifulSoup
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io import ConfigFile
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.base_read import BaseReadConfig
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
class Xml2Object(BaseReadConfig):
    '''
        Defined class Xml2Object with attribute(s) and method(s).
        Created API for reading a configuration/information from a xml file.
        It defines:

            :attributes:
                | __FORMAT - format of configuration content.
                | __verbose - enable/disable verbose option.
            :methods:
                | __init__ - initial constructor.
                | read_configuration - read a configuration from file.
                | __str__ - str dunder method for object Xml2Object.
    '''

    __FORMAT = 'xml'

    def __init__(self, configuration_file, verbose=False):
        '''
            Initial constructor.

            :param configuration_file: configuration file path.
            :type configuration_file: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:configuration_file', configuration_file)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        BaseReadConfig.__init__(self, verbose=verbose)
        self.__verbose = verbose
        self.file_path = configuration_file
        verbose_message(Xml2Object.VERBOSE, verbose, configuration_file)

    def read_configuration(self, verbose=False):
        '''
            Read a configuration from a xml file.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: configuration object | None.
            :rtype: <BeautifulSoup> | <NoneType>
            :exceptions: None
        '''
        content, config = None, None
        try:
            with ConfigFile(self.file_path, 'r', Xml2Object.__FORMAT) as xml:
                if bool(xml):
                    content = xml.read()
                    config = BeautifulSoup(content, Xml2Object.__FORMAT)
        except AttributeError:
            pass
        verbose_message(Xml2Object.VERBOSE, self.__verbose or verbose, config)
        return config

    def __str__(self):
        '''
            Dunder str method for Xml2Object.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, BaseReadConfig.__str__(self),
            str(self.__verbose)
        )
