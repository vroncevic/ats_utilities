# encoding: utf-8
"""
app.configuration.json.object2json - class Object2Json

Usage:
	from app.configuration.json.object2json import Object2Json

	config_writer = Object2Json("simple_file.json")
	# prepare configuration
	# ...
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
from json import dump

class Object2Json(AbstractSetConfig):
	"""
	Define class Object2Json with attribute(s) and method(s).
	Convert a configuration object to a json format and write to file.
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path
		method:
			__init__ - Initial constructor
			set_configuration - Write configuration to a json file
	"""

	__FORMAT = "json"

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
			file_extension = ".{0}".format(Object2Json.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					configuration_file = open(self.__file_path, "w")
					dump(configuration, configuration_file)
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
				else:
					configuration_file.close()
					return True
		return False
