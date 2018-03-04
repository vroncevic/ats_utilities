# -*- coding: UTF-8 -*-
# json_base.py
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
from abc import ABCMeta, abstractmethod

try:
    from ats_utilities.console_io.verbose import Verbose
    from ats_utilities.console_io.error import Error
    from ats_utilities.ats_info import ATSInfo
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
    from ats_utilities.json_settings import JsonSettings
    from ats_utilities.option.ats_option_parser import ATSOptionParser
    from ats_utilities.config.check_base_config import CheckBaseConfig
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


class JsonBase(ATSInfo, JsonSettings, ATSOptionParser):
    """
        Define class JsonBase with attribute(s) and method(s).
        Load a settings, create a CL interface and run operation.
        It defines:
            attribute:
                VERBOSE - Console text indicator for current process-phase
                __tool_operational - Control operational flag
            method:
                __init__ - Initial constructor
                add_new_option - Adding new option for CL interface
                get_tool_status - Getting tool status
                set_tool_status - Setting tool status
                process - Process and run tool operation (Abstract method)
                __str__ - Dunder (magic) method
                __repr__ - Dunder (magic) method
    """

    __metaclass__ = ABCMeta
    VERBOSE = '[ATS_UTILITIES::JSON_BASE]'

    def __init__(self, base_config_file, verbose=False):
        """
            Setting version, build date, name and license of App/Tool/Script.
            :param base_config_file: Configuration file path
            :type base_config_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls, ver, err = self.__class__, Verbose(), Error()
        if verbose:
            ver.message = "{0}".format('Initial CFG settings')
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        self.__tool_operational = False  # App/Tool/Script not operative
        JsonSettings.__init__(self, base_config_file, verbose=verbose)
        configuration = self.read_configuration(verbose=verbose)
        check_configuration = CheckBaseConfig.is_correct(
            configuration, verbose=verbose
        )
        if configuration and check_configuration:
            try:
                ATSInfo.__init__(self, configuration, verbose=verbose)
            except (ATSBadCallError, ATSTypeError) as e:
                err.message = e
                msg = "{0} {1}".format(cls.VERBOSE, err.message)
                print(msg)
            else:
                statuses = []
                tool_version = self.get_ats_version()
                statuses.append(tool_version)
                tool_build_date = self.get_ats_build_date()
                statuses.append(tool_build_date)
                tool_name = self.get_ats_name()
                statuses.append(tool_name)
                tool_lic = self.get_ats_license()
                statuses.append(tool_lic)
                if all(status for status in statuses):
                    tool_info = "{0} {1}".format(tool_version, tool_build_date)
                    ATSOptionParser.__init__(
                        self, tool_info, tool_name, tool_lic, verbose=verbose
                    )
                    self.__tool_operational = True  # App/Tool/Script operative

    def add_new_option(self, *args, **kwargs):
        """
            Adding new option for CL interface.
            :param args: List of arguments (objects)
            :type args: <list>
            :param kwargs: Arguments in shape of dictionary
            :type kwargs: <dict>
        """
        self.add_operation(*args, **kwargs)

    def get_tool_status(self, verbose=False):
        """
            Getting tool status.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (tool ready) | False
            :rtype: <bool>
        """
        return self.__tool_operational

    def set_tool_status(self, tool_status, verbose=False):
        """
            Setting tool status.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :param tool_status: True (tool ready) | False
            :type tool_status: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func, ver = self.__class__, stack()[0][3], Verbose()
        if tool_status is None:
            txt = 'Argument: missing tool_status <bool> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSBadCallError(msg)
        if not isinstance(tool_status, bool):
            txt = 'Argument: expected tool_status <bool> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSTypeError(msg)
        if verbose:
            if status:
                ver.message = "{0}".format('Set tool operative')
            else:
                ver.message = "{0}".format('Set tool not operative')
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        self.__tool_operational = tool_status

    @abstractmethod
    def process(self, verbose=False):
        """
            Process and run tool operation (Abstract method).
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        pass

    def __str__(self):
        """
            Return human readable string (JsonBase).
            :return: String representation of JsonBase
            :rtype: <str>
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
            Return unambiguous string (JsonBase).
            :return: String representation of JsonBase
            :rtype: <str>
        """
        file_path = self.get_file_path()
        return "{0}(\'{1}\')".format(type(self).__name__, file_path)
