# encoding: utf-8
"""
app.configuration.json.object2json - class Object2Json

Usage:
	from app.configuration.json.object2json import Object2Json

	config_writter = Object2Json("simple_file.json")
	config_writter.set_configuration(config)

@date: Feb 21, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.configuration.abstract_set_config import AbstractSetConfig
from app.configuration.file_config import FileConfig
from json import dump

class Object2Json(AbstractSetConfig):
	"""
	Define class Object2Json with atribute(s) and method(s).
	Convert a configuration object to a json format and write to file.
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path (provide absolute path)
		method:
			__init__ - Create and initial instance
			set_configuration - Write configuration to a json file
	"""

	__FORMAT = "json"

	def __init__(self, json_file):
		"""
		@summary: Basic constructor
		@param json_file: Absolute configuration file path
		"""
		self.__file_path = json_file

	def set_configuration(self, config):
		"""
		@summary: Convert configuration from an object to a json file
		@param config: Configuration object
		@return: Success return true, else return false
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Object2Json.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					cfile = open(self.__file_path, "w")
					dump(config, cfile)
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
				else:
					cfile.close()
					return True
		return False

