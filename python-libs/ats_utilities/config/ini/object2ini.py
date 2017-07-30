# encoding: utf-8

from ats_utilities.config.base_write_config import BaseWriteConfig
from ats_utilities.config.file_config import FileConfig

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Object2Ini(BaseWriteConfig):
    """
    Define class Object2Ini with attribute(s) and method(s).
    Convert a configuration object to an ini format and write to file.
    It defines:
        attribute:
            __FORMAT - Format of configuration content
            VERBOSE - Verbose prefix text
        method:
            __init__ - Initial constructor
            write_configuration - Write configuration to an ini file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    __FORMAT = 'ini'
    VERBOSE = '[OBJECT_TO_INI]'

    def __init__(self, configuration_file, verbose=False):
        """
        Setting configuration file path.
        :param configuration_file: Absolute configuration file path
        :type: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        if verbose:
            msg = Object2Ini.VERBOSE
            print(msg)
        BaseWriteConfig.__init__(self, verbose)
        self.set_file_path(configuration_file)

    def write_configuration(self, configuration, verbose=False):
        """
        Write configuration to an ini file.
        :param configuration: Configuration object
        :type: ConfigParser
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: Boolean status
        :rtype: bool
        """
        status = False
        file_path = self.get_file_path()
        check_cfg_file = FileConfig.check_file(file_path, verbose)
        if check_cfg_file:
            file_extension = ".{0}".format(Object2Ini.__FORMAT)
            check_cfg_file_format = FileConfig.check_format(
                file_path, file_extension, verbose
            )
            if check_cfg_file_format:
                try:
                    configuration_file = open(file_path, 'w')
                    configuration.write(
                        configuration_file, space_around_delimiters=True
                    )
                except IOError as e:
                    msg = "I/O error({0}): {1}".format(e.errno, e.strerror)
                    print(msg)
                else:
                    configuration_file.close()
                    status = True
                    if verbose:
                        msg = Object2Ini.VERBOSE + ' Done'
                        print(msg)
        return True if status else False

    def __str__(self):
        """
        Return human readable string (Object2Ini).
        :return: String representation of Object2Ini
        :rtype: str
        """
        file_path = self.get_file_path()
        return 'File path {0}'.format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (Object2Ini).
        :return: String representation of Object2Ini
        :rtype: str
        """
        file_path = self.get_file_path()
        return '{0}(\'{1}\')'.format(type(self).__name__, file_path)
