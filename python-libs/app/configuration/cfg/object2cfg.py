# encoding: utf-8
"""
app.configuration.cfg.Object2Cfg - class Object2Cfg

Usage:
	from app.configuration.cfg.object2cfg import Object2Cfg

	config_writer = Object2Cfg("simple_file.cfg")
	# setting configuration object - dictionary
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

class Object2Cfg(AbstractSetConfig):
	"""
	Define class Object2Cfg with attribute(s) and method(s).
	Convert a configuration object to cfg format and write to a file.
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path
		method:
			__init__ - Initial constructor
			set_configuration - Write configuration to a cfg file
	"""

	__FORMAT = "cfg"

	def __init__(self, configuration_file):
		"""
		:arg: configuration_file - Absolute configuration file path
		:type: str
		"""
		self.__file_path = configuration_file

	def set_configuration(self, configuration):
		"""
		:arg: configuration - Configuration object
		:type: dict
		:return: Boolean status
		:rtype: bool
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Object2Cfg.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					configuration_file = open(self.__file_path, "w")
					for key in configuration:
						configuration_file.write(
							"{0} = {1}\n".format(key, configuration[key])
						)
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
				else:
					configuration_file.close()
					return True
		return False
