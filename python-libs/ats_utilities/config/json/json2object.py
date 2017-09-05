# -*- coding: utf-8 -*-

import sys
from json import load

try:
    from ats_utilities.config.base_read_config import BaseReadConfig
    from ats_utilities.config.file_checking import FileChecking
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


class Json2Object(BaseReadConfig):
    """
    Define class Json2Object with attribute(s) and method(s).
    Convert a configuration from json file to an object config.
    It defines:
        attribute:
            __FORMAT - Format of configuration content
            VERBOSE - Verbose prefix console text
        method:
            __init__ - Initial constructor
            read_configuration - Read configuration from file
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    __FORMAT = 'json'
    VERBOSE = 'JSON_TO_OBJECT'

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
        msg = "{0}".format('Setting JSON interface')
        COut.print_console_msg(msg, verbose=verbose)
        super(Json2Object, self).__init__(verbose)
        self.set_file_path(configuration_file)

    def read_configuration(self, verbose=False):
        """
        Read configuration from file.
        :param verbose: Enable/disable verbose option
        :type verbose: <bool>
        :return: Configuration object | None
        :rtype: <Python object(s)> | <NoneType>
        """
        cls, json_path, content = self.__class__, self.get_file_path(), None
        msg = "{0}\n{1}".format('Read configuration from file', json_path)
        COut.print_console_msg(msg, verbose=verbose)
        check_json_file = FileChecking.check_file(json_path, verbose)
        if check_json_file:
            file_extension = ".{0}".format(cls.__FORMAT)
            check_json_file_format = FileChecking.check_format(
                json_path, file_extension, verbose
            )
            if check_json_file_format:
                try:
                    with ConfigFile(json_path, 'r') as configuration_file:
                        content = load(configuration_file)
                except ATSValueError as e:
                    print(e)
                else:
                    if content:
                        msg = "{0}".format('Done')
                        COut.print_console_msg(msg, verbose=verbose)
        return content

    def __str__(self):
        """
        Return human readable string (Json2Object).
        :return: String representation of Json2Object
        :rtype: <str>
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (Json2Object).
        :return: String representation of Json2Object
        :rtype: <str>
        """
        file_path = self.get_file_path()
        return "{0}(\'{1}\')".format(type(self).__name__, file_path)
