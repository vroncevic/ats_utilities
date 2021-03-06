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
from inspect import stack
from re import match

try:
    from ats_utilities.config.base_read_config import BaseReadConfig
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


class Cfg2Object(BaseReadConfig):
    """
        Define class Cfg2Object with attribute(s) and method(s).
        Convert configuration from a cfg file to an object.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __FORMAT - Format of configuration content
                | __REGEX_MATCH_LINE - Regular expression for matching line
            :methods:
                | __init__ - Initial constructor
                | read_configuration - Read configuration from file
    """

    __slots__ = ('VERBOSE', '__FORMAT', '__REGEX_MATCH_LINE')
    VERBOSE = 'ATS_UTILITIES::CONFIG::CFG::CFG_TO_OBJECT'
    __FORMAT = 'cfg'
    __REGEX_MATCH_LINE = r'^\s*$'

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
        verbose_message(Cfg2Object.VERBOSE, verbose, 'Setting CFG interface')
        BaseReadConfig.__init__(self)
        self.file_path = configuration_file

    def read_configuration(self, verbose=False):
        """
            Read configuration from file.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Configuration object | None
            :rtype: <dict> | <NoneType>
            :exceptions: None
        """
        config = None
        verbose_message(
            Cfg2Object.VERBOSE, verbose,
            'Read configuration from file', self.file_path
        )
        try:
            with ConfigFile(self.file_path, 'r', Cfg2Object.__FORMAT) as cfg:
                if bool(cfg):
                    content = cfg.read()
                    config, lines = {}, content.splitlines()
                    for line in lines:
                        regex_match = match(Cfg2Object.__REGEX_MATCH_LINE, line)
                        if not regex_match:
                            pairs = line.split('=')
                            config[pairs[0].strip()] = pairs[1].strip()
            verbose_message(Cfg2Object.VERBOSE, verbose, 'Done')
        except AttributeError:
            pass
        return config
