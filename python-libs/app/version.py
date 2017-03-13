# encoding: utf-8
"""
app.version - class AppVersion

Usage:
	from app.version import AppVersion

	ver = AppVersion("1.0")
	version = ver.get_version()
	# operate with version
	# ...
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
	Define class AppVersion with attribute(s) and method(s).
	Keep, set, get version number of App/Tool/Script.
	It defines:
		attribute:
			__version - Version number of App/Tool/Script
		method:
			__init__ - Initial constructor
			set_version - Setting version number of App/Tool/Script
			get_version - Getting version number of App/Tool/Script
	"""

	def __init__(self, version=None):
		"""
		:arg: version - App/Tool/Script version
		:type: str
		"""
		self.__version = version

	def set_version(self, version):
		"""
		:arg: version - App/Tool/Script version
		:type: str
		"""
		self.__version = version

	def get_version(self):
		"""
		:return: App/Tool/Script version
		:rtype: str
		"""
		return self.__version
