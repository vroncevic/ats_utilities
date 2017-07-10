# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

class BuildDate(object):
    """
    Define class BuildDate with attribute(s) and method(s).
    Keep, set, get build date of App/Tool/Script.
    It defines:
        attribute:
            __build_date - Build date of App/Tool/Script
        method:
            __init__ - Initial constructor
            set_build_date - Setting build date of App/Tool/Script
            get_build_date - Getting build date of App/Tool/Script
    """

    def __init__(self, build_date=None):
        """
        :param build_date: Build date of App/Tool/Script
        :type: str
        """
        self.__build_date = build_date

    def set_build_date(self, build_date):
        """
        :param build_date: Build date of App/Tool/Script
        :type: str
        """
        self.__build_date = build_date

    def get_build_date(self):
        """
        :return: Build date of App/Tool/Script
        :rtype: str
        """
        return self.__build_date
