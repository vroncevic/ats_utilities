# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from app.configuration.json.json2object import Json2Object
from app.configuration.json.object2json import Object2Json

class Settings(Json2Object, Object2Json):
	"""
	Define class Settings with attribute(s) and method(s).
	Settings class with json type of configuration.
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
		Json2Object.__init__(self, base_config_file)
		Object2Json.__init__(self, base_config_file)
