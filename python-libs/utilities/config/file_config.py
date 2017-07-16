# encoding: utf-8

from os.path import exists, isfile, splitext

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
            None
        method:
            check_file - Check config file path
            check_format - Check config file format by extension
    """

    @classmethod
    def check_file(cls, file_path):
        """
        Check config file path.
        :param file_path: Absolute config file path
        :type: str
        :return: Boolean status
        :rtype: bool
        """
        file_path_exist = exists(file_path)
        file_path_regular = isfile(file_path)
        return True if file_path_exist and file_path_regular else False

    @classmethod
    def check_format(cls, file_path, file_extension):
        """
        Check config file format by extension.
        :param file_path: Absolute config file path
        :type: str
        :param file_extension: File format (file extension)
        :type: str
        :return: Boolean status
        :rtype: bool
        """
        ext = splitext(file_path)[-1].lower()
        return True if ext == file_extension else False
