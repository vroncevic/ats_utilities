# encoding: utf-8
"""
app.configuration.yaml.object2yaml - class Object2Yaml

Usage:
	from app.configuration.yaml.object2yaml import Object2Yaml

	config_writer = Object2Yaml("simple_file.yaml")
	status = config_writer.set_configuration(config)
	# notify User/Admin about (not) success operation
	# ...

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
	Define class Object2Yaml with attribute(s) and method(s).
	Convert a configuration object to a yaml format and write to file.
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path
		method:
			__init__ - Initial constructor
			set_configuration - Write configuration to a yaml file
	"""

	__FORMAT = "yaml"

	def __init__(self, configuration_file):
		"""
		:arg: configuration_file - Absolute configuration file path
		:type: str
		"""
		self.__file_path = configuration_file

	def set_configuration(self, configuration):
		"""
		:arg: configuration - Configuration object
		:type: Python object(s)
		:return: Boolean status
		:rtype: bool
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Object2Yaml.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					configuration_file = open(self.__file_path, "w")
					dump(
						configuration,
						configuration_file,
						default_flow_style=False
					)
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
				else:
					configuration_file.close()
					return True
		return False
