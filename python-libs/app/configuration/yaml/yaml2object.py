# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2007, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from app.configuration.abstract_get_config import AbstractGetConfig
from app.configuration.file_config import FileConfig
from yaml import load

class Yaml2Object(AbstractGetConfig):
	"""
	Define class Yaml2Object with attribute(s) and method(s).
	Convert a yaml configuration file to an object with structure composed of
	sections, properties, and values.
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path
		method:
			__init__ - Initial constructor
			get_configuration - Getting a configuration from file
	"""

	__FORMAT = "yaml"

	def __init__(self, configuration_file):
		"""
		:param configuration_file: Absolute configuration file path
		:type: str
		"""
		self.__file_path = configuration_file

	def get_configuration(self):
		"""
		:return: Configuration object
		:rtype: Python object(s) or NoneType
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Yaml2Object.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					configuration_file = open(self.__file_path, "r")
					config = load(configuration_file)
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
				else:
					if config:
						configuration_file.close()
						return config
		return None
