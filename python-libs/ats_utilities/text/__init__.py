# -*- coding: UTF-8 -*-
# __init__.py
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

try:
    from ats_utilities.text.stdout_text import ATS_PROCESS
    from ats_utilities.text.info_decorator import info
    from ats_utilities.text.verbose_decorator import verbose
    from ats_utilities.text.error_decorator import error
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


class COut(object):
    """
    Define class COut with attribute(s) and method(s).
    Define class with interface for print to console mechanism.
    It defines:
        attribute:
            __ATS_PHASE_PROCESS - Phase process name
            __VERBOSE - Verbose key for kwargs
            __ERROR - Error key for kwargs
        method:
            __init__ - Initial constructor
            set_ats_phase_process - Setting ATS phase process
            get_ats_phase_process - Getting ATS phase process
            print_info_msg - Print info message to console
            print_verbose_msg - Print verbose message to console
            print_error_msg - Print error message to console
            print_console_msg - Print console message
    """

    __ATS_PHASE_PROCESS = None
    __VERBOSE = 'verbose'
    __ERROR = 'error'

    def set_ats_phase_process(self, phase_process):
        """
        Setting ATS phase process.
        :param phase_process: Phase process name
        :type phase_process: <str>
        """
        cls = self.__class__
        cls.__ATS_PHASE_PROCESS = phase_process

    def get_ats_phase_process(self):
        """
        Getting ATS phase process name.
        :return: Phase process name | None
        :rtype: <str> | <NoneType>
        """
        cls = self.__class__
        return cls.__ATS_PHASE_PROCESS

    @staticmethod
    @info
    def print_info_msg(*args, **kwargs):
        """
        Print info message to console.
        :param args: List of arguments (objects)
        :type args: <list>
        :param kwargs: Arguments in shape of dictionary
        :type kwargs: <dict>
        """
        pass

    @staticmethod
    @verbose
    def print_verbose_msg(*args, **kwargs):
        """
        Print verbose message to console.
        :param args: List of arguments (objects)
        :type args: <list>
        :param kwargs: Arguments in shape of dictionary
        :type kwargs: <dict>
        """
        pass

    @staticmethod
    @error
    def print_error_msg(*args, **kwargs):
        """
        Print error message to console.
        :param args: List of arguments (objects)
        :type args: <list>
        :param kwargs: Arguments in shape of dictionary
        :type kwargs: <dict>
        """
        pass

    @staticmethod
    def print_console_msg(*args, **kwargs):
        """
        Print console message.
        :param args: List of arguments (objects)
        :type args: <list>
        :param kwargs: Arguments in shape of dictionary
        :type kwargs: <dict>
        """
        # Setting ATS phase process
        kwargs[ATS_PROCESS] = COut.__ATS_PHASE_PROCESS
        if COut.__VERBOSE in kwargs.keys():
            for arg_key, arg_val in kwargs.items():
                if arg_key == COut.__VERBOSE and arg_val:
                    COut.print_verbose_msg(*args, **kwargs)
        elif COut.__ERROR in kwargs.keys():
            for arg_key, arg_val in kwargs.items():
                if arg_key == COut.__ERROR and arg_val:
                    COut.print_error_msg(*args, **kwargs)
        else:
            COut.print_info_msg(*args, **kwargs)
