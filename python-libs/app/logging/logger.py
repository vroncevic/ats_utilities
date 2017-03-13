# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from logging import basicConfig, debug, info, warning, critical, error
from logging import DEBUG, WARNING, CRITICAL, ERROR, INFO
from app.error.lookup_error import AppError

class Logger(object):
	"""
	Define class Logger with attribute(s) and method(s).
	Logging mechanism for App/Tool/Script.
	It defines:
		attribute:
			__file_name - Log file path
		method:
			__init__ - Initial constructor
			write_log - Write message to log file
	"""

	def __init__ (self, logging_file):
		"""
		:arg: log_file - Log file path of App/Tool/Script
		:type: str
		"""
		self.__file_name = logging_file
		basicConfig(
			format="%(asctime)s - %(levelname)s - %(message)s",
			datefmt="%m/%d/%Y %I:%M:%S %p",
			filename=self.__file_name,
			level=DEBUG
		)

	def write_log(self, msg, ctrl):
		"""
		@summary: Write log message to file
		:arg: msg - Log message
		:type: str
		:arg: ctrl - Control flag (debug, warning, critical, error, info)
		:type: str
		"""
		try:
			if ctrl == DEBUG:
				debug(msg)
			elif ctrl == WARNING:
				warning(msg)
			elif ctrl == CRITICAL:
				critical(msg)
			elif ctrl == ERROR:
				error(msg)
			elif ctrl == INFO:
				info(msg)
			else:
				raise AppError("not implemented log level")
		except AppError as e:
			print("Error: ", e)
