# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

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
		:param version: App/Tool/Script version
		:type: str
		"""
		self.__version = version

	def set_version(self, version):
		"""
		:param version: App/Tool/Script version
		:type: str
		"""
		self.__version = version

	def get_version(self):
		"""
		:return: App/Tool/Script version
		:rtype: str
		"""
		return self.__version
