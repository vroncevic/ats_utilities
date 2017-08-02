# encoding: utf-8

from re import match

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


class Cfg2Object(BaseReadConfig):
    """
    Define class Cfg2Object with attribute(s) and method(s).
    Convert configuration from a cfg file to an object with structure composed
    of keys and values (key_1 = value_1, ..., key_n = value_n).
    It defines:
        attribute:
            __FORMAT - Format of configuration content
            VERBOSE - Verbose prefix text
        method:
            __init__ - Initial constructor
            read_configuration - Read configuration from file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    __FORMAT = 'cfg'
    VERBOSE = '[CFG_TO_OBJECT]'

    def __init__(self, configuration_file, verbose=False):
        """
        Setting configuration file path.
        :param configuration_file: Absolute configuration file path
        :type configuration_file: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        if verbose:
            msg = Cfg2Object.VERBOSE
            print(msg)
        BaseReadConfig.__init__(self, verbose)
        self.set_file_path(configuration_file)

    def read_configuration(self, verbose=False):
        """
        Read configuration from file.
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: Configuration object
        :rtype: dict | NoneType
        """
        file_path = self.get_file_path()
        if verbose:
            txt = "{0} {1}".format(
                Cfg2Object.VERBOSE, 'Read configuration from file'
            )
            msg = "{0} {1}".format(txt, file_path)
            print(msg)
        check_cfg_file = FileConfig.check_file(file_path, verbose)
        if check_cfg_file:
            file_extension = ".{0}".format(Cfg2Object.__FORMAT)
            check_cfg_file_format = FileConfig.check_format(
                file_path, file_extension, verbose
            )
            if check_cfg_file_format:
                try:
                    configuration_file = open(file_path, 'r')
                    content = configuration_file.read()
                except IOError as e:
                    msg = "I/O error({0}): {1}".format(e.errno, e.strerror)
                    print(msg)
                else:
                    if content:
                        configuration_file.close()
                        lines = content.splitlines()
                        config = {}
                        for line in lines:
                            regex_match = match(r'^\s*$', line)
                            if not regex_match:
                                pairs = line.split('=')
                                config[pairs[0].strip()] = pairs[1].strip()
                        if verbose:
                            msg = "{0} {1}".format(Cfg2Object.VERBOSE, 'Done')
                            print(msg)
                        return config
        return None

    def __str__(self):
        """
        Return human readable string (Cfg2Object).
        :return: String representation of Cfg2Object
        :rtype: str
        """
        file_path = self.get_file_path()
        return 'File path {0}'.format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (Cfg2Object).
        :return: String representation of Cfg2Object
        :rtype: str
        """
        file_path = self.get_file_path()
        return '{0}(\'{1}\')'.format(type(self).__name__, file_path)
