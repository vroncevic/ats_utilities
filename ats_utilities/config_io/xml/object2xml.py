# -*- coding: UTF-8 -*-

"""
 Module
     object2xml.py
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
     Define class Object2Xml with attribute(s) and method(s).
     Convert a configuration object to a xml format and write to file.
"""

import sys

try:
    from ats_utilities.config_io import ConfigFile
    from ats_utilities.config_io.base_write import BaseWriteConfig
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Object2Xml(BaseWriteConfig):
    """
        Define class Object2Xml with attribute(s) and method(s).
        Convert a configuration object to a xml format and write to file.
        It defines:

            :attributes:
                | __FORMAT - Format of configuration content
            :methods:
                | __init__ - Initial constructor.
                | write_configuration - Write configuration to a xml file.
    """

    __FORMAT = 'xml'

    def __init__(self, configuration_file):
        """
            Initial constructor.

            :param configuration_file: Configuration file path.
            :type configuration_file: <str>
            :exceptions: None
        """
        BaseWriteConfig.__init__(self)
        self.file_path = configuration_file

    def write_configuration(self, configuration):
        """
            Write configuration to a xml file.

            :param configuration: Configuration object.
            :type: <BeautifulSoup>
            :return: True (success) | False.
            :rtype: <bool>
            :exception: None
        """
        status = False
        if configuration is None:
            return status
        with ConfigFile(self.file_path, 'w', Object2Xml.__FORMAT) as xml:
            if bool(xml):
                xml.write("{0}".format(configuration))
                status = True
        return True if status else False
