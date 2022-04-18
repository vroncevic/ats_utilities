# -*- coding: UTF-8 -*-

'''
 Module
     cfg2object.py
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
     Defined class Cfg2Object with attribute(s) and method(s).
     Created API for reading configuration/information from a cfg file.
'''

import sys
from re import match

try:
    from six import add_metaclass
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
class Cfg2Object(BaseReadConfig):
    '''
        Defined class Cfg2Object with attribute(s) and method(s).
        Created API for read configuration/information from a cfg file.
        It defines:

            :attributes:
                | __FORMAT - format of configuration content.
                | __REGEX_MATCH_LINE - regular expression for matching line.
                | __verbose - enable/disable verbose option.
            :methods:
                | __init__ - initial constructor.
                | read_configuration - read configuration from file.
                | __str__ - str dunder method for object Cfg2Object.
    '''

    __FORMAT = 'cfg'
    __REGEX_MATCH_LINE = r'^\s*$'

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
        verbose_message(Cfg2Object.VERBOSE, verbose, configuration_file)

    def read_configuration(self, verbose=False):
        '''
            Getting a configuration from cfg file.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: configuration object | None.
            :rtype: <dict> | <NoneType>
            :exceptions: None
        '''
        config = None
        try:
            with ConfigFile(self.file_path, 'r', Cfg2Object.__FORMAT) as cfg:
                if bool(cfg):
                    content = cfg.read()
                    config, lines = {}, content.splitlines()
                    for line in lines:
                        regex_match = match(
                            Cfg2Object.__REGEX_MATCH_LINE, line
                        )
                        if not regex_match:
                            pairs = line.split('=')
                            config[pairs[0].strip()] = pairs[1].strip()
        except AttributeError:
            pass
        verbose_message(Cfg2Object.VERBOSE, self.__verbose or verbose, config)
        return config

    def __str__(self):
        '''
            Dunder str method for Cfg2Object.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, BaseReadConfig.__str__(self),
            str(self.__verbose)
        )
