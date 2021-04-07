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
     Created API for reading configuration from a cfg file.
'''

import sys
from re import match

try:
    from ats_utilities.config_io import ConfigFile
    from ats_utilities.config_io.base_read import BaseReadConfig
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Cfg2Object(BaseReadConfig):
    '''
        Defined class Cfg2Object with attribute(s) and method(s).
        Created API for read configuration from a cfg file.
        It defines:

            :attributes:
                | __FORMAT - Format of configuration content.
                | __REGEX_MATCH_LINE - Regular expression for matching line.
            :methods:
                | __init__ - Initial constructor.
                | read_configuration - Read configuration from file.
                | __str__ - Dunder method for object Cfg2Object.
    '''

    __FORMAT = 'cfg'
    __REGEX_MATCH_LINE = r'^\s*$'

    def __init__(self, configuration_file):
        '''
            Initial constructor.

            :param configuration_file: Configuration file path.
            :type configuration_file: <str>
            :exceptions: None
        '''
        BaseReadConfig.__init__(self)
        self.file_path = configuration_file

    def read_configuration(self):
        '''
            Read configuration from file.

            :return: Configuration object | None.
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
        return config

    def __str__(self):
        '''
            Dunder method for Cfg2Object.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, BaseReadConfig.__str__(self)
        )
