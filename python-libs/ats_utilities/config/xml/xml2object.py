# -*- coding: UTF-8 -*-
# xml2object.py
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
    from bs4 import BeautifulSoup

    from ats_utilities.console_io.error import ATSError
    from ats_utilities.console_io.verbose import ATSVerbose
    from ats_utilities.config.base_read_config import BaseReadConfig
    from ats_utilities.config.config_context_manager import ConfigFile
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
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


class Xml2Object(BaseReadConfig):
    """
        Define class Xml2Object with attribute(s) and method(s).
        Convert a xml configuration file (xml tags) to an object.
        It defines:
            attribute:
                __FORMAT - Format of configuration content
                VERBOSE - Console text indicator for current process-phase
            method:
                __init__ - Initial constructor
                read_configuration - Read a configuration from file
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    __FORMAT = 'xml'
    VERBOSE = '[ATS_UTILITIES::CONFIG::XML::XML_TO_OBJECT]'

    def __init__(self, configuration_file, verbose=False):
        """
            Setting configuration file path.
            :param configuration_file: Absolute configuration file path
            :type configuration_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func, status = self.__class__, stack()[0][3], False
        if configuration_file is None:
            txt = 'Argument: missing configuration_file <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSBadCallError(msg)
        if not isinstance(configuration_file, str):
            txt = 'Argument: expected configuration_file <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSTypeError(msg)
        if verbose:
            ver = ATSVerbose()
            ver.message = 'Setting XML interface'
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        super(Xml2Object, self).__init__()
        self.set_file_path(file_path=configuration_file)

    def read_configuration(self, verbose=False):
        """
            Read a configuration from file.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Configuration object | None
            :rtype: <BeautifulSoup> | <NoneType>
        """
        cls, content, config = self.__class__, None, None
        ver, err = ATSVerbose(), ATSError()
        xml_path = self.get_file_path()
        if verbose:
            ver.message = "{0} {1}".format(
                'Read configuration from file', xml_path
            )
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        try:
            with ConfigFile(xml_path, 'r', cls.__FORMAT) as xml_file:
                content = xml_file.read()
        except (ATSBadCallError, ATSTypeError) as e:
            err.message = e
            msg = "{0} {1}".format(cls.VERBOSE, err.message)
            print(msg)
        else:
            config = BeautifulSoup(content, cls.__FORMAT)
            if verbose:
                ver.message = 'Done'
                msg = "{0} {1}".format(cls.VERBOSE, ver.message)
                print(msg)
        return config

    def __str__(self):
        """
            Return human readable string (Xml2Object).
            :return: String representation of Xml2Object
            :rtype: <str>
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
            Return unambiguous string (Xml2Object).
            :return: String representation of Xml2Object
            :rtype: <str>
        """
        file_path = self.get_file_path()
        return "{0}(\'{1}\')".format(type(self).__name__, file_path)
