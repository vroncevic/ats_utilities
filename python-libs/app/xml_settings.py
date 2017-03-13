# encoding: utf-8
"""
app.xml_settings - class Settings

Usage:
	from app.xml_settings import Settings

	class XmlBase(Settings):
		# Use settings in Base class of App
		# ...

@date: Mar 13, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.configuration.xml.xml2object import Xml2Object
from app.configuration.xml.object2xml import Object2Xml

class Settings(Xml2Object, Object2Xml):
	"""
	Define class Settings with attribute(s) and method(s).
	Settings class with xml type of configuration.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
	"""

	def __init__(self, base_config_file):
		"""
		:arg: base_config_file - File configuration path
		:type: str
		"""
		Xml2Object.__init__(self, base_config_file)
		Object2Xml.__init__(self, base_config_file)
