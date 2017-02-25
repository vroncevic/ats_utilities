# encoding: utf-8
"""
app.configuration.cfg.Object2Cfg - class Object2Cfg

Usage:
	from app.configuration.cfg.object2cfg import Object2Cfg

	config_writter = Object2Cfg("simple_file.cfg")
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

class Object2Cfg(AbstractSetConfig):
	"""
	Define class Object2Cfg with atribute(s) and method(s).
	Convert a configuration object to cfg format and write to a file.
	It defines:
		attribute:
			__FORMAT - format of configuration content
			__file_path - configuration file path (provide absolute path)
		method:
			__init__ - create and initial instance
			set_configuration - write configuration to a cfg file
	"""

	__FORMAT = "cfg"

	def __init__(self, cfg_file):
		"""
		@summary: Basic constructor
		@param cfg_file: absolute configuration file path
		"""
		self.__file_path = cfg_file

	def set_configuration(self, config):
		"""
		@summary: Convert configuration from an object to a cfg file
		@param config: configuration object (dictionary)
		@return: Success return true, else return false
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Object2Cfg.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					cfile = open(self.__file_path, "w")
					for key in config:
						cfile.write("{0} = {1}\n".format(key, config[key]))
					cfile.close()
					return True
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
		return False

