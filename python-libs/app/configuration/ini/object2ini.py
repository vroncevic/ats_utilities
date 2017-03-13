# encoding: utf-8
"""
app.configuration.ini.object2ini - class Object2Ini

Usage:
	from app.configuration.ini.object2ini import Object2Ini

	config_writer = Object2Ini("simple_file.ini")
	# prepare configuration
	# ...
	status = config_writer.set_configuration(config)
	# notify User/Admin about (not) success operation
	# ...

@date: Feb 20, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.configuration.abstract_set_config import AbstractSetConfig
from app.configuration.file_config import FileConfig

class Object2Ini(AbstractSetConfig):
	"""
	Define class Object2Ini with attribute(s) and method(s).
	Convert a configuration object to an ini format and write to file.
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path
		method:
			__init__ - Initial constructor
			set_configuration - Write configuration to an ini file
	"""

	__FORMAT = "ini"

	def __init__(self, configuration_file):
		"""
		:arg: ini_file - Absolute configuration file path
		:type: str
		"""
		self.__file_path = configuration_file

	def set_configuration(self, configuration):
		"""
		:arg: configuration - Configuration object
		:type: ConfigParser
		:return: Boolean status
		:rtype: bool
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Object2Ini.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					configuration_file = open(self.__file_path, "w")
					configuration.write(
						configuration_file, space_around_delimiters=True
					)
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
				else:
					configuration_file.close()
					return True
		return False
