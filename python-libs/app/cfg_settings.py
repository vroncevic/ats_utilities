# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from app.configuration.cfg.cfg2object import Cfg2Object
from app.configuration.cfg.object2cfg import Object2Cfg

class Settings(Cfg2Object, Object2Cfg):
	"""
	Define class Settings with attribute(s) and method(s).
	Settings class with cfg type of configuration.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
	"""

	def __init__(self, base_config_file):
		"""
		:param base_config_file: File configuration path
		:type: str
		"""
		Cfg2Object.__init__(self, base_config_file)
		Object2Cfg.__init__(self, base_config_file)
