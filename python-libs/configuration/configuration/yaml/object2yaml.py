# encoding: utf-8
"""
configuration.yaml.object2yaml - class Object2Yaml

Usage:
	from configuration.yaml.object2yaml import Object2Yaml

	config_writter = Object2Yaml("simple_file.yaml")
	config_writter.set_configuration(config)

@date: Feb 21, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from configuration.abstract_set_config import AbstractSetConfig
from configuration.file_config import FileConfig
from yaml import dump

class Object2Yaml(AbstractSetConfig):
	"""
	Define class Object2Yaml with atribute(s) and method(s).
	Convert configuration object to yaml format and write to configuration file.
	It defines:
		attribute:
			__format - format of configuration content
			__file_path - configuration file path (provide absolute path)
		method:
			__init__ - create and initial instance
			set_configuration - write configuration to yaml file
	"""

	__format = "yaml"

	def __init__(self, yaml_file):
		"""
		@summary: Basic constructor
		@param yaml_file: absolute configuration file path
		"""
		self.__file_path = yaml_file

	def set_configuration(self, config):
		"""
		@summary: Convert content from object to yaml file
		@param config: configuration object
		@return: Success return true, else return false
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(self.__format)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					cfile = open(self.__file_path, "w")
					dump(config, cfile, default_flow_style=False)
					cfile.close()
					return True
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
		return False

