# encoding: utf-8
"""
configuration.ini.ini2object - class Ini2Object

Usage:
	from configuration.ini.ini2object import Ini2Object

	config_reader = Ini2Object("simple_file.ini")
	config = config_reader.get_configuration()

@date: Feb 20, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from configuration.abstract_get_config import AbstractGetConfig
from configuration.file_config import FileConfig
from configparser import ConfigParser

class Ini2Object(AbstractGetConfig):
	"""
	Define class Ini2Object with atribute(s) and method(s).
	Convert configuration from ini file to object with structure composed of
	sections, properties, and values.
	It defines:
		attribute:
			__format - format of configuration content
			__file_path - configuration file path (provide absolute path)
		method:
			__init__ - create and initial instance
			get_configuration - return configuration object
	"""

	__format = "ini"

	def __init__(self, ini_file):
		"""
		@summary: Basic constructor
		@param ini_file: absolute configuration file path
		"""
		self.__file_path = ini_file

	def get_configuration(self):
		"""
		@summary: Convert content from ini file to object
		@return: Success return configuration object, else return None
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(self.__format)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					config = ConfigParser()
					config.read(self.__file_path, encoding=None)
					return config
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
		return None

