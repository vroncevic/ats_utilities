# -*- coding: utf-8 -*-
# file_checking.py
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
from os.path import exists, isfile, splitext

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
    from ats_utilities.exceptions.ats_file_error import ATSFileError
    from ats_utilities.console_io.error import Error
    from ats_utilities.console_io.verbose import Verbose
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


class FileChecking(object):
    """
        Define class FileChecking with attribute(s) and method(s).
        Operations with configuration files.
        It defines:
            attribute:
                __MODES - Mode file options
                VERBOSE - Console text indicator for current process-phase
                __file_path_ok -
                __file_extension_ok -
                __file_mode_ok -
            method:
                __init__ - Initial constructor
                check_file - Check configuration file path
                check_format - Check configuration file format by extension
                check_mode -  Checking operation mode for configuration file
    """

    __MODES = ['r', 'w', 'a', 'b', 'x', 't', '+']
    VERBOSE = '[ATS_UTILITIES::CONFIG::FILE_CHECKING]'

    def __init__(self, verbose=False):
        """
            Initial constructor.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = self.__class__
        if verbose:
            ver = Verbose()
            ver.message = "{0}".format('Initial file checking interface')
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        self.__file_path_ok = False
        self.__file_extension_ok = False
        self.__file_mode_ok = False

    def check_file(self, file_path, verbose=False):
        """
            Check configuration file path.
            :param file_path: Absolute configuration file path
            :type file_path: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (exist and regular file) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError | ATSFileError
        """
        cls, func, status = self.__class__, stack()[0][3], False
        if file_path is None:
            txt = 'Argument: missing file_path <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSBadCallError(msg)
        if not isinstance(file_path, str):
            txt = 'Argument: expected file_path <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSTypeError(msg)
        file_path_exist, file_path_regular = False, False
        ver, err = Verbose(), Error()
        if verbose:
            ver.message = "{0} {1}".format('Checking file', file_path)
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        try:
            file_path_exist = exists(file_path)
            file_path_regular = isfile(file_path)
            if not file_path_exist:
                msg = "{0} {1}".format('Check file', file_path)
                raise ATSFileError(msg)
            if not file_path_regular:
                msg = "{0} {1}".format('File is not regular', file_path)
                raise ATSFileError(msg)
            if file_path_exist and file_path_regular:
                self.__file_path_ok = True
        except ATSFileError as e:
            err.message = e
            msg = "{0} {1}".format(cls.VERBOSE, err.message)
            print(msg)
        status = all([file_path_exist, file_path_regular])
        return True if status else False

    def check_format(self, file_path, file_extension, verbose=False):
        """
            Check configuration file format by extension.
            :param file_path: Absolute configuration file path
            :type file_path: <str>
            :param file_extension: File format (file extension)
            :type file_extension: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (correct file format) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError | ATSFileError
        """
        cls, status, func = self.__class__, False, stack()[0][3]
        if file_path is None:
            txt = 'Argument: missing file_path <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSBadCallError(msg)
        if not isinstance(file_path, str):
            txt = 'Argument: expected file_path <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSTypeError(msg)
        if file_extension is None:
            txt = 'Argument: missing file_extension <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSBadCallError(msg)
        if not isinstance(file_extension, str):
            txt = 'Argument: expected file_extension <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSTypeError(msg)
        ver, err = Verbose(), Error()
        if verbose:
            ver.message = "{0} {1}".format('Checking file format', file_path)
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        try:
            extension = splitext(file_path)[-1].lower()
            status = extension == file_extension
            if not status:
                msg = "{0} [{1}] {2}".format(
                    'Not matched file extension', file_extension, file_path
                )
                raise ATSFileError(msg)
            else:
                self.__file_extension_ok = True
        except ATSFileError as e:
            err.message = e
            msg = "{0} {1}".format(cls.VERBOSE, err.message)
            print(msg)
        return True if status else False

    def check_mode(self, file_mode, verbose=False):
        """
            Checking operation mode for configuration file.
            :param file_mode: File mode ('r', 'w', 'a', 'b', 'x', 't', '+')
            :type file_mode: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (regular file mode) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError | ATSFileError
        """
        cls, split_mode = self.__class__, list(file_mode)
        status, func = False, stack()[0][3]
        if file_mode is None:
            txt = 'Argument: missing mode <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSBadCallError(msg)
        if not isinstance(file_mode, str):
            txt = 'Argument: expected mode <str> object'
            msg = "{0} {1} {2}".format(cls.VERBOSE, func, txt)
            raise ATSTypeError(msg)
        ver, err = Verbose(), Error()
        if verbose:
            ver.message = "{0}".format('Checking operation mode')
            msg = "{0} {1}".format(cls.VERBOSE, ver.message)
            print(msg)
        try:
            for item_mode in split_mode:
                if item_mode not in cls.__MODES:
                    msg = "{0} [{1}]".format('Not supported mode', file_mode)
                    raise ATSValueError(msg)
        except ATSValueError as e:
            err.message = e
            msg = "{0} {1}".format(cls.VERBOSE, err.message)
            print(msg)
        else:
            self.__file_mode_ok = True
            status = True
        return True if status else False

    def is_file_ok(self):
        """
            Return final status of file.
            :return: True (correct file) | False
            :rtype: <bool>
        """
        status = all([
            self.__file_path_ok, self.__file_extension_ok, self.__file_mode_ok
        ])
        return True if status else False

