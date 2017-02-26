# encoding: utf-8
"""
app.version - class AppVersion

Usage:
	from app.version import AppVersion

	ver = AppVersion("1.0")
	version = ver.get_version()
	ver.set_version("1.1")

@date: Feb 22, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

class AppVersion(object):
	"""
	Define class AppVersion with atribute(s) and method(s).
	Keep, set, get version number of App/Tool/Script.
	It defines:
		attribute:
			__version - Version number of App/Tool/Script
		method:
			__init__ - Create and initial instance
			set_version - Setting version number
			get_version - Return version number
	"""

	def __init__(self, version=None):
		"""
		@summary: Basic constructor
		@param version: App/Tool/Script version (provide in string format)
		"""
		self.__version = version

	def set_version(self, version):
		"""
		@summary: Setter for version of App/Tool/Script
		@param version: App/Tool/Script version (provide in string format)
		"""
		self.__version = version

	def get_version(self):
		"""
		@summary: Getter for version of App/Tool/Script
		@return: App/Tool/Script version
		"""
		return self.__version

