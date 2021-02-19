# -*- coding: UTF-8 -*-

"""
 Module
     cfg2object.py
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
     Define class Cfg2Object with attribute(s) and method(s).
     Convert configuration from a cfg file to an object.
"""

import sys
from re import match

try:
    from ats_utilities.config_io import ConfigFile
    from ats_utilities.config_io.base_read import BaseReadConfig
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Cfg2Object(BaseReadConfig):
    """
        Define class Cfg2Object with attribute(s) and method(s).
        Convert configuration from a cfg file to an object.
        It defines:

            :attributes:
                | __FORMAT - Format of configuration content.
                | __REGEX_MATCH_LINE - Regular expression for matching line.
            :methods:
                | __init__ - Initial constructor.
                | read_configuration - Read configuration from file.
    """

    __FORMAT = 'cfg'
    __REGEX_MATCH_LINE = r'^\s*$'

    def __init__(self, configuration_file):
        """
            Initial constructor.

            :param configuration_file: Configuration file path.
            :type configuration_file: <str>
            :exceptions: None
        """
        BaseReadConfig.__init__(self)
        self.file_path = configuration_file

    def read_configuration(self):
        """
            Read configuration from file.

            :return: Configuration object | None.
            :rtype: <dict> | <NoneType>
            :exceptions: None
        """
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
