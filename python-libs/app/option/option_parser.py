# encoding: utf-8
"""
app.option.option_parser - class AppOptionParser

Usage:
	from app.option.option_parser import AppOptionParser
	...

	app_option = AppOptionParser(version, epilog, description)
	app_option.add_option(
		"-i",
		"--in",
		dest="infile",
		help="set input path [default: %default]",
		metavar="FILE"
	)
	ops, args = app_option.parse_args(argv)

@date: Feb 22, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

from optparse import OptionParser
from app.error.lookup_error import AppError

class AppOptionParser(object):
	"""
	Define class AppOptionParser with atribute(s) and method(s).
	Create option parser and process arguments from start.
	It defines:
		attribute:
			__opt_parser - Options parser
		method:
			__init__ - Create and initial instance
			add_operation - Adding option to App/Tool/Script
			parese_args - Process arguments from start
	"""

	def __init__(self, version, epilog, description):
		"""
		@summary: Basic constructor
		@param version: App/Tool/Script version and build date
		@param epilog: App/Tool/Script long description
		@param description: App/Tool/Script author and license
		"""
		try:
			if version and epilog and description:
				self.__opt_parser = OptionParser(
					version=version, epilog=epilog, description=description
				)
			else:
				raise AppError("missing argument(s)!")
		except AppError as e:
			print("Error: ", e)

	def add_operation(self, *args, **kwargs):
		"""
		@summary: Adding option to App/Tool/Script
		@param args: list of arguments
		@param kwargs: options and texts
		"""
		self.__opt_parser.add_option(*args, **kwargs)

	def parse_args(self, argv):
		"""
		@summary: Parse arguments from start
		@param argv: arguments
		@return: options and arguments
		"""
		(opts, args) = self.__opt_parser.parse_args(argv)
		return opts, args

