# -*- coding: utf-8 -*-

import sys

try:
    from ats_utilities.config.base_write_config import BaseWriteConfig
    from ats_utilities.config.config_context_manager import ConfigFile
    from ats_utilities.error.ats_value_error import ATSValueError
    from ats_utilities.text.stdout_text import DBG, RST
    from ats_utilities.text import COut
except ImportError as e:
    msg = "\n{0}\n".format(e)
    sys.exit(msg)  # Force close python ATS ###################################

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
            VERBOSE - Verbose prefix console text
        method:
            __init__ - Initial constructor
            write_configuration - Write configuration to an ini file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    __FORMAT = 'ini'
    VERBOSE = 'OBJECT_TO_INI'

    def __init__(self, configuration_file, verbose=False):
        """
        Setting configuration file path.
        :param configuration_file: Absolute configuration file path
        :type configuration_file: <str>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        """
        cls, cout = self.__class__, COut()
        cout.set_ats_phase_process(cls.VERBOSE)
        msg = "{0}".format('Setting INI interface')
        COut.print_console_msg(msg, verbose=verbose)
        super(Object2Ini, self).__init__(verbose)
        self.set_file_path(configuration_file)

    def write_configuration(self, configuration, verbose=False):
        """
        Write configuration to an ini file.
        :param configuration: Configuration object
        :type: <ConfigParser>
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: True (success) | False
        :rtype: <bool>
        """
        cls, ini_path, status = self.__class__, self.get_file_path(), False
        msg = "{0}\n{1}".format('Write configuration to file', ini_path)
        COut.print_console_msg(msg, verbose=verbose)
        try:
            with ConfigFile(ini_path, 'w', cls.__FORMAT) as ini_file:
                configuration.write(
                    ini_file, space_around_delimiters=True
                )
        except (ATSValueError, AttributeError) as e:
            print(e)
        else:
            status = True
            msg = "{0}".format('Done')
            COut.print_console_msg(msg, verbose=verbose)
        return True if status else False

    def __str__(self):
        """
        Return human readable string (Object2Ini).
        :return: String representation of Object2Ini
        :rtype: <str>
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (Object2Ini).
        :return: String representation of Object2Ini
        :rtype: <str>
        """
        file_path = self.get_file_path()
        return "{0}(\'{1}\')".format(type(self).__name__, file_path)
