# encoding: utf-8

from os.path import exists, isfile, splitext

from ats_utilities.error.ats_file_error import ATSFileError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class FileConfig(object):
    """
    Define class FileConfig with attribute(s) and method(s).
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
            VERBOSE - Verbose prefix text
        method:
            check_file - Check configuration file path
            check_format - Check configuration file format by extension
    """

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
            msg = "{0} {1} \n{2}".format(
                FileConfig.VERBOSE, 'checking file', file_path
            )
            print(msg)
        file_path_exist, file_path_regular = False, False
        try:
            file_path_exist = exists(file_path)
            file_path_regular = isfile(file_path)
            if not file_path_exist:
                msg = "{0} {1}\n{2}".format(
                    FileConfig.VERBOSE, 'file does not exist', file_path
                )
                raise ATSFileError(msg)
            elif not file_path_regular:
                msg = "{0} {1}\n{2}".format(
                    FileConfig.VERBOSE, 'file is not regular', file_path
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
            msg = "{0} {1} {2}".format(
                FileConfig.VERBOSE, 'checking file extension', file_path
            )
            print(msg)
        status = False
        try:
            ext = splitext(file_path)[-1].lower()
            status = ext == file_extension
            if not status:
                msg = "{0} {1} [{2}] {3}".format(
                    FileConfig.VERBOSE, 'not matched file extension',
                    file_extension, file_path
                )
                raise ATSFileError(msg)
        except ATSFileError as e:
            print(e)
        return True if status else False
