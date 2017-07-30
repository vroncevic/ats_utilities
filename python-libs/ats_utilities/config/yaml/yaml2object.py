# encoding: utf-8

from yaml import load

from ats_utilities.config.base_read_config import BaseReadConfig
from ats_utilities.config.file_config import FileConfig

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Yaml2Object(BaseReadConfig):
    """
    Define class Yaml2Object with attribute(s) and method(s).
    Convert a yaml configuration file to an object with structure composed of
    sections, properties, and values.
    It defines:
        attribute:
            __FORMAT - Format of configuration content
            VERBOSE - Verbose prefix text
        method:
            __init__ - Initial constructor
            get_configuration - Getting a configuration from file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    __FORMAT = 'yaml'
    VERBOSE = '[YAML_TO_OBJECT]'

    def __init__(self, configuration_file, verbose=False):
        """
        Setting configuration file path.
        :param configuration_file: Absolute configuration file path
        :type: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        if verbose:
            msg = Yaml2Object.VERBOSE
            print(msg)
        BaseReadConfig.__init__(self, verbose)
        self.set_file_path(configuration_file)

    def read_configuration(self, verbose=False):
        """
        Getting a configuration from file.
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: Configuration object
        :rtype: Python object(s) | NoneType
        """
        file_path = self.get_file_path()
        check_cfg_file = FileConfig.check_file(file_path, verbose)
        if check_cfg_file:
            file_extension = ".{0}".format(Yaml2Object.__FORMAT)
            check_cfg_file_format = FileConfig.check_format(
                file_path, file_extension, verbose
            )
            if check_cfg_file_format:
                try:
                    configuration_file = open(file_path, 'r')
                    config = load(configuration_file)
                except IOError as e:
                    msg = "I/O error({0}): {1}".format(e.errno, e.strerror)
                    print(msg)
                else:
                    if config:
                        configuration_file.close()
                        if verbose:
                            msg = Yaml2Object.VERBOSE + ' Done'
                            print(msg)
                        return config
        return None

    def __str__(self):
        """
        Return human readable string (Yaml2Object).
        :return: String representation of Yaml2Object
        :rtype: str
        """
        file_path = self.get_file_path()
        return 'File path {0}'.format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (Yaml2Object).
        :return: String representation of Yaml2Object
        :rtype: str
        """
        file_path = self.get_file_path()
        return '{0}(\'{1}\')'.format(type(self).__name__, file_path)
