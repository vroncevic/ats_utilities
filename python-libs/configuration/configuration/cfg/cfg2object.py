# encoding: utf-8
"""
configuration.cfg.cfg2object - class Cfg2Object

Usage:
	from configuration.cfg.cfg2object import Cfg2Object

	config_reader = Cfg2Object("simple_file.cfg")
	config = config_reader.get_configuration()

@date: Feb 21, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from configuration.abstract_get_config import AbstractGetConfig
from configuration.file_config import FileConfig
from re import match

class Cfg2Object(AbstractGetConfig):
	"""
	Define class Cfg2Object with atribute(s) and method(s).
	Convert configuration from cfg file to object with structure composed of
	keys and values (key_1 = value_1, ..., key_n = value_n).
	It defines:
		attribute:
			__format - format of configuration content
			__file_path - configuration file path (provide absolute path)
		method:
			__init__ - create and initial instance
			get_configuration - return configuration object
	"""

	__format = "cfg"

	def __init__(self, cfg_file):
		"""
		@summary: Basic constructor
		@param cfg_file: absolute configuration file path
		"""
		self.__file_path = cfg_file

	def get_configuration(self):
		"""
		@summary: Convert content from cfg file to object
		@return: Success return configuration object, else return None
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(self.__format)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					with open(self.__file_path, "r") as cfg:
						content = cfg.read()
					lines = content.splitlines()
					config = {}
					for line in lines:
						if not match(r'^\s*$', line):
							pairs = line.split("=")
							config[pairs[0].strip()] = pairs[1].strip()
					return config
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
		return None

