# encoding: utf-8
"""
app.configuration.ini.ini2object - class Ini2Object

Usage:
	from app.configuration.ini.ini2object import Ini2Object

	config_reader = Ini2Object("simple_file.ini")
	config = config_reader.get_configuration()

@date: Feb 20, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.configuration.abstract_get_config import AbstractGetConfig
from app.configuration.file_config import FileConfig
from configparser import ConfigParser

class Ini2Object(AbstractGetConfig):
	"""
	Define class Ini2Object with atribute(s) and method(s).
	Convert configuration from an ini file to an object with structure composed
	of sections, properties, and values.
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path (provide absolute path)
		method:
			__init__ - Create and initial instance
			get_configuration - Return configuration object
	"""

	__FORMAT = "ini"

	def __init__(self, ini_file):
		"""
		@summary: Basic constructor
		@param ini_file: Absolute configuration file path
		"""
		self.__file_path = ini_file

	def get_configuration(self):
		"""
		@summary: Convert content from an ini file to an object
		@return: Success return configuration object, else return None
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Ini2Object.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					config = ConfigParser()
					config.read(self.__file_path, encoding=None)
					return config
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
		return None

