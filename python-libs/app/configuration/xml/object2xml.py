# encoding: utf-8
"""
app.configuration.xml.object2xml - class Object2Xml

Usage:
	from app.configuration.xml.object2xml import Object2Xml

	config_writer = Object2Xml("simple_file.xml")
	# ...
	status = config_writer.set_configuration(config.extract())
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

class Object2Xml(AbstractSetConfig):
	"""
	define class Object2Xml with attribute(s) and method(s).
	Convert a configuration object to a xml format and write to file.
	It defines:
		attribute:
			__FORMAT - Format of configuration content
			__file_path - Configuration file path
		method:
			__init__ - Initial constructor
			set_configuration - Write configuration to a xml file
	"""

	__FORMAT = "xml"

	def __init__(self, configuration_file):
		"""
		:arg: configuration_file - Absolute configuration file path
		:type: str
		"""
		self.__file_path = configuration_file

	def set_configuration(self, configuration):
		"""
		:arg: configuration - Configuration object
		:type: BeautifulSoup
		:return: Boolean status
		:rtype: bool
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(Object2Xml.__FORMAT)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					configuration_file = open(self.__file_path, "w")
					configuration_file.write("{}".format(configuration))
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
				else:
					configuration_file.close()
					return True
		return False
