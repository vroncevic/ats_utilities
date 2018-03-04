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
    from ats_utilities.console_io.error import Error
    from ats_utilities.console_io.verbose import Verbose
    from ats_utilities.config.base_read_config import BaseReadConfig
    from ats_utilities.config.config_context_manager import ConfigFile
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n".format(e)
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
                __FORMAT - Format of configuration content
                __REGEX_MATCH_LINE - Regular expression for matching line
                VERBOSE - Console text indicator for current process-phase
            method:
                __init__ - Initial constructor
                read_configuration - Read configuration from file
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    __FORMAT = 'cfg'
    __REGEX_MATCH_LINE = r'^\s*$'
    VERBOSE = '[ATS_UTILITIES::CONFIG::CFG::CFG_TO_OBJECT]'

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
        ver = Verbose()
        if verbose:
            ver.message = 'Setting CFG interface'
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        super(Cfg2Object, self).__init__(verbose=verbose)
        self.set_file_path(file_path=configuration_file, verbose=verbose)

    def read_configuration(self, verbose=False):
        """
            Read configuration from file.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Configuration object | None
            :rtype: <dict> | <NoneType>
        """
        cls, cfg_path, content = self.__class__, self.get_file_path(), None
        ver, err, config = Verbose(), Error(), None
        if verbose:
            ver.message = "{0} {1}".format(
                'Read configuration from file', cfg_path
            )
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        try:
            with ConfigFile(cfg_path, 'r', cls.__FORMAT) as cfg_file:
                content = cfg_file.read()
        except (ATSTypeError, ATSBadCallError) as e:
            err.message = e
            msg = "{0} {1}".format(cls.VERBOSE, err.message)
            print(msg)
        else:
            if content:
                config, lines = {}, content.splitlines()
                for line in lines:
                    regex_match = match(cls.__REGEX_MATCH_LINE, line)
                    if not regex_match:
                        pairs = line.split('=')
                        config[pairs[0].strip()] = pairs[1].strip()
                if verbose:
                    ver.message = 'Done'
                    msg = "{0} {1}".format(cls.VERBOSE, ver.message)
                    print(msg)
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
        file_path = self.get_file_path()
        return "{0}(\'{1}\')".format(type(self).__name__, file_path)

