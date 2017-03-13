# encoding: utf-8
"""
app.ini_settings - class Settings

Usage:
	from app.ini_settings import Settings

	class IniBase(Settings):
		# Use settings in Base class of App
		# ...

@date: Mar 13, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.configuration.ini.ini2object import Ini2Object
from app.configuration.ini.object2ini import Object2Ini

class Settings(Ini2Object, Object2Ini):
	"""
	Define class Settings with attribute(s) and method(s).
	Settings class with ini type of configuration.
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
		Ini2Object.__init__(self, base_config_file)
		Object2Ini.__init__(self, base_config_file)
