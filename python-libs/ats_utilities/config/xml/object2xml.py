# -*- coding: UTF-8 -*-
# object2xml.py
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
from inspect import stack

try:
    from ats_utilities.config.base_write_config import BaseWriteConfig
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config.config_context_manager import ConfigFile
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Object2Xml(BaseWriteConfig):
    """
        Define class Object2Xml with attribute(s) and method(s).
        Convert a configuration object to a xml format and write to file.
        It defines:
            attribute:
                __FORMAT - Format of configuration content
                VERBOSE - Console text indicator for current process-phase
            method:
                __init__ - Initial constructor
                write_configuration - Write configuration to a xml file
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    __FORMAT = 'xml'
    VERBOSE = 'ATS_UTILITIES::CONFIG::XML::OBJECT_TO_XML'

    def __init__(self, configuration_file, verbose=False):
        """
            Setting configuration file path.
            :param configuration_file: Absolute configuration file path
            :type configuration_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func, status = Object2Xml, stack()[0][3], False
        cfg_file_txt = 'Argument: expected configuration_file <str> object'
        cfg_file_msg = "{0} {1} {2}".format(cls.VERBOSE, func, cfg_file_txt)
        if configuration_file is None or not configuration_file:
            raise ATSBadCallError(cfg_file_msg)
        if not isinstance(configuration_file, str):
            raise ATSTypeError(cfg_file_msg)
        verbose_message(cls.VERBOSE, verbose, 'Setting XML interface')
        super(Object2Xml, self).__init__()
        self.set_file_path(file_path=configuration_file)

    def write_configuration(self, configuration, verbose=False):
        """
            Write configuration to a xml file.
            :param configuration: Configuration object
            :type: <BeautifulSoup>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exception: ATSBadCallError
        """
        cls, func, status = Object2Xml, stack()[0][3], False
        cfg_txt = 'Argument: expected configuration <Python> object'
        cfg_msg = "{0} {1} {2}".format(cls.VERBOSE, func, cfg_txt)
        if configuration is None or not configuration:
            raise ATSBadCallError(cfg_msg)
        xml_path = self.get_file_path()
        verbose_message(
            cls.VERBOSE, verbose, 'Write configuration to file', xml_path
        )
        with ConfigFile(xml_path, 'w', cls.__FORMAT) as xml_file:
            xml_file.write("{0}".format(configuration))
            status = True
        verbose_message(cls.VERBOSE, verbose, 'Done')
        return True if status else False

    def __str__(self):
        """
            Return human readable string (Object2Xml).
            :return: String representation of Object2Xml
            :rtype: <str>
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
            Return unambiguous string (Object2Xml).
            :return: String representation of Object2Xml
            :rtype: <str>
        """
        cls, file_path = Object2Xml, self.get_file_path()
        return "{0}(\'{1}\')".format(cls.__name__, file_path)
