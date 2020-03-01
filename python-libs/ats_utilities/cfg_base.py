# -*- coding: UTF-8 -*-

"""
 Module
     cfg_base.py
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
     Define class CfgBase with attribute(s) and method(s).
     Load a settings, info and run operation.
"""

import sys
from inspect import stack

try:
    from ats_utilities.ats_info import ATSInfo
    from ats_utilities.config.cfg.cfg2object import Cfg2Object
    from ats_utilities.config.cfg.object2cfg import Object2Cfg
    from ats_utilities.option.ats_option_parser import ATSOptionParser
    from ats_utilities.abstract import abstract_method
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE) # Force close python ATS ###############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CfgBase(ATSInfo):
    """
        Define class CfgBase with attribute(s) and method(s).
        Load a settings, info and run operation.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __tool_operational - Control operational flag
                __cfg2obj - In API for configuration
                __obj2cfg - Out API for configuration
                __option_parser - Option parser
            method:
                __init__ - Initial constructor
                add_new_option - Adding new option
                parse_args - Parse arguments
                tool_status - Getting/Setting tool status
                process - Process and run tool operation (Abstract method)
    """

    __slots__ = (
        'VERBOSE',
        '__tool_operational',
        '__cfg2obj',
        '__obj2cfg',
        '__option_parser'
    )
    VERBOSE = 'ATS_UTILITIES::CFG_BASE'

    def __init__(self, base_config_file, verbose=False):
        """
            Setting version, build date, name and license of App/Tool/Script.
            :param base_config_file: Configuration file path
            :type base_config_file: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        configuration = None
        verbose_message(CfgBase.VERBOSE, verbose, 'Initial ATS base settings')
        self.__tool_operational = False # App/Tool/Script not operative
        self.__cfg2obj = Cfg2Object(base_config_file, verbose=verbose)
        self.__obj2cfg = Object2Cfg(base_config_file, verbose=verbose)
        if all([self.__cfg2obj, self.__obj2cfg]):
            configuration = self.__cfg2obj.read_configuration(verbose=verbose)
        if configuration:
            ATSInfo.__init__(self, configuration, verbose=verbose)
            if self.is_ats_info_ok():
                tool_info = "{0} {1}".format(self.name, self.build_date)
                self.__option_parser = ATSOptionParser(
                    tool_info, self.version, self.license, verbose=verbose
                )
                self.__tool_operational = True # App/Tool/Script operative

    def add_new_option(self, *args, **kwargs):
        """
            Adding new option.
            :param args: List of arguments (objects)
            :type args: <list>
            :param kwargs: Arguments in shape of dictionary
            :type kwargs: <dict>
            :exceptions: None
        """
        self.__option_parser.add_operation(*args, **kwargs)

    def parse_args(self, argv):
        """
            Process arguments from start.
            :param argv: Arguments
            :type argv: <Python object(s)>
            :return: Options and arguments
            :rtype: <Python object(s)>
            :exceptions: None
        """
        (opts, args) = self.__option_parser.parse_args(argv)
        return opts, args

    @property
    def tool_status(self):
        """
            Getting tool status.
            :return: True (tool ready) | False
            :rtype: <bool>
            :exceptions: None
        """
        return self.__tool_operational

    @tool_status.setter
    def tool_status(self, tool_status):
        """
            Setting tool status.
            :param tool_status: Tool status (boolean)
            :type tool_status: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        tool_status_txt = 'Argument: expected tool_status <bool> object'
        tool_status_msg = "{0} {1} {2}".format('def', func, tool_status_txt)
        if tool_status is None:
            raise ATSBadCallError(tool_status_msg)
        if not isinstance(tool_status, bool):
            raise ATSTypeError(tool_status_msg)
        self.__tool_operational = tool_status

    @abstract_method
    def process(self, verbose=False):
        """
            Process and run tool operation (Abstract method).
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exception: NotImplementedError
        """
        pass
