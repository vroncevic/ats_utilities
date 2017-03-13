# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from abc import ABCMeta, abstractmethod
from app.info import AppInfo
from app.json_settings import Settings
from app.option.option_parser import AppOptionParser
from app.configuration.check_base_config import CheckBaseConfig
from app.error.lookup_error import AppError

class JsonBase(AppInfo, Settings, AppOptionParser):
	"""
	Define class JsonBase with attribute(s) and method(s).
	Load a settings, create a CL interface and run operation.
	It defines:
		attribute:
			__tool_operational - Control operational flag
		method:
			__init__ - Initial constructor
			process - Process and run tool operation
	"""

	__metaclass__ = ABCMeta

	def __init__(self, base_config_file):
		"""
		:arg: base_config_file - Configuration file path
		:type: str
		"""
		Settings.__init__(self, base_config_file)
		try:
			configuration = self.get_configuration()
			if configuration and CheckBaseConfig.now(configuration):
				AppInfo.__init__(self, configuration)
				AppOptionParser.__init__(
					self, "{0} {1}".format(
						self.get_version(), self.get_build_date()
					),
					self.get_name(), self.get_license()
				)
				self.__tool_operational = True
			else:
				raise AppError("wrong configuration base structure!")
		except AppError as e:
			print("Error: ", e)
			self.__tool_operational = False

	def add_new_option(self, *args, **kwargs):
		"""
		:arg: args - Arguments
		:type: Python object(s)
		:arg: kwargs - Options and texts
		:type: Python object(s)
		"""
		self.add_operation(*args, **kwargs)

	def get_tool_status(self):
		"""
		:return: Operational boolean status
		:rtype: bool
		"""
		return self.__tool_operational

	@abstractmethod
	def process(self):
		pass
