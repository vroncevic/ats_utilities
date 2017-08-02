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


class Object2Cfg(BaseWriteConfig):
    """
    Define class Object2Cfg with attribute(s) and method(s).
    Convert a configuration object to cfg format and write to a file.
    It defines:
        attribute:
            __FORMAT - Format of configuration content
            VERBOSE - Verbose prefix text
        method:
            __init__ - Initial constructor
            write_configuration - Write config to a cfg file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    __FORMAT = 'cfg'
    VERBOSE = '[OBJECT_TO_CFG]'

    def __init__(self, configuration_file, verbose=False):
        """
        Setting configuration file path.
        :param configuration_file: Absolute configuration file path
        :type configuration_file: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        if verbose:
            msg = Object2Cfg.VERBOSE
            print(msg)
        BaseWriteConfig.__init__(self, verbose)
        self.set_file_path(configuration_file)

    def write_configuration(self, configuration, verbose=False):
        """
        Write configuration to file.
        :param configuration: Configuration object
        :type configuration: dict
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        :return: True (success) | False
        :rtype: bool
        """
        file_path = self.get_file_path()
        if verbose:
            txt = "{0} {1}".format(
                Object2Cfg.VERBOSE, 'write configuration to file'
            )
            msg = "{0} {1}".format(txt, file_path)
            print(msg)
        status = False
        check_cfg_file = FileConfig.check_file(file_path, verbose)
        if check_cfg_file:
            file_extension = ".{0}".format(Object2Cfg.__FORMAT)
            check_cfg_file_format = FileConfig.check_format(
                file_path, file_extension, verbose
            )
            if check_cfg_file_format:
                try:
                    configuration_file = open(file_path, 'w')
                    for key in configuration:
                        config_value = configuration.get(key)
                        line = "{0} = {1}\n".format(key, config_value)
                        configuration_file.write(line)
                except IOError as e:
                    msg = "I/O error({0}): {1}".format(e.errno, e.strerror)
                    print(msg)
                else:
                    configuration_file.close()
                    status = True
                    if verbose:
                        msg = "{0} {1}".format(Object2Cfg.VERBOSE, 'Done')
                        print(msg)
        return True if status else False

    def __str__(self):
        """
        Return human readable string (Object2Cfg).
        :return: String representation of Object2Cfg
        :rtype: str
        """
        file_path = self.get_file_path()
        return 'File path {0}'.format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (Object2Cfg).
        :return: String representation of Object2Cfg
        :rtype: str
        """
        file_path = self.get_file_path()
        return '{0}(\'{1}\')'.format(type(self).__name__, file_path)
