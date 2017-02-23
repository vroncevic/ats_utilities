# encoding: utf-8
"""
app.license - class AppLicense

Usage:
	from app.license import AppLicense

	lic = AppLicense(txt_license=None)
	lic.set("GPLv3")
	license = lic.get()

@date: Feb 22, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

class AppLicense:
	"""
	Define class AppLicense with atribute(s) and method(s).
	Keep, set, get text license of App/Tool/Script.
	It defines:
		attribute:
			__license - text with license (use string format)
		method:
			__init__ - create and initial instance
			set - setting text license
			get - getting text license
	"""

	def __init__(self, txt_license=None):
		"""
		@summary: Basic constructor
		@param txt_license: text license (provide in string format)
		"""
		self.__license = txt_license

	def set(self, txt_license):
		"""
		@summary: Setter for text license of App/Tool/Script
		@param txt_license: text license (provide in string format)
		"""
		self.__license = txt_license

	def get(self):
		"""
		@summary: Getter for text license of App/Tool/Script
		@return: text license (string representation)
		"""
		return self.__license

