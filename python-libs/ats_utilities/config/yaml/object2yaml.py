# -*- coding: UTF-8 -*-
# object2yaml.py
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
    from yaml import dump

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


class Object2Yaml(BaseWriteConfig):
    """
        Define class Object2Yaml with attribute(s) and method(s).
        Convert a configuration object to a yaml format and write to file.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __FORMAT - Format of configuration content
            method:
                __init__ - Initial constructor
                write_configuration - Write configuration to a yaml file
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    __slots__ = (
        'VERBOSE', '__FORMAT'  # Read-Only
    )
    VERBOSE = 'ATS_UTILITIES::CONFIG::YAML::OBJECT_TO_YAML'
    __FORMAT = 'yaml'

    def __init__(self, configuration_file, verbose=False):
        """
            Setting configuration file path.
            :param configuration_file: Absolute configuration file path
            :type configuration_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func = Object2Yaml, stack()[0][3]
        cfg_file_txt = 'Argument: expected configuration_file <str> object'
        cfg_file_msg = "{0} {1} {2}".format('def', func, cfg_file_txt)
        if configuration_file is None or not configuration_file:
            raise ATSBadCallError(cfg_file_msg)
        if not isinstance(configuration_file, str):
            raise ATSTypeError(cfg_file_msg)
        verbose_message(cls.VERBOSE, verbose, 'Setting YAML interface')
        super(Object2Yaml, self).__init__()
        self.set_file_path(file_path=configuration_file)

    def write_configuration(self, configuration, verbose=False):
        """
            Write configuration to a yaml file.
            :param configuration: Configuration object
            :type configuration: <Python object(s)>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exception: ATSBadCallError
        """
        cls, func, status = Object2Yaml, stack()[0][3], False
        cfg_txt = 'Argument: expected configuration <Python> object'
        cfg_msg = "{0} {1} {2}".format('def', func, cfg_txt)
        if configuration is None or not configuration:
            raise ATSBadCallError(cfg_msg)
        yaml_path = self.get_file_path()
        verbose_message(
            cls.VERBOSE, verbose, 'Write configuration to file', yaml_path
        )
        with ConfigFile(yaml_path, 'w', cls.__FORMAT) as yaml_file:
            dump(configuration, yaml_file, default_flow_style=False)
            status = True
        verbose_message(cls.VERBOSE, verbose, 'Done')
        return True if status else False

    def __str__(self):
        """
            Return human readable string (Object2Yaml).
            :return: String representation of Object2Yaml
            :rtype: <str>
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
            Return unambiguous string (Object2Yaml).
            :return: String representation of Object2Yaml
            :rtype: <str>
        """
        cls, file_path = Object2Yaml, self.get_file_path()
        return "{0}(\'{1}\')".format(cls.__name__, file_path)
