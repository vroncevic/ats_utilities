# encoding: utf-8
"""
configuration.xml.object2xml - class Object2Xml

Usage:
	from configuration.xml.object2xml import Object2Xml

	config_writter = Object2Xml("simple_file.xml")
	config_writter.set_configuration(config.extract())

@date: Feb 20, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from configuration.abstract_set_config import AbstractSetConfig
from configuration.file_config import FileConfig

class Object2Xml(AbstractSetConfig):
	"""
	define class Object2Xml with atribute(s) and method(s).
	Convert configuration object to xml format and write to configuration file.
	It defines:
		attribute:
			__format - format of configuration content
			__file_path - configuration file path (provide absolute path)
		method:
			__init__ - create and initial instance
			set_configuration - write configuration to xml file
	"""

	__format = "xml"

	def __init__(self, xml_file):
		"""
		@summary: Basic constructor
		@param xml_file: absolute configuration file path
		"""
		self.__file_path = xml_file

	def set_configuration(self, config):
		"""
		@summary: Convert content from object to xml file
		@param config: configuration object
		@return: Success return true, else return false
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(self.__format)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					cfile = open(self.__file_path, "w")
					cfile.write("{}".format(config))
					cfile.close()
					return True
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
		return False

