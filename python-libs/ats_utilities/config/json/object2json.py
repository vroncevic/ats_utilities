# -*- coding: UTF-8 -*-

"""
 Module
     object2json.py
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
     Define class Object2Json with attribute(s) and method(s).
     Convert a configuration object to a json format and write to file.
"""

import sys
from inspect import stack
from json import dump

try:
    from ats_utilities.config.base_write_config import BaseWriteConfig
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config.config_context_manager import ConfigFile
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Object2Json(BaseWriteConfig):
    """
        Define class Object2Json with attribute(s) and method(s).
        Convert a configuration object to a json format and write to file.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __FORMAT - Format of configuration content
            :methods:
                | __init__ - Initial constructor
                | write_configuration - Write configuration to a json file
    """

    __slots__ = ('VERBOSE', '__FORMAT')
    VERBOSE = 'ATS_UTILITIES::CONFIG::JSON::OBJECT_TO_JSON'
    __FORMAT = 'json'

    def __init__(self, configuration_file, verbose=False):
        """
            Setting configuration file path.

            :param configuration_file: Absolute configuration file path
            :type configuration_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        cfg_file_txt = 'Argument: expected configuration_file <str> object'
        cfg_file_msg = "{0} {1} {2}".format('def', func, cfg_file_txt)
        if configuration_file is None or not configuration_file:
            raise ATSBadCallError(cfg_file_msg)
        if not isinstance(configuration_file, str):
            raise ATSTypeError(cfg_file_msg)
        verbose_message(Object2Json.VERBOSE, verbose, 'Setting JSON interface')
        BaseWriteConfig.__init__(self)
        self.file_path = configuration_file

    def write_configuration(self, configuration, verbose=False):
        """
            Write configuration to a json file.

            :param configuration: Configuration object
            :type: <Python object(s)>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exception: ATSBadCallError
        """
        func, status = stack()[0][3], False
        cfg_txt = 'Argument: expected configuration <Python> object'
        cfg_msg = "{0} {1} {2}".format('def', func, cfg_txt)
        if configuration is None or not configuration:
            raise ATSBadCallError(cfg_msg)
        verbose_message(
            Object2Json.VERBOSE, verbose,
            'Write configuration to file', self.file_path
        )
        with ConfigFile(self.file_path, 'w', Object2Json.__FORMAT) as json:
            if bool(json):
                dump(configuration, json)
                status = True
        verbose_message(Object2Json.VERBOSE, verbose, 'Done')
        return True if status else False
