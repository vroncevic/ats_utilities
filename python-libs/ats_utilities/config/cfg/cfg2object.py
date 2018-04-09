# -*- coding: UTF-8 -*-
# cfg2object.py
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
from re import match

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


class Cfg2Object(BaseReadConfig):
    """
        Define class Cfg2Object with attribute(s) and method(s).
        Convert configuration from a cfg file to an object.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __FORMAT - Format of configuration content
                __REGEX_MATCH_LINE - Regular expression for matching line
            method:
                __init__ - Initial constructor
                read_configuration - Read configuration from file
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    __slots__ = (
        'VERBOSE', '__FORMAT', '__REGEX_MATCH_LINE'  # Read-Only
    )
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
        cls, func = Cfg2Object, stack()[0][3]
        cfg_file_txt = 'Argument: expected configuration_file <str> object'
        cfg_file_msg = "{0} {1} {2}".format('def', func, cfg_file_txt)
        if configuration_file is None or not configuration_file:
            raise ATSBadCallError(cfg_file_msg)
        if not isinstance(configuration_file, str):
            raise ATSTypeError(cfg_file_msg)
        verbose_message(cls.VERBOSE, verbose, 'Setting CFG interface')
        super(Cfg2Object, self).__init__()
        self.set_file_path(file_path=configuration_file)

    def read_configuration(self, verbose=False):
        """
            Read configuration from file.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Configuration object | None
            :rtype: <dict> | <NoneType>
        """
        cls, cfg_path, config = Cfg2Object, self.get_file_path(), None
        verbose_message(
            cls.VERBOSE, verbose, 'Read configuration from file', cfg_path
        )
        try:
            with ConfigFile(cfg_path, 'r', cls.__FORMAT) as cfg_file:
                content = cfg_file.read()
                config, lines = {}, content.splitlines()
                for line in lines:
                    regex_match = match(cls.__REGEX_MATCH_LINE, line)
                    if not regex_match:
                        pairs = line.split('=')
                        config[pairs[0].strip()] = pairs[1].strip()
            verbose_message(cls.VERBOSE, verbose, 'Done')
        except AttributeError:
            pass
        return config

    def __str__(self):
        """
            Return human readable string (Cfg2Object).
            :return: String representation of Cfg2Object
            :rtype: <str>
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
            Return unambiguous string (Cfg2Object).
            :return: String representation of Cfg2Object
            :rtype: <str>
        """
        cls, file_path = Cfg2Object, self.get_file_path()
        return "{0}(\'{1}\')".format(cls.__name__, file_path)
