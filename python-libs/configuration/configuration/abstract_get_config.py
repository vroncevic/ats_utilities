# encoding: utf-8
"""
configuration.abstract_get_config - class AbstractGetConfig

@date: Feb 20, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

class AbstractGetConfig:
	"""
	Define class AbstractGetConfig with atribute(s) and method(s).
	It defines:
		attribute:
			None
		method:
			get_configuration - abstract method
	"""

	def get_configuration(self):
		"""
		@summary: Subclass must implement this method
		"""
		raise NotImplementedError("Not implemented")

