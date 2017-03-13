# encoding: utf-8
"""
app.license - class AppLicense

Usage:
	from app.license import AppLicense

	lic = AppLicense()
	lic.set_license("GPLv3")
	# operate with license
	# ...
	license = lic.get_license()

@date: Feb 22, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

class AppLicense(object):
	"""
	Define class AppLicense with attribute(s) and method(s).
	Keep, set, get text license of App/Tool/Script.
	It defines:
		attribute:
			__license - Text with license
		method:
			__init__ - Initial constructor
			set_license - Setting App/Tool/Script text license
			get_license - Getting App/Tool/Script text license
	"""

	def __init__(self, txt_license=None):
		"""
		:arg: txt_license - App/Tool/Script text license
		:type: str
		"""
		self.__license = txt_license

	def set_license(self, txt_license):
		"""
		:arg: txt_license - App/Tool/Script text license
		:type: str
		"""
		self.__license = txt_license

	def get_license(self):
		"""
		:return: App/Tool/Script text license
		:rtype: str
		"""
		return self.__license
