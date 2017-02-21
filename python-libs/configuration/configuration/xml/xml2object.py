# encoding: utf-8
"""
configuration.xml.xml2object - class Xml2Object

Usage:
	from configuration.xml.xml2object import Xml2Object

	config_reader = Xml2Object("simple_file.xml")
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
from bs4 import BeautifulSoup

class Xml2Object(AbstractGetConfig):
	"""
	Define class Xml2Object with atribute(s) and method(s).
	Convert xml configuration file (xml tags) to object with structure
	composed of sections, properties, and values.
	It defines:
		attribute:
			__format - format of configuration content
			__file_path - configuration file path (provide absolute path)
		method:
			__init__ - create and initial instance
			get_configuration - return configuration object
	"""

	__format = "xml"

	def __init__(self, xml_file):
		"""
		@summary: Basic constructor
		@param xml_file: absolute configuration file path
		"""
		self.__file_path = xml_file

	def get_configuration(self):
		"""
		@summary: Convert content from xml file to object
		@return: Success return configuration object, else return None
		"""
		if FileConfig.check_file(self.__file_path):
			file_extension = ".{0}".format(self.__format)
			if FileConfig.check_format(self.__file_path, file_extension):
				try:
					cfile = open(self.__file_path, "r")
					content = cfile.read()
					config = BeautifulSoup(content, self.__format)
					cfile.close()
					return config
				except IOError as e:
					print("I/O error({0}): {1}".format(e.errno, e.strerror))
		return None

