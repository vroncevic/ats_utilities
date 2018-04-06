# -*- coding: UTF-8 -*-
# json2object.py
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
from json import load

try:
    from ats_utilities.config.base_read_config import BaseReadConfig
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


class Json2Object(BaseReadConfig):
    """
        Define class Json2Object with attribute(s) and method(s).
        Convert a configuration from json file to an object config.
        It defines:
            attribute:
                __FORMAT - Format of configuration content
                VERBOSE - Console text indicator for current process-phase
            method:
                __init__ - Initial constructor
                read_configuration - Read configuration from file
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    __FORMAT = 'json'
    VERBOSE = 'ATS_UTILITIES::CONFIG::JSON::JSON_TO_OBJECT'

    def __init__(self, configuration_file, verbose=False):
        """
            Setting configuration file path.
            :param configuration_file: Absolute configuration file path
            :type configuration_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func, status = Json2Object, stack()[0][3], False
        cfg_file_txt = 'Argument: expected configuration_file <str> object'
        cfg_file_msg = "{0} {1} {2}".format('def', func, cfg_file_txt)
        if configuration_file is None or not configuration_file:
            raise ATSBadCallError(cfg_file_msg)
        if not isinstance(configuration_file, str):
            raise ATSTypeError(cfg_file_msg)
        verbose_message(cls.VERBOSE, verbose, 'Setting JSON interface')
        super(Json2Object, self).__init__()
        self.set_file_path(file_path=configuration_file)

    def read_configuration(self, verbose=False):
        """
            Read configuration from file.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Configuration object | None
            :rtype: <Python object(s)> | <NoneType>
        """
        cls, content = Json2Object, None
        json_path = self.get_file_path()
        verbose_message(
            cls.VERBOSE, verbose, 'Read configuration from file', json_path
        )
        with ConfigFile(json_path, 'r', cls.__FORMAT) as json_file:
            content = load(json_file)
        verbose_message(cls.VERBOSE, verbose, 'Done')
        return content

    def __str__(self):
        """
            Return human readable string (Json2Object).
            :return: String representation of Json2Object
            :rtype: <str>
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
            Return unambiguous string (Json2Object).
            :return: String representation of Json2Object
            :rtype: <str>
        """
        cls, file_path = Json2Object, self.get_file_path()
        return "{0}(\'{1}\')".format(cls.__name__, file_path)
