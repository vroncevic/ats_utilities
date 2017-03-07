# encoding: utf-8
"""
app.base - class Base

Usage:
	from app.base import Base

	class MyApp(Base):
		# define App atribute(s) and method(s)

@date: Mar 07, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from abc import ABCMeta, abstractmethod
from app.info import AppInfo
from app.settings import Settings
from app.option.option_parser import AppOptionParser
from app.configuration.check_base_config import CheckBaseConfig
from app.error.lookup_error import AppError
from os.path import dirname, realpath

class Base(AppInfo, Settings, AppOptionParser):
	"""
	Define class Base with atribute(s) and method(s).
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
		@summary: Basic constructor
		@param base_config_file: Configuration file path
		"""
		Settings.__init__(self, base_config_file)
		try:
			config = self.get_configuration()
			if config != None and CheckBaseConfig.now(config):
				AppInfo.__init__(self, config)
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
		@summary: Add new option to tool
		@param args: list of arguments
		@param kwargs: options and texts
		"""
		self.add_operation(*args, **kwargs)

	def get_tool_status(self):
		"""
		@summary: Getting tool status
		@return: Tool operational return true, else return false
		"""
		return self.__tool_operational

	@abstractmethod
	def process(self):
		pass

