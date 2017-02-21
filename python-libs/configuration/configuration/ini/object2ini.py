# encoding: utf-8
"""
configuration.ini.object2ini - class Object2Ini

Usage:
	from configuration.ini.object2ini import Object2Ini

	config_writter = Object2Ini("simple_file.ini")
	config_writter.set_configuration(config)

@date: Feb 20, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from configuration.abstract_set_config import AbstractSetConfig
from configuration.file_config import FileConfig

class Object2Ini(AbstractSetConfig):
	"""
	define class Object2Ini with atribute(s) and method(s).
	Convert configuration object to ini format and write to configuration file.
	It defines:
		attribute:
			__format - format of configuration content
			__file_path - configuration file path (provide absolute path)
		method:
			__init__ - create and initial instance
			set_configuration - write configuration to ini file
	"""

	__format = "ini"

	def __init__(self, ini_file):
		"""
		@summary: Basic constructor
		@param ini_file: absolute configuration file path
		"""
		self.__file_path = ini_file

	def set_configuration(self, config):
		"""
		@summary: Convert content from object to ini file
		@param config: configuration object
		@return: Success return true, else return false
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(self.__format)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					cfile = open(self.__file_path, "w")
					config.write(cfile, space_around_delimiters=True)
					cfile.close()
					return True
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
		return False

