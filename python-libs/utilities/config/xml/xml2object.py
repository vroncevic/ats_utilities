# encoding: utf-8

from utilities.config.abstract_get_config import AbstractGetConfig
from utilities.config.file_config import FileConfig
from bs4 import BeautifulSoup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Xml2Object(AbstractGetConfig):
    """
    Define class Xml2Object with attribute(s) and method(s).
    Convert a xml configuration file (xml tags) to an object with structure
    composed of sections, properties, and values.
    It defines:
        attribute:
            __FORMAT - Format of configuration content
            __file_path - Configuration file path
        method:
            __init__ - Initial constructor
            get_configuration - Getting a configuration from file
    """

    __FORMAT = 'xml'

    def __init__(self, configuration_file):
        """
        Setting configuration file path.
        :param configuration_file: Absolute configuration file path
        :type: str
        """
        self.__file_path = configuration_file

    def get_configuration(self):
        """
        Getting a configuration from file.
        :return: Configuration object
        :rtype: BeautifulSoup | NoneType
        """
        check_cfg_file = FileConfig.check_file(self.__file_path)
        if check_cfg_file:
            file_extension = ".{0}".format(Xml2Object.__FORMAT)
            check_cfg_file_format = FileConfig.check_format(
                self.__file_path, file_extension
            )
            if check_cfg_file_format:
                try:
                    configuration_file = open(self.__file_path, 'r')
                    content = configuration_file.read()
                except IOError as e:
                    msg = "I/O error({0}): {1}".format(e.errno, e.strerror)
                    print(msg)
                else:
                    config = BeautifulSoup(content, Xml2Object.__FORMAT)
                    if content:
                        configuration_file.close()
                        return config
        return None
