# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

class AppName(object):
    """
    Define class AppName with attribute(s) and method(s).
    Keep, set, get App/Tool/Script name.
    It defines:
        attribute:
            __program_name - Name of App/Tool/Script
        method:
            __init__ - Initial constructor
            set_name - Setting program name of App/Tool/Script
            get_name - Getting program name of App/Tool/Script
    """

    def __init__(self, program_name=None):
        """
        :param program_name: App/Tool/Script name
        :type: str
        """
        self.__program_name = program_name

    def set_name(self, program_name):
        """
        :param program_name: App/Tool/Script name
        :type: str
        """
        self.__program_name = program_name

    def get_name(self):
        """
        :return: App/Tool/Script name
        :rtype: str
        """
        return self.__program_name
