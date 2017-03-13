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
	Define class AppOptionParser with attribute(s) and method(s).
	Create option parser and process arguments from start.
	It defines:
		attribute:
			__opt_parser - Options parser
		method:
			__init__ - Initial constructor
			add_operation - Adding option to App/Tool/Script
			parese_args - Process arguments from start
	"""

	def __init__(self, version, epilog, description):
		"""
		:arg: version - App/Tool/Script version and build date
		:type: str
		:arg: epilog - App/Tool/Script long description
		:type: str
		:arg: description - App/Tool/Script author and license
		:type: str
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
		:arg: args - List of arguments
		:type: Python object(s)
		:arg: kwargs: Options and texts
		:type: Python object(s)
		"""
		self.__opt_parser.add_option(*args, **kwargs)

	def parse_args(self, argv):
		"""
		:arg: argv - Arguments
		:type: Python object(s)
		:return: Options and arguments
		:type: Python object(s)
		"""
		(opts, args) = self.__opt_parser.parse_args(argv)
		return opts, args
