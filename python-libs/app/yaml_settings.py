# encoding: utf-8
"""
app.yaml_settings - class Settings

Usage:
	from app.yaml_settings import Settings

	class YamlBase(Settings):
		# Use settings in Base class of App
		# ...

@date: Mar 13, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.configuration.yaml.yaml2object import Yaml2Object
from app.configuration.yaml.object2yaml import Object2Yaml

class Settings(Yaml2Object, Object2Yaml):
	"""
	Define class Settings with attribute(s) and method(s).
	Settings class with yaml type of configuration.
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
		Yaml2Object.__init__(self, base_config_file)
		Object2Yaml.__init__(self, base_config_file)
