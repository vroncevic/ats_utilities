# encoding: utf-8

from ats_utilities.config.json.json2object import Json2Object
from ats_utilities.config.json.object2json import Object2Json

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class JsonSettings(Json2Object, Object2Json):
    """
    Define class JsonSettings with attribute(s) and method(s).
    JsonSettings class with json type of config.
    It defines:
        attribute:
            VERBOSE - Verbose prefix text
        method:
            __init__ - Initial constructor
            __str__ - Dunder (magic) method
            __repr__ - Dunder (magic) method
    """

    VERBOSE = '[JSON_SETTINGS]'

    def __init__(self, base_config_file, verbose=False):
        """
        Setting interfaces for json object.
        :param base_config_file: File config path
        :type: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        if verbose:
            msg = JsonSettings.VERBOSE
            print(msg)
        Json2Object.__init__(self, base_config_file, verbose)
        Object2Json.__init__(self, base_config_file, verbose)

    def __str__(self):
        """
        Return human readable string (JsonSettings).
        :return: String representation of JsonSettings
        :rtype: str
        """
        file_path = self.get_file_path()
        return 'File path {0}'.format(file_path)

    def __repr__(self):
        """
        Return unambiguous string (JsonSettings).
        :return: String representation of JsonSettings
        :rtype: str
        """
        file_path = self.get_file_path()
        return '{0}(\'{1}\')'.format(type(self).__name__, file_path)
