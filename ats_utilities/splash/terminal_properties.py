# -*- coding: UTF-8 -*-

'''
 Module
     terminal_properties.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class TerminalProperties with attribute(s) and method(s).
     Defined API for getting terminal properties.
'''

import sys
from os import open, close, ctermid, O_RDONLY
from fcntl import ioctl
from termios import TIOCGWINSZ
from struct import unpack

try:
    from six import add_metaclass
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(VerboseRoot)
class TerminalProperties:
    '''
        Defined class TerminalProperties with attribute(s) and method(s).
        Defined API for getting terminal properties.
        It defines:

            :attributes:
                | __verbose - enable/disable verbose option.
                | __window_size - terminal window size.
            :methods:
                | __init__ - initial constructor.
                | __ioctl_get_window_size - size for descriptor.
                | __ioctl_for_all_descriptors - size for all descriptors.
                | size - getting size of terminal window.
                | __str__ - dunder method for TerminalProperties.
    '''

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__verbose = verbose
        self.__window_size = None
        verbose_message(
            TerminalProperties.VERBOSE, self.__verbose or verbose,
            'init terminal properties'
        )

    def __ioctl_get_window_size(self, file_descriptor, verbose=False):
        '''
            Check window size for descriptor.

            :param file_descriptor: file descriptor.
            :type file_descriptor: <int>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: window size of terminal.
            :rtype: <tupple>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('int:file_descriptor', file_descriptor)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        try:
            self.__window_size = unpack('hh', ioctl(
                file_descriptor, TIOCGWINSZ, '1234')
            )
        except:
            pass
        verbose_message(
            TerminalProperties.VERBOSE, self.__verbose or verbose,
            'terminal window size', self.__window_size
        )
        return self.__window_size

    def __ioctl_for_all_descriptors(self, verbose=False):
        '''
            Check window size for all descriptors.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: status true window size checked else false.
            :rtype: <bool>
            :exceptions: None
        '''
        std_in = self.__ioctl_get_window_size(0)
        std_out = self.__ioctl_get_window_size(1)
        std_err = self.__ioctl_get_window_size(2)
        self.__window_size = std_in or std_out or std_err
        verbose_message(
            TerminalProperties.VERBOSE, self.__verbose or verbose,
            'terminal window size', self.__window_size
        )
        return bool(self.__window_size)

    def size(self, verbose=False):
        '''
            Center console line.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: window size | None.
            :rtype: <tuple> | <NoneType>
            :exceptions: None
        '''
        checked_size = self.__ioctl_for_all_descriptors()
        if not checked_size:
            try:
                file_descriptor = open(ctermid(), O_RDONLY)
                checked_size = self.__ioctl_get_window_size(
                    file_descriptor
                )
                close(file_descriptor)
                if not checked_size:
                    error_message(
                        TerminalProperties.VERBOSE,
                        'failed to check terminal window size'
                    )
            except:
                pass
        verbose_message(
            TerminalProperties.VERBOSE, self.__verbose or verbose,
            'terminal window size', self.__window_size
        )
        return self.__window_size

    def __str__(self):
        '''
            Dunder str method for TerminalProperties.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__verbose),
            str(self.__window_size)
        )
