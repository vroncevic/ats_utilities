# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

class AbstractGetConfig(object):
	"""
	Define class AbstractGetConfig with attribute(s) and method(s).
	It defines:
		attribute:
			None
		method:
			get_configuration - Abstract method
	"""

	def get_configuration(self):
		raise NotImplementedError("Not implemented")
