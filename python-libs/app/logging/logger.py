# encoding: utf-8
"""
app.logging.logger - class Logger

Usage:
	from app.logging.logger import Logger
	from logging import DEBUG, WARNING, CRITICAL, ERROR, INFO

	logger = Logger("simple_file.log")
	logger.write_log("simple test", DEBUG)
	logger.write_log("simple test", WARNING)
	logger.write_log("simple test", CRITICAL)
	logger.write_log("simple test", ERROR)
	logger.write_log("simple test", INFO)

@date: Feb 21, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from logging import basicConfig, debug, info, warning, critical, error
from logging import DEBUG, WARNING, CRITICAL, ERROR

class Logger(object):
	"""
	Define class Logger with atribute(s) and method(s).
	Logging mechanism for App/Tool/Script.
	It defines:
		attribute:
			__file_name - Log file path (provide absolute path)
		method:
			__init__ - Create and initial instance
			write_log - Write message to log file
	"""

	def __init__ (self, log_file):
		"""
		@summary: Basic constructor
		@param log_file: Log file path of App/Tool/Script
		"""
		self.__file_name = log_file
		basicConfig(
			format="%(asctime)s - %(levelname)s - %(message)s",
			datefmt="%m/%d/%Y %I:%M:%S %p",
			filename=self.__file_name,
			level=DEBUG
		)

	def write_log(self, msg, ctrl):
		"""
		@summary: Write log message to file
		@param msg: Log message
		@param ctrl: Control flag (debug, warrning, critical, error, info)
		"""
		if ctrl == DEBUG:
			debug(msg)
		elif ctrl == WARNING:
			warning(msg)
		elif ctrl == CRITICAL:
			critical(msg)
		elif ctrl == ERROR:
			error(msg)
		else:
			info(msg)

