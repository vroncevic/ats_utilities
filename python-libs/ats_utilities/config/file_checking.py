# encoding: utf-8

from os.path import exists, isfile, splitext

from ats_utilities.error.ats_file_error import ATSFileError
from ats_utilities.text.stdout_text import DBG, ERR, RST

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class FileChecking(object):
    """
    Define class FileChecking with attribute(s) and method(s).
    File can contain config in next formats:
        XML  -  Configuration described by Extensible Markup Language.
        INI  -  Configuration described by basic structure composed of sections,
                properties, and values.
        CFG  -  Configuration described by keys and values.
        YAML -  Configuration described by basic structure composed of sections,
                properties, and values.
        JSON -  Configuration described by basic structure composed of sections,
                properties, and values.
    It defines:
        attribute:
            __MODES - Mode options
            VERBOSE - Verbose prefix console text
        method:
            check_file - Check configuration file path
            check_format - Check configuration file format by extension
            check_mode -  Checking operation mode for configuration file
    """

    __MODES = ['r', 'w', 'a', 'b', 'x', 't', '+']
    VERBOSE = '[FILE_CONFIG]'

    @classmethod
    def check_file(cls, file_path, verbose=False):
        """
        Check config file path.
        :param file_path: Absolute config file path
        :type: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: True (exist and regular) | False
        :rtype: bool
        """
        if verbose:
            msg = "{0} {1}{2} \n{3}{4}".format(
                cls.VERBOSE, DBG, 'Checking configuration file', file_path, RST
            )
            print(msg)
        file_path_exist, file_path_regular = False, False
        try:
            file_path_exist = exists(file_path)
            file_path_regular = isfile(file_path)
            if not file_path_exist:
                msg = "{0} {1}{2}\n{3}{4}".format(
                    cls.VERBOSE, ERR, 'File does not exist', file_path, RST
                )
                raise ATSFileError(msg)
            elif not file_path_regular:
                msg = "{0} {1}{2}\n{3}{4}".format(
                    cls.VERBOSE, ERR, 'File is not regular', file_path, RST
                )
                raise ATSFileError(msg)
        except ATSFileError as e:
            print(e)
        return True if file_path_exist and file_path_regular else False

    @classmethod
    def check_format(cls, file_path, file_extension, verbose=False):
        """
        Check config file format by extension.
        :param file_path: Absolute config file path
        :type: str
        :param file_extension: File format (file extension)
        :type: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: Boolean status
        :rtype: bool
        """
        if verbose:
            msg = "{0} {1}{2}\n{3}{4}".format(
                cls.VERBOSE, DBG, 'Checking file extension', file_path, RST
            )
            print(msg)
        status = False
        try:
            ext = splitext(file_path)[-1].lower()
            status = ext == file_extension
            if not status:
                msg = "{0} {1}{2} [{3}]\n{4}{5}".format(
                    cls.VERBOSE, ERR, 'Not matched file extension',
                    file_extension, file_path, RST
                )
                raise ATSFileError(msg)
        except ATSFileError as e:
            print(e)
        return True if status else False

    @classmethod
    def check_mode(cls, mode, verbose=False):
        """
        Checking operation mode for configuration file.
        :param mode: File mode
        :type mode: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: True (regular mode) | False
        :rtype: bool
        """
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Checking operation mode', RST
            )
            print(msg)
        split_mode = list(mode)
        for item_mode in split_mode:
            if item_mode not in cls.__MODES:
                if verbose:
                    msg = "{0} {1}{2} [{3}]{4}".format(
                        cls.VERBOSE, ERR, 'Not supported mode', mode, RST
                    )
                    print(msg)
                return False
        if verbose:
            msg = "{0} {1}{2}{3}".format(
                cls.VERBOSE, DBG, 'Operation mode supported', RST
            )
            print(msg)
        return True
