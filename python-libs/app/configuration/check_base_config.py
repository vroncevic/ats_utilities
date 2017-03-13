# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

class CheckBaseConfig(object):
	"""
	Define class GenPyModule with attribute(s) and method(s).
	Checking basic configuration structure.
	It defines:
		attribute:
			None
		method:
			now - Check basic configuration
	"""

	@classmethod
	def now(cls, configuration):
		"""
		:arg: configuration - Base configuration
		:type: dict
		:return: Boolean status
		:rtype: bool
		"""
		ck_name = "app_name" in configuration.keys()
		ck_version = "app_version" in configuration.keys()
		ck_build_date = "app_build_date" in configuration.keys()
		ck_license = "app_license" in configuration.keys()
		if ck_name and ck_version and ck_build_date and ck_license:
			return True
		return False
