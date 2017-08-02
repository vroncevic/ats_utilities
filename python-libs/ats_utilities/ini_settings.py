# encoding: utf-8

from ats_utilities.config.ini.ini2object import Ini2Object
from ats_utilities.config.ini.object2ini import Object2Ini

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class IniSettings(Ini2Object, Object2Ini):
    """
    Define class IniSettings with attribute(s) and method(s).
    IniSettings class with ini type of configuration.
    It defines:
        attribute:
            VERBOSE - Verbose prefix text
        method:
            __init__ - Initial constructor
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = '[INI_SETTINGS]'

    def __init__(self, base_config_file, verbose=False):
        """
        Setting interfaces for ini object.
        :param base_config_file: File config path
        :type base_config_file: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        if verbose:
            msg = IniSettings.VERBOSE
            print(msg)
        Ini2Object.__init__(self, base_config_file, verbose)
        Object2Ini.__init__(self, base_config_file, verbose)

    def __str__(self):
        """
        Return human readable string (IniSettings).
        :return: String representation of IniSettings
        :rtype: str
        """
        file_path = self.get_file_path()
        return "File path {0}".format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (IniSettings).
        :return: String representation of IniSettings
        :rtype: str
        """
        file_path = self.get_file_path()
        return "{0}(\'{1}\')".format(type(self).__name__, file_path)
