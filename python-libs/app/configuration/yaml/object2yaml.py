# encoding: utf-8
"""
app.configuration.yaml.object2yaml - class Object2Yaml

Usage:
	from app.configuration.yaml.object2yaml import Object2Yaml

	config_writter = Object2Yaml("simple_file.yaml")
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
from yaml import dump

class Object2Yaml(AbstractSetConfig):
	"""
	Define class Object2Yaml with atribute(s) and method(s).
	Convert a configuration object to a yaml format and write to file.
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path (provide absolute path)
		method:
			__init__ - Create and initial instance
			set_configuration - Write configuration to a yaml file
	"""

	__FORMAT = "yaml"

	def __init__(self, yaml_file):
		"""
		@summary: Basic constructor
		@param yaml_file: Absolute configuration file path
		"""
		self.__file_path = yaml_file

	def set_configuration(self, config):
		"""
		@summary: Convert a configuration from object to a yaml file
		@param config: Configuration object
		@return: Success return true, else return false
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Object2Yaml.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					cfile = open(self.__file_path, "w")
					dump(config, cfile, default_flow_style=False)
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
				else:
					cfile.close()
					return True
		return False

