# -*- coding: UTF-8 -*-

"""
 Module
     xml2object.py
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
     Define class Xml2Object with attribute(s) and method(s).
     Convert a xml configuration file (xml tags) to an object.
"""

import sys

try:
    from bs4 import BeautifulSoup
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


class Xml2Object(BaseReadConfig):
    """
        Define class Xml2Object with attribute(s) and method(s).
        Convert a xml configuration file (xml tags) to an object.
        It defines:

            :attributes:
                | __FORMAT - Format of configuration content.
            :methods:
                | __init__ - Initial constructor.
                | read_configuration - Read a configuration from file
    """

    __FORMAT = 'xml'

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
            Read a configuration from file.

            :return: Configuration object | None.
            :rtype: <BeautifulSoup> | <NoneType>
            :exceptions: None
        """
        content, config = None, None
        try:
            with ConfigFile(self.file_path, 'r', Xml2Object.__FORMAT) as xml:
                if bool(xml):
                    content = xml.read()
                    config = BeautifulSoup(content, Xml2Object.__FORMAT)
        except AttributeError:
            pass
        return config
