# encoding: utf-8
"""
app.build_date - class BuildDate

Usage:
	from app.build_date import BuildDate

	build_date = BuildDate("23 Feb 2017")
	date = build_date.get_build_date()
	# operate with build date
	# ...
	build_date.set_build_date("22 Feb 2017")

@date: Feb 22, 2017
@author: Vladimir Roncevic
@contact: <elektron.ronca@gmail.com>
@copyright: 2017 Free software to use and distributed it.
@license: GNU General Public License (GPL)
@deffield: updated: Updated
"""

class BuildDate(object):
	"""
	Define class BuildDate with attribute(s) and method(s).
	Keep, set, get build date of App/Tool/Script.
	It defines:
		attribute:
			__build_date - Build date of App/Tool/Script
		method:
			__init__ - Initial constructor
			set_build_date - Setting build date of App/Tool/Script
			get_build_date - Getting build date of App/Tool/Script
	"""

	def __init__(self, build_date=None):
		"""
		:arg: build_date - Build date of App/Tool/Script
		:type: str
		"""
		self.__build_date = build_date

	def set_build_date(self, build_date):
		"""
		:arg: build_date - Build date of App/Tool/Script
		:type: str
		"""
		self.__build_date = build_date

	def get_build_date(self):
		"""
		:return: Build date of App/Tool/Script
		:rtype: str
		"""
		return self.__build_date
