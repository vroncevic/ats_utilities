# encoding: utf-8
"""
app.configuration.abstract_set_config - class AbstractSetConfig

Usage:
	from app.configuration.abstract_set_config import AbstractSetConfig

	class ToolSetConfig(AbstractSetConfig):
		def set_configuration(self, config):
			# override segment code
			# ...

@date: Feb 20, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

class AbstractSetConfig(object):
	"""
	Define class AbstractSetConfig with attribute(s) and method(s).
	It defines:
		attribute:
			None
		method:
			set_configuration - Abstract method
	"""

	def set_configuration(self, configuration):
		"""
		:arg: configuration - Configuration object
		"""
		raise NotImplementedError("Not implemented")
