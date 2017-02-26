# encoding: utf-8
"""
app.configuration.ini.object2ini - class Object2Ini

Usage:
	from app.configuration.ini.object2ini import Object2Ini

	config_writter = Object2Ini("simple_file.ini")
	config_writter.set_configuration(config)

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
	define class Object2Ini with atribute(s) and method(s).
	Convert a configuration object to an ini format and write to file.
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path (provide absolute path)
		method:
			__init__ - Create and initial instance
			set_configuration - Write configuration to an ini file
	"""

	__FORMAT = "ini"

	def __init__(self, ini_file):
		"""
		@summary: Basic constructor
		@param ini_file: Absolute configuration file path
		"""
		self.__file_path = ini_file

	def set_configuration(self, config):
		"""
		@summary: Convert a configuration from object to an ini file
		@param config: Configuration object
		@return: Success return true, else return false
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Object2Ini.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					cfile = open(self.__file_path, "w")
					config.write(cfile, space_around_delimiters=True)
					cfile.close()
					return True
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
		return False

