# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

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
