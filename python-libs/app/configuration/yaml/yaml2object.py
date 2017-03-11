# encoding: utf-8
"""
app.configuration.yaml.yaml2object - class Yaml2Object

Usage:
	from app.configuration.yaml.yaml2object import Yaml2Object

	config_reader = Yaml2Object("simple_file.yaml")
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
from yaml import load

class Yaml2Object(AbstractGetConfig):
	"""
	Define class Yaml2Object with atribute(s) and method(s).
	Convert a yaml configuration file to an object with structure composed of
	sections, properties, and values.
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path (provide absolute path)
		method:
			__init__ - Create and initial instance
			get_configuration - Return a configuration object
	"""

	__FORMAT = "yaml"

	def __init__(self, yaml_file):
		"""
		@summary: Basic constructor
		@param yaml_file: Absolute configuration file path
		"""
		self.__file_path = yaml_file

	def get_configuration(self):
		"""
		@summary: Convert a configuration from yaml file to an object
		@return: Success return configuration object, else return None
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Yaml2Object.__FORMAT)
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

