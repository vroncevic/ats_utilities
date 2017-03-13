# encoding: utf-8
"""
app.cfg_settings - class Settings

Usage:
	from app.cfg_settings import Settings

	class CfgBase(Settings):
		# Use settings in Base class of App
		# ...

@date: Feb 23, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.configuration.cfg.cfg2object import Cfg2Object
from app.configuration.cfg.object2cfg import Object2Cfg

class Settings(Cfg2Object, Object2Cfg):
	"""
	Define class Settings with attribute(s) and method(s).
	Settings class with cfg type of configuration.
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
		Cfg2Object.__init__(self, base_config_file)
		Object2Cfg.__init__(self, base_config_file)
