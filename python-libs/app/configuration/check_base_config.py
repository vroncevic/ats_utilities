# encoding: utf-8
"""
app.configuration.check_base_config - class CheckBaseConfig

Usage:
	from app.configuration.check_base_config import CheckBaseConfig
	...

	if CheckBaseConfig.now(config):
		# Everything is ok

@date: Feb 25, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

class CheckBaseConfig(object):
	"""
	Define class GenPyModule with atribute(s) and method(s).
	Checking basic configuration structure.
	It defines:
		attribute:
			None
		method:
			now - Check basic configuration
	"""

	@classmethod
	def now(cls, config):
		"""
		@summray: Check basic configuration
		@param config: Base configuration (dictionary)
		@return: Success return true, else return false
		"""
		ck_name = "app_name" in config.keys()
		ck_version = "app_version" in config.keys()
		ck_build_date = "app_build_date" in config.keys()
		ck_license = "app_license" in config.keys()
		if ck_name and ck_version and ck_build_date and ck_license:
			return True
		return False

