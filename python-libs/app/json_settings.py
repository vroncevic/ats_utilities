# encoding: utf-8
"""
app.json_settings - class Settings

Usage:
	from app.json_settings import Settings

	class JsonBase(Settings):
		# Use settings in Base class of App
		# ...

@date: Mar 13, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.configuration.json.json2object import Json2Object
from app.configuration.json.object2json import Object2Json

class Settings(Json2Object, Object2Json):
	"""
	Define class Settings with attribute(s) and method(s).
	Settings class with json type of configuration.
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
		Json2Object.__init__(self, base_config_file)
		Object2Json.__init__(self, base_config_file)
