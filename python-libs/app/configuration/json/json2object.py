# encoding: utf-8
"""
app.configuration.json.json2object - class Json2Object

Usage:
	from app.configuration.json.json2object import Json2Object

	config_reader = Json2Object("simple_file.json")
	config = config_reader.get_configuration()

@date: Feb 21, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.configuration.abstract_get_config import AbstractGetConfig
from app.configuration.file_config import FileConfig
from json import load

class Json2Object(AbstractGetConfig):
	"""
	Define class Json2Object with atribute(s) and method(s).
	Convert a configuration from json file to an object configuration. 
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path (provide absolute path)
		method:
			__init__ - Create and initial instance
			get_configuration - Return configuration object
	"""

	__FORMAT = "json"

	def __init__(self, json_file):
		"""
		@summary: Basic constructor
		@param json_file: Absolute configuration file path
		"""
		self.__file_path = json_file

	def get_configuration(self):
		"""
		@summary: Convert a configuration from json file to an object
		@return: Success return a configuration object, else return None
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Json2Object.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					cfile = open(self.__file_path, "r")
					config = load(cfile)
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
				else:
					if bool(config):
						cfile.close()
						return config
		return None

