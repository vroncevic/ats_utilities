# encoding: utf-8

from app.configuration.ini.ini2object import Ini2Object
from app.configuration.ini.object2ini import Object2Ini

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Settings(Ini2Object, Object2Ini):
    """
    Define class Settings with attribute(s) and method(s).
    Settings class with ini type of configuration.
    It defines:
        attribute:
            None
        method:
            __init__ - Initial constructor
    """

    def __init__(self, base_config_file):
        """
        Setting interfaces for ini object.
        :param base_config_file: File configuration path
        :type: str
        """
        Ini2Object.__init__(self, base_config_file)
        Object2Ini.__init__(self, base_config_file)
