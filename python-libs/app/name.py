# encoding: utf-8
"""
app.name - class AppName

Usage:
	from app.name import AppName

	app = AppName("RCP")
	app_name = app.get_name()
	app.set_name("RCP2")

@date: Feb 22, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

class AppName(object):
	"""
	Define class AppName with atribute(s) and method(s).
	Keep, set, get App/Tool/Script name.
	It defines:
		attribute:
			__program_name - Name of App/Tool/Script
		method:
			__init__ - Create and initial instance
			set_name - Setting program name
			get_name - Getting program name
	"""

	def __init__(self, program_name=None):
		"""
		@summary: Basic constructor
		@param program_name: App/Tool/Script name (provide in string format)
		"""
		self.__program_name = program_name

	def set_name(self, program_name):
		"""
		@summary: Setter for name of App/Tool/Script
		@param program_name: App/Tool/Script name (provide in string format)
		"""
		self.__program_name = program_name

	def get_name(self):
		"""
		@summary: Getter for name of App/Tool/Script
		@return: App/Tool/Script name
		"""
		return self.__program_name

