# -*- coding: UTF-8 -*-

"""
 Module
     yaml2object.py
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
     Define class Yaml2Object with attribute(s) and method(s).
     Convert a yaml configuration file to an object.
"""

import sys

try:
    from yaml import load
    from ats_utilities.config_io import ConfigFile
    from ats_utilities.config_io.base_read import BaseReadConfig
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.3.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Yaml2Object(BaseReadConfig):
    """
        Define class Yaml2Object with attribute(s) and method(s).
        Convert a yaml configuration file to an object.
        It defines:

            :attributes:
                | __FORMAT - Format of configuration content.
            :methods:
                | __init__ - Initial constructor.
                | get_configuration - Getting a configuration from file.
    """

    __FORMAT = 'yaml'

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
            Getting a configuration from file.

            :return: Configuration object | None.
            :rtype: <Python object(s)> | <NoneType>
            :exceptions: None
        """
        config = None
        with ConfigFile(self.file_path, 'r', Yaml2Object.__FORMAT) as yaml:
            if bool(yaml):
                config = load(yaml)
        return config
