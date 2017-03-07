# encoding: utf-8
"""
app.settings - class Settings

Usage:
	from app.settings import Settings

	class Base(Settings, CLI):
		# Use settings in Base class of App

@date: Feb 23, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from app.configuration.cfg.cfg2object import Cfg2Object

class Settings(Cfg2Object):
	"""
	Define class Settings with atribute(s) and method(s).
	Settings class with cfg interface.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
	"""

	def __init__(self, base_config_file):
		"""
		@summary: Basic constructor
		@param base_config_file: File configuration path
		"""
		Cfg2Object.__init__(self, base_config_file)

