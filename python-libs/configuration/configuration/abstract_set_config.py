# encoding: utf-8
"""
configuration.abstract_set_config - class AbstractSetConfig

@date: Feb 20, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

class AbstractSetConfig:
	"""
	Define class AbstractSetConfig with atribute(s) and method(s).
	It defines:
		attribute:
			None
		method:
			set_configuration - abstract method
	"""

	def set_configuration(self, config):
		"""
		@summary: Subclass must implement this method
		@param config: configuration object
		"""
		raise NotImplementedError("Not implemented")

