# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from app.configuration.xml.xml2object import Xml2Object
from app.configuration.xml.object2xml import Object2Xml

class Settings(Xml2Object, Object2Xml):
	"""
	Define class Settings with attribute(s) and method(s).
	Settings class with xml type of configuration.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
	"""

	def __init__(self, base_config_file):
		"""
		:arg: base_config_file - File configuration path
		:type: str
		"""
		Xml2Object.__init__(self, base_config_file)
		Object2Xml.__init__(self, base_config_file)
