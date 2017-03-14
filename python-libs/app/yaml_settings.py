# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from app.configuration.yaml.yaml2object import Yaml2Object
from app.configuration.yaml.object2yaml import Object2Yaml

class Settings(Yaml2Object, Object2Yaml):
	"""
	Define class Settings with attribute(s) and method(s).
	Settings class with yaml type of configuration.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
	"""

	def __init__(self, base_config_file):
		"""
		:param base_config_file: File configuration path
		:type: str
		"""
		Yaml2Object.__init__(self, base_config_file)
		Object2Yaml.__init__(self, base_config_file)
